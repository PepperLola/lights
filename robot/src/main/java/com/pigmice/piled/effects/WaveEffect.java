package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import com.pigmice.piled.util.ColorRamp;

public class WaveEffect extends Effect {
    @SerializeField
    private ColorRamp colors;
    @SerializeField
    private double increment;
    @SerializeField
    private double speed;
    @SerializeField
    private int repeats;

    /**
     * Create a new wave effect
     * @param colors color ramp of the wave effect
     * @param increment increment of the wave effect
     * @param speed speed of the wave effect
     * @param repeats number of waves visible at once
     */
    public WaveEffect(ColorRamp colors, double increment, double speed, int repeats) {
        super("wave");
        this.colors = colors;
        this.increment = increment;
        this.speed = speed;
        this.repeats = repeats;
    }

    /**
     * Get the wave color ramp
     * @return wave color ramp
     */
    public ColorRamp getColors() {
        return colors;
    }

    /**
     * Set the wave color ramp
     * @param colors wave color ramp
     */
    public void setColors(ColorRamp colors) {
        this.colors = colors;
    }

    /**
     * Get the increment of the wave effect
     * @return increment of the wave effect
     */
    public double getIncrement() {
        return increment;
    }

    /**
     * Set the increment of the wave effect
     * @param increment increment of the wave effect
     */
    public void setIncrement(double increment) {
        this.increment = increment;
    }

    /**
     * Get the speed of the wave effect
     * @return speed of the wave effect
     */
    public double getSpeed() {
        return speed;
    }

    /**
     * Set the speed of the wave effect
     * @param speed speed of the wave effect
     */
    public void setSpeed(double speed) {
        this.speed = speed;
    }

    /**
     * Get the number of waves visible at once
     * @return number of waves visible at once
     */
    public int getRepeats() {
        return repeats;
    }

    /**
     * Set the number of waves visible at once
     * @param repeats number of waves visible at once
     */
    public void setRepeats(int repeats) {
        this.repeats = repeats;
    }
}
