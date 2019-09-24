from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/genericos', methods=['GET'])
def get_genericos():
    f=open('inicio_genericos.json', 'r')
    return json.dumps(f.read())

if __name__ == '__main__':
    api.run()
