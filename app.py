from flask import Flask,request,render_template,session,redirect,flash,url_for
import mysql.connector
import requests
import pandas as pd
from flask_mail import *
import secrets
import smtplib
from datetime import datetime
import hashlib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from Crypto import Random
# from Crypto.Random import random
# from Crypto.PublicKey import ElGamal
# from Crypto.Util.number import GCD
from test1 import *
import blockchain


app=Flask(__name__)
app.config['SECRET_KEY']='lakshmi'
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    port=3306,
    database="tabe-dac-blockchain",
    charset='utf8'
)
mycursor = mydb.cursor()


@app.route("/")
def index():
    return render_template("index.html")
@app.route('/owner')
def owner():
    return render_template('owner.html')
@app.route('/ownerreg',methods=['POST','GET'])
def ownerreg():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        pwd=request.form['pwd']
        cpwd=request.form['cpwd']
        addr=request.form['addr']
        ph=request.form['ph']
        sql = "select * from owner"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed", "success")
            return render_template('owner.html')
        if (pwd == cpwd):
	    #blockchainprocess(name,email,pwd,ph)
            sql = "INSERT INTO owner (name,email,pwd,ph,addr) VALUES (%s,%s,%s,%s,%s)"
            val = (name,email,pwd,ph,addr)
            mycursor.execute(sql, val)
            mydb.commit()
            session['email'] = email
            flash("Successfully Registered", "warning")
            return render_template('owner.html')
        else:
            flash("Password and Confirm Password not same")
    return render_template('user.html',msg="registered successfully")

def blockchainprocess(s1,s2,s3,s4):
    blockchain = Blockchain()
    t1 = blockchain.new_transaction(s1, s2, s3)
    t2 = blockchain.new_transaction(s2, s4)
    blockchain.new_block(12345)
    t3 = blockchain.new_transaction(s1, s2, s3)
    t4 = blockchain.new_transaction(s2, s4)
    blockchain.new_block(6789)
    print("block: ", blockchain.chain)


@app.route('/authority')
def authority():
    return render_template('authority.html')

@app.route('/auhome')
def auhome():
    return render_template('auhome.html')

@app.route('/auback',methods=['POST', 'GET'])
def auback():

    if request.method == "POST":
        username = request.form['name']
        password1 = request.form['pwd']
        if username == 'authority' and password1 == 'authority' :
            return render_template('auhome.html')
        else:
            return render_template('authority.html')

    return render_template('authority.html')

@app.route("/viewowner")
def viewowner():
    sql = "select * from owner where sign='waiting' "
    x = pd.read_sql_query(sql, mydb)
    print(type(x))
    print(x)
    x = x.drop(['pwd'], axis=1)
    x = x.drop(['sign'], axis=1)
    return render_template("viewowner.html", col_name=x.columns.values, row_val=x.values.tolist())
@app.route('/signback/<s>/<s1>/<s2>')
def signback(s=0,s1='',s2=''):
    otp=secrets.token_urlsafe(16)
    msg='Hi'
    m1="Find a signature key which was sent through mail."
    m2='Here is the key---'
    mail_content = msg +' '+s1+'\n'+m1 + ',' + msg + m1 + m2 + otp
    sender_address = 'padmni.cse@gmail.com'
    sender_pass = 'lkzpsicfkidzzxkc'
    receiver_address = s2
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Dynamic Access Control Using Blockchain With An Encryption Scheme To Secure Information Stored In The Cloud'

    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    sql="update owner set sign='%s' where id='%s' "%(otp,s)
    mycursor.execute(sql)
    mydb.commit()
    flash("Signature successfully generted and sent to Owner Email","warning")
    return redirect(url_for('viewowner'))

@app.route('/ownerback',methods=['POST', 'GET'])
def ownerback():
    if request.method == "POST":
        email = request.form['email']
        password1 = request.form['pwd']
        sign = request.form['sign']
        print('p')
        sql = "select * from owner where email='%s' and pwd='%s' and sign='%s'" % (email, password1,sign)
        print('q')
        x = mycursor.execute(sql)
        print(x)
        results = mycursor.fetchall()
        print(results)
        global name
        session['email'] = email
        if len(results) > 0:
            flash("Welcome ", "primary")
            return render_template('ownerhome.html', msg=results[0][1])
        else:
            flash("Invali Email/Password ", "danger")
            return render_template('owner.html', msg="invalid value")

    return render_template('owner.html')
@app.route('/ownerhome')
def ownerhome():
    return render_template('ownerhome.html')

@app.route("/maliciousfiles")
def maliciousfiles():
    sql="select id,filename,status from attacker"
    data=pd.read_sql_query(sql,mydb)
    return render_template("maliciousfiles.html",col_name=data.columns.values, row_val=data.values.tolist())




@app.route('/upload')
def upload():
    return render_template('upload.html')
@app.route("/upback",methods=["POST","GET"])
def upback():
    if request.method=="POST":
        algorithmname = request.form['algorithmname']
        print(algorithmname)
        fname = request.form['fname']
        file =request.form['file']
        email = session.get('email')
        if algorithmname == 'sha1':
            now1 = datetime.now()
            dd = "text_files/" + file
            f = open(dd, "r")
            data = f.read()
            print('Upload Process....1')
            dataleee = len(data)
            datalen = int(len(data) / 2)
            print(datalen, len(data))
            g = 0
            a = ''
            b = ''
            c = ''
            for i in range(0, 2):
                if i == 0:
                    a = data[g: datalen:1]
                    # a=a.decode('utf-8')
                    print(a)
                    result = hashlib.sha1(a.encode())
                    hash1 = result.hexdigest()

                    print(hash1)
                    print("===================================")
                    # result = hashlib.sha1(a.encode())
                    # hash1 = result.hexdigest()
                    # print(hash1)
                    print("++++++++++++++++++++++++++")
                    # print(g)
                    # print(len(data))
                    # b = data[g: len(data):1]
                    # print(c)

            print(g)
            print(len(data))
            c = data[datalen: len(data):1]
            # c = c.decode('utf-8')
            print(c)
            print("===================================")
            print("*****************************")
            result = hashlib.sha1(c.encode())
            hash2 = result.hexdigest()
            print(hash2)

            now = datetime.now()
            now2 = datetime.now()
            currentDay = datetime.now().strftime('%Y-%m-%d')
            t1 = datetime.now().strftime('%H:%M:%S')
            mycursor = mydb.cursor()
            sql = "select * from data_files where fname='%s'" % (fname)
            result = pd.read_sql_query(sql, mydb)
            fname1 = result['fname'].values
            # prm1 = result['sname'].values

            if fname in fname1:
                flash("File with this name already exists", "danger")
                return render_template('upload.html')
            else:
                timer = now2 - now1
                sql = "INSERT INTO data_files (fname,email,block1,block2,hash1,hash2,date,time1,timer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (fname,email, a, c, hash1, hash2,currentDay,t1,timer)
                mycursor.execute(sql, val)
                mydb.commit()
                sql = "select * from data_files where time1='%s' " % (t1)
                x = pd.read_sql_query(sql, mydb)
                print("^^^^^^^^^^^^^")
                print(type(x))
                print(x)
                # x = x.drop(['demail'], axis=1)
                x = x.drop(['email'], axis=1)
                x = x.drop(['hash1'], axis=1)
                x = x.drop(['hash2'], axis=1)
                x = x.drop(['date'], axis=1)
                x = x.drop(['id'], axis=1)
                x = x.drop(['time1'], axis=1)
                flash("file uploaded successfully", "success")
                return render_template("upback.html", col_name=x.columns.values, row_val=x.values.tolist())
            flash('Somethig went wrong','info')
            return render_template('upload.html')
        elif algorithmname == 'sha256':
            now1 = datetime.now()
            dd = "text_files/" + file
            f = open(dd, "r")
            data = f.read()

            dataleee = len(data)
            datalen = int(len(data) / 2)
            print(datalen, len(data))
            g = 0
            a = ''
            b = ''
            c = ''
            for i in range(0, 2):
                if i == 0:
                    a = data[g: datalen:1]
                    # a=a.decode('utf-8')
                    print(a)
                    result = hashlib.sha256(a.encode())
                    hash1 = result.hexdigest()

                    print(hash1)
                    print("===================================")
                    # result = hashlib.sha1(a.encode())
                    # hash1 = result.hexdigest()
                    # print(hash1)
                    print("++++++++++++++++++++++++++")
                    # print(g)
                    # print(len(data))
                    # b = data[g: len(data):1]
                    # print(c)

            print(g)
            print(len(data))
            c = data[datalen: len(data):1]
            # c = c.decode('utf-8')
            print(c)
            print("===================================")
            print("*****************************")
            result = hashlib.sha256(c.encode())
            hash2 = result.hexdigest()
            print(hash2)

            now = datetime.now()
            now2 = datetime.now()
            currentDay = datetime.now().strftime('%Y-%m-%d')
            t1 = datetime.now().strftime('%H:%M:%S')
            mycursor = mydb.cursor()
            sql = "select * from data_files where fname='%s'" % (fname)
            result = pd.read_sql_query(sql, mydb)
            fname1 = result['fname'].values
            # prm1 = result['sname'].values

            if fname in fname1:
                flash("File with this name already exists", "danger")
                return render_template('upload.html')
            else:
                timer= now2-now1
                sql = "INSERT INTO data_files (fname,email,block1,block2,hash1,hash2,date,time1,timer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (fname, email, a, c, hash1, hash2, currentDay, t1, timer)
                mycursor.execute(sql, val)
                mydb.commit()
                sql = "select * from data_files where time1='%s' " % (t1)
                x = pd.read_sql_query(sql, mydb)
                print("^^^^^^^^^^^^^")
                print(type(x))
                print(x)
                # x = x.drop(['demail'], axis=1)
                x = x.drop(['email'], axis=1)
                x = x.drop(['hash1'], axis=1)
                x = x.drop(['hash2'], axis=1)
                x = x.drop(['date'], axis=1)
                x = x.drop(['id'], axis=1)
                x = x.drop(['time1'], axis=1)
                flash("file uploaded successfully", "success")
                return render_template("upback.html", col_name=x.columns.values, row_val=x.values.tolist())
            flash('Somethig went wrong', 'info')
            return render_template('upload.html')
        elif algorithmname == 'elgamal':
            now1 = datetime.now()

            dd = "text_files/" + file
            f = open(dd, "r")
            data = f.read()
            print("============================")
            print(data)
            q = random.randint(pow(10, 20), pow(10, 50))
            g = random.randint(2, q)
            key = gen_key(q)  # Private key for receiver
            h = power(g, key, q)
            print("g used : ", g)
            print("g^a used : ", h)
            print("privatekey : ", key)
            en_msg, p, k = encrypt(data, q, h, g)
            print("senderkey", k)
            dr_msg = decrypt(en_msg, p, key, q)
            dmsg = ''.join(dr_msg)
            print("Decrypted Message :", dmsg);
            print("sender key : ", k)
            print("============================")
            now = datetime.now()
            currentDay = datetime.now().strftime('%Y-%m-%d')
            t1 = datetime.now().strftime('%H:%M:%S')
            datalen = int(len(data) / 2)
            print(datalen, len(data))
            g = 0
            a = ''
            b = ''
            c = ''
            for i in range(0, 2):
                if i == 0:
                    a = data[g: datalen:1]
                    # a=a.decode('utf-8')
                    print(a)
                    print("===================================")

                    print("++++++++++++++++++++++++++")


            print(g)
            print(len(data))
            c = data[datalen: len(data):1]

            print(c)
            print("===================================")
            print("*****************************")
            now2 = datetime.now()

            mycursor = mydb.cursor()
            sql = "select * from data_files where fname='%s'" % (fname)
            result = pd.read_sql_query(sql, mydb)
            fname1 = result['fname'].values
            # prm1 = result['sname'].values

            if fname in fname1:
                flash("File with this name already exists", "danger")
                return render_template('upload.html')
            else:
                timer = now2 - now1
                sql = "INSERT INTO data_files (fname,email,block1,block2,hash1,hash2,date,time1,timer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (fname, email, a, c, key, key, currentDay, t1,timer)
                mycursor.execute(sql, val)
                mydb.commit()
                sql = "select * from data_files where time1='%s' " % (t1)
                x = pd.read_sql_query(sql, mydb)
                print("^^^^^^^^^^^^^")
                print(type(x))
                print(x)
                # x = x.drop(['demail'], axis=1)
                x = x.drop(['email'], axis=1)
                x = x.drop(['hash1'], axis=1)
                x = x.drop(['hash2'], axis=1)
                x = x.drop(['date'], axis=1)
                x = x.drop(['id'], axis=1)
                x = x.drop(['time1'], axis=1)
                flash("file uploaded successfully", "success")
                return render_template("upback.html", col_name=x.columns.values, row_val=x.values.tolist())
            flash('Somethig went wrong', 'info')
            return render_template('upload.html')
    return render_template('upload.html')

@app.route('/viewdata')
def viewdata():
    email=session.get('email')
    sql = "select * from data_files where email='%s' "%(email)
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['email'], axis=1)
    x = x.drop(['block1'], axis=1)
    x = x.drop(['block2'], axis=1)
    x = x.drop(['hash1'], axis=1)
    x = x.drop(['hash2'], axis=1)
    return render_template("viewdata.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/user')
def user():
    return render_template('user.html')
@app.route('/userreg',methods=['POST','GET'])
def userreg():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        pwd=request.form['pwd']
        cpwd=request.form['cpwd']
        sql = "select * from user"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("email already existed", "success")
            return render_template('user.html')
        if (pwd == cpwd):
            sql = "INSERT INTO user (name,email,pwd) VALUES (%s,%s,%s)"
            val = (name,email,pwd)
            mycursor.execute(sql, val)
            mydb.commit()
            session['email'] = email
            flash("Successfully Registered", "warning")
            return render_template('user.html')
        else:
            flash("Password and Confirm Password not same")
    return render_template('user.html',msg="registered successfully")

@app.route('/userback',methods=['POST', 'GET'])
def userback():
    if request.method == "POST":

        email = request.form['email']

        password1 = request.form['pwd']
        sign = request.form['skey']
        print('p')

        sql = "select * from user where email='%s' and pwd='%s' and skey='%s'" % (email, password1,sign)
        print('q')
        x = mycursor.execute(sql)
        print(x)
        results = mycursor.fetchall()
        print(results)
        global name
        session['email'] = email
        if len(results) > 0:
            flash("Welcome ", "primary")
            return render_template('userhome.html', msg=results[0][1])
        else:
            flash("Invali Email/Password ", "danger")
            return render_template('user.html')

    return render_template('user.html')


@app.route("/viewusers")
def viewusers():
    sql = "select * from user where skey='pending' "
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['pwd'], axis=1)
    x = x.drop(['skey'], axis=1)
    return render_template("viewusers.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/skey/<s>/<s1>/<s2>')
def skey(s=0,s1='',s2=''):
    otp=  secrets.token_hex(4)
    msg='Hi'
    m1="Find a Secret key which was sent through mail."
    m2='Here is the SKID---'
    mail_content = msg +' '+s1+'\n'+m1 + ',' + msg + m1 + m2 + otp
    sender_address = 'padmni.cse@gmail.com'
    sender_pass = 'lkzpsicfkidzzxkc'
    receiver_address = s2
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Dynamic Access Control Using Blockchain With An Encryption Scheme To Secure Information Stored In The Cloud'

    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    sql="update user set skey='%s' where id='%s' "%(otp,s)
    mycursor.execute(sql)
    mydb.commit()
    flash("Secret key generated and sent to user Email","warning")
    # return render_template('viewusers.html')
    return  redirect(url_for('viewusers'))

@app.route('/userhome')
def userhome():
    return render_template('userhome.html')

@app.route('/vfile')
def vfile():
    email=session.get('email')
    sql = "select * from data_files"
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['email'], axis=1)
    x = x.drop(['block1'], axis=1)
    x = x.drop(['block2'], axis=1)
    x = x.drop(['hash1'], axis=1)
    x = x.drop(['hash2'], axis=1)
    x = x.drop(['time1'], axis=1)
    x = x.drop(['date'], axis=1)

    return render_template("vfile.html", col_name=x.columns.values, row_val=x.values.tolist())
@app.route('/req/<s>/<s1>')
def req(s=0,s1=''):
    email=session.get('email')
    sql="insert into request_files(id,fname,email) values(%s,%s,%s)"
    val=(s,s1,email)
    mycursor.execute(sql,val)
    mydb.commit()
    flash("Request sended to Cloud Provider","warning")
    # return render_template('viewusers.html')
    return  redirect(url_for('vfile'))
@app.route('/cp')
def cp():
    return render_template('cp.html')

@app.route('/cpback',methods=['POST', 'GET'])
def cpback():

    if request.method == "POST":
        username = request.form['name']
        password1 = request.form['pwd']
        if username == 'cloud' and password1 == 'cloud':
            return render_template('cphome.html')
        elif username=='user@gmail.com' and password1=='User@12345678':
            return render_template('attacker.html')
        else:
            flash('Invalid credentials','danger')
            return render_template('cp.html')

    return render_template('cp.html')



@app.route("/attackfile",methods=["POST","GET"])
def attackfile():
    if request.method=="POST":
        try:
            fname = request.form['fname']
            print(fname)
            sql = "select fname,email from data_files where fname='%s'"%(fname)
            mycursor.execute(sql)
            d = mycursor.fetchall()
            print(d)
            filname = d[0][0]
            owneremail= d[0][1]
            s = "select * from owner where email='%s'"%(owneremail)
            mycursor.execute(s)
            d1 = mycursor.fetchall()
            print(d1)
            contact = d1[0][4]
            url = "https://www.fast2sms.com/dev/bulkV2"

            message = 'ALERT:Unauthorised person trying to access your file'
            no = "8500141612"
            data = {
                "route": "q",
                "message": message,
                "language": "english",
                "flash": 0,
                "numbers": no,
            }

            headers = {
                "authorization": "wQeWmH3RV01Lr5CbphuvnN9TytsdfoYgBcaXKODUxPE2M4qJklMZvhnOu5pJm70QKfo3IgSVcxYqeLwN",
                "Content-Type": "application/json"
            }

            response = requests.post(url, headers=headers, json=data,verify=True)
            print(response)
            status="Trying to attack"
            sq="insert into attacker(filename,owneremail,status)values(%s,%s,%s)"
            val = (filname,owneremail,status)
            mycursor.execute(sq,val)
            mydb.commit()
        except:
            return render_template("attacked.html",msg="WARNING:Unauthorised Access")
    return render_template("attacked.html")

@app.route('/cphome')
def cphome():
    return render_template('cphome.html')

@app.route('/vusers')
def vusers():
    sql="select * from user"
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['pwd'], axis=1)
    x = x.drop(['skey'], axis=1)
    return render_template('vusers.html',col_name=x.columns.values,row_val=x.values.tolist())

@app.route('/viewfile')
def viewfile():
    email=session.get('email')
    sql = "select * from data_files"
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['block1'], axis=1)
    x = x.drop(['block2'], axis=1)
    x = x.drop(['hash1'], axis=1)
    x = x.drop(['hash2'], axis=1)

    return render_template("viewfile.html", col_name=x.columns.values, row_val=x.values.tolist())
@app.route('/vreq')
def vreq():
    email=session.get('email')
    sql = "select * from request_files where status='request'"
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['status'], axis=1)
    x = x.drop(['skey'], axis=1)

    return render_template("vreq.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/vreq1/<s>/<s1>/<s2>')
def vreq1(s=0,s1=0,s2=''):
    otp = random.randint(000000, 999999)
    # otp = s1 = secrets.token_hex(4)
    msg = 'Hi Dear'
    m1 = "Find a Decrypted key which was sent through mail."
    m2 = 'Here is the Key:'
    mail_content = msg +' '+'\n'+m1 + ',' + msg + m1 + m2 +str(otp)
    sender_address = 'padmni.cse@gmail.com'
    sender_pass = 'lkzpsicfkidzzxkc'
    receiver_address = s2
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Dynamic Access Control Using Blockchain With An Encryption Scheme To Secure Information Stored In The Cloud'

    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    sql = "update request_files set skey='%s',status='Accepted' where id='%s' " % (otp, s)
    mycursor.execute(sql)
    mydb.commit()
    flash("Decrypted key generated and sent to user Email", "warning")
    # return render_template('viewusers.html')
    return redirect(url_for('vreq'))

@app.route("/down")
def down():
    email = session.get('email')
    sql = "select * from request_files where status='Request' and email='%s' " % (email)
    x = pd.read_sql_query(sql, mydb)

    x = x.drop(['email'], axis=1)
    x = x.drop(['status'], axis=1)
    x = x.drop(['skey'], axis=1)

    # x["View Data"] = " "
    # x["Send Request"] = ""

    return render_template("down.html", col_name=x.columns.values, row_val=x.values.tolist())
@app.route("/download/<s>/<s1>")
def download(s=0,s1=0):
    global g,f1,a1
    g=s
    f1=s1

    return render_template("download.html",g=g,f1=f1)


@app.route("/downfile",methods=['POST','GET'])
def downfile():
    print("dfhlksokhso")
    if request.method == 'POST':
        print("gekjhiuth")
        sno = request.form['sno']
        id = request.form['id']
        skey = request.form['s1']

        sql = "select count(*),CONCAT(block1,block2,'') from data_files,request_files where data_files.id='"+id+"' and request_files.id='"+id+"' and request_files.skey='"+skey+"' "
        x = pd.read_sql_query(sql, mydb)
        count=x.values[0][0]
        print(count)
        asss=x.values[0][1]
        asss=asss.decode('utf-8')

        print("^^^^^^^^^^^^^")
        if count==0:
            flash("Enter Valid Key","danger")
            return redirect(url_for('download'))
        else:
            return render_template("downfile.html", msg=asss)

    return render_template("downfile.html")

@app.route('/rfile')
def rfile():
    email=session.get('email')
    sql = "select * from data_files"
    x = pd.read_sql_query(sql, mydb)
    print("^^^^^^^^^^^^^")
    print(type(x))
    print(x)
    x = x.drop(['block1'], axis=1)
    x = x.drop(['block2'], axis=1)
    x = x.drop(['hash1'], axis=1)
    x = x.drop(['hash2'], axis=1)

    return render_template("rfile.html", col_name=x.columns.values, row_val=x.values.tolist())
#################################################################################################################



if __name__=="__main__":
    app.run(debug=True)
