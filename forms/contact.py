import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        send_email()
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    smtp_email = 'affanghani786@gmail.com'
    smtp_password = 'ydikxvobtecvaiel'
    name = request.form['name']
    sender_email = request.form['email']
    msg_body = request.form['message']
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = "affanghani786@gmail.com"
    msg['Subject'] = f'Portfolio Contact Message From: {name}'
    # Email body
    body = f'Email:{sender_email}\nMessage:\n{msg_body}'
    # Attach body to the message
    msg.attach(MIMEText(body, 'plain'))
    # Establish a connection to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Login to Gmail
    server.login(smtp_email, smtp_password)
    # Send email
    server.sendmail(smtp_email, "affanghani786@gmail.com", msg.as_string())
    # Close the SMTP server connection
    server.quit()
        # Add your email sending logic here

    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)
