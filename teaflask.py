import json
from flask import Flask, jsonify, request

app = Flask(__name__)

db = dict()
@app.route('/', methods=['POST'])
def create_record():
    idcount = 0
    record = json.loads(request.data)
    if ('fname',record['fname']) and ('lname',record['lname']) not in db.items():
        db['1'] = record
        # db['lname'] = record['lname']
    else:
        return jsonify('Name already exists!')
        
    print(db.items())
    print(db)
    return jsonify('Record received!')

@app.route('/', methods=['GET'])
def query_records():
    # print(db)
    return jsonify(db)    

# @app.route('/data/<id>', methods=['GET'])
# def query_srecords(id=0):

#     return jsonify(db[id])

if __name__ == '__main__':
    app.run(debug = True)