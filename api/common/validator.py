import re
from marshmallow import ValidationError

def required(value):
    """Validate that field under validation does not contain null value."""
    
    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('The parameter cannot be null')
        return value
    elif value:
        return value

def email(value):
    """Validate field matches email format."""

    if not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", value):
        raise ValidationError('The parameter must be a valid email')
    return value

def password(value):
    if not value or value.isspace():
        return 'Password field can not be left empty.'
    elif len(value) < 8:
        return 'Password has to be longer than 8 characters.'
