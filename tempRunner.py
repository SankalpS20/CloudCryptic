from flask import Flask, render_template
application = Flask(__name__, template_folder='templates')
@application.route("/")
def index():
    return render_template("restore_success.html")

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=8000, debug=True)