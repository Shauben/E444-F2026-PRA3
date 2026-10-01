from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError

class NameEmailForm(FlaskForm):
    name = StringField(
        "First name",
        validators=[
            DataRequired(),
            Regexp(
                r"^[A-Za-z]+$",
                message="Please enter only your first name."
            )
        ]
    )

    email = StringField(
        "UofT email address",
        validators=[DataRequired(), Email()]
    )

    submit = SubmitField("Submit")

    def validate_email(self, field):
        if "utoronto" not in field.data.lower():
            raise ValidationError("Please enter a UofT email address.")