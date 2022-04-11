import requests

version = "0.2"
api_spec_version = "0.1"

host = "http://127.0.0.1"
port = "5555"

def call_server():
    r = requests.get(host + ':' + port + '/system/test')
    print(r.text)

    r = requests.get(host + ':' + port + '/system/info')
    print(r.text)

    r = requests.get(host + ':' + port + '/api/v1.0/system/test')
    print(r.text)

    r = requests.get(host + ':' + port + '/api/v1.0/system/info')
    print(r.text)

    r = requests.post(host + ':' + port + '/api/v1.0/post/echo', json = {"username":"xyz","password":"xyz"})
    print(r.text)

if __name__ == '__main__':
    call_server()
