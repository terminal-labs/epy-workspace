from flask import Flask, jsonify, request

app = Flask(__name__)

version = "0.2"
api_spec_version = "0.1"
status = 'good'

test = {
        'status': status,
        }

info = {
        'status': status,
        'version': version,
        'api-spec-version': api_spec_version,
        }

@app.route('/system/test', methods=['GET'])
def std_system_test():
    return jsonify(test)

@app.route('/system/info', methods=['GET'])
def std_system_general_info():
    return jsonify(info)

@app.route('/api/v1.0/system/test', methods=['GET'])
def system_test():
    return jsonify(test)

@app.route('/api/v1.0/system/info', methods=['GET'])
def system_general_info():
    return jsonify(info)

@app.route('/api/v1.0/post/echo', methods=['POST'])
def post():
    return jsonify(request.json)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
