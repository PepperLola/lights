package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;

public class SolidEffect extends Effect {
    private Color color;

    /**
     * Solid effect
     * @param color color of solid effect
     */
    public SolidEffect(Color color) {
        super("Solid");
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

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
            .put("name", this.getName())
            .put("color", ColorUtil.toInt(this.color))
            .toString();
    }
}
