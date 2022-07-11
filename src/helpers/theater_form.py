from wtforms import Form
from wtforms import SelectField, SubmitField
from wtforms import validators

from ..helpers import principal


class Formulario_Teatro(Form):
    teatro = SelectField('Teatros', choices=[], validators=[principal.validate_choose])