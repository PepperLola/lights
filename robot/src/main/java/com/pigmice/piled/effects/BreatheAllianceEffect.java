package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class BreatheAllianceEffect extends Effect {
    @SerializeField
    private Color redColor;
    @SerializeField
    private Color blueColor;
    @SerializeField
    private double speed;

    /**
     * Breathe alliance effect
     * @param redColor red alliance color of breathing effect
     * @param blueColor blue alliance color of breathing effect
     * @param speed number of pulses per second
     */
    public BreatheAllianceEffect(Color redColor, Color blueColor, double speed) {
        super("breathe_alliance");
        this.redColor = redColor;
        this.blueColor = blueColor;
        this.speed = speed;
    }

    /**
     * Get the red alliance color of the breathing effect
     * @return the red alliance color of the breathing effect
     * @see Color
     */
    public Color getRedColor() {
        return this.redColor;
    }

    /**
     * Get the blue alliance color of the breathing effect
     * @return the blue alliance color of the breathing effect
     * @see Color
     */
    public Color getBlueColor() {
        return this.blueColor;
    }

    /**
     * Set the red alliance color of the breathing effect
     * @param color the red alliance color of the breathing effect
     */
    public void setRedColor(Color color) {
        this.redColor = color;
    }

    /**
     * Set the blue alliance color of the breathing effect
     * @param color the blue alliance color of the breathing effect
     */
    public void setBlueColor(Color color) {
        this.blueColor = color;
    }

    /**
     * Get the speed of the breathing effect in pulses per second
     * @return speed of the breathing effect
     */
    public double getSpeed() {
        return speed;
    }

    /**
     * Set the speed of the breathing effect in pulses per second
     * @param speed speed of the breathing effect
     */
    public void setSpeed(double speed) {
        this.speed = speed;
    }
}
