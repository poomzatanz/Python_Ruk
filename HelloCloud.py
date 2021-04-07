from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
  return "Hello 5906021622033 Raksit kongwong from Server"

if __name__ == "__main__":
  server.run(host='0.0.0.0',port=80)
