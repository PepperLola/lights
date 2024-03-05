package com.pigmice.piled.effects;

import org.json.JSONObject;

public class RainbowEffect extends Effect {
    private double speed;
    private double increment;

    /**
     * Rainbow effect
     * @param speed speed of the rainbow effect
     * @param increment increment of the rainbow effect
     */
    public RainbowEffect(double speed, double increment) {
        super("rainbow");
        this.speed = speed;
        this.increment = increment;
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
     * Get the increment of the rainbow effect
     * @return increment of the rainbow effect
     */
    public double getIncrement() {
        return increment;
    }

    /**
     * Set the increment of the rainbow effect
     * @param increment increment of the rainbow effect
     */
    public void setIncrement(double increment) {
        this.increment = increment;
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
            .put("increment", this.getIncrement())
            .toString();
    }
}
