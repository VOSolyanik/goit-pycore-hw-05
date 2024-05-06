import sys
from typing import List, Tuple
from contacts import get_available_commands, get_commands_handler

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def read_contacts(file_path: str) -> dict:
    """
    Reads contacts from file and returns dictionary
    """
    contacts = {}
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) != 2:
                raise Exception("File has invalid format")
            contacts[parts[0]] = parts[1]
    except FileNotFoundError:
        print(f"File {file_path} not found. It will be created.")
    except Exception as e:
        print(f"Error: {e}")
    return contacts

def write_contacts(file_path: str, contacts: dict) -> None:
    """
    Writes contacts to file. Creates file if not exists
    """
    try:
        with open(file_path, 'w+') as file:
            for name, phone in contacts.items():
                file.write(f"{name},{phone}\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    contacts = {}
    # check if file mode is enabled (if file name passed as an argument)
    is_file_mode = len(sys.argv) == 2
    # if file mode is enabled, read contacts from file
    if is_file_mode:
        contacts = read_contacts(sys.argv[1])

    print("Welcome to the assistant bot!")
    while True:
        user_input = ""
        try:
            user_input = input("Enter a command: ")
        except KeyboardInterrupt:
            print("\nGood bye!")
            break

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            # if file mode is enabled, write contacts to file
            if is_file_mode:
                write_contacts(sys.argv[1], contacts)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in get_available_commands():
            print(get_commands_handler(contacts)(command, *args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()