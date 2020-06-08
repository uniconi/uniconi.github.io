from flask import Flask,jsonify
from flask_cors import CORS
import pickle
import os

app = Flask('table')
CORS(app)

table = { }
no=0
@app.route('/')
def plisk():
    global table,no
    if os.path.isfile('pbookdata.pickle'):
        file = open('pbookdata.pickle','rb')
        table = pickle.load(file)
        file.close()
        file1 = open('pbookdata1.pickle','rb')
        no = pickle.load(file1)
        file1.close()
        return jsonify(table)
    else:
        return jsonify(table)

@app.route('/add/<cate>/<per>/<name>/<title>/<genre>/<comment>')
def add(cate,per,name, title, genre, comment ):
    global no
    no = no + 1 
    table[str(no)]=cate,per,name,title, genre, comment
    save()
    return jsonify(table)

@app.route('/del/<no>')
def delete(no):
    del table[no]
    return jsonify(table)

def save():
    file=open('pbookdata.pickle', 'wb')
    pickle.dump(table,file)
    file.close()
    file1=open('pbookdata1.pickle', 'wb')
    pickle.dump(no,file1)
    file1.close()


@app.route('/load')
def load():
    global no
    file = open('pbookdata.pickle','rb')
    table = pickle.load(file)
    file.close()
    file1 = open('pbookdata1.pickle','rb')
    no = pickle.load(file1)
    file1.close()
    return jsonify(table)

app.run(host='203.255.186.215',port=9018)

