# Add your Python code here. E.g.
from microbit import *

# Declare variables
hits = 0
press = 0
miss = 0
playing = 1
userContinue = 1

# Continuously waits for input
while playing == 1 :
    # Ends the program when both buttons are pressed
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("Are you sure? [A/B]")
        # Waits for input
        while userContinue == 1:
            if button_a.is_pressed() or button_b.is_pressed() :
                userContinue = 0
        # Exits
        if button_a.is_pressed() :
            playing = 0
            # Find the total
            total = hits - miss
            display.scroll(str.format("Hits: {} Miss: {} Total: {}", hits, miss, total))
            stop
        # Continues
        
    # Adds to the number of hits when button A is pressed
    if button_a.is_pressed() :
        hits = hits + button_a.get_presses()
        display.show(hits)
    # Adds to the number of misses when button B is pressed
    if button_b.is_pressed() :
        miss = miss + button_b.get_presses()
        display.show(miss)
    
# while True:
#    display.scroll('Hello, World!')
#    display.show(Image.HEART)
#    sleep(2000)
