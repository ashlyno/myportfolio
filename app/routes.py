from flask import Flask, render_template, request, flash
from forms import contactForm
from flask_mail import Message, Mail

mail = Mail()

app = Flask(__name__,template_folder="../partials")

app.secret_key="Thee Hot Girl Secret Recipe"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact.ashlynopgrande@gmail.com'
app.config["MAIL_PASSWORD"] = 'TheeSecretHotGirlRecipe6!'
 
mail.init_app(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/artwork')
def artwork():
    return render_template('artwork.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])

def contact():

    form = contactForm(request.form)

    if request.method == 'POST':

        subject = form.subject.data
        message = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)

        msg = Message(sender='contact.ashlynopgrande@gmail.com', recipients=['aopgrande@gmail.com'], subject=subject, body=message)

        mail.send(msg)

        return render_template('contact.html', success=True)

    elif request.method == 'GET':

        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)