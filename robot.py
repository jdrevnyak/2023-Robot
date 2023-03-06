import wpilib
import ctre
import wpilib.drive
from robotcontainer import RobotContainer


class UHSRobot(wpilib.TimedRobot):
    # Channels on the roboRIO that the motor controllers are plugged in to
    
    


    # The channel on the driver station that the joystick is connected to
    joystickChannel = 0

    def robotInit(self):
        wpilib.CameraServer.launch()
        m_frontleft = wpilib.Talon(0)
        m_backleft = wpilib.Talon(1)
        m_frontright = wpilib.Talon(2)
        m_backright = wpilib.Talon(3)
        
        leftMotors = wpilib.MotorControllerGroup(m_frontleft, m_backleft)
        rightMotors = wpilib.MotorControllerGroup(m_frontright, m_backright)
        rightMotors.setInverted(True)
        
        # object that handles basic drive operations
        self.myRobot = wpilib.drive.DifferentialDrive(leftMotors, rightMotors)
        self.myRobot.setExpiration(0.1)

        # joystick #0
        self.stick = wpilib.Joystick(0)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        self.myRobot.arcadeDrive(
            self.stick.getRawAxis(0), self.stick.getRawAxis(1), True
        )


if __name__ == "__main__":
    wpilib.run(UHSRobot)