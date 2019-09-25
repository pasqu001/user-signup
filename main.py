from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/", methods=['POST', 'GET'])
def index():


    if request.method=='POST':
        name = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        email = request.form['email']

        pass_error = ''
        mail_error = ''
        user_error = ''

        if name == '':
            user_error = user_error + 'Username cannot be blank. '
        else:
            if name.strip(' ') != name:
                user_error = user_error + 'Spaces are not allowed in password. '
            if len(name) < 3 or len(name) > 20:
                user_error = user_error + 'Username has to be between 3 and 20 characters. '


        if password == '':
            pass_error = pass_error + 'Password Cannot be blank. '
        else:
            if password != password2:
                pass_error = pass_error + 'Password does not Match. '
            if password.strip(' ') != password:
                pass_error = pass_error + 'Spaces are not allowed in password. '
            if len(password) < 3 or len(password) > 20:
                pass_error = pass_error + 'Password has to be between 3 and 20 characters. '

        if email != '':
            if email.strip(' ') != email:
                mail_error = mail_error + 'You cannot have a space. '
            if '@' not in email or '.' not in email:
                mail_error = mail_error + 'You have to have a @ and a . symbol. '
            if len(email) < 3 or len(email) > 20:
                mail_error = mail_error + 'Email has to be between 3 and 20 characters. '

        if pass_error != '' or mail_error != '' or user_error != '':
            return render_template('index.html', username_error=user_error, email_error=mail_error, password_error=pass_error, username=name, email=email)
        else:
            return redirect('/welcome?username={0}'.format(name))
    else:
        return render_template('index.html')

@app.route("/welcome")
def welcome():
    name = request.args.get('username')
    return render_template('welcome.html', user_name=name)

app.run()