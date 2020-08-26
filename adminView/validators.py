from django.core.exceptions import ValidationError

def validate_description(value):
	description = value
	if description == '':
		raise ValidationError('Field description must be required')

def validate_name(value):
	name = value
	if name == '':
		raise ValidationError('Field name must be required')