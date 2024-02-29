package com.pigmice.piled.effects;

import com.pigmice.piled.util.ColorUtil;
import org.json.JSONObject;

public class AnimationEffect extends Effect {
    private String path;
    private int speed;

    /**
     * Animation effect
     * @param path path to animation
     * @param speed speed of the animation (in frames per second)
     */
    public AnimationEffect(String path, int speed) {
        super("animation");
        this.path = path;
        this.speed = speed;
    }

    /**
     * Animation effect
     * @param path path to animation
     */
    public AnimationEffect(String path) {
        this(path, 24);
    }

    /**
     * Animation effect
     */
    public AnimationEffect() {
        this("animations/bad_apple.gif", 24);
    }

    /**
     * Get the path of the animation
     * @return the path of the animation
     */
    public String getPath() {
        return this.path;
    }

    /**
     * Get the speed of the animation (in frames per second)
     * @return the speed of the animation (in frames per second)
     */
    public int getSpeed() {
        return this.speed;
    }

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("path", this.getPath())
                .put("speed", this.getSpeed())
                .toString();
    }
}
