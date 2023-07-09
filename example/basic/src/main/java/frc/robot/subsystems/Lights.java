// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot.subsystems;

import com.pigmice.piled.PiLED;
import com.pigmice.piled.effects.Effect;
import com.pigmice.piled.effects.RainbowEffect;
import com.pigmice.piled.led.LED;
import com.pigmice.piled.led.LEDStrip;

import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class Lights extends SubsystemBase {
  private LED led;
  private SendableChooser<Effect> effectChooser;
  private Effect lastEffect = null;

  public Lights(SendableChooser<Effect> effectChooser) {
    // creates an LEDStrip with name "strip1" and length of 10 LEDs
    this.led = new LEDStrip("strip1", 0, 10);
    this.effectChooser = effectChooser;
    PiLED.getInstance().registerLED(this.led);
    // PiLED.getInstance().setLEDEffect(this.led, new RainbowEffect(1F));

    // automatically sets the alliance from DriverStation
    PiLED.getInstance().setAlliance();
  }

  @Override
  public void periodic() {
    // System.out.println("LIGHTS PERIODIC");
    // This method will be called once per scheduler run

    Effect chosenEffect = effectChooser.getSelected();
    if (chosenEffect != null && !chosenEffect.equals(lastEffect)) {
      System.out.println(chosenEffect.getName());
      PiLED.getInstance().setLEDEffect(this.led, chosenEffect);
      this.lastEffect = chosenEffect;
    }
  }

  @Override
  public void simulationPeriodic() {
    // This method will be called once per scheduler run during simulation
  }

  public LED getLED() {
    return this.led;
  }
}
