package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;

public class SolidAllianceEffect extends Effect {
    private Color red_color;
    private Color blue_color;

    /**
     * Solid alliance effect
     * @param red_color red alliance color of solid effect
     * @param blue_color blue alliance color of solid effect
     */
    public SolidAllianceEffect(Color red_color, Color blue_color) {
        super("solid_alliance");
        this.red_color = red_color;
        this.blue_color = blue_color;
    }

    /**
     * Get the red allinace color of the solid effect
     * @return the red alliance color of the solid effect
     * @see Color
     */
    public Color getRedColor() {
        return this.red_color;
    }

    /**
     * Get the blue allinace color of the solid effect
     * @return the blue alliance color of the solid effect
     * @see Color
     */
    public Color getBlueColor() {
        return this.blue_color;
    }

    /**
     * Set the red alliance color of the solid effect
     * @param color the red alliance color of the solid effect
     * @see Color
     */
    public void setRedColor(Color color) {
        this.red_color = color;
    }

    /**
     * Set the blue alliance color of the solid effect
     * @param color the blue alliance color of the solid effect
     * @see Color
     */
    public void setBlueColor(Color color) {
        this.blue_color = color;
    }

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
            .put("name", this.getName())
            .put("red_color", ColorUtil.toInt(this.red_color))
            .put("blue_color", ColorUtil.toInt(this.blue_color))
            .toString();
    }
}
