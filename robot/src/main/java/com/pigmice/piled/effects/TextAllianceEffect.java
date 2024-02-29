package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;

public class TextAllianceEffect extends Effect {
    private String text;
    private Color redColor;
    private Color blueColor;

    /**
     * Text effect
     * @param text text to display
     * @param redColor color of the text for the red alliance
     * @param blueColor color of the text for the blue alliance
     */
    public TextAllianceEffect(String text, Color redColor, Color blueColor) {
        super("text");
        this.text = text;
        this.redColor = redColor;
        this.blueColor = blueColor;
    }

    /**
     * Get the text to display
     * @return text to display
     */
    public String getText() {
        return this.text;
    }

    /**
     * Get the color of the text for the red alliance
     * @return color of the text for the red alliance
     */
    public Color getRedColor() {
        return this.redColor;
    }

    /**
     * Get the color of the text for the blue alliance
     * @return color of the text for the blue alliance
     */
    public Color getBlueColor() {
        return this.blueColor;
    }

    /**
     * Set the text to display
     * @param text text to display
     */
    public void setText(String text) {
        this.text = text;
    }

    /**
     * Set the color of the text for the red alliance
     * @param color color of the text for the red alliance
     */
    public void setRedColor(Color color) {
        this.redColor = color;
    }

    /**
     * Set the color of the text for the blue alliance
     * @param color color of the text for the blue alliance
     */
    public void setBlueColor(Color color) {
        this.blueColor = color;
    }

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("text", this.getText())
                .put("red_color", ColorUtil.toInt(this.getRedColor()))
                .put("blue_color", ColorUtil.toInt(this.getBlueColor()))
                .toString();
    }
}
