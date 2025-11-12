import subprocess
from subprocess import PIPE, STDOUT

print ("Starting tests for Ch 01 Assignment 01")

cmd = subprocess.run(["python", "Ch01_A01_favorite_quote.py"], stdout=PIPE, stderr=STDOUT,)
stdout = cmd.stdout.decode()  # bytes => str
theLines = stdout.splitlines()
if len(theLines) < 2 or not stdout.startswith("This is the favorite quote of "): 
    print("Error with Favorite Quote ")
    print("\tExpecting at least 2 lines of text"
    + "and for the starting string to match exactly what is specified in the assignment")
    print("instead I recieved "+ str(len(theLines)) + " line(s) and the following quoted text'")
    print(stdout)
    print("'")

def check_and_remove(c):
    global info
    if(not info.startswith(c)):
        return False
    info = info.removeprefix(c)
    info = info.removeprefix("\n")
    return True

cmd = subprocess.run(["python", "Ch01_A01_Go_SUU.py"], stdout=PIPE, stderr=STDOUT,)
stdout = cmd.stdout.decode()  # bytes => str
info = stdout
info = info.replace("\r","")
if (
        not check_and_remove("##### #   # #   #") or
        not check_and_remove("#     #   # #   #") or
        not check_and_remove("##### #   # #   #") or
        not check_and_remove("    # #   # #   #") or
        not check_and_remove("##### ##### #####") or
        not check_and_remove("") or
        not check_and_remove("We will che-er for the red and white, of our fighting SUU!") or
        not check_and_remove("Hear our battle cry, echo through the sky, As our team comes blazing through!") or
        not check_and_remove("They will fight, fight, fight, when they hear us shout, As we sing our victory song.") or
        not check_and_remove("We will run, we will score, till the Thunder Roars, And the T-Birds win once more!") or
        not check_and_remove("Go, Go, Go,") or
        not check_and_remove("Fight, Fight, Fight,") or
        not check_and_remove("Win T-Birds!")
    ):
    print ("Something in your Go_SUU.py file isn't quite correct.  Please check the following carefully '")
    print(stdout)
    print("'")
print ("Finished testing")






