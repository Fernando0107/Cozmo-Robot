import cozmo
from flask import Flask
app = Flask(__name__)



def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello Flask").wait_for_completed()


@app.route('/')
def hello_world():
    cozmo.run_program(cozmo_program)

    return 'Hello, World!'


if __name__ == "__main__":
    app.run(host="0.0.0.0")