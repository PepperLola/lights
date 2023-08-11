package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import org.json.JSONObject;

import edu.wpi.first.wpilibj.util.Color;

public class BreatheAllianceEffect extends Effect {
    private Color red_color;
    private Color blue_color;
    private double speed;

    /**
     * Breathe alliance effect
     * @param red_color red alliance color of breathing effect
     * @param blue_color blue alliance color of breathing effect
     * @param speed number of pulses per second
     */
    public BreatheAllianceEffect(Color red_color, Color blue_color, double speed) {
        super("breathe_alliance");
        this.red_color = red_color;
        this.blue_color = blue_color;
        this.speed = speed;
    }

    /**
     * Get the red alliance color of the breathing effect
     * @return the red alliance color of the breathing effect
     * @see Color
     */
    public Color getRedColor() {
        return this.red_color;
    }

    /**
     * Get the blue alliance color of the breathing effect
     * @return the blue alliance color of the breathing effect
     * @see Color
     */
    public Color getBlueColor() {
        return this.blue_color;
    }

    /**
     * Set the red alliance color of the breathing effect
     * @param color the red alliance color of the breathing effect
     */
    public void setRedColor(Color color) {
        this.red_color = color;
    }

    /**
     * Set the blue alliance color of the breathing effect
     * @param color the blue alliance color of the breathing effect
     */
    public void setBlueColor(Color color) {
        this.blue_color = color;
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

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("red_color", ColorUtil.toInt(this.getRedColor()))
                .put("blue_color", ColorUtil.toInt(this.getBlueColor()))
                .put("speed", this.getSpeed())
                .toString();
    }
}
