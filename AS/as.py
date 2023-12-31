from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store DNS records
dns_records = {}

@app.route('/register', methods=['PUT'])
def register():
    # Extract information from the request body
    data = request.get_json()
    hostname = data['name']
    ip = data['value']
    ttl = data['ttl']

    dns_records[hostname] = {'ip': ip, 'ttl': ttl}

    return jsonify({'message': 'Registration successful'}), 201

@app.route('/dns', methods=['GET'])
def dns_query():
    # Extract the hostname from the request
    hostname = request.args.get('hostname')

    if hostname in dns_records:
        dns_record = dns_records[hostname]
        response = {
            'type': 'A',
            'name': hostname,
            'value': dns_record['ip'],
            'ttl': dns_record['ttl']
        }
        return jsonify(response), 200
    else:
        return jsonify({'error': 'Hostname not found in DNS records'}), 404

if __name__ == '__main__':
    app.run(port=30001)
