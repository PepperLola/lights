package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

public class TextEffect extends Effect {
    @SerializeField
    private String text;
    @SerializeField
    private Color color;
    @SerializeField
    private int x;
    @SerializeField
    private int y;
    @SerializeField
    private int scrollSpeed;
    @SerializeField
    private boolean loop;

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param color color of the text
     */
    public TextEffect(String text, int x, int y, Color color) {
        this(text, x, y, color, 0, true);
    }

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param color color of the text
     * @param scrollSpeed scroll speed in pixels per second
     */
    public TextEffect(String text, int x, int y, Color color, int scrollSpeed) {
        this(text, x, y, color, scrollSpeed, true);
    }

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param color color of the text
     * @param loop whether or not to loop the scroll animation
     */
    public TextEffect(String text, int x, int y, Color color, boolean loop) {
        // this constructor doesn't really make sense - why loop when no scroll?
        this(text, x, y, color, 0, loop);
    }

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param color color of the text
     * @param scrollSpeed scroll speed in pixels per second
     * @param loop whether or not to loop the scroll animation
     */
    public TextEffect(String text, int x, int y, Color color, int scrollSpeed, boolean loop) {
        super("text");
        this.text = text;
        this.x = x;
        this.y = y;
        this.color = color;
        this.scrollSpeed = scrollSpeed;
        this.loop = loop;
    }

    /**
     * Get the text to display
     * @return text to display
     */
    public String getText() {
        return this.text;
    }

    /**
     * Get the x position of the text
     * @return x position of the text
     */
    public int getX() {
        return this.x;
    }

    /**
     * Get the y position of the text
     * @return y position of the text
     */
    public int getY() {
        return this.y;
    }

    /**
     * Get the color of the text
     * @return color of the text
     */
    public Color getColor() {
        return this.color;
    }

    /**
     * Get the scroll speed of the effect
     * @return scroll speed of the effect
     */
    public int getScrollSpeed() {
        return this.scrollSpeed;
    }

    /**
     * Gets if the scroll animation should loop
     * @return whether the scroll animation should loop
     */
    public boolean shouldLoop() {
        return this.loop;
    }

    /**
     * Set the text to display
     * @param text text to display
     */
    public void setText(String text) {
        this.text = text;
    }

    /**
     * Set the x position of the text
     * @param x x position of the text
     */
    public void setX(int x) {
        this.x = x;
    }

    /**
     * Set the y position of the text
     * @param y y position of the text
     */
    public void setY(int y) {
        this.y = y;
    }

    /**
     * Set the color of the text
     * @param color color of the text
     */
    public void setColor(Color color) {
        this.color = color;
    }

    /**
     * Set the scroll speed of the effect in pixels per second
     * @param scrollSpeed scroll speed of the effect
     */
    public void setScrollSpeed(int scrollSpeed) {
        this.scrollSpeed = scrollSpeed;
    }

    /**
     * Set if the scroll animation should loop
     * @param loop whether the scroll animation should loop
     */
    public void setLoop(boolean loop) {
        this.loop = loop;
    }
}