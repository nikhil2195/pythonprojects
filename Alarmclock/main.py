import time
import webbrowser
import os
import random

def alarm():
    if not os.path.isfile("YT.txt"):
        print("error: file not found. creating file")
        flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
        filecreate = os.open("YT.txt",flags)
        with os.fdopen(filecreate,'w') as fileCreated:
            fileCreated.write("https://www.youtube.com/watch?v=eVTXPUF4Oz4")


    print("what time do you wanna wake up ?")
    print("Example: 06:30 AM")
    Alarm = input("> ")
    Time =time.strftime('%H:%M %p')


    with open("YT.txt") as f:
        content = f.readlines()
    while Time != Alarm:
        Time = time.strftime("%I:%M %p")
    if Time==Alarm:
        print("Time to Wake up!")
        random_video = random.choice(content)
        webbrowser.open(random_video)


def main():
    alarm()



if __name__ == '__main__':
    os.system('cls')
    main()

