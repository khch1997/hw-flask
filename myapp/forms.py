from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired, required

class TopCities(FlaskForm):
  city_name = StringField("City Name", validators=[DataRequired()])
  city_rank = IntegerField("City Rank", [validators.required()])
  is_visited = BooleanField("visited")
  submit = SubmitField("Submit")