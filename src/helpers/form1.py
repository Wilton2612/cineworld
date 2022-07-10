from wtforms import Form
from wtforms import StringField, TextAreaField, DecimalField, SelectField, EmailField, SubmitField
from wtforms import validators

class Formulario1(Form):
    email = EmailField('Correo electrónico', [validators.InputRequired(message='Ingresa el email!.'),validators.Email(message='Ingrese un email válido!.')])
    nombre = StringField('Nombre completo',[ validators.InputRequired(message='Ingresa el nombre!.'), validators.length(min=15, max=45, message='Ingrese un nombre válido!.')])
    telefono = StringField('Número telefónico',[ validators.InputRequired(message='Ingresa el número!.'), validators.length(min=10, max=10, message='Ingrese un número válido!.')])
    motivo = SelectField('Tipo de comentario', choices=[('0', '----'), ('Solicitud de información', 'Solicitud de información'), ('Sugerencias', 'Sugerencias'), ('Quejas y reclamos', 'Quejas y reclamos'), ('Empleo', 'Empleo'),('Otros', 'Otros')])
    comentario = TextAreaField('Comentario')