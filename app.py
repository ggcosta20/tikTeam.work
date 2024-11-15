from flask import Flask, render_template, request, redirect, url_for, flash,render_template_string
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kYUs,0.VK,s]'  # Replace with a strong secret key

# Email server configurations
app.config['MAIL_SERVER'] = 'mail.tikteam.work'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False  # Ensure this matches your server's requirements
app.config['MAIL_USERNAME'] = 'contact@tikteam.work'
app.config['MAIL_PASSWORD'] = 'kYUs,0.VK,s]'
app.config['MAIL_DEFAULT_SENDER'] = 'contact@tikteam.work'

mail = Mail(app)


# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user store
users = {
    'admin': {'password': 'pa77W0rd2024'}  # Replace with actual user data
}

# User class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# User loader callback
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            user_obj = User(username)
            login_user(user_obj)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/generate')
@login_required
def tiktok():
    return render_template('tiktok.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        # Here, you can add code to save the email to your database
        send_security_update_email(email,"admin","pa77W0rd2024")
        flash('A welcome email has been sent to your address.', 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html')


def send_security_update_email(recipient_email, username, temp_password):
    # Define the email subject
    subject = 'Important Update: Temporary Suspension of New Sign-Ups Due to Data Security Enhancements'

    # Define the email body with HTML formatting
    email_body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }}
            h2 {{
                color: #333;
            }}
            p {{
                margin-bottom: 15px;
            }}
            ul {{
                margin-bottom: 15px;
            }}
            .highlight {{
                font-weight: bold;
                color: #d9534f;
            }}
        </style>
    </head>
    <body>
        <p>Dear user,</p>
        <p>We are writing to inform you of a recent development at TikTeam Community. Our commitment to providing a secure and reliable platform is paramount, and as part of this dedication, we have identified and are addressing a data security issue.</p>
        <h2>Temporary Suspension of New Sign-Ups</h2>
        <p>To ensure the highest standards of security, we have temporarily suspended new sign-ups. This measure allows us to implement necessary enhancements and safeguards.</p>
        <h2>Access to Your Account</h2>
        <p>We understand the importance of uninterrupted service. Therefore, we are providing you with administrative access to your account. This access will enable you to generate as many followers as needed without limitations.</p>
        <h3>Your Temporary Credentials:</h3>
        <ul>
            <li><span class="highlight">Username:</span> {username}</li>
            <li><span class="highlight">Password:</span> {temp_password}</li>
        </ul>
        <p>Please use these credentials to log in and manage your account as required.</p>
        <h2>Our Commitment to You</h2>
        <p>We apologize for any inconvenience this may cause and appreciate your understanding and patience. Our team is working diligently to resolve the issue and will notify you once new sign-ups are available.</p>
        <p>If you have any questions or need further assistance, please do not hesitate to contact us at contact@tikteam.work.</p>
        <p>Thank you for being a valued member of the TikTeam community.</p>
        <p>Best regards,</p>
        <p><br>TikTeam<br>contact@tikteam.work</p>
    </body>
    </html>
    """

    # Create the email message
    msg = Message(
        subject=subject,
        recipients=[recipient_email],
        html=email_body
    )

    # Send the email
    try:
        mail.send(msg)
        app.logger.info(f'Email successfully sent to {recipient_email}')
    except Exception as e:
        app.logger.error(f'Error sending email to {recipient_email}: {e}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
