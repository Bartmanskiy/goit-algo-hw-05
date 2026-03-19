def parse_input(user_input):
    user_input = user_input.strip()
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    return cmd.lower(), args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if not args or len(args[0]) == 0:
                return "Give me name and phone please."
            elif len(args[0]) == 1:
                return "Give me a phone please."
        except IndexError:
            return "Give me a name please"
        except KeyError:
            return "Contact not found"

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def phone_username(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def all_users(args, contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if not command:
            print("You entered an empty command.")
            continue
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all_users(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
