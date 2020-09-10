from flask import *
from shouhin import Shouhin,ShouhinDB

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/find')
def find():
    db = ShouhinDB()
    shouhins = db.get_all()
    db.close()
    return json.dumps(shouhins)

@app.route('/api/add',methods=['post'])
def add_post():
    sname = request.form['sname']
    tanka = request.form['tanka']
    db = ShouhinDB()
    s = Shouhin(0,sname,tanka)
    db.insert(s)
    db.close()
    return json.dumps({"result":True})

@app.route('/api/del',methods=['post'])
def del_post():
    sid = request.form['sid']
    db = ShouhinDB()
    db.delete(sid)
    db.close()
    return json.dumps({"result":True})

@app.route('/api/update',methods=['post'])
def update_post():
    sid = request.form['sid']
    sname = request.form['sname']
    tanka = request.form['tanka']
    
    db = ShouhinDB()
    s = Shouhin(sid,sname,tanka)
    db.update(s)
    db.close()
    return json.dumps({"result":True})

@app.route('/api/uriage')
def uriage():
    sid = request.args.get('sid')
    sdb = ShouhinDB()
    s = sdb.get(sid)
    sdb.close()

    udb = UriageDB()
    uriages = udb.find_by_sid(sid)
    udb.close()

    return json.dumps(uriages)

@app.route('/uadd',methods=['post'])
def uadd_post():
    sid = request.form['sid']
    kosu = request.form['kosu']

    db = UriageDB()
    u = Uriage(0,sid,kosu,None)
    db.insert(u)
    db.close()
    return json.dumps({"result":True})

app.run(debug=True)
