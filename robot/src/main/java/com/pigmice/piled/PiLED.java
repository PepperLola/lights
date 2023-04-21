package com.pigmice.piled;

import com.pigmice.piled.NTValues.GameStage;
import com.pigmice.piled.effects.Effect;
import com.pigmice.piled.led.LED;
import com.pigmice.piled.util.NTValue;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.DriverStation;

public class PiLED {
    private static final String TABLE_NAME = "PiLED";
    private static final String LED_SUBTABLE_NAME = "LEDs";
    private static final String EFFECTS_SUBTABLE_NAME = "effects";

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
     */
    public static PiLED getInstance() {
        if (instance == null)
            instance = new PiLED();
        return instance;
    }

    /**
     * Register an LED device with the PiLED controller
     * 
     * @param LED device
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
     * @param LED device
     */
    public void unregisterLED(LED led) {
        ledTable
                .getEntry(led.getName())
                .delete();
    }

    /**
     * Set the effect for an LED device
     * 
     * @param LED    device
     * @param Effect effect
     */
    public void setLEDEffect(LED led, Effect effect) {
        effectsTable
                .getEntry(led.getName())
                .setString(effect.toString());
    }

    /**
     * 
     */
    public void setAlliance() {
        ntValues.setAlliance(DriverStation.getAlliance());
    }

    public void setStage(GameStage stage) {
        ntValues.setStage(stage);
    }

    public NTValues getNTValues() {
        return ntValues;
    }

    public enum LEDType {
        Strip,
        Panel
    }
}
