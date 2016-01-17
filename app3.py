from flask import Flask, render_template, request,url_for ,flash,session,redirect #NEW IMPORT -- request
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField
from forms import ContactForm, GeturlForm, ChangeForm				# NEW IMPORT LINE
from flaskext.mysql import MySQL
from flask.ext.login import login_user, login_required, logout_user, LoginManager
from functools import wraps

mysql = MySQL()
app = Flask(__name__)
app.secret_key = 'WebDesign'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '223119'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "user.login"

UPLOAD_FOLDER = '/Home/Github/Teamproject/static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#decorator that links...
@app.route('/')          								#This is the main URL
def default():
    return render_template("index.html", name = "index", title = "HOME PAGE")			#The argument should be in templates folder

@app.route('/index')          								#This is the main URL
def index():
    return render_template("index.html", name = "index", title = "HOME PAGE")			#The argument should be in templates folder

def login_required(test):
    @wraps(test)
    def wrap(*args,**kwargs):
        if 'username' in session:   #i changed it into usename, it can still work ,why?
            return test(*args,**kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/mypage', methods = ['GET','POST'])
@login_required
def mypage():
    conn = mysql.connect()
    cursor = conn.cursor()
    username = session['username']
    print username
    cursor.execute("SELECT src from User where Username='" + username + "'")
    data1 = cursor.fetchone()
    print data1
    data2 = str(data1[0])
    print data2

    form = ChangeForm()
    if request.method == 'POST':
        reusername = form.name.data
        newpassword = form.password.data
        print form.name.data
        print form.password.data
        conn = mysql.connect()
        cursor = conn.cursor()
        if reusername == username:

        # cursor.execute("SELECT * from User where Username='" + username + "'")
        # conn.commit()
        # data = cursor.fetchone()
        # if data is None:
        #     flash( "Sorry, you are updating a wrong user's information")
        #     return redirect(url_for('mypage'))
        # else:
            cursor.execute("UPDATE user SET Password = '" +newpassword+ "' WHERE Username='" + username + "' ")
            conn.commit()
            flash('Congratulations, you have successfully updated your personal profile')
            return redirect(url_for('mypage'))
        else:
            flash('Sorry, you are updating the wrong user profile')
            return redirect(url_for('mypage'))
    else:
        return render_template('mypage.html', form=form,data2 = data2)


# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',filename=filename))

@app.route('/history')         								#This is the main URL
def history():
    return render_template("history.html", name = "history", title = "HISTORY PAGE")			#The argument should be in templates folder

@app.route('/tools')          								#This is the main URL
def tools():
    return render_template("tools.html", name = "tools", title = "TOOLS PAGE")			#The argument should be in templates folder

@app.route('/masterpieces',methods = ['GET','POST'])          								#This is the main URL
def masterpieces():
    form = GeturlForm()
    if request.method =='POST':
        if 'username' in session:
            beforenewurl = form.imageurl.data
            newurl = str(beforenewurl)
            print form.imageurl.data
            print newurl
            currentuser = session['username']
            print currentuser
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE user SET src = '" +newurl+ "' WHERE Username='" + currentuser + "' ")
            conn.commit()
            return render_template("masterpieces.html", name = "masterpieces", title = "MASTERPIECES PAGE", form=form)
        else:
            flash('Sorry, you need to log in to collect the items')
            return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template("masterpieces.html", name = "masterpieces", title = "MASTERPIECES PAGE", form=form)

@app.errorhandler(404)
def pageNotFound(e):
    return 'Sorry pal, you gotta have another url'

@app.errorhandler(500)
def pageNotFound(e):
    return 'You know what, why not try a different url?'

@login_manager.user_loader    #don't understand
def load_user(user_id):
    return User.get(user_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = ContactForm()

    if request.method == 'POST':
        newusername = form.name.data
        newpassword = form.password.data
        print form.name.data
        print form.password.data
        # cursor = mysql.connect().cursor()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * from User where Username='" + newusername + "'")
        conn.commit()
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO user (userName,password) VALUES ('{0}', '{1}')".format(newusername,newpassword))
            conn.commit()
            flash('Congratulations, you have successfully registered!')
            return redirect(url_for('login'))
        else:
            flash('The username is currently been used, smart as you must can come up with another one')
            return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = ContactForm()

    if request.method == 'POST':
        username = form.name.data
        password = form.password.data
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()   # define after this ?
        if data is None:
            flash( "Username or Password is wrong")
            return redirect(url_for('login'))
        else:
            session['logged_in']=True; #what does this do? After i comment it, it still works anyway, yet all the tutorials are saying it.
            session['username']=username # Is it the right way to give the session a temporary id?
            print (session) #seems doesn't work, how can i know whether i'm in the session?
            # flash('Logged in successfully')
            # return render_template('login.html', form=form)
            return redirect(url_for('mypage'))

    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route('/logout')
@login_required         # means after user login?
def logout():
    session.pop('username',None)   # remove the username from the session
    print (session)
    flash('You were successfully logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
