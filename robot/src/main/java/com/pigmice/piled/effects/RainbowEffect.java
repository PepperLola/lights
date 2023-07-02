package com.pigmice.piled.effects;

import org.json.JSONObject;

public class RainbowEffect extends Effect {
    private double speed;

    /**
     * Rainbow effect
     * @param speed speed of the rainbow effect
     */
    public RainbowEffect(double speed) {
        super("rainbow");
        this.speed = speed;
    }

    /**
     * Get the speed of the rainbow effect
     * @return speed of the rainbow effect
     */
    public double getSpeed() {
        return speed;
    }

    /**
     * Set the speed of the rainbow effect
     * @param speed speed of the rainbow effect
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
            .put("speed", this.getSpeed())
            .toString();
    }
}
