from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/b3Ryb3BfaHRsYWVoX29wdXJnX3NvY2lyZW5lZw==', methods=['GET'])
def get_genericos():
    with open('inicio_genericos.json', 'r', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return str(data)

@api.route('/ZXRpY29zX2dydXBvX2hlYWx0aF9wb3J0bw==', methods=['GET'])
def get_eticos():
    with open('inicio_eticos.json', 'r', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return str(data)

@api.route('/YXMgZmFybWFjaWFzIHRhbyByaWNhcw==', methods=['GET'])
def get_ganho():
    with open('inicio_ganho.json', 'r', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return str(data)

@api.route('/YXNldWd1dHJvcCBhaWxpbWFmIGxhbm9pY2lkYXJ0IGFkIGFpY2FtcmFm', methods=['GET'])
def get_otc():
    with open('inicio_farmacia_familia.json', 'r', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return str(data)\

@api.route('/P29hbnVvLXNhZGlkbmV2X3NlZGFkaW51', methods=['GET'])
def get_vendas():
    with open('inicio_vendas.json', 'r', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return str(data)



if __name__ == '__main__':
    api.run()
