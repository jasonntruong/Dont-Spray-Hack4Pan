import pyfirmata
from datetime import datetime
from pynput.mouse import Listener

board = pyfirmata.Arduino('COM8')
print("Connected")
startTime = 0
endTime = 0
sprayed = 0

SPRAYTHRESHOLDMS = 800

def on_click(x, y, button, pressed):
    global startTime
    global endTime
    global sprayed
    
    if button == button.left:
        if pressed:
            startTime = datetime.now().second*1000000 + datetime.now().microsecond
        else:
            endTime = datetime.now().second*1000000 + datetime.now().microsecond
            print("That last one was", (endTime - startTime)/1000, "ms!")
            if (endTime - startTime) > SPRAYTHRESHOLDMS * 1000:
                sprayed += 1

                for i in range(0, sprayed):
                    board.digital[13].write(1)
                    board.pass_time(0.1)
                    board.digital[13].write(0)
                    board.pass_time(0.2)

with Listener(on_click=on_click) as listener:
    listener.join()