from flask import Flask #importing the flask module
from flask_cors import CORS #intializing the cors module 
#cors allows the frontend to communicate with the backend. like a hall pass
app = Flask(__name__)
CORS(app)

app.config['DEBUG']= True, #this allows the app to run in debug mode and show errors
app.config['SECRET_KEY'] = 'hfh38r83913103iqw920121123unsnuee'
@app.route('/')
def home():
    return "<h1>hello world</h1>""
@app.route('/signup')
@app.route('login')



if __name__ == '__main__':
    app.run(debug = True)










#app = Flask (__name__) #creating an instance of the flask class
#@app.route ("/") #thsi tells flask that then when the user visit this homepage
#def home():
    #return 'hello world'
#if __name__ == '__main__': #this just ends flask
    app.run(debug = True)
