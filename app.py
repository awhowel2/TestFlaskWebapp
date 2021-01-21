# import flask module and create app
from flask import Flask, render_template
app = Flask(__name__)

# define basic route '/'
@app.route("/")
def main():
    return render_template('index.html')

# check if executed file is in the main program
if __name__ == "__main__":
    app.run()