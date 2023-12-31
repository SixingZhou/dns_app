from flask import Flask, request, jsonify

app = Flask(__name__)

registered_hosts = {}

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = data['as_port']

    registered_hosts[hostname] = {'ip': ip, 'as_ip': as_ip, 'as_port': as_port}

    as_registration = {
        'type': 'A',
        'name': hostname,
        'value': ip,
        'ttl': 10
    }

    # Assuming AS has an API endpoint for registration
    as_response = requests.put(f'http://{as_ip}:{as_port}/register', json=as_registration)

    return jsonify({'message': 'Registration successful'}), 201

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    number = request.args.get('number')

    try:
        number = int(number)
    except ValueError:
        return jsonify({'error': 'Invalid sequence number format'}), 400

    fibonacci_number = fib(number)

    return jsonify({'fibonacci_number': fibonacci_number}), 200

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    app.run(port=9090)
