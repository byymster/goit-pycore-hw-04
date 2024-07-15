def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact_command(args, contacts):
    username, phone = args
    if contacts.get(username):
        return "Contact already exists."
    contacts[username] = phone
    return "Contact added."


def change_contact_command(args, contacts):
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Contact changed."
    return "Contact not found."


def phone_command(args, contacts):
    username = args[0]
    if username in contacts:
        return f"Phone number: {contacts[username]}"
    return "Contact not found."


def all_command(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact_command(args, contacts))
                case "change":
                    print(change_contact_command(args, contacts))
                case 'phone':
                    print(phone_command(args, contacts))
                case 'all':
                    print(all_command(contacts))
                case 'help':
                    print("""
                    Available commands:
                        hello - Greet the bot.
                        add <username> <phone> - Add a new contact.
                        change <username> <phone> - Change an existing contact.
                        phone <username> - Get phone number of a contact.
                        all - List all contacts.
                    """)
                case _:
                    print("Invalid command.")
        except ValueError as e:
            print(str(e))
            print("Type 'help' to see available commands.")
        except KeyboardInterrupt:
            print("Good bye!")
            break


if __name__ == "__main__":
    main()
