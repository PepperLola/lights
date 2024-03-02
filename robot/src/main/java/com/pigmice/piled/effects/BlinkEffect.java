package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;

public class BlinkEffect extends Effect {
    private Color color;
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

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("color", ColorUtil.toInt(this.getColor()))
                .put("interval", this.getInterval())
                .toString();
    }
}
