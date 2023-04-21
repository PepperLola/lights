package com.pigmice.piled.led;

import org.json.JSONObject;

import com.pigmice.piled.PiLED.LEDType;

public class LEDPanel extends LED {
    private int width;
    private int height;

    public LEDPanel(String name, int port, int width, int height) {
        super(name, port, width * height, LEDType.Panel);
        this.width = width;
        this.height = height;
    }

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

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