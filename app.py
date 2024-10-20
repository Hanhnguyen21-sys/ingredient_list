import sqlite3
import random
from flask import Flask, session, render_template, request, g


app = Flask(__name__)
app.secret_key = "hnguyen"


#Session in flask allows to share data between different functions
@app.route('/',methods=['POST','GET'])
def index():
    #all_items: all ingridient in the store
    #alist : 5 random ingridients - LET CALL list A
    session['all_items'],session['alist'] = get_db()
    return render_template("index.html",all_items= session['all_items'], alist =session['alist'])

@app.route('/add_item',methods=["post"])
def add_item():
    #add item from the whole list into a list A
    session['alist'].append(request.form['select_items'])
    session.modified=True
    return render_template("index.html",all_items= session['all_items'], alist =session['alist'])

@app.route('/remove_item',methods=['POST'])
def remove_item():
    #collect all checkbox from html file
    # delete all of them
    checked_boxes = request.form.getlist("check")
    for item in checked_boxes:
        #check if the item exist in a list, then remove
        if item in session['alist']:
            i = session['alist'].index(item)
            session['alist'].pop(i)
            session.modified = True
    return render_template("index.html",all_items= session['all_items'], alist =session['alist'])


#the function connects to database
def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database = sqlite3.connect('ingredients.db')
    
        #we will fetch all information from database
    
        cursor = db.cursor()
        cursor.execute("select name from ingredient")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        a_list = all_data.copy()
        random.shuffle(a_list)
        a_list = a_list[:5]
    return all_data, a_list

#terminate database when we're done
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,'_database',None)
    if db is not None:
        db.close()
        
        
if __name__ =='__main__':
    app.run()