import json
from flask import Flask, jsonify, request

app = Flask(__name__)

db = []
@app.route('/', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    print(record)
    db.append(record)
    return jsonify('Record received!')


@app.route('/', methods=['GET'])
def query_records():
    return jsonify(db)    

@app.route('/data', methods=['GET'])
def query_srecords():
    fname = request.args.get('fname')
    # lname = request.args.get('lname')
    for item in db:
        if item['name'] == fname:
            return jsonify({'Message':'name found!!!'})
    return jsonify({'Message': 'name not found!!!'})


if __name__ == '__main__':
    app.run()