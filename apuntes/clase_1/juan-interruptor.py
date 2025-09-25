is_on = False

while True:
    user_input = input("Press Enter to toggle the switch (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    is_on = not is_on
    print("Switch ON" if is_on else "Switch OFF")