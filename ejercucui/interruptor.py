switch = False

def interruptor(switch):
    if switch == False:
        return True
    else:
        return False

print(switch)

while True:
    f = input("Enciende o apaga el switch: ")
    if f == "exit":
        break
    else:
        switch= interruptor(switch)
        print(switch)
