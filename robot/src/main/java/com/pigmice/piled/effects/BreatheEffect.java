package com.pigmice.piled.effects;

import org.json.JSONObject;

import edu.wpi.first.wpilibj.util.Color;

public class BreatheEffect extends Effect {
    private Color color;
    private double speed;

    public BreatheEffect(Color color, double speed) {
        super("Breathe");
        this.color = color;
        this.speed = speed;
    }

    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }

    public double getSpeed() {
        return speed;
    }

    public void setSpeed(double speed) {
        this.speed = speed;
    }

    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("color", this.getColor())
                .put("speed", this.getSpeed())
                .toString();
    }
}
