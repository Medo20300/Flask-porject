
from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
#def index():
 #   return "<h1>Hello World !</h1>" 

def index():
    first_name= "Medhat"
    stuff ="this is <strong>Bold</strong> text"
    favorite_pizza = ["pizza", "machrom", "mallon", 55]
    return render_template("index.html", first_name=first_name , 
    stuff=stuff , favorite_pizza=favorite_pizza)
#localhost:5000/user/medhat
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name) 

#create Custom Error Page

#Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

# Interal Server Error thing 

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
