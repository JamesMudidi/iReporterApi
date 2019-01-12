# Import neccessary depencies
# From the module or framework, we import the class datatype.
from flask import Flask
from api import app

if __name__ == '__main__':
    app.run(debug=True)