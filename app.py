from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/genericos', methods=['GET'])
def get_genericos():
    with open('inicio_genericos.json') as data_file:
        data = json.dump(data_file)
    return data

if __name__ == '__main__':
    api.run()
