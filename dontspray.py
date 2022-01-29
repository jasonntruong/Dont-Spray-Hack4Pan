import pyfirmata
from datetime import datetime
from pynput.mouse import Listener

#change this according to your port
board = pyfirmata.Arduino('COM8')
print("Connected")

startTime = 0
endTime = 0
sprayed = 0

SPRAYTHRESHOLDMS = 800

#detects mouse clicks
def on_click(x, y, button, pressed):
    global startTime
    global endTime
    global sprayed
    
    if button == button.left:
        #gets time of on click
        if pressed:
            startTime = datetime.now().second*1000000 + datetime.now().microsecond

        else:
            #gets total click time on release
            endTime = datetime.now().second*1000000 + datetime.now().microsecond
            print("Last mouse click:", (endTime - startTime)/1000, "ms!")
            
            #if above SPRAYTHRESHOLDMS
            if (endTime - startTime) > SPRAYTHRESHOLDMS * 1000:
                sprayed += 1
                print("\n---------------------------------\n", "You've sprayed", sprayed, "times!", "\n---------------------------------\n")

                #get sprayed for # of times sprayed so far
                #NOTE: while being sprayed, you cannot move your mouse (further punishment LOL)
                for i in range(0, sprayed):
                    board.digital[13].write(1)
                    board.pass_time(0.1)
                    board.digital[13].write(0)
                    board.pass_time(0.2)

with Listener(on_click=on_click) as listener:
    listener.join()