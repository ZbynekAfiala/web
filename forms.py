from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField, TextAreaField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, Length

def Kontrola_delky_tcisla(form,field):
    data = field.data
    if type(data) == str:
        strip(data)
        delka = len(data)
        data = int(data)
        if delka > 12 or delka < 9:
            raise ValidationError("Neodpovídající délka")

    elif type(data) == int:
        delka = len(str(data))
        if delka > 12 or delka < 9:
            raise ValidationError("Neodpovídající délka")

class PoptatForm(FlaskForm):
    email = StringField('Váš email ', validators=[DataRequired(), Email(), Length(min=6)],render_kw={"placeholder": "karel.novak@seznam.cz"})
    krestni_jmeno = StringField("Vaše jméno ", validators=[DataRequired()],render_kw={"placeholder": "Karel"})
    prijmeni = StringField("Vaše přijmení ", validators=[DataRequired()],render_kw={"placeholder": "Novák"})
    telefon = IntegerField('Vaše telefonní číslo ', validators=[DataRequired(),Kontrola_delky_tcisla],render_kw={"placeholder": "666111222"})
    vzkaz = TextAreaField("Text emailu ",validators=[DataRequired(),Length(min=10,max=1000)],render_kw={"placeholder": "Dobrý den, ...."})
    potvrdit = SubmitField('Poslat !')
