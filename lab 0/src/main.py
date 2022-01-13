"""!
@file main.py
This file contains Lab 0 which controls the voltage of pinA0 using PWM,
resulting in a sawtooth wave LED pattern.

TODO: Create a sawtooth wave LED pattern using a PWM cycle

@author Jacob Wong
@author Wyatt Conner
@author Jameson Spitz
@date   6-Jan-2022
@copyright by Jacob Wong all rights reserved
"""
import utime
import pyb

## Channel Number for Timer
ch1=None

def led_setup():
    """!
    Compute the answer to the ultimate question.
    This function computes the greatest answer of all answers using
    information of great relevance.
    """
    global ch1
    ## pinA0 use to control GND pin
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    ## Defining pyb Timer
    tim2 = pyb.Timer(2, freq=20000)
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)
def led_brightness(duty):
    """!
    Changes LED brightness by changing the duty cycle to a specified
    value between 0 and 100.
    @param   duty Duty cycle for PWM cycle
    """
    # Changes PWM
    ch1.pulse_width_percent (duty)

if __name__ == "__main__":
    led_setup()
    ## Establishes a startTime to the while loop
    startTime=utime.ticks_ms()
    while True:
        try:
            ## Current time with respect to beginning of while loop
            current_time=utime.ticks_diff(utime.ticks_ms(),startTime)/1000
            # Uses remainder operator to repeat cycle every 5 seconds
            led_brightness(20*(current_time%5))
        except KeyboardInterrupt:
            break
