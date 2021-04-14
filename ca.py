import os
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#import all relevant libraries
from flask_migrate import Migrate
from forms import NewOrderForm
from datetime import date
from wtforms.validators import ValidationError, DataRequired, Length

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#connect to the server
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sha2user:Boot!camp2021!@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

#create the table for the sales order
class Order(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key= True)
    item = db.Column(db.Text)
    dateyr = db.Column(db.Date)
    datewk = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    empid = db.Column(db.Text)
    
    def __init__(self, item, dateyr, datewk, empid, quantity):
    
        self.item = item
        self.quantity = quantity
        self.dateyr = dateyr
        self.datewk = datewk
        self.empid = empid

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/NewOrder', methods=['GET', 'POST'])
def neworder():

    form = NewOrderForm()
#this is used to store the data into the table from the database
    if form.validate_on_submit():
        item = form.item.data
        dateyr = "2021"
        datewk = "14"
        empid = form.empid.data
        quantity = form.quantity.data
        new_order = Order(id, item, dateyr, datewk, empid, quantity)
        db.session.add(new_order)
        db.session.commit()

        flash("The order has been added.")
        return redirect(url_for('thankyou'))
    return render_template('neworder.html', form=form)
    


@app.route('/submitted') 
def thankyou():
    return render_template('thankyou.html')

def page_not_found(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
