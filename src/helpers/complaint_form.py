from wtforms import Form
from wtforms import StringField, TextAreaField, DecimalField, SelectField, EmailField, SubmitField
from wtforms import validators

from ..helpers import principal

class Formulario_Queja(Form):
    email = EmailField('Correo electrónico', [validators.InputRequired(message='Ingresa el email!.'),
    validators.Email(message='Ingrese un email válido!.')])
    nombre = StringField('Nombre completo',[ validators.InputRequired(message='Ingresa el nombre!.'), 
    validators.length(min=15, max=45, message='Ingrese un nombre válido!.'),principal.validate_caracter_special_and_number])
    telefono = StringField('Número telefónico',[ validators.InputRequired(message='Ingresa el número!.'),
    validators.length(min=10, max=10, message='El número de tener 10 digitos!.'), principal.validate_telefono])
    motivo = SelectField('Tipo de comentario', choices=[ ('Solicitud de información', 'Solicitud de información'),
     ('Sugerencias', 'Sugerencias'), ('Quejas y reclamos', 'Quejas y reclamos'), ('Empleo', 'Empleo'),('Otros', 'Otros')], validators=[principal.validate_choose])
    comentario = TextAreaField('Comentario',[validators.InputRequired(message='Ingresa un mensaje!.'), 
    validators.length(max=200)] )