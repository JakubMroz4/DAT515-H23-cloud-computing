from flask import Flask, jsonify, make_response, request
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
mail = Mail(app)
db = SQLAlchemy(app)

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
@app.route('/')
def hello():
    return 'backend'


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


#TODO add db
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


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

if __name__ == "__main__":
    app.run(debug=True)