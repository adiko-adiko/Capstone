import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from forms import NewOrderForm///
from datetime import date

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sha2user:Boot!camp2021!@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)
'''
class Order(db.Model):

    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key= True)
    item = db.Column(db.Text)
    dateyr = db.Column(db.Date)
    datewk = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    empid = db.Column(db.Text)
  #  robot = db.Column(db.Boolean)
  #  owner = db.relationship('Owner', backref='puppy', uselist=False)
    
    
    def __init__(self, item, dateyr, datewk, empid, quantity):
    
        self.item = item
        self.quantity = quantity
        self.dateyr = dateyr
        self.datewk = datewk
        self.empid = empid

'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if form.validate_on_submit():
        return redirect(url_for('neworder'))
    return render_template('index.html')

@app.route('/NewOrder', methods=['GET', 'POST'])
def neworder():

    form = NewOrderForm()

    if form.validate_on_submit():
        item = form.item.data
        dateyr = "2021"
        datewk = "14"
        empid = form.empid.data
        quantity = form.quantity.data
        new_order = Order(item, dateyr, datewk, empid, quantity)
        db.session.add(new_order)
        db.session.commit()

        flash("The order has been added.")
        return redirect(url_for('neworder'))
    return render_template('neworder.html', form=form)
    
@app.route('/salesorder')
def listorders():
  
    Orders = Order.query.all()
    return render_template('orderadded.html', Orders=Orders)

def page_not_found(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
