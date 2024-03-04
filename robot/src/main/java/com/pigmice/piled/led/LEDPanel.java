package com.pigmice.piled.led;

import org.json.JSONObject;

import com.pigmice.piled.PiLED.LEDType;

import java.util.Map;

public class LEDPanel extends LED {
    private int width;
    private int height;

    /**
     * Creates a new LED panel
     * @param name name of the LED panel
     * @param port port of the LED panel
     * @param width width of the LED panel
     * @param height height of the LED panel
     * @param segments segments of the LED panel
     */
    public LEDPanel(String name, int port, int width, int height, Map<String, LEDSegment> segments) {
        super(name, port, width * height, LEDType.Panel, segments);
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
                .put("segments", this.getSegments().values().stream().map(LEDSegment::toString).toArray())
                .toString();
    }
}