package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class BlinkEffect extends Effect {
    @SerializeField
    private Color color;
    @SerializeField
    private double interval;

    /**
     * Blink effect
     * @param color color of blinking effect
     * @param interval seconds to stay on/off
     */
    public BlinkEffect(Color color, double interval) {
        super("breathe");
        this.color = color;
        this.interval = interval;
    }

    /**
     * Get the color of the blinking effect
     * @return the color of the blinking effect
     * @see Color
     */
    public Color getColor() {
        return color;
    }

    /**
     * Set the color of the blinking effect
     * @param color the color of the blinking effect
     */
    public void setColor(Color color) {
        this.color = color;
    }

    /**
     * Get the interval of the blinking effect in seconds
     * @return interval of the blinking effect
     */
    public double getInterval() {
        return interval;
    }

    /**
     * Set the interval of the blinking effect in seconds
     * @param interval interval of the blinking effect
     */
    public void setInterval(double interval) {
        this.interval = interval;
    }
}
