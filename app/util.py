def validate_email( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        if not len(email) or not email:
            return False
        validate_email(email)
        return True
    except ValidationError:
        return False