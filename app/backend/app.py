from flask import Flask, jsonify, make_response, request, session
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig
from flask_cors import CORS, cross_origin
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(BaseConfig)
CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
server_session = Session(app)
ma=Marshmallow(app)

from models import *
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

# TODO move to init and env
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'g02946888@gmail.com'
app.config['MAIL_PASSWORD'] = 'qwstuemdjpzsketi'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# gmail acc pass
# g02946888@gmail.com
# qwst uemd jpzs keti

#TODO test funct remove
@app.route('/')
def hello():
    return 'backend'


#TODO test funct remove
@app.route('/get_data')
def get_data():
    test_response = {
        "courses": [
            {"name": "Cloud Computing", "code": "DAT515", "semester": "Autumn 2023"}
        ]
    }
    # JSONify response
    response = make_response(jsonify(test_response))

    # Access-Control-Allow-Origin header forcross-site request
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


#TODO test funct remove
@app.route('/add_data', methods=["POST"])
def add_data():
    data = request.get_json(force=True)
    #print(data["email"])

    # valid cors response
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'

    send_mail("g02946888@gmail.com", [data["email"]])
    return response, 200


# health check
@app.route('/health')
def health():
    return "Liveness check completed", 200


def send_mail(sender, recipients):
    msg = Message('Newsletter Group16', sender=sender, recipients=recipients)
    msg.body = "Thank you for subscribing to our newsletter"
    mail.send(msg)

#TODO test funct remove
@app.route('/test_users', methods=["GET"])
def test_get_users():
    #users = User.query.order_by(User.id)
    #test = db.session.query(User).order_by(User.id)
    #users = db.session.execute(test).all()[0]

    query = db.session.query(User).all()
    print(query)
    print(query[0])
    print("#############")
    print(query[0].id)
    print(query[0].name)
    print(query[0].email)
    print(query[0].password)

    #response = make_response(users)

    #response.headers['Access-Control-Allow-Origin'] = '*'

    #return response
    return "test", 200


@cross_origin(methods=['POST'], supports_credentials=True, headers=['Content-Type', 'Authorization'])
@app.route('/register', methods=["POST"])
def register():
    data = request.get_json(force=True)
    email = data["email"]
    password = data["password"]
    name = data["name"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "User already exists"}), 410

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password, name=name)
    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.id
    print(f"USER ID: {new_user.id}")

    return jsonify({
        "id": new_user.id,
        "name": new_user.name
    })


@app.route("/login", methods=["POST"])
def login_user():
    data = request.get_json(force=True)
    email = data["email"]
    password = data["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "Unauthorized"}), 401

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    session["user_id"] = user.id

    print(f"USER ID: {user.id}")

    return jsonify({
        "id": user.id,
        "name": user.name
    })



@app.route("/authenticate")
def authenticate():
    user_id = session.get("user_id")

    print(f"USER ID: {user_id}")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "name": user.name
    })


@app.route("/logout")
def logout():
    session.pop("user_id")
    return "User logged out", 200


@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    data = request.get_json(force=True)

    author = data["author"]
    text = data["text"]

    new_post = Post(author = author, text=text)

    db.session.add(new_post)
    db.session.commit()

    return "Post Added", 200


@app.route('/get_comments', methods=['GET'])
def get_comments():
    comments = Post.query.all()
    results = posts_schema.dump(comments)
    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)