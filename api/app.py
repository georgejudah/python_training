# import statements always come at the top
from flask import Flask

app = Flask(__name__)


#https://www.instagram.com/cristiano/?hl=en
#https://www.instagram.com/
#query parameters

#route - 1
@app.route("/")
def home():
    return "Welcome to Judah and Sarah's Website :)"

#route - 1
@app.route("/sarah")
def sarah():
    return "Welcome to Sarah's page"

@app.route("/judah")
def judah():
    return "Welcome to judah page"

# runs blocks of code only when script is executed by a user
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)