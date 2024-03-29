package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class BreatheEffect extends Effect {
    @SerializeField
    private Color color;
    @SerializeField
    private double speed;

    /**
     * Breathe effect
     * @param color color of breathing effect
     * @param speed number of pulses per second
     */
    public BreatheEffect(Color color, double speed) {
        super("breathe");
        this.color = color;
        this.speed = speed;
    }

    /**
     * Get the color of the breathing effect
     * @return the color of the breathing effect
     * @see Color
     */
    public Color getColor() {
        return color;
    }

    /**
     * Set the color of the breathing effect
     * @param color the color of the breathing effect
     */
    public void setColor(Color color) {
        this.color = color;
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
