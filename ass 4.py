event_queue = []

def add_event(event):
    event_queue.append(event)
    print(f"Event'{event}' added to queue")

def process_Next_event():
    if event_queue:
        x = event_queue.pop(0)
        print(f"Event'{x}'is processed")
    else:
        print("No Event available for process")

def display_Curent_event():
    if event_queue:
        print(" pending event ")
        for event in event_queue:
            print(event)
    else:
        print(" No display_event")

def cancel_event(event_name):
    if event_queue:
        event_queue.remove(event_name)
        print(f"Event'{event_name}'is canceled")
    else:
        print("No events are avaliable")

def exit_event():
    print("Exit the program, Thank You !")

def menu():
    while True:
        print("/n----Event Menu----")
        print("1.Add_Event")
        print("2.Process_Event")
        print("3.Display curent event")
        print("4.Cancel_event")
        print("5.Exit_event")
    
        choice = int(input("Enter the choices(0-5) is : "))
        if choice == 1:
            event = input("enter the event")
            add_event(event)
        elif choice == 2:
            process_Next_event()
        elif choice == 3:
            display_Curent_event()
        elif choice == 4:
            event_name = input("Enter the event name to cancel")
            cancel_event(event_name)
        elif choice == 5:
            exit_event()
            break
        else:
            print("Invalid choice")

menu()
