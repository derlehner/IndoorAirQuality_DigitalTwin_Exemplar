from fastapi import Body, FastAPI

app = FastAPI()

class AlarmService:

    @app.post("set_alarm")
    def set_alarm(value: bool = Body(...)):
        # TODO: put code for setting/desetting LED light here
        pass