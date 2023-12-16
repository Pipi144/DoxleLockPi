import RPi.GPIO as GPIO
import time

def unlock_mechanism():
    servo_pin = 11
    try:      
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(servo_pin, GPIO.OUT)
        
        pwm = GPIO.PWM(servo_pin, 50)
        pwm.start(0)
        
        for angle in range(0, 141, 10):
            duty_cycle = angle/18 + 2
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.2)
        
        time.sleep(2)

        for angle in range(140, -1, -10):
            duty_cycle = angle/18 + 2
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.2)
        
        
        
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    unlock_mechanism()