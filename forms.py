from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField

class NewOrderForm(FlaskForm):
    empid = StringField('Employer ID:', validators = [DataRequired ()])
    item = SelectField('Select the item: ')
    dateyr = DateField('Enter the date: ', format='%Y', validators = [DataRequired ()])
    dateyr = IntegerField('Enter the date: ', format='%Y', validators = [DataRequired ()])
    quantity = IntegerField('Enter the quantity of the item:', validators = [DataRequired ()])
    submit = SubmitField('Submit')