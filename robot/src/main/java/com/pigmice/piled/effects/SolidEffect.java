package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class SolidEffect extends Effect {
    @SerializeField
    private Color color;

    /**
     * Solid effect
     * @param color color of solid effect
     */
    public SolidEffect(Color color) {
        super("solid");
        this.color = color;
    }

    /**
     * Get the color of the solid effect
     * @return the color of the solid effect
     * @see Color
     */
    public Color getColor() {
        return color;
    }

    /**
     * Set the color of the solid effect
     * @param color the color of the solid effect
     * @see Color
     */
    public void setColor(Color color) {
        this.color = color;
    }
}
