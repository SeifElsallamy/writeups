from flask import Flask
from flask import request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
@app.route("/")
def welcome():
    html = """
<h1>Welcome to our website!</h1>
<h2>Please Sign Up NOW</h2>
<form action="/mail" method="post">
Name:<br>
<input name="name" type="text"><br>
Email:<br>
<input name="email" type="email"><br>
Password:<br>
<input name="password" type="password"><br>
<button>submit</button>
</form>
"""
    return html

@app.route("/mail", methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    HTML = """
<html><head>
<style>
.green{color:green;}
.btnn{
color:black;
background-color:white;
border-style: solid;
display:inline-block;
padding:10px;
text-decoration: none;
}
</style>
</head>
<body>
<div>
<h1>Welcome %s!</h1>
<h2 class="green">Please verify your email:</h2>
<a class="btnn" href="http://127.0.0.1:5000/verify?123">Verify</a>
</div>
</body>
</html>
""" % name
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "welcome to our website!"
    msg['From'] = 'EMAIL@gmail.com'
    msg['To'] = request.form.get('email')
    msg.attach(MIMEText(HTML,'html'))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('EMAIL@gmail.com', 'PASSWORD')
    server.sendmail('EMAIL@gmail.com', request.form.get('email'), msg.as_string())
    server.close()
    return 'Please visit your email to verify it'



    
