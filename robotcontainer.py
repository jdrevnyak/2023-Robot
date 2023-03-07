# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
import ctre
import enum
import commands2
import wpilib



class RobotContainer:
    class MotorControllers:
        def __init__(self, m_frontleft, m_backleft, m_frontright, m_backright):
            self.m_frontleft = m_frontleft
            self.m_backleft = m_backleft
            self.m_frontright = m_frontright
            self.m_backright = m_backright
            
    
    def motorcontrollers(self) -> MotorControllers:
        m_frontleft = wpilib.Talon(0)
        m_backleft = wpilib.Talon(1)
        m_frontright = wpilib.Talon(2)
        m_backright = wpilib.Talon(3)

        return self.MotorControllers(m_frontleft, m_backleft, m_frontright, m_backright)

    def configureButtonBindings(self) -> wpilib.XboxController:
        stick = wpilib.XboxController(1)
        return stick