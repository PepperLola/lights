package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class MorseEffect extends Effect {
    @SerializeField
    private String text;
    @SerializeField
    private Color color;
    @SerializeField
    private int wpm;

    /**
     * Morse effect
     * @param text text to display in Morse code
     * @param color color of morse effect
     * @param wpm words per minute to show
     */
    public MorseEffect(String text, Color color, int wpm) {
        super("breathe");
        this.text = text;
        this.color = color;
        this.wpm = wpm;
    }

    /**
     * Get the text of the morse effect
     * @return text of the morse effect
     */
    public String getText() {
        return text;
    }

    /**
     * Set the text of the morse effect
     * @param text text of the morse effect
     */
    public void setText(String text) {
        this.text = text;
    }

    /**
     * Get the color of the morse effect
     * @return the color of the morse effect
     * @see Color
     */
    public Color getColor() {
        return color;
    }

    /**
     * Set the color of the morse effect
     * @param color the color of the morse effect
     */
    public void setColor(Color color) {
        this.color = color;
    }

    /**
     * Get the wpm of the morse effect
     * @return wpm of the morse effect
     */
    public int getWPM() {
        return wpm;
    }

    /**
     * Set the wpm of the morse effect
     * @param wpm wpm of the morse effect
     */
    public void setWPM(int wpm) {
        this.wpm = wpm;
    }
}
