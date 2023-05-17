// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot.subsystems;

import com.pigmice.piled.PiLED;
import com.pigmice.piled.led.LED;
import com.pigmice.piled.led.LEDStrip;

import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class Lights extends SubsystemBase {
  private LED led;

  public Lights() {
    // creates an LEDStrip with name "strip1" and length of 10 LEDs
    this.led = new LEDStrip("strip1", 0, 10);
    System.out.println("REGISTERING LED STRIP");
    PiLED.getInstance().registerLED(this.led);

    // automatically sets the alliance from DriverStation
    PiLED.getInstance().setAlliance();
  }

  public static void registerLED() {
    LEDStrip testStrip = new LEDStrip("test_strip", 1, 20);
    System.out.println("REGISTERING TEST LED STRIP");
    PiLED.getInstance().registerLED(testStrip);
  }

  @Override
  public void periodic() {
    // System.out.println("LIGHTS PERIODIC");
    // This method will be called once per scheduler run
  }

  @Override
  public void simulationPeriodic() {
    // This method will be called once per scheduler run during simulation
  }

  public LED getLED() {
    return this.led;
  }
}
