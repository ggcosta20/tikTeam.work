from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kYUs,0.VK,s]'  # Replace with a strong secret key

# Email server configurations
app.config['MAIL_SERVER'] = 'mail.tikteam.work'
app.config['MAIL_PORT'] = 2079
app.config['MAIL_USE_TLS'] = False  # TLS is not recommended with the provided settings
app.config['MAIL_USE_SSL'] = False  # SSL is not recommended with the provided settings
app.config['MAIL_USERNAME'] = 'contact@tikteam.work'
app.config['MAIL_PASSWORD'] = 'kYUs,0.VK,s]'
app.config['MAIL_DEFAULT_SENDER'] = 'contact@tikteam.work'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        # Here, you can add code to save the email to your database
        send_welcome_email(email)
        flash('A welcome email has been sent to your address.', 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html')


def send_welcome_email(recipient_email):
    msg = Message(
        'Welcome to TikTeam',
        recipients=[recipient_email]
    )
    msg.body = 'Thank you for signing up for TikTeam. We are excited to have you on board!'
    try:
        mail.send(msg)
    except Exception as e:
        print(f'Error sending email: {e}')





from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kYUs,0.VK,s]'  # Replace with a strong secret key

# Email server configurations
app.config['MAIL_SERVER'] = 'mail.tikteam.work'
app.config['MAIL_PORT'] = 2079
app.config['MAIL_USE_TLS'] = False  # TLS is not recommended with the provided settings
app.config['MAIL_USE_SSL'] = False  # SSL is not recommended with the provided settings
app.config['MAIL_USERNAME'] = 'contact@tikteam.work'
app.config['MAIL_PASSWORD'] = 'kYUs,0.VK,s]'
app.config['MAIL_DEFAULT_SENDER'] = 'contact@tikteam.work'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        # Here, you can add code to save the email to your database
        send_welcome_email(email)
        flash('A welcome email has been sent to your address.', 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html')


def send_welcome_email(recipient_email):
    msg = Message(
        'Welcome to TikTeam',
        recipients=[recipient_email]
    )
    msg.body = 'Thank you for signing up for TikTeam. We are excited to have you on board!'
    try:
        mail.send(msg)
    except Exception as e:
        print(f'Error sending email: {e}')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

