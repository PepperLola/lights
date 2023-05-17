// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot;

import com.pigmice.piled.PiLED;
import com.pigmice.piled.effects.BreatheEffect;
import com.pigmice.piled.led.LED;
import com.pigmice.piled.led.LEDStrip;

import edu.wpi.first.wpilibj.GenericHID;
import edu.wpi.first.wpilibj.XboxController;
import edu.wpi.first.wpilibj.shuffleboard.Shuffleboard;
import edu.wpi.first.wpilibj.util.Color;
import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.InstantCommand;
import edu.wpi.first.wpilibj2.command.WaitCommand;
import frc.robot.commands.SetLEDCommand;
import frc.robot.subsystems.Lights;

/**
 * This class is where the bulk of the robot should be declared. Since
 * Command-based is a
 * "declarative" paradigm, very little robot logic should actually be handled in
 * the {@link Robot}
 * periodic methods (other than the scheduler calls). Instead, the structure of
 * the robot (including
 * subsystems, commands, and button mappings) should be declared here.
 */
public class RobotContainer {
  // Define a Lights subsystem
  private final Lights lights;

  // Define a command to set the lights to a BreatheEffect with builtin WPILib
  // color and number of pulses per second
  // private final SetLEDCommand autoCommand = new SetLEDCommand(lights, new
  // BreatheEffect(Color.kPurple, 1));

  /**
   * The container for the robot. Contains subsystems, OI devices, and commands.
   */
  public RobotContainer() {
    configureButtonBindings();
    lights = new Lights();
    Shuffleboard.getTab("Lights").add(new InstantCommand(() -> {
      System.out.println("REGISTERING LIGHTS");
      PiLED.getInstance().registerLED(new LEDStrip(
          "Test", 0, 5));
    }));
  }

  /**
   * Use this method to define your button->command mappings. Buttons can be
   * created by
   * instantiating a {@link GenericHID} or one of its subclasses ({@link
   * edu.wpi.first.wpilibj.Joystick} or {@link XboxController}), and then passing
   * it to a {@link
   * edu.wpi.first.wpilibj2.command.button.JoystickButton}.
   */
  private void configureButtonBindings() {
  }

  /**
   * Use this to pass the autonomous command to the main {@link Robot} class.
   *
   * @return the command to run in autonomous
   */
  public Command getAutonomousCommand() {
    return new WaitCommand(1);
  }
}
