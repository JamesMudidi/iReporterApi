import re
from marshmallow import ValidationError


def required(value):
    # Validate that field under validation does not contain empty values.
    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('This field cannot be empty')
        return value
    elif value:
        return value


def email(value):
    # Validate field matches email format.
    if not re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", value):
        raise ValidationError('Enter a valid email address')
    return value


def verifyStatus(value):
    # Validate status matches the required status
    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('Status field cannot be empty')

    status = ['Accepted', 'Rejected', 'Under Investigation', 'Draft']

    if value not in status:
        raise ValidationError(
            'The allowed creteria for this field is: Accepted, Rejected, Under Investigation or Draft')
    return value


def verifyType(value):
    # Validate type matches the required types
    if isinstance(value, str):
        if not value.strip(' '):
            raise ValidationError('Record type cannot be null')

    types = ['redflag', 'intervention']

    if value not in types:
        raise ValidationError(
            'The allowed creteria for this field is either Redflag or Intervention')
    return value
