from flask import Flask, request
from flask import jsonify
app = Flask(__name__)

data_store = {}

@app.route('/setip', methods=['POST','GET'])
def set_ip():
    try:
        if request.method == 'POST':
            data = request.get_json()
            data_store['ip'] = data.get('ip')
            data_store['port'] = data.get('port')
            if data_store['ip'] and data_store['port']:
                return jsonify({'message': 'IP address set successfully'}), 200
            else:
                return jsonify({'error': 'No IP provided'}), 400
        else:
            return jsonify({'message': 'Please use POST method to set IP'}), 200
    except:
        return jsonify({'error': 'Invalid data format'}), 400
@app.route('/getip', methods=['GET'])
def get_ip():
    ip = data_store.get('ip')
    port = data_store.get('port')
    if ip and port:
        return jsonify({'ip': ip, 'port': port}), 200
    else:
        return jsonify({'error': 'No IP address set'}), 404
        
if __name__ == '__main__':
    app.run(debug=True)
