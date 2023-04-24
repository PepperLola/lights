package com.pigmice.piled.effects;

public class Effect {
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
     * Get the JSON representation of the effect
     * @return JSON representation of the effect
     */
    @Override
    public String toString() {
        return "{\"name\": \"" + this.name + "\"}";
    }
}
