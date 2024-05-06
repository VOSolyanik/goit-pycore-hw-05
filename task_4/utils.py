from functools import wraps

def input_error(func):
	@wraps(func)
	def inner(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except KeyError as e:
			return f"Contact {e} not found"
		except ValueError as e:
			return "Contact name and phone are required"
		except IndexError as e:
			return "Contact name is required"
	return inner