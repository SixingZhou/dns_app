from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    # Extract parameters from the request
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if None in [hostname, fs_port, number, as_ip, as_port]:
        return jsonify({'error': 'Missing parameters'}), 400

    # Perform DNS query to get the IP address
    dns_response = requests.get(f'http://{as_ip}:{as_port}/dns?hostname={hostname}')
    ip_address = dns_response.json()['value']

    # Request Fibonacci number from Fibonacci Server
    fs_response = requests.get(f'http://{hostname}:{fs_port}/fibonacci?number={number}')

    return fs_response.text, fs_response.status_code

if __name__ == '__main__':
    app.run(port=8080)