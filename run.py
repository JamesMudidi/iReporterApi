# Import neccessary depencies
# From the module or framework, we import the class datatype.
from api import app

# The value of the __name__  attribute is set to '__main__'
# When the module runs as main program.
if __name__ == '__main__':
    app.run(debug='True')