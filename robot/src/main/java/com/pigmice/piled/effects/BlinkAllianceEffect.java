package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;

public class BlinkAllianceEffect extends Effect {
    private Color red_color;
    private Color blue_color;
    private double interval;

    /**
     * Blink alliance effect
     * @param red_color red alliance color of blinking effect
     * @param blue_color blue alliance color of blinking effect
     * @param interval seconds to stay on/off
     */
    public BlinkAllianceEffect(Color red_color, Color blue_color, double interval) {
        super("blink_alliance");
        this.red_color = red_color;
        this.blue_color = blue_color;
        this.interval = interval;
    }

    /**
     * Get the red alliance color of the blinking effect
     * @return the red alliance color of the blinking effect
     * @see Color
     */
    public Color getRedColor() {
        return this.red_color;
    }

    /**
     * Get the blue alliance color of the blinking effect
     * @return the blue alliance color of the blinking effect
     * @see Color
     */
    public Color getBlueColor() {
        return this.blue_color;
    }

    /**
     * Set the red alliance color of the blinking effect
     * @param color the red alliance color of the blinking effect
     */
    public void setRedColor(Color color) {
        this.red_color = color;
    }

    /**
     * Set the blue alliance color of the blinking effect
     * @param color the blue alliance color of the blinking effect
     */
    public void setBlueColor(Color color) {
        this.blue_color = color;
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

    @Override
    public JSONObject toJson() {
        return new JSONObject()
                .put("name", this.getName())
                .put("red_color", ColorUtil.toInt(this.getRedColor()))
                .put("blue_color", ColorUtil.toInt(this.getBlueColor()))
                .put("interval", this.getInterval());
    }
}
