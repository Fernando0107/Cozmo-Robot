import cozmo
from flask import Flask
app = Flask(__name__)



def cozmo_say(robot: cozmo.robot.Robot):
    robot.say_text("Hello Flask").wait_for_completed()

def cozmo_turn(robot: cozmo.robot.Robot, accel, angle, speed):
    robot.turn_in_place(angle, speed, accel).wait_for_completed()

def cozmo_move(robot: cozmo.robot.Robot, distance, speed, should_play_anim=None):
    robot.drive_straight(distance, speed, should_play_anim)

def cozmo_off(robot: cozmo.robot.Robot, parallel=False, num_retries=1):
    robot.drive_off_charger_contacts(parallel, num_retries)

def cozmo_pick(robot: cozmo.robot.Robot, obj, in_parallel, num_retries=1):
    robot.pickup_object(obj, in_parallel, num_retries)

def command_center_drive(funct, arg1=None, arg2=None, arg3=None):
    cozmo.run_program(drive[funct](arg1,arg2,arg3))
drive  = {
    'MOVE': cozmo_say,
    'TURN': cozmo_turn,
    'PICK': cozmo_pick,
    'DRIVE_OFF': cozmo_off
}

'''@app.route('/')
def hello_world():
    cozmo.run_program(cozmo_program)

    return 'Hello, World!'''


#if __name__ == "__main__":
 #   app.run(host="0.0.0.0")

