import pyb
import time

class MotorDriver():
    
# Motor 1 (tim3)
# p1 = pyb.Pin.board.PB4
# p2 = pyb.Pin.board.PB5
# en = pyb.Pin.board.PA10
# Motor 2 (tim5)
# p1 = pyb.Pin.board.PA0
# p2 = pyb.Pin.board.PA1
# en = pyb.Pin.board.PC1
    
    def __init__(self, pin1, pin2, pin_enable, timer):
        
        self.pinIN1A = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pinIN2A = pyb.Pin(pin2, pyb.Pin.OUT_PP)

        # pinIN1B = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
        # pinIN2B = pyb.Pin(pyb.Pin.board.PA1, pyb.Pin.OUT_PP)

        self.pinENOCDA = pyb.Pin(pin_enable, pyb.Pin.IN, pull = pyb.Pin.PULL_UP)
        # pinENOCDB = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.IN, pull = pyb.Pin.PULL_UP)

        self.tim3 = pyb.Timer(timer, freq = 20000)
        # tim5 = pyb.Timer(5, freq = 20000)

        self.t3ch1 = self.tim3.channel(1, pyb.Timer.PWM, pin = self.pinIN1A)
        self.t3ch2 = self.tim3.channel(2, pyb.Timer.PWM, pin = self.pinIN2A)
        # t5ch1 = tim5.channel(1, pyb.Timer.PWM, pin = pinIN1B)
        # t5ch2 = tim5.channel(2, pyb.Timer.PWM, pin = pinIN2B)

    def set_duty_cycle(self, duty):
        
        ''' @brief              Accepts a duty cycle percentage and sets it as a pwm to nucleo pins
            @details            Sets the duty to move either encoder 1 or encoder 2 backwards or forwards
            @param              Duty is a percentage of how much power a user wants to run the motor at
            @param              enc is a shared variable that specifies which motor to set duty for
        '''
        
        if (duty > 0):
                self.t3ch1.pulse_width_percent(0)
                self.t3ch2.pulse_width_percent(abs(duty)) 
                
        elif (duty <= 0):
                self.t3ch1.pulse_width_percent(abs(duty))
                self.t3ch2.pulse_width_percent(0)
                
        print('Duty: ', duty)
                
    def enable (self):
        
        ''' @brief              Enables motor to move
            @details            Disables any previous fault condition and sets nSLEEP to high to enable motor
        '''
        
        self.pinENOCDA.high()
        
    def disable (self):
        
        ''' @brief              Disables motor, preventing movement
            @details            Sets nSLEEP to low to disable motor
        '''
        
        self.pinENOCDA.low()
                
if __name__ == "__main__":
    motor1 = MotorDriver(pyb.Pin.board.PB4, pyb.Pin.board.PB5, pyb.Pin.board.PA10, 3)
    motor2 = MotorDriver(pyb.Pin.board.PA0, pyb.Pin.board.PA1, pyb.Pin.board.PC1, 5)
    
    motor2.enable()
    motor2.set_duty_cycle(0)

