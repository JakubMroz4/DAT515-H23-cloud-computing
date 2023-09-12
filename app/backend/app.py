from flask import Flask, jsonify, make_response, request

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
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


@app.route('/add_data', methods=["POST"])
def add_data():
    todo_data = request.get_json()
    response = make_response(jsonify("done"))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)