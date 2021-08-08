from flask_sqlalchemy import model
from wtforms import Form, StringField, SelectField, fields
from db import Food

from wtforms.ext.sqlalchemy.orm import model_form

FoodForm = model_form(Food)
