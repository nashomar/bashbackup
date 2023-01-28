def add_note(note): 
    with open("guestbook.txt", "a") as f:
        f.write(note + "\n")

def list_notes():
    with open("guestbook.txt", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"{i+1}. {line}")

def edit_note(index, new_note):
    with open("guestbook.txt", "r") as f:
        lines = f.readlines()
    lines[index] = new_note + "\n"
    with open("guestbook.txt", "w") as f:
        f.writelines(lines)

def delete_note(index):
    with open("guestbook.txt", "r") as f:
        lines = f.readlines()
    del lines[index]
    with open("guestbook.txt", "w") as f:
        f.writelines(lines)

def main():
    command = input("Enter command (new, list, edit, delete): ")
    if command == 'new':
        note = input("Enter note: ")
        add_note(note)
    elif command == 'list':
        list_notes()
    elif command == 'edit':
        index = int(input("Enter note index: ")) - 1
        new_note = input("Enter new note: ")
        edit_note(index, new_note)
    elif command == 'delete':
        index = int(input("Enter note index: ")) - 1
        delete_note(index)
    else:
        print("Invalid command")

if __name__ == '__main__':
    main()
