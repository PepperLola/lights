package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;

public class ConwayEffect extends Effect {
    @SerializeField
    private double fullness;
    @SerializeField
    private int[][] initialPattern;

    /**
     * Conway's game of life effect
     * @param fullness chance that each cell will start alive, from [0, 1]
     */
    public ConwayEffect(double fullness) {
        this(fullness, null);
    }

    /**
     * Conway's game of life effect
     * @param fullness chance that each cell will start alive, from [0, 1]
     * @param initialPattern starting pattern
     */
    public ConwayEffect(double fullness, int[][] initialPattern) {
        super("conway");
        this.fullness = fullness;
        this.initialPattern = initialPattern;
    }

    /**
     * Get the fullness of the grid effect
     * @return fullness of the effect
     */
    public double getFullness() {
        return fullness;
    }

    /**
     * Set the fullness of the effect
     * @param fullness fullness of the effect
     */
    public void setFullness(double fullness) {
        this.fullness = fullness;
    }

    /**
     * Get the initial pattern of the effect
     * @return initial pattern of the effect
     */
    public int[][] getInitialPattern() {
        return this.initialPattern;
    }

    /**
     * Set the initial pattern of the effect
     * @param initialPattern initial pattern of the effect
     */
    public void setInitialPattern(int[][] initialPattern) {
        this.initialPattern = initialPattern;
    }
}
