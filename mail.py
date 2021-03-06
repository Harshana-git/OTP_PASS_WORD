from flask import *
from flask_mail import *
from random import*
import os


template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)


app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'username@gmail.com'
app.config['MAIL_PASSWORD'] = '*************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
otp = randint(000000, 999999)
mail = Mail(app)


@app.route('/')
def index():
    return render_template("homepage.html")


@app.route("/verify", methods=['GET', 'POST'])
def verify():
    email = request.form["email"]
    msg = Message('OTP', sender='username@gmail.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template('verify.html')


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3> Email  verification is  successful </h3>"
    else:
        return "<h3>failure, OTP does not match</h3>"


if __name__ == '__main__':
    app.run(debug=True)
