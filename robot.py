import wpilib
import ctre
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        wpilib.CameraServer.launch("vision.py:main")
        # Initialize Xbox controller on port 0
        self.controller = wpilib.XboxController(0)
        
        # Initialize Victor SPX motor controllers on CAN IDs 6, 7, 8, and 9
        self.left_motor_1 = ctre.WPI_VictorSPX(6)
        self.left_motor_2 = ctre.WPI_VictorSPX(7)
        self.right_motor_1 = ctre.WPI_VictorSPX(8)
        self.right_motor_2 = ctre.WPI_VictorSPX(9)
        
        # Create speed controller groups for left and right sides
        self.left_motors = self.left_motor_1
        self.left_motor_2.follow(self.left_motor_1)
        self.right_motors = self.right_motor_1
        self.right_motor_2.follow(self.right_motor_1)
        
        # Create differential drive object
        self.drive = DifferentialDrive(self.left_motors, self.right_motors)
        
    def teleopPeriodic(self):
        # Drive robot with Xbox controller thumbstick
        y_axis = self.controller.getRawAxis(1)
        x_axis = self.controller.getRawAxis(4)
        self.drive.arcadeDrive(y_axis, x_axis)
        
if __name__ == "__main__":
    wpilib.run(MyRobot)
