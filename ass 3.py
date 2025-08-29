undo = []
redo = []

def make_change():
    print("enter data to text editor")
    text = input()
    undo.append(text)
    redo.clear()

def undo_action():
    if undo:
        x = undo.pop()
        redo.append(x)
    else:
        print("no undo action possible")
    return
    
def redo_action():
    if redo:
        x = redo.pop()
        undo.append(x)
    else:
        print("No redo action possible")
    return

def display_state():
    print("current status of text is:", *undo)
    while True:
        print("\n--- MENU ---")
        print("1. Make a Change")
        print("2. Undo")
        print("3. Redo")
        print("4. Display Document State")
        print("5. Exit")

        choice=int(input("Enter a choice"))
        if choice == 1:
            make_change()
        elif choice == 2:
            undo_action()
        elif choice == 3:
            redo_action()
        elif choice == 4:
            display_state()
        elif choice == 5:
            print("exit,thank you")
            break
        else:
            print("Invalid choice ")