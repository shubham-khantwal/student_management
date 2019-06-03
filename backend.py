import sqlite3

def studentresult():
    con = sqlite3.connect('studentrecord.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS studentrecord(id INTEGER PRIMARY KEY, \
                 stdid text , firstname text, surname text , coursecode text,\
                 maths text,english text,biology text,computing text,chemistry text,\
                 physics text,addmaths text,business text,totalscore text,average text,ranking text)')
    con.commit()
    con.close()

def addstdrec(stdid,firstname,surname,coursecode,maths,english,biology,computing,\
              chemistry,physics,addmaths,business,totalscore,average,ranking):
    con = sqlite3.connect('studentrecord.db')
    cur = con.cursor()
    cur.execute('INSERT INTO studentrecord VALUES (null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',\
                (stdid,firstname,surname,coursecode,maths,english,biology,computing,chemistry,\
                 physics,addmaths,business,totalscore,average,ranking))
    con.commit()
    con.close()

def viewdata():
    con = sqlite3.connect('studentrecord.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM studentrecord')
    rows = cur.fetchall()
    con.close()
    return rows

def deleterec():
    con = sqlite3.connect('studentrecord.db')
    cur = con.cursor()
    cur.execute('DELETE * FROM studentrecord WHERE id = ? ',(id))
    con.commit()
    con.close()
     
def searchdata(stdid='',firstname='',surname='',coursecode='',maths='',english='',biology='',computing='',chemistry='',physics='',addmaths='',business='',totalscore='',average='',ranking=''):
    con = sqlite3.connect('studentrecord.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM studentrecord WHERE  stdid = ? OR , firstname =? OR,coursecode=? OR,\
                 maths=? OR, english=? OR , biology=? OR, computing=? OR chemistry=? OR,physics=? OR,addmaths=? OR ,business =? OR ,\
                 totalscore=? OR,average=? OR,ranking=?',(stdid,firstname,surname,coursecode,maths,english,biology,computing,\
                                         chemistry,physics,addmaths,business,totalscore,average,ranking))
    rows.cur.fetchall()
    con.close()
    return rows

def updatedata(stdid='',firstname='',surname='',coursecode='',maths='',english='',biology='',computing='',chemistry='',physics='',addmaths='',business='',totalscore='',average='',ranking=''):
    con.sqlite3.connect('studentrecord.db')
    cur = con.cursor()
    cur.execute('UPDATE studentrecord SET stdid = ?, firstname=?,surname=?,coursecode=?,maths=?,\
                english=?,biology=?,computing=?,chemistry=?,physics=?,addmaths=?,business=?,totalscore=?,\
                average=?,ranking=?',(stdid,firstname,surname,coursecode,maths,english,biology,computing,\
                                      chemistry,physics,addmaths,business,totalscore,average,ranking))
    con.commit()
    con.close()


studentresult()
    
