from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import RadioField
from wtforms import SelectField
from wtforms.fields import EmailField
from wtforms import validators
from wtforms import IntegerField
from wtforms import FloatField, DecimalField
from wtforms import BooleanField
from wtforms.fields import TimeField
from wtforms.fields import DateField
from wtforms import HiddenField
from wtforms import SubmitField


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo no debe estar vacio.')

class login(Form):
    usuario = StringField("", [validators.InputRequired(message="Nombre de usuario vacio!")])
    clave = PasswordField("", [validators.InputRequired(message="Ingrese la contraseña!"),
                               validators.Length(min=6,max=15,message="Se requiere contraseña")])
    honeypot = HiddenField('',[length_honeypot])
    
class pagina_2(Form):
    orden=StringField("", [validators.InputRequired(message="Rellene este campo por favor")])
    
class pagina_3(Form):
     
     puestos_d_trabajo = SelectField('Puestos de trabajo', choices=[('1', 'Electricista'), ('2', 'Mecánico'), ('3', 'Supervisor'), ('4', 'Servicios Generales')])
     ficha = IntegerField("", [validators.input_required(message="Ingrese los datos en el campo soicitado")])
     tiempo_real = IntegerField("", [validators.input_required(message="Ingrese los datos en el campo soicitado")])
     checkbox=BooleanField( "", default="checked" )