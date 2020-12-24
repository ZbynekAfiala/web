import os
from flask import Flask,render_template, request,redirect, flash, session
from forms import PoptatForm
from flask_mail import Mail, Message


app = Flask(__name__)


app.config["DEBUG"] = True

app.config['MAIL_SERVER'] = 'smtp.gmail.com' #adresa serveru, dokumentace od providera mailu --> gmail, seznam etc. všichni jiný mail servery ofc, localhost předpokládá, že server je ten pc na kterým je soubor pro gmail = smtp.gmail.com
app.config['MAIL_PORT'] = 587 #port skrze který je email posílán na MAIL_SERVER opět v dokumentaci od providera, většinou je to 25 nebo 465, gmail = 587
app.config['MAIL_USE_TLS'] = True #for encryption purposes
app.config['MAIL_USE_SSL'] = False #to samé jako TLS
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'financni.poradkyne@gmail.com'
app.config['MAIL_PASSWORD'] = ' 8AX26S6cchCmSshz'
app.config['MAIL_DEFAULT_SENDER'] = 'financni.poradkyne@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None #max počet stejných mailu poslaných
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHEMENTS'] = False

mail=Mail(app)

app.config['SECRET_KEY'] = "r1a2n3d4o5m6"

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/kontakt',methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route('/nabídka')
def nabidka():
    return render_template("pricing.html")

@app.route('/Reference',methods=["GET","POST"])
def reference():
    return render_template("reference.html")

@app.route('/dokumenty')
def documents():
    return render_template("documents.html")


@app.route('/kontaktovat',methods=["GET","POST"])
def contact_person():
    form = PoptatForm()
    msg = Message("text",sender="financni.poradkyne@gmail.com",recipients=["financni.poradkyne@gmail.com"])
    if form.validate_on_submit():

        session['email'] = form.email.data
        session['krestni_jmeno'] = form.krestni_jmeno.data
        session['prijmeni'] = form.prijmeni.data
        session['telefon'] = form.telefon.data
        session['vzkaz'] = form.vzkaz.data #min 10 znaků
        msg = Message('Poptávka po službě od '+session['krestni_jmeno'] + ' ' + session['prijmeni'],recipients=["financni.poradkyne@gmail.com"])
        msg.body = session['vzkaz'] + ' telefonní číslo: ' + str(session['telefon']) + ' emailová adresa: ' + session['email']
        mail.send(msg)

        return redirect('/odeslano')

    return render_template('contact.html', form = form)

@app.route('/odeslano')
def email_odeslan():
    return render_template("email_odeslan.html")

if __name__ == "__main__":
    app.run(debug=True)
