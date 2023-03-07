import wpilib
import wpilib.drive
from robotcontainer import RobotContainer


class UHSRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        controls = RobotContainer()
        talons = controls.motorcontrollers()
        controller = controls.configureButtonBindings()
        
        wpilib.CameraServer.launch('vision.py:main')
        
        leftMotors = wpilib.MotorControllerGroup(talons.m_frontleft, talons.m_backleft)
        rightMotors = wpilib.MotorControllerGroup(talons.m_frontright, talons.m_backright)
        rightMotors.setInverted(True)
        
        # object that handles basic drive operations
        self.myRobot = wpilib.drive.DifferentialDrive(leftMotors, rightMotors)
        self.myRobot.setExpiration(0.1)

        # joystick #0
        self.stick = controller

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