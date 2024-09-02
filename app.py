from flask import redirect,url_for,Flask, request,render_template,make_response
import sqlite3

app = Flask(__name__)
def cee(eid):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    query = "SELECT 1 FROM empl WHERE eid = ? LIMIT 1"
    cursor.execute(query, (eid,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
def cce(cid):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    query = "SELECT 1 FROM clients WHERE cid = ? LIMIT 1"
    cursor.execute(query, (cid,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
def ccoe(consid):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    query = "SELECT 1 FROM consult WHERE consid = ? LIMIT 1"
    cursor.execute(query, (consid,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
@app.route('/efindo') 
def efindo():
     EID = request.cookies.get('EID')
     EID=str(EID)
     if EID=="1" or EID==1 or EID=="1" :
       con = sqlite3.connect("db.db")
       eid = request.args.get('eid')
       cur = con.cursor()
       cur.execute("SELECT * FROM empl WHERE eid=(?)",[eid])
       rows=list(cur.fetchall())
       rows=rows[0]
       return render_template('efindo.html',rows=rows)
     else:return redirect(url_for("dhome"))


@app.route('/addcl') 
def addcl():
     EID = request.cookies.get('EID')
     EID=str(EID)
     if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
     else:return render_template('addcl.html',EID=EID)
@app.route('/addstaff') 
def addstaff():
     EID = request.cookies.get('EID')
     EID=str(EID)
     if EID=="1" or EID==1 :return render_template('addstaff.html',EID=EID)
     else:
       err="utilisateur non autoriser pour faire cette operation"
       return render_template('dhome.html',err=err,)
@app.route('/') 
def login():
     resp = make_response(render_template('login.html'))
     resp.delete_cookie('EID')
     return resp

@app.route('/checko') 
def checko():
     err="id ou motdepass incorrect"
     eid = request.args.get('sid')
     if cee(eid):
       mtp = request.args.get('pass')
       con = sqlite3.connect("db.db")
       cur = con.cursor()
       cur.execute("SELECT * FROM empl WHERE eid=(?)",[eid])
       sdata=list(cur.fetchall())
       sdata=sdata[0]
       if sdata[10]==mtp:
         resp = make_response(render_template('dhome.html'))
         resp.set_cookie("EID",eid)
         return resp
	
       else: return render_template('login.html',err=err,)
     else: return render_template('login.html',err=err,)
@app.route('/cpn') 
def cpn():
     EID = request.cookies.get('EID')
     EID=str(EID)
     if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
     else:
       name = request.args.get('name')
       con = sqlite3.connect("db.db")
       cur = con.cursor()
       name="%"+str(name)+"%"
       cur.execute("SELECT * FROM clients WHERE name LIKE ?", (name,))
       rows = cur.fetchall()
       row=list(rows)
       j=0
       for i in row:
          row[j]=list(row[j])
          j=j+1
       rows=row
       con.close()
       return render_template("cpn.html",rows=rows)
@app.route('/addar') 
def addar():
     EID = request.cookies.get('EID')
     EID=str(EID)
     if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
     else:return render_template('addar.html',EID=EID)
@app.route('/dhome') 
def dhome():
     EID = request.cookies.get('EID')
     if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
     else:return render_template('dhome.html')
@app.route('/consultation')
def consultation():
     EID = request.cookies.get('EID')
     EID=str(EID)
     if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
     else:
      con = sqlite3.connect("db.db")
      cur3=con.cursor()
      cur4=con.cursor()
      cur3.execute("SELECT sname FROM services WHERE stype = ? ",("medicaments",))
      cur4.execute("SELECT sname FROM services WHERE stype = ? OR stype = ?",("analyses","Radio",))
      sname=list(cur3.fetchall())
      aname=list(cur4.fetchall())
      sname=list(sname)
      aname=list(aname) 
      j=0
      for name in sname:
       sname[j]=list(sname[j])[0]
       j=j+1
      j=0
      for name in aname:
       aname[j]=list(aname[j])[0]
       j=j+1
      return render_template('consultation.html',EID=EID,sname=sname,aname=aname)

@app.route('/cartei')
def cartei():
     EID = request.cookies.get('EID')
     cid = request.args.get('cid')
     con = sqlite3.connect("db.db")
     cur2=con.cursor()
     cur2.execute("SELECT * FROM clients WHERE cid=(?)",[cid])
     rows = list(cur2.fetchall())
     if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
     else:return render_template('carte.html',rows=rows)
@app.route('/scartei')
def scartei():
     EID = request.cookies.get('EID')
     con = sqlite3.connect("db.db")
     cur2=con.cursor()
     cur2.execute("SELECT * FROM empl ORDER BY eid DESC LIMIT 1;")
     rows = list(cur2.fetchall())
     if EID==1 or EID=="1":return render_template('scarte.html',rows=rows)
     else:return redirect(url_for("login"))    

@app.route('/insertion')

def insertion():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
    name = request.args.get('name')
    dob = request.args.get('dob')
    iobs = request.args.get('iobs')
    tel = request.args.get('tel')
    rh = request.args.get('rh')
    eid = request.args.get('eid')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur2=con.cursor()
    cur.execute("INSERT INTO clients (tel,name,dob,iobs,rh,eid)VALUES (?,?,?,?,?,?)",(tel,name,dob,iobs,rh,eid) )
    con.commit()
    cur2.execute("SELECT * FROM clients ORDER BY cid DESC LIMIT 1;")
    rows = list(cur2.fetchall())
    return render_template('carte.html',rows=rows)
@app.route('/sinsertion')

def sinsertion():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
    ename = request.args.get('ename')
    edob = request.args.get('edob')
    etel = request.args.get('etel')
    
    etype = request.args.get('etype')
    esubtype = request.args.get('esubtype')
    edoj = request.args.get('edoj')
    nsc = request.args.get('nsc')
    nid = request.args.get('nid')
    adress = request.args.get('adress')
    mtp = request.args.get('mtp')
    rh = request.args.get('rh')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur2=con.cursor()
    cur.execute("INSERT INTO empl (ename,edob,etel,etype,esubtype,edoj,nsc,nid,adress,mtp,rh)VALUES (?,?,?,?,?,?,?,?,?,?,?)",(ename,edob,etel,etype,esubtype,edoj,nsc,nid,adress,mtp,rh) )
    con.commit()
    cur2.execute("SELECT * FROM empl where nid=?",(nid,))
    rows = list(cur2.fetchall())
    return render_template("scarte.html",rows=rows) 

@app.route('/inranal')

def inranal():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
    cid = request.args.get('cid')
    sid = request.args.get('sid')
    atype = request.args.get('atype')
    aval = request.args.get('aval')
    norm = request.args.get('norm')
    obs = request.args.get('obs')
    dateofan = request.args.get('dateofan')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO anal (cid,sid,atype,aval,norm,obs,dateofan)VALUES (?,?,?,?,?,?,?)",(cid,sid,atype,aval,norm,obs,dateofan) )         
    con.commit()
    return redirect(url_for("addar")) 
@app.route('/facture')

def facture():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
    cid = request.args.get('cid')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM vfacture where cid=?",(cid,))
    rowv = list(cur.fetchall())
    cur1 = con.cursor()
    cur1.execute("SELECT * FROM sfacture where cid=?",(cid,))
    rows = list(cur1.fetchall())
    ttv=0
    j=0
    for i in rowv :
      rowv[j]=list(rowv[j])
      ttv=ttv+rowv[j][1]
      j=j+1
    tts=0
    k=0
    for i in rows :
      rows[k]=list(rows[k])
      tts=tts+rows[k][6]
      k=k+1  
    ttr=tts-ttv
    cur3=con.cursor()
    cur4=con.cursor()
    cur5=con.cursor()
    cur3.execute("SELECT name FROM clients WHERE cid=(?)",[cid])
        
    cur4.execute("SELECT dob FROM clients WHERE cid=(?)",[cid])
    cur5.execute("SELECT tel FROM clients WHERE cid=(?)",[cid])
    cname = list(cur3.fetchall())

    cname=list(cname)[0][0]
    dob = list(cur4.fetchall())
    dob=dob[0][0]  
    tel = list(cur5.fetchall())
    tel=tel[0][0]  
    rows.reverse()
    rowv.reverse()
    cur3.execute("SELECT sname FROM services")
    sname=list(cur3.fetchall())
    sname=list(sname)
    j=0
    for name in sname:
       sname[j]=list(sname[j])[0]
       j=j+1


    return render_template("facture.html",sname=sname,cname=cname,dob=dob,tel=tel,cid=cid,rows=rows,rowv=rowv,ttr=ttr,ttv=ttv,tts=tts)
    
@app.route('/coinsertion')

def coinsertion():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
   cid= request.args.get('cid')
   if cce(cid):
    did= request.args.get('did')
    cobs= request.args.get('cobs')
    dep= request.args.get('dep')
    doc= request.args.get('doc')
    med1= request.args.get('med1')
    dose1= request.args.get('dose1')
    med2= request.args.get('med2')
    dose2= request.args.get('dose2')
    med3= request.args.get('med3')
    dose3= request.args.get('dose3')
    med4= request.args.get('med4')
    dose4= request.args.get('dose4')
    med5= request.args.get('med5')
    dose5= request.args.get('dose5')
    med6= request.args.get('med6')
    dose6= request.args.get('dose6')
    med7= request.args.get('med7')
    dose7= request.args.get('dose7')
    med8= request.args.get('med8')
    dose8= request.args.get('dose8')
    med9= request.args.get('med9')
    dose9= request.args.get('dose9')
    med10= request.args.get('med10')
    dose10= request.args.get('dose10')
    ana1= request.args.get('ana1')
    ana2= request.args.get('ana2')
    ana3= request.args.get('ana3')
    ana4= request.args.get('ana4')
    ana5= request.args.get('ana5')
    ana6= request.args.get('ana6')
    ana7= request.args.get('ana7')
    ana8= request.args.get('ana8')
    ana9= request.args.get('ana9')
    ana10= request.args.get('ana10')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur2=con.cursor()
    cur3=con.cursor()
    cur4=con.cursor()
    cur.execute("INSERT INTO consult (cid,did,cobs,dep,doc,med1,dose1,med2,dose2,med3,dose3,med4,dose4,med5,dose5,med6,dose6,med7,dose7,med8,dose8,med9,dose9,med10,dose10,ana1,ana2,ana3,ana4,ana5,ana6,ana7,ana8,ana9,ana10)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(cid,EID,cobs,dep,doc,med1,dose1,med2,dose2,med3,dose3,med4,dose4,med5,dose5,med6,dose6,med7,dose7,med8,dose8,med9,dose9,med10,dose10,ana1,ana2,ana3,ana4,ana5,ana6,ana7,ana8,ana9,ana10) )            
    con.commit()
    cur2.execute("SELECT * FROM consult ORDER BY cid DESC LIMIT 1;")
    rows = list(cur2.fetchall())
    cur3.execute("SELECT name FROM clients WHERE cid=(?)",[cid])
    cur4.execute("SELECT dob FROM clients WHERE cid=(?)",[cid])
    name = list(cur3.fetchall())
    name=name[0][0]
    dob = list(cur4.fetchall())
    dob=dob[0][0]
    rows=rows[0]
    return render_template('ordanance.html',rows=rows,name=name,dob=dob)
   else:
    err="id client inccorect insertion impossible"
    return render_template("dhome.html",err=err)
@app.route('/fv',methods=['GET'])
def fv():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
    cid = request.args.get('cid')
    date = request.args.get('date')
    mnt=request.args.get('mnt')
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO vfacture (cid,by,date,mnt)VALUES (?,?,?,?)",(cid,EID,date,mnt,))
    con.commit()
    return redirect(url_for("facture",cid=cid))
@app.route('/addser',methods=['GET'])
def addser():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
    cid = request.args.get('cid')
    sname = request.args.get('sname')
    date=request.args.get('date')
    qty=request.args.get('qty')
    qty=int(qty)
    con = sqlite3.connect("db.db")
    cur2 = con.cursor()
    cur3= con.cursor()
    cur2.execute("SELECT * FROM services WHERE sname=(?)",(sname,))
    rows = list(cur2.fetchall())[0]

    cur3.execute("INSERT INTO sfacture (cid,by,sn,qty,sp,tp,date)VALUES (?,?,?,?,?,?,?)",(cid,EID,rows[1],qty,rows[3],int(rows[3]*qty),date))
    con.commit()
    return redirect(url_for("facture",cid=cid))
@app.route('/findo',methods=['GET'])
def findo():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
    cid = request.args.get('cid')
    if cce(cid) :
      con = sqlite3.connect("db.db")
      cur0= con.cursor()
      cur= con.cursor()
      cur1= con.cursor()
      cur2= con.cursor()
      cur3 = con.cursor()
      cur4 = con.cursor()
      cur5 = con.cursor()
      cur6 = con.cursor()
      cur8 = con.cursor()
      cur9 = con.cursor()
      cur.execute("SELECT name FROM clients WHERE cid=(?)",[cid])
      cur1.execute("SELECT dob FROM clients WHERE cid=(?)",[cid])
      cur2.execute("SELECT tel FROM clients WHERE cid=(?)",[cid])
      cur3.execute("SELECT iobs FROM clients WHERE cid=(?)",[cid])
      cur4.execute("SELECT atype FROM anal WHERE cid=(?)",[cid])
      cur5.execute("SELECT aval FROM anal WHERE cid=(?)",[cid])
      cur6.execute("SELECT dateofan FROM anal WHERE cid=(?)",[cid])
      cur8.execute("SELECT analid FROM anal WHERE cid=(?)",[cid])
      cur9.execute("SELECT rh FROM clients WHERE cid=(?)",[cid])
      name=cur.fetchone()[0]
      dob=cur1.fetchone()[0]
      tel=cur2.fetchone()[0]
      iobs=cur3.fetchone()[0]
      rh=cur9.fetchone()[0]
      atype=cur4.fetchall()
      aval=cur5.fetchall()
      dateofan=cur6.fetchall()
      analid=cur8.fetchall()

      cur11= con.cursor()
      cur22= con.cursor()
      cur33 = con.cursor()
      cur33.execute("SELECT dep FROM consult WHERE cid=(?)",[cid])
      cur11.execute("SELECT doc FROM consult WHERE cid=(?)",[cid])
      cur22.execute("SELECT consid FROM consult WHERE cid=(?)",[cid])

      deplist=cur33.fetchall()
      doclist=cur11.fetchall()
      considlist=cur22.fetchall()
      return render_template('find.html',rh=rh,cid=cid,atype=atype,dateofan=dateofan,analid=analid,name=name,dob=dob,tel=tel,iobs=iobs,deplist=deplist,doclist=doclist,considlist=considlist,)
    else : 
      err="client non existant"
      return render_template("dhome.html",err=err,)
@app.route('/consview')
def consview():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
   consid = request.args.get('consid')
   if ccoe(consid):
    
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM consult WHERE consid=(?)",[consid])
    rows = list(cur.fetchall())
    cur.execute("SELECT * FROM consult WHERE consid=(?)",[consid])
    return render_template("consview.html",rows=rows,)
   else:
    err="consultation non existante" 
    return render_template("dhome.html",err=err)
@app.route('/analprint')
def analprint():
  EID = request.cookies.get('EID')
  EID=str(EID)
  if EID=="" or EID==0 or EID=="0" or EID=="None":return redirect(url_for("login"))
  else:
   con = sqlite3.connect("db.db")
   cur2=con.cursor()
   coid=request.args.get("coid")
   cur2.execute("SELECT * FROM consult WHERE consid=(?)",(coid,))
   rows = list(cur2.fetchone())
   cur2.execute("SELECT name FROM clients WHERE cid=(?)",(rows[1],))
   nm = list(cur2.fetchone())
   cur2.execute("SELECT dob FROM clients WHERE cid=(?)",(rows[1],))
   dob = list(cur2.fetchone())
   rows = nm +dob+rows
   for i in range(3,13) : rows.pop(i)
   return render_template("analprint.html",rows=rows)
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("dhome")), 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
