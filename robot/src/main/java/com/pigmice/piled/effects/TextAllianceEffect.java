package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;

public class TextAllianceEffect extends Effect {
    private String text;
    private int x;
    private int y;
    private Color redColor;
    private Color blueColor;
    private int scrollSpeed;
    private boolean loop;

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param redColor color of the text for the red alliance
     * @param blueColor color of the text for the blue alliance
     */
    public TextAllianceEffect(String text, int x, int y, Color redColor, Color blueColor) {
        this(text, x, y, redColor, blueColor, 0, true);
    }

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param redColor color of the text for the red alliance
     * @param blueColor color of the text for the blue alliance
     * @param scrollSpeed scroll speed in pixels per second
     */
    public TextAllianceEffect(String text, int x, int y, Color redColor, Color blueColor, int scrollSpeed) {
        this(text, x, y, redColor, blueColor, scrollSpeed, true);
    }

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param redColor color of the text for the red alliance
     * @param blueColor color of the text for the blue alliance
     * @param loop whether or not to loop the scroll animation
     */
    public TextAllianceEffect(String text, int x, int y, Color redColor, Color blueColor, boolean loop) {
        // this constructor doesn't really make sense - why loop when no scroll?
        this(text, x, y, redColor, blueColor, 0, loop);
    }

    /**
     * Text effect
     * @param text text to display
     * @param x x position of the text
     * @param y y position of the text
     * @param redColor color of the text for the red alliance
     * @param blueColor color of the text for the blue alliance
     * @param scrollSpeed scroll speed in pixels per second
     * @param loop whether or not to loop the scroll animation
     */
    public TextAllianceEffect(String text, int x, int y, Color redColor, Color blueColor, int scrollSpeed, boolean loop) {
        super("text");
        this.text = text;
        this.x = x;
        this.y = y;
        this.redColor = redColor;
        this.blueColor = blueColor;
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

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("text", this.getText())
                .put("x", this.getX())
                .put("y", this.getY())
                .put("red_color", ColorUtil.toInt(this.getRedColor()))
                .put("blue_color", ColorUtil.toInt(this.getBlueColor()))
                .put("scroll_speed", this.getScrollSpeed())
                .put("loop", this.shouldLoop())
                .toString();
    }
}
