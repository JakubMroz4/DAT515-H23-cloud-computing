from flask import Flask, jsonify, make_response

app = Flask(__name__)


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
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response

if __name__ == "__main__":
    app.run(debug=True)