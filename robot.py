import wpilib
import ctre
import networktables
from wpilib.drive import DifferentialDrive
from wpilib.interfaces import GenericHID
from networktables import NetworkTables

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
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
        
        # Initialize NetworkTables
        NetworkTables.initialize(server='roborio-1537-frc.local')
        
        # Initialize Limelight network table
        self.limelight_table = NetworkTables.getTable('limelight')
        
        # Set Limelight pipeline to use
        self.limelight_table.putNumber('pipeline', 0)
        
        # Set Limelight LEDs to off
        self.limelight_table.putNumber('ledMode', 1)
        
    def teleopPeriodic(self):
        # Get Limelight target data
        target_visible = self.limelight_table.getNumber('tv', 0)
        target_x = self.limelight_table.getNumber('tx', 0)
        target_y = self.limelight_table.getNumber('ty', 0)
        target_area = self.limelight_table.getNumber('ta', 0)
        
        # Use target data for vision processing (add your own code here)
        if target_visible:
            # Target is visible, do something
            pass
        else:
            # Target is not visible, do something else
            pass
        
        # Drive robot with Xbox controller thumbstick
        y_axis = self.controller.getRawAxis(1)
        x_axis = self.controller.getRawAxis(4)
        self.drive.arcadeDrive(y_axis, x_axis)
        
if __name__ == "__main__":
    wpilib.run(MyRobot)
