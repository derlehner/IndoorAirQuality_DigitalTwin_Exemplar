from fastapi import Body, FastAPI

import RPi.GPIO as GPIO # IMPORTANT: remember to change the gpio pin (18) also it needs to be programmed in Thonny Python IDE
import time #used in raspberry pi model 4



app = FastAPI()


class AlarmService:

    def __init__(self) -> None:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(18, GPIO.OUT)
        pass

    @app.post("set_alarm")
    def set_alarm(value: bool = Body(...)):
        if () # Condition
        GPIO.output(18, True) 
        # For alarm: make series connectioin of beeper along with this  LED in the breadboard
        else () # else condition
        GPIO.output(18, False) 
        pass
