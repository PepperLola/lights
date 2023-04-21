package com.pigmice.piled.led;

import org.json.JSONObject;

import com.pigmice.piled.PiLED.LEDType;

public abstract class LED {
    private String name;
    private int port;
    private int length;
    private LEDType ledType;

    public LED(String name, int port, int length, LEDType ledType) {
        this.name = name;
        this.port = port;
        this.length = length;
        this.ledType = ledType;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public LEDType getLEDType() {
        return ledType;
    }

    public void setLEDType(LEDType ledType) {
        this.ledType = ledType;
    }

    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("port", this.getPort())
                .put("length", this.getLength())
                .put("type", this.getLEDType().toString())
                .toString();
    }
}
