from flask import Flask, jsonify, make_response, request, session
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig
from flask_cors import CORS
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(BaseConfig)
CORS(app, supports_credentials=True)
db = SQLAlchemy(app)
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



@app.route('/add_data', methods=["POST"])
def add_data():
    data = request.get_json(force=True)
    email = data["email"]

    new_email = Email(email=email)
    db.session.add(new_email)
    db.session.commit()

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