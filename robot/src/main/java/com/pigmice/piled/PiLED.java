package com.pigmice.piled;

import com.pigmice.piled.effects.Effect;
import com.pigmice.piled.led.LED;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.DriverStation;
import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.shuffleboard.Shuffleboard;

public class PiLED {
    private static final String TABLE_NAME = "PiLED";
    private static final String LED_SUBTABLE_NAME = "led_devices";
    private static final String EFFECTS_SUBTABLE_NAME = "led_effects";

    private static PiLED instance;

    private NetworkTable table;
    private NetworkTable ledTable;
    private NetworkTable effectsTable;

    private NTValues ntValues;

    /**
     * PiLED controller
     */
    public PiLED() {
        table = NetworkTableInstance.getDefault().getTable(TABLE_NAME);
        ledTable = table.getSubTable(LED_SUBTABLE_NAME);
        effectsTable = table.getSubTable(EFFECTS_SUBTABLE_NAME);
        ntValues = new NTValues();
    }

    /**
     * Get the PiLED instance
     *
     * @return PiLED instance
     * @see PiLED
     */
    public static PiLED getInstance() {
        if (instance == null)
            instance = new PiLED();
        return instance;
    }

    /**
     * Register an LED device with the PiLED controller
     *
     * @param led device
     * @see LED
     */
    public void registerLED(LED led) {
        ledTable
                .getEntry(led.getName())
                .setString(led.toString());
    }

    /**
     * Unregister an LED device with the PiLED controller, which will turn it off
     * and halt all updates
     *
     * @param led device
     * @see LED
     */
    public void unregisterLED(LED led) {
        ledTable
                .getEntry(led.getName())
                .delete();
    }

    /**
     * Set the effect for an LED device
     *
     * @param led    device
     * @param effect effect
     * @see LED
     * @see Effect
     */
    public void setLEDEffect(LED led, Effect effect) {
        effectsTable
                .getEntry(led.getName())
                .setString(effect.toString());
    }

    /**
     * Automatically set the alliance from DriverStation
     */
    public void setAlliance() {
        ntValues.setAlliance(DriverStation.getAlliance());
    }

    /**
     * Set the game stage. Should call this in
     * {@link edu.wpi.first.wpilibj.TimedRobot#disabledInit()},
     * {@link TimedRobot#autonomousInit()},
     * {@link edu.wpi.first.wpilibj.TimedRobot#teleopInit()},
     * and {@link edu.wpi.first.wpilibj.TimedRobot#testInit()}
     *
     * @param stage game stage
     */
    public void setStage(NTValues.GameStage stage) {
        ntValues.setStage(stage);
    }

    /**
     * Get the NTValues instance
     * 
     * @return NTValues instance
     */
    public NTValues getNTValues() {
        return ntValues;
    }

    /**
     * LED type enum
     */
    public enum LEDType {
        Strip,
        Panel
    }
}
