package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;

public class RainbowEffect extends Effect {
    @SerializeField
    private double speed;
    @SerializeField
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
}
