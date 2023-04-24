// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot.commands;

import frc.robot.subsystems.Lights;

import com.pigmice.piled.PiLED;
import com.pigmice.piled.effects.Effect;

import edu.wpi.first.wpilibj2.command.CommandBase;

/** An example command that uses an example subsystem. */
public class SetLEDCommand extends CommandBase {
  @SuppressWarnings({ "PMD.UnusedPrivateField", "PMD.SingularField" })
  private final Lights lights;
  private final Effect effect;

  /**
   * Creates a new ExampleCommand.
   *
   * @param subsystem The subsystem used by this command.
   */
  public SetLEDCommand(Lights lights, Effect effect) {
    this.lights = lights;
    this.effect = effect;

    addRequirements(lights);
  }

  // Called when the command is initially scheduled.
  @Override
  public void initialize() {
    PiLED.getInstance().setLEDEffect(lights.getLED(), effect);
  }

  // Called every time the scheduler runs while the command is scheduled.
  @Override
  public void execute() {
  }

  // Called once the command ends or is interrupted.
  @Override
  public void end(boolean interrupted) {
  }

  // Returns true when the command should end.
  @Override
  public boolean isFinished() {
    return false;
  }
}
