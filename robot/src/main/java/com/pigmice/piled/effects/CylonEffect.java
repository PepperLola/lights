package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class CylonEffect extends Effect {
    @SerializeField
    private Color color;
    @SerializeField
    private int speed;
    @SerializeField
    private int dist;

    /**
     * Cylon effect
     * @param color color of cylon effect
     * @param speed number of pixels per second
     */
    public CylonEffect(Color color, int speed) {
        super("breathe");
        this.color = color;
        this.speed = speed;
    }

    /**
     * Get the color of the cylon effect
     * @return the color of the cylon effect
     * @see Color
     */
    public Color getColor() {
        return color;
    }

    /**
     * Set the color of the cylon effect
     * @param color the color of the cylon effect
     */
    public void setColor(Color color) {
        this.color = color;
    }

    /**
     * Get the speed of the cylon effect in pixels per second
     * @return speed of the cylon effect
     */
    public int getSpeed() {
        return speed;
    }

    /**
     * Set the speed of the cylon effect in pixels per second
     * @param speed speed of the cylon effect
     */
    public void setSpeed(int speed) {
        this.speed = speed;
    }

    /**
     * Get the distance across which to fade of the cylon effect in pixels
     * @return distance for the cylon effect
     */
    public int getDistance() {
        return dist;
    }

    /**
     * Set the distance across which to fade of the cylon effect in pixels
     * @param dist distance for the cylon effect
     */
    public void setDistance(int dist) {
        this.dist = dist;
    }
}
