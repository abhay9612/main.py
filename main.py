from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)

@app.route('/price', methods=['GET'])
def get_price():
    url = 'https://www.metal.com/Lithium-ion-Battery/202303240001'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_element = soup.find('div', {'class': 'block___2RfAT'}).text
    return jsonify({'price': price_element})

if __name__ == '__main__':
    app.run(port=4000, debug=True)
