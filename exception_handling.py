import json


STUDENT_MARKS = {"ali": 78, "sara": 91, "hamza": 64}
SUBJECTS = ["Math", "Physics", "Computer Science"]


def read_number(prompt):
    try:
        value = float(input(prompt).strip())
    except ValueError:
        print("Invalid input: please enter a valid number such as 10 or 3.5.")
        return None
    except EOFError:
        print("No input received. Please type a value and press Enter.")
        return None
    else:
        return value
    finally:
        print("[finally] Input step finished.")

def demo_invalid_input():
    print("\n--- Demo 1: Invalid numeric input (ValueError) ---")
    number = read_number("Enter a number: ")
    if number is not None:
        print(f"You entered {number}. Its square is {number ** 2}.")


def demo_division():
    print("\n--- Demo 2: Division by zero (ZeroDivisionError) ---")
    numerator = read_number("Enter numerator: ")
    denominator = read_number("Enter denominator: ")
    if numerator is None or denominator is None:
        return
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: division by zero is not allowed. Use a non-zero denominator.")
    else:
        print(f"Result: {numerator} / {denominator} = {result}")
    finally:
        print("[finally] Division attempt completed.")


def demo_missing_key():
    print("\n--- Demo 3: Missing value in dictionary (KeyError) ---")
    name = input("Enter student name (ali, sara, hamza): ").strip().lower()
    try:
        marks = STUDENT_MARKS[name]
    except KeyError:
        print(f"Error: no record found for '{name}'. Check the spelling and try again.")
    else:
        print(f"{name.title()} scored {marks} marks.")
    finally:
        print("[finally] Lookup completed.")


def demo_list_index():
    print("\n--- Demo 4: Missing item in list (IndexError) ---")
    print("Available subjects:", ", ".join(SUBJECTS))
    raw = input("Enter subject number (starting from 0): ").strip()
    try:
        position = int(raw)
        subject = SUBJECTS[position]
    except ValueError:
        print("Error: the subject number must be a whole number.")
    except IndexError:
        print(f"Error: there is no subject at position {raw}. Valid range is 0 to {len(SUBJECTS) - 1}.")
    else:
        print(f"Selected subject: {subject}")
    finally:
        print("[finally] Subject selection completed.")


def demo_none_value():
    print("\n--- Demo 5: Missing value / None used in calculation (TypeError) ---")
    first = read_number("Enter first number: ")
    second = None
    try:
        total = first + second
    except TypeError:
        print("Error: a required value is missing (None), so the numbers cannot be added.")
    else:
        print(f"Total: {total}")
    finally:
        print("[finally] Addition attempt completed.")


def demo_file_reading():
    print("\n--- Demo 6: Reading a file (FileNotFoundError, PermissionError) ---")
    filename = input("Enter file name to read: ").strip()
    file = None
    try:
        file = open(filename, "r", encoding="utf-8")
        content = file.read()
    except FileNotFoundError:
        print(f"Error: the file '{filename}' does not exist in this folder.")
    except PermissionError:
        print(f"Error: you do not have permission to open '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a folder, not a file.")
    except UnicodeDecodeError:
        print("Error: this file is not a readable text file.")
    else:
        print(f"File read successfully. It contains {len(content)} characters.")
    finally:
        if file is not None:
            file.close()
            print("[finally] File closed.")
        else:
            print("[finally] No file was open, nothing to close.")


def demo_json_parsing():
    print("\n--- Demo 7: Parsing JSON text (JSONDecodeError) ---")
    text = input('Enter JSON text, e.g. {"name": "Ali"}: ').strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        print(f"Error: invalid JSON at position {error.pos}: {error.msg}.")
    else:
        print("Parsed successfully:", data)
    finally:
        print("[finally] JSON parsing attempt completed.")


def show_menu():
    print("\n===== Exception Handling Practice =====")
    print("1. Invalid numeric input")
    print("2. Division by zero")
    print("3. Missing dictionary key")
    print("4. List index out of range")
    print("5. Missing (None) value")
    print("6. File not found")
    print("7. Invalid JSON")
    print("0. Exit")


def main():
    actions = {
        "1": demo_invalid_input,
        "2": demo_division,
        "3": demo_missing_key,
        "4": demo_list_index,
        "5": demo_none_value,
        "6": demo_file_reading,
        "7": demo_json_parsing,
    }
    while True:
        show_menu()
        try:
            choice = input("Choose an option: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted. Goodbye!")
            break
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please enter a number from the menu.")
            continue
        try:
            action()
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")


if __name__ == "__main__":
    main()