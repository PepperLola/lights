package com.pigmice.piled.effects;

import org.json.JSONObject;

public abstract class Effect {
    private String name;

    /**
     * LED effect
     *
     * @param name name of the effect
     */
    public Effect(String name) {
        this.name = name;
    }

    /**
     * Get the name of the effect
     * @return name of the effect
     */
    public String getName() {
        return name;
    }

    /**
     * Set the name of the effect
     * @param name name of the effect
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Get the JSONObject representing the effect
     * @return JSONObject representing the effect
     */
    protected abstract JSONObject toJson();

    /**
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return this.toJson().toString();
    }
}
