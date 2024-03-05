package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorRamp;
import org.json.JSONObject;

public class FireEffect extends Effect {
    private ColorRamp colors;
    private double height;
    private double flareChance;
    private double flareBrightness;
    private double centerBias;

    /**
     * Create a new fire effect
     * @param colors color ramp of the fire effect
     * @param height height of the fire effect (multiplier)
     * @param flareChance chance for a flare (0.0 - 1.0)
     * @param flareBrightness brightness of the flare (multiplier)
     * @param centerBias bias towards the center of the fire (0.0 - 1.0)
     */
    public FireEffect(ColorRamp colors, double height, double flareChance, double flareBrightness, double centerBias) {
        super("fire");
        this.colors = colors;
        this.height = height;
        this.flareChance = flareChance;
        this.flareBrightness = flareBrightness;
        this.centerBias = centerBias;
    }

    /**
     * Create a new fire effect
     * @param name name of the effect
     * @param colors color ramp of the fire effect
     * @param height height of the fire effect (multiplier)
     * @param flareChance chance for a flare (0.0 - 1.0)
     * @param flareBrightness brightness of the flare (multiplier)
     */
    public FireEffect(String name, ColorRamp colors, double height, double flareChance, double flareBrightness) {
        this(colors, height, flareChance, flareBrightness, 0.0);
    }

    /**
     * Get the fire color ramp
     * @return the fire color ramp
     */
    public ColorRamp getColors() {
        return colors;
    }

    /**
     * Get the height of the fire
     * @return the height of the fire (multiplier)
     */
    public double getHeight() {
        return height;
    }

    /**
     * Get the flare chance
     * @return the flare chance (0.0 - 1.0)
     */
    public double getFlareChance() {
        return flareChance;
    }

    /**
     * Get the flare brightness
     * @return the flare brightness (multiplier)
     */
    public double getFlareBrightness() {
        return flareBrightness;
    }

    /**
     * Set the color ramp of the fire effect
     * @param colors color ramp of the fire effect
     */
    public void setColors(ColorRamp colors) {
        this.colors = colors;
    }

    /**
     * Set the height multiplier of the fire effect
     * @param height height multiplier of the fire effect
     */
    public void setHeight(double height) {
        this.height = height;
    }

    /**
     * Set the flare chance
     * @param flareChance chance for a flare (0.0 - 1.0)
     */
    public void setFlareChance(double flareChance) {
        this.flareChance = flareChance;
    }

    /**
     * Set the flare brightness multiplier of the fire effect
     * @param flareBrightness brightness multiplier of the fire effect (0.0 - 1.0)
     */
    public void setFlareBrightness(double flareBrightness) {
        this.flareBrightness = flareBrightness;
    }

    /**
     * Get the center bias of the fire effect
     * @return the center bias of the fire effect (0.0 - 1.0)
     */
    public double getCenterBias() {
        return centerBias;
    }

    /**
     * Set the center bias of the fire effect
     * @param centerBias the center bias of the fire effect (0.0 - 1.0)
     */
    public void setCenterBias(double centerBias) {
        this.centerBias = centerBias;
    }

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("colors", this.colors)
                .put("height", this.height)
                .put("flare_chance", this.flareChance)
                .put("flare_brightness", this.flareBrightness)
                .put("center_bias", this.centerBias)
                .toString();
    }
}
