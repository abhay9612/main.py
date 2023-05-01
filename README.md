# main.py
Lohum
Flask App for Getting Product Price
This Flask app allows you to retrieve the price of a product from the website https://www.metal.com/Lithium-ion-Battery/202303240001.

Prerequisites
To run this app, you need to have Python 3.x installed on your computer.

Installation
Clone this repository to your local machine.
Navigate to the root directory of the project.
Install the required Python packages by running pip install -r requirements.txt.
Usage
Start the Flask app by running python app.py.
Navigate to http://localhost:4000/price in your web browser to get the product price.
API Reference
/price
Returns the current price of the product in the following JSON format:

json
{
    "price": "XXX.XX USD"
}
Deployment
This app can be deployed to any hosting platform that supports Python and Flask, such as Heroku or AWS.
