import jsonschema


def assert_json(json_instance, expected_json_instance=None, expected_json_schema=None):
	"""Validate and assert JSON instances against expected instances or schemas.
	
	This function is designed for asserting JSON data, such as API responses or other JSON-based data.
	You can provide either an `expected_json_instance` or an `expected_json_schema` for validation.
	If an `expected_json_instance` is provided, a direct comparison is made against the provided JSON instance.
	If an `expected_json_schema` is provided, the function utilizes the `jsonschema` library to validate
	the JSON instance against the specified schema.
	
	Args:
		json_instance (dict or list): The JSON instance to be validated and asserted.
		expected_json_instance (dict or list, optional): The expected JSON instance for direct comparison.
		expected_json_schema (dict, optional): The JSON schema to validate the JSON instance against.

	Raises:
		AssertionError:	The JSON instance doesn't match the expected instance or schema.

	Example:
		# Direct instance comparison
		assert_json(json_data, expected_json_instance={'key': 'value'})
		
		# Schema-based validation
		schema = {
			'type': 'object',
			'properties': {
				'name': {'type': 'string'},
				'age': {'type': 'number'}
			},
			'required': ['name']
		}
		assert_json(json_data, expected_json_schema=schema)

	"""
	if expected_json_instance:
		assert json_instance == expected_json_instance,	\
			f'Expected JSON response body was `{expected_json_instance}` but got `{json_instance}`'
	elif expected_json_schema:
		try:
			jsonschema.validate(json_instance, expected_json_schema)
		except jsonschema.ValidationError as e:
			raise AssertionError('JSON instance does not match the expected JSON schema') from e
