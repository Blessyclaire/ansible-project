from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    return "Hello, I am almost a Devops Engineer!"

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000)

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()    