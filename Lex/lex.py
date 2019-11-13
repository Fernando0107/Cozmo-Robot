import cozmo
from flask import Flask , render_template
app = Flask(__name__)
from datetime import datetime
import os

robot = cozmo.robot.Robot
measures = cozmo.util
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

def generate_code(test, arg1,arg2):
    truename = datetime.now().minute
    with open('cozmo_generated_program.py', 'w') as f:
        f.write('import datetime \nimport cozmo\nclass transpiled:\n def __init__(self, robot: cozmo.robot.Robot, cube: cozmo.objects.LightCube):\n self.robot = robot\n self.cube = cube\n \ndef cozmo_program(robot: cozmo.robot.Robot):\n '+test+'('+arg1+','+arg2+')'+'\ncozmo.run_program(cozmo_program)')

    #import cozmo_generated_program as p
    
    os.rename(r'cozmo_generated_program.py', r'cozmo_generated_program'+str(truename)+r'.py')


#revisar COZMO.UTIL para sacar medidas y datos
drive  = {
    'SAY': 'robot.say_text',
    'TURN': cozmo_turn,
    'PICK': cozmo_pick,
    'DRIVE': 'robot.drive_straight',
    'DRIVE_OFF': cozmo_off
}

'''@app.route('/')
def hello_world():
    cozmo.run_program(cozmo_program)

    return 'Hello, World!'''
codigo_generado = "import datetime \nimport cozmo\nclass transpiled:\n\n  def _init_(self, robot: cozmo.robot.Robot, cube: cozmo.objects.LightCube):\n      self.robot = robot\n      self.cube = cube\n\n  def cozmo_program(self, robot: cozmo.robot.Robot):\n      measure = cozmo.util\n+test+'\n  def run(self):\n      cozmo.run_program(self.cozmo_program)\nCOZMO = transpiled(cozmo.robot.Robot, cozmo.objects.LightCube)\nCOZMO.run()'"
print(codigo_generado)
@app.route('/root')
def index():
    
    return render_template('index.html' , codigo_generado = codigo_generado)


if __name__ == "__main__":
   app.run(debug=True)

generate_code(drive['DRIVE'], 'cozmo.util.distance_mm(200.0)', 'cozmo.util.Speed(50.0)')