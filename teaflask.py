from flask import Flask, jsonify, request
import json
# app = Flask(__name__)
# @app.route('/hello/', methods=['GET', 'POST'])
# def welcome():
#     return "Hello World!"

#     app.run(host='0.0.0.0', port=105)

    #!/usr/bin/env python
# encoding: utf-8

app = Flask(__name__)
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return jsonify({'name': 'alice',
#                     'email': 'alice@outlook.com'})

# @app.route('/', methods=['GET'])
# def query_records():
#     name = request.args.get('name')
#     print (name)
#     with open('/tmp/data.txt', 'r') as f:
#         data = f.read()
#         records = json.loads(data)
#         for record in records:
#             if record['name'] == name:
#                 return jsonify(record)
#         return jsonify({'error': 'data not found'})

# new comment
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)