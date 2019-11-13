import datetime 
import cozmo
class transpiled:
 def __init__(self, robot: cozmo.robot.Robot, cube: cozmo.objects.LightCube):
 self.robot = robot
 self.cube = cube
 
def cozmo_program(robot: cozmo.robot.Robot):
 robot.drive_straight(cozmo.util.distance_mm(200.0),cozmo.util.Speed(50.0))
cozmo.run_program(cozmo_program)