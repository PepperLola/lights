package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;

public class TextEffect extends Effect {
    private String text;
    private Color color;

    /**
     * Text effect
     * @param text text to display
     * @param color color of the text
     */
    public TextEffect(String text, Color color) {
        super("text");
        this.text = text;
        this.color = color;
    }

    /**
     * Get the text to display
     * @return text to display
     */
    public String getText() {
        return this.text;
    }

    /**
     * Get the color of the text
     * @return color of the text
     */
    public Color getColor() {
        return this.color;
    }

    /**
     * Set the text to display
     * @param text text to display
     */
    public void setText(String text) {
        this.text = text;
    }

    /**
     * Set the color of the text
     * @param color color of the text
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
                .put("text", this.getText())
                .put("color", ColorUtil.toInt(this.getColor()))
                .toString();
    }
}