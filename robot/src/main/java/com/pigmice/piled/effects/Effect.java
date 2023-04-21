package com.pigmice.piled.effects;

public class Effect {
    private String name;

    public Effect(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "{\"name\": \"" + this.name + "\"}";
    }
}
