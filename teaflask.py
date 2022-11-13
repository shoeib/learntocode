import json
from flask import Flask, jsonify, request

app = Flask(__name__)

db = dict()
@app.route('/', methods=['POST'])
def create_record():
    db = json.loads(request.data)
    print(db)
    # db['id'] = record[]
    # db['fname'] = record['fname']
    # db['lname'] = record['lname']
    return jsonify('Record received!')


@app.route('/', methods=['GET'])
def query_records():
    print(db)
    return jsonify(db)    

@app.route('/data', methods=['GET'])
def query_srecords():
    fname = request.args.get('fname')
    # lname = request.args.get('lname')
    for item in db:
        if item['fname'] == fname:
            return jsonify({'Message':'name found!!!'})
    return jsonify({'Message': 'name not found!!!'})


if __name__ == '__main__':
    app.run(debug = True)