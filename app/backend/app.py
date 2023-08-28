from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'backend'

@app.route('/get_data')
def get_data():
    return {
        'Course': "DAT515 Cloud Computing",
        "Semester": "Autumn 2023",
        'Assignment': "1"
    }

@app.route('/comment',methods = ['POST', 'GET'])
def comment():
    

if __name__ == "__main__":
    app.run(debug=True)