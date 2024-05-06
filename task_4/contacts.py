from utils import input_error


def get_available_commands() -> list[str]:
	"""
	Returns list of available commands
	"""
	return ["phone", "add", "change", "all"]

def get_commands_handler(contacts: dict):
	"""
	contacts: dict - contacts dictionary
	"""
	def handler(command: str, *args: list[str]) -> str:
		"""
		Handles user commands
		command: str - user command
		args: list[str] - command arguments
		"""
		match command:
			case "phone":
				return __get_phone(contacts, *args)
			case "add":
				return __add_contact(contacts, *args)
			case "change":
				return __change_contact(contacts, *args)
			case "all":
				return __get_all_contacts(contacts)
			case _:
				return "Invalid command."
			
	return handler


@input_error
def __get_phone(contacts: dict, *args) -> str:
	"""
	Returns phone number for contact
	contacts: dict - contacts dictionary
	args: list[str] - command arguments
	"""
	name = args[0]
	return contacts[name]

@input_error
def __add_contact(contacts: dict, *args) -> str:
	"""
	Adds contact to contacts dictionary
	contacts: dict - contacts dictionary
	args: list[str] - command arguments
	"""
	name, phone = args
	contacts[name] = phone
	return f"Contact {name} added"

@input_error
def __change_contact(contacts: dict, *args) -> str:
	"""
	Changes contact phone
	contacts: dict - contacts dictionary
	args: list[str] - command arguments
	"""
	name, phone = args
	contacts[name] = phone
	return f"Contact {name} phone changed"

def __get_all_contacts(contacts: dict) -> str:
	"""
	Returns all contacts
	contacts: dict - contacts dictionary
	"""
	if not contacts:
		return "No contacts found"
	
	return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])