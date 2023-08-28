from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get-data')
def get_data():
    return {
        'Emne': "DAT515 Cloud Computing",
        "Semester": "H23",
        'Assignment': "1"
    }

if __name__ == "__main__":
    app.run(debug=True)