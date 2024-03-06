package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class BlinkAllianceEffect extends Effect {
    @SerializeField
    private Color redColor;
    @SerializeField
    private Color blueColor;
    @SerializeField
    private double interval;

    /**
     * Blink alliance effect
     * @param redColor red alliance color of blinking effect
     * @param blueColor blue alliance color of blinking effect
     * @param interval seconds to stay on/off
     */
    public BlinkAllianceEffect(Color redColor, Color blueColor, double interval) {
        super("blink_alliance");
        this.redColor = redColor;
        this.blueColor = blueColor;
        this.interval = interval;
    }

    /**
     * Get the red alliance color of the blinking effect
     * @return the red alliance color of the blinking effect
     * @see Color
     */
    public Color getRedColor() {
        return this.redColor;
    }

    /**
     * Get the blue alliance color of the blinking effect
     * @return the blue alliance color of the blinking effect
     * @see Color
     */
    public Color getBlueColor() {
        return this.blueColor;
    }

    /**
     * Set the red alliance color of the blinking effect
     * @param color the red alliance color of the blinking effect
     */
    public void setRedColor(Color color) {
        this.redColor = color;
    }

    /**
     * Set the blue alliance color of the blinking effect
     * @param color the blue alliance color of the blinking effect
     */
    public void setBlueColor(Color color) {
        this.blueColor = color;
    }

    /**
     * Get the interval of the blinking effect in pulses per second
     * @return interval of the blinking effect
     */
    public double getInterval() {
        return interval;
    }

    /**
     * Set the interval of the blinking effect in pulses per second
     * @param interval interval of the blinking effect
     */
    public void setInterval(double interval) {
        this.interval = interval;
    }
}
