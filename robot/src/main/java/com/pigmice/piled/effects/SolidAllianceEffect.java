package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class SolidAllianceEffect extends Effect {
    @SerializeField
    private Color redColor;
    @SerializeField
    private Color blueColor;

    /**
     * Solid alliance effect
     * @param redColor red alliance color of solid effect
     * @param blueColor blue alliance color of solid effect
     */
    public SolidAllianceEffect(Color redColor, Color blueColor) {
        super("solid_alliance");
        this.redColor = redColor;
        this.blueColor = blueColor;
    }

    /**
     * Get the red allinace color of the solid effect
     * @return the red alliance color of the solid effect
     * @see Color
     */
    public Color getRedColor() {
        return this.redColor;
    }

    /**
     * Get the blue allinace color of the solid effect
     * @return the blue alliance color of the solid effect
     * @see Color
     */
    public Color getBlueColor() {
        return this.blueColor;
    }

    /**
     * Set the red alliance color of the solid effect
     * @param color the red alliance color of the solid effect
     * @see Color
     */
    public void setRedColor(Color color) {
        this.redColor = color;
    }

    /**
     * Set the blue alliance color of the solid effect
     * @param color the blue alliance color of the solid effect
     * @see Color
     */
    public void setBlueColor(Color color) {
        this.blueColor = color;
    }
}
