from flask import Flask,render_template,url_for,request
from flask_mysqldb import MySQL

appp = Flask(__name__)
appp.config['MYSQL_HOST'] = 'localhost'
appp.config['MYSQL_USER'] = 'root'
appp.config['MYSQL_PASSWORD'] =''
appp.config['MYSQL_DB']='signup'
appp.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(appp)



@appp.route('/')
@appp.route('/home')
def home():
    return render_template('amazon.html')

@appp.route('/signin',methods=['GET','POST'])
def signin():
    if request.method=="POST":
        name=request.form.get('name')
        b=request.form.get('mobile')
        c=request.form.get('email')
        d=request.form.get('password')
        e=request.form.get('cpassword')
        cur=mysql.connection.cursor()
        cur.execute(
            "insert into sss(Name,Mobile,Email,Password,ConfirmPassword) values(%s,%s,%s,%s,%s)",(name,b,c,d,e)
        )
        mysql.connection.commit()
        cur.close()
    return render_template('signin.html')

@appp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        cur=mysql.connection.cursor()
        cur.execute(
            "select * from sss where Email=%s and Password=%s ",(email,password ))
        data=cur.fetchone()
        if data:
            return "valid user"
        else:
            return "invalid user"
    return render_template('signup.html')

@appp.route('/contactus',methods=['GET','POST'])
def contactus():
    if request.method=="POST":
        name=request.form.get('a')
        b=request.form.get('b')
        c=request.form.get('c')
        cur=mysql.connection.cursor()
        cur.execute("insert into e(Name,Mobileno,Feedback) values(%s,%s,%s)",(name,b,c))
        mysql.connection.commit()
        cur.close()
    return render_template('contactus.html')
    
if __name__=='__main__':
    appp.run()