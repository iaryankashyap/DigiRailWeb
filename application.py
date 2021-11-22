from flask import Flask, render_template, request
import random
import smtplib

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("Landing.html")

@app.route("/login")
def login():
    return render_template("Login.html")


@app.route("/Signup")
def Signup():
    return render_template("Signup.html")


@app.route("/Login", methods = ['POST'])
def Login():
    user_name = request.form.get("user")
    key = request.form.get("key")
    file = open("../DigiRailWeb/login_database.txt","r+")
    flag = 0
    index = 0
    for line in file:  
        index += 1 
        if key in line:
            flag = 1
            break 
    
    if (flag != 0):
        return render_template("home.html")
    else:
        return render_template("Wrong.html", username = user_name)


@app.route("/otp", methods = ['POST'])
def otp():
    global msg, user_name, key
    user_name = request.form.get("user-name")
    mail = request.form.get("mail")
    key = request.form.get("user-key")
    msg = str(random.randint(1000, 9999))
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("pythonatyou@gmail.com", "hellothere123")
    server.sendmail("pythonatyou@gmail.com", mail, msg)
    server.quit()
    return render_template("OTP.html")

@app.route("/check", methods = ['POST'])
def check():
    otp = request.form.get("key-otp")
    if(otp == msg):
        f = open("../DigiRailWeb/login_database.txt", "a")
        f.write("-$-" + user_name + "${" + key + "}")
        return render_template("Login_after.html")
    else:
        return render_template("Wrong.html")








if __name__ == "__main__":
    app.run(debug = True)