from flask import *
import pymysql as p
from DBMS import insertData,getConnection,selectAllStd,deleteData,selectStdById,updateData
import email

f=Flask(__name__)
f.secret_key = 'dd0816f5175444f8b564fe220751307a'

@f.route('/') 
@f.route('/login')
def login():
    return render_template("login.html")
  
@f.route("/home")
def home():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        return render_template('home.html')  #templates

@f.route("/reg")
def register():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@f.route('/addStd',methods=['POST'])
def add_Std():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        id=request.form['id']
        name=request.form['name']
        fathername=request.form['fathername']
        mothername=request.form['mothername']
        course=request.form['course']
        contact=request.form['contact']
        address=request.form['address']
        email=request.form['email']
        password=request.form['password']
    # print(id,name,fathername,mothername,course,contact,address,email,password)
        t=(id,name,fathername,mothername,course,contact,address,email,password)
        insertData(t)
        return render_template('home.html')   

@f.route("/stdlist")
def std_list():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        sl=selectAllStd()
        print('--------------> ',sl)
        return render_template('stdlist.html',stdlist=sl)

@f.route('/deleteStd')
def delete_std():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        id=request.args.get('id')
        deleteData(id)
        return redirect('/stdlist')

@f.route('/editStd')
def edit_Std():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        id=request.args.get('id')
        std=selectStdById(id)
        return render_template('updateStd.html',s=std)

@f.route('/updateStd', methods=['POST'])
def update_Std():
    id=request.form['id']
    name=request.form['name']
    fathername=request.form['fathername']
    mothername=request.form['mothername']
    course=request.form['course']
    contact=request.form['contact']
    email=request.form['email']
    address=request.form['address']
    password=request.form['password']
    t=(name,fathername,mothername,course,contact,address,email,password,id)
    updateData(t)
    return redirect('/stdlist')
@f.route('/check_user', methods = ['POST'])
def checkUser():
    username= request.form['username']
    password = request.form['password']
    db = getConnection()
    cr = db.cursor()
    cr.execute("select * from Admin where username = '"+username+"' AND password ='"+password+"'")
    user=cr.fetchone()
    print(user)
    if user is not None:
        session['username'] = request.form['username']
        print(session['username'])
        return redirect(url_for('home'))
    else:
        return """
 <h1 style='color:red'; font-family:cursive;>You have Entered Wrong Email or password </h1>
 <h1 style='color:red'; font-family:cursive;>Please Try Again Later</h1>
 <a href="/" style="text-decoration:none;color:white; border:1px solid; background-color:blue; padding:12px; margin:20px; border-radius: 7px;  font-family:cursive;">Login Again</a>
 """
    
@f.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login')) 

if __name__=='__main__':
    f.run(debug=True)
