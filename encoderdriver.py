

import pyb
import time


class EncoderDriver():
# pins for the encoders
# pinINB6 = pyb.Pin(pyb.Pin.board.PB6, pyb.Pin.IN)
# pinINB7 = pyb.Pin(pyb.Pin.board.PB7, pyb.Pin.IN)

# pinA1 = pyb.Pin.board.PB6
# pinA2 = pyb.Pin.board.PB7
# pinB1 = pyb.Pin.board,PC6
# pinB2 = pyb.Pin.board,PC7

    def __init__(self, pinA1, pinA2, timer):
        
        self.pinA1 = pyb.Pin(pinA1, pyb.Pin.IN)
        self.pinA2 = pyb.Pin(pinA2, pyb.Pin.IN)
        
        self.tim4 = pyb.Timer(timer, period = 65535, prescaler = 0)
        self.t4ch1 = self.tim4.channel(1, pyb.Timer.ENC_AB, pin = self.pinA1)
        self.t4ch2 = self.tim4.channel(2, pyb.Timer.ENC_AB, pin = self.pinA2)
        
        
        self.per = 65535
        self.old_tick = 0
        self.position = 0

        ''' @brief              Updates encoder value
            @details            Updates encoder value by adding delta to position. Handles overflows by adding or subtracting the period from delta when delta exceeds half the period
        '''
        
    def update_delta(self):
        new_tick = self.tim4.counter()
        #print(new_tick)
        delta = new_tick - self.old_tick
        self.old_tick = new_tick

        if(abs(delta) >= self.per/2):    #handle overflow if delta is greater than half the period
            if(delta > 0):
                delta -= self.per        #if delta is positive, subtract period
            else:
                delta += self.per        #if delta is negative, add period
                
        self.position += delta
        time.sleep(.1)
            
    def get_position(self):
        return self.position
    
    def set_position(self, val):
        self.position = val
        
    
if __name__ == "__main__":
    my_encoder1 = EncoderDriver(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    my_encoder2 = EncoderDriver(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    while True:
        my_encoder2.update_delta()
