from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired, URL


class MyForm(FlaskForm):
    quality_options = ["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"]
    strength_options = ["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    power_options = ["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    cafe_name = StringField("Cafe Name", validators=[DataRequired(message="Required!")])
    location = StringField(label="Get Google Map Location (Map Link)",
                           validators=[DataRequired(message="Required!"), URL(message="Please provide valid map link")])
    open_time = StringField(label="Open", validators=[DataRequired(message="Required!")])
    close_time = StringField(label="Close", validators=[DataRequired(message="Required!")])
    quality_select = SelectField('Coffee Quality Rating', validators=[DataRequired()], choices=quality_options)
    strength_select = SelectField(label="Wifi Strength Rating", validators=[DataRequired()], choices=strength_options)
    power_select = SelectField(label="Power Availability Rating", validators=[DataRequired()], choices=power_options)
    submit = SubmitField('Submit')
