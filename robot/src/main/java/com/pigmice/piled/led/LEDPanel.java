package com.pigmice.piled.led;

import org.json.JSONObject;

import com.pigmice.piled.PiLED.LEDType;

public class LEDPanel extends LED {
    private int width;
    private int height;

    /**
     * Creates a new LED panel
     * @param name name of the LED panel
     * @param port port of the LED panel
     * @param width width of the LED panel
     * @param height height of the LED panel
     */
    public LEDPanel(String name, int port, int width, int height) {
        super(name, port, width * height, LEDType.Panel);
        this.width = width;
        this.height = height;
    }

    /**
     * Get the width of the LED panel
     * @return width of the LED panel
     */
    public int getWidth() {
        return width;
    }

    /**
     * Set the width of the LED panel
     * @param width width of the LED panel
     */
    public void setWidth(int width) {
        this.width = width;
    }

    /**
     * Get the height of the LED panel
     * @return height of the LED panel
     */
    public int getHeight() {
        return height;
    }

    /**
     * Set the height of the LED panel
     * @param height height of the LED panel
     */
    public void setHeight(int height) {
        this.height = height;
    }

    /**
     * Get the JSON representation of the LED panel
     * @return JSON representation of the LED panel
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("port", this.getPort())
                .put("width", this.getWidth())
                .put("height", this.getHeight())
                .put("type", this.getLEDType().toString())
                .toString();
    }
}