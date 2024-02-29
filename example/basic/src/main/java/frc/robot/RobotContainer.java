// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot;

import com.pigmice.piled.PiLED;
import com.pigmice.piled.effects.*;
import com.pigmice.piled.led.LEDStrip;

import com.pigmice.piled.util.ColorRamp;
import edu.wpi.first.math.Pair;
import edu.wpi.first.wpilibj.GenericHID;
import edu.wpi.first.wpilibj.XboxController;
import edu.wpi.first.wpilibj.shuffleboard.BuiltInWidgets;
import edu.wpi.first.wpilibj.shuffleboard.Shuffleboard;
import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
import edu.wpi.first.wpilibj.util.Color;
import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.InstantCommand;
import edu.wpi.first.wpilibj2.command.WaitCommand;
import frc.robot.subsystems.Lights;

import java.util.List;

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
  private SendableChooser<Effect> effectChooser;

  // Define a command to set the lights to a BreatheEffect with builtin WPILib
  // color and number of pulses per second
  // private final SetLEDCommand autoCommand = new SetLEDCommand(lights, new
  // BreatheEffect(Color.kPurple, 1));

  /**
   * The container for the robot. Contains subsystems, OI devices, and commands.
   */
  public RobotContainer() {
    configureButtonBindings();

    effectChooser = new SendableChooser<>();
    Shuffleboard.getTab("Lights")
        .add("Effect", effectChooser)
        .withPosition(3, 0);

    effectChooser.addOption("Solid Purple", new SolidEffect(Color.kPurple));
    effectChooser.addOption("Solid Alliance Color", new SolidAllianceEffect(Color.kRed, Color.kBlue));
    effectChooser.addOption("Breathing Purple", new BreatheEffect(Color.kPurple, 1.0F));
    effectChooser.addOption("Rainbow", new RainbowEffect(1F));
    effectChooser.addOption("Breathing Alliance Color", new BreatheAllianceEffect(Color.kRed, Color.kBlue, 1.0F));
    effectChooser.addOption("Fire", new FireEffect(
            new ColorRamp(List.of(
                    new Pair<>(Color.kRed, 0d),
                    new Pair<>(Color.kOrangeRed, 0.2d),
                    new Pair<>(Color.kOrange, 0.5d),
                    new Pair<>(Color.kYellow, 0.6d),
                    new Pair<>(Color.kBlack, 1.0d)
            )),
            3,
            0.65,
            0.25
    ));

    // these effects should only be used with an LED panel
    effectChooser.addOption("Animation", new AnimationEffect());
    effectChooser.addOption("Text", new TextEffect("Text", Color.kPurple));
    effectChooser.addOption("Text Alliance Color", new TextAllianceEffect("Text", Color.kRed, Color.kBlue));
    effectChooser.setDefaultOption("None", null);

    lights = new Lights(effectChooser);
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
