package com.pigmice.piled.led;

import org.json.JSONObject;

public abstract class LEDSegment {
    private final String name;
    protected int length;

    /**
     * Creates a new LED segment
     * @param name name of the segment
     */
    public LEDSegment(String name) {
        this.name = name;
    }

    /**
     * Get the name of the segment
     * @return name of the segment
     */
    public String getName() {
        return name;
    }

    /**
     * Get the length of the segment
     * @return length of the segment
     */
    public int getLength() {
        return this.length;
    }

    /**
     * Check if the segment fits on the device
     * @param device device to check if the segment fits on
     * @return true if the segment fits on the device, false otherwise
     */
    public abstract boolean fitsOnDevice(LED device);

    /**
     * Get the JSONObject representing the effect
     * @return JSONObject representing the effect
     */
    protected abstract JSONObject toJson();

    /**
     * Get the JSON representation of the segment
     * @return JSON representation of the segment
     */
    @Override
    public String toString() {
        return this.toJson().toString();
    }
}
