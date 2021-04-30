from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length



class NewOrderForm(FlaskForm):
    empid = StringField('Employer ID:', validators = [DataRequired(), Length(min=6, max=6, message='Please, enter the correct employee ID ')])
    item = StringField('Enter the product ID: ', [DataRequired(), Length(min=6, max=8, message='And/Or Please, enter the correct product ID.')])
    dateyr = SelectField('Select the year: ', choices=[("2021", "2021")], default="2021", validators = [DataRequired()])
    datewk = SelectField('Select the week: ', choices=[("14", "14")], default="1", validators = [DataRequired()])
    quantity = IntegerField('Enter the quantity of the item:', validators = [DataRequired()])
    submit = SubmitField('Submit')