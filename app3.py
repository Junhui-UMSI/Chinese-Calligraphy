from flask import Flask, render_template, request  #NEW IMPORT -- request
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from forms import ContactForm 					# NEW IMPORT LINE
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'WebDesign'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '223119'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



# app = Flask(__name__)    #This is creating a new Flask object

# app.secret_key = 'WebDesign'

#decorator that links...
@app.route('/')          								#This is the main URL
def default():
    return render_template("index.html", name = "index", title = "HOME PAGE")			#The argument should be in templates folder

@app.route('/index')          								#This is the main URL
def home():
    return render_template("index.html", name = "index", title = "HOME PAGE")			#The argument should be in templates folder

# @app.route('/courses')          								#This is the main URL
# def courses():
#     return render_template("courses.html", name = "courses", title = "COURSES PAGE")			#The argument should be in templates folder
#
# @app.route('/interests')          								#This is the main URL
# def interests():
#     return render_template("interests.html", name = "interests", title = "INTERESTS PAGE")			#The argument should be in templates folder
#
# @app.route('/other')          								#This is the main URL
# def other():
#     return render_template("other.html", name = "other", title = "OTHER PAGE")			#The argument should be in templates folder

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def pageNotFound(e):
    return render_template('500.html'), 500

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        newusername = form.name.data
        newpassword = form.password.data
        print form.name.data
        print form.password.data
        # cursor = mysql.connect().cursor()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (userName,password) VALUES ('{0}', '{1}')".format(newusername,newpassword))
        conn.commit()
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)
# def Authenticate():
#     form = ContactForm()
#     if request.method == 'POST':
#         username = form.name.data
#         password = form.password.data
#         cursor = mysql.connect().cursor()
#         cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
#         data = cursor.fetchone()
#         if data is None:
#             return "Username or Password is wrong"
#         else:
#             return render_template('contact.html', data=data, form=form)
#
#     elif request.method == 'GET':
#         return render_template('contact.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def contact():
#     form = ContactForm()
#
#     if request.method == 'POST':
#         newusername = form.name.data
#         newpassword = form.password.data
#         print form.name.data
#         print form.password.data
#         # cursor = mysql.connect().cursor()
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO user (userName,password) VALUES ('{0}', '{1}')".format(newusername,newpassword))
#         conn.commit()
#         return 'Form posted.'
#
#     elif request.method == 'GET':
#         return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
