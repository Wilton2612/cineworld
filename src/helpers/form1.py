from wtforms import Form
from wtforms import StringField, TextAreaField, DecimalField, SelectField, EmailField, SubmitField
from wtforms import validators

class Formulario1(Form):
    email = EmailField('Correo electrónico', [validators.Required(message='Ingresa el email!.'),validators.Email(message='Ingrese un email válido!.')])
    nombre = StringField('Nombre completo',[ validators.Required(message='Ingresa el nombre!.'), validators.length(min=10, max=45, message='Ingrese un nombre válido!.')])
    motivo = SelectField('Tipo de comentario', choices=[('0', '----'), ('1', 'Solicitud de información'), ('2', 'Sugerencias'), ('3', 'Quejas y reclamos'), ('4', 'Empleo'),('5', 'Otros')])
    comentario = TextAreaField('Comentario')