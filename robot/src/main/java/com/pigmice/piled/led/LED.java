package com.pigmice.piled.led;

import org.json.JSONObject;

import com.pigmice.piled.PiLED.LEDType;

import java.util.Map;

public abstract class LED {
    private String name;
    private int port;
    private int length;
    private LEDType ledType;
    private Map<String, LEDSegment> segments;

    /**
     * Creates a new LED object
     * @param name name of the LED
     * @param port port of the LED
     * @param length length of the LED
     * @param ledType type of the LED
     * @param segments segments of the LED
     * @see LEDType
     * @see LEDSegment
     */
    public LED(String name, int port, int length, LEDType ledType, Map<String, LEDSegment> segments) {
        this.name = name;
        this.port = port;
        this.length = length;
        this.ledType = ledType;

        for (LEDSegment segment : segments.values()) {
            if (!segment.fitsOnDevice(this)) {
                throw new IllegalArgumentException(String.format("Segment \"%s\" does not fit on device", segment.getName()));
            }
        }
        this.segments = segments;
    }

    /**
     * Get the name of the LED
     * @return name of the LED
     */
    public String getName() {
        return name;
    }

    /**
     * Set the name of the LED
     * @param name name of the LED
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Get the port of the LED
     * @return port of the LED
     */
    public int getPort() {
        return port;
    }

    /**
     * Set the port of the LED
     * @param port port of the LED
     */
    public void setPort(int port) {
        this.port = port;
    }

    /**
     * Get the length of the LED
     * @return length of the LED
     */
    public int getLength() {
        return length;
    }

    /**
     * Set the length of the LED
     * @param length length of the LED
     */
    public void setLength(int length) {
        this.length = length;
    }

    /**
     * Get the type of the LED
     * @return type of the LED
     * @see LEDType
     */
    public LEDType getLEDType() {
        return ledType;
    }

    /**
     * Set the type of the LED
     * @param ledType type of the LED
     * @see LEDType
     */
    public void setLEDType(LEDType ledType) {
        this.ledType = ledType;
    }

    /**
     * Get the segments of the LED
     * @return segments of the LED
     */
    public Map<String, LEDSegment> getSegments() {
        return segments;
    }

    /**
     * Set the segments of the LED
     * @param segments segments of the LED
     */
    public void setSegments(Map<String, LEDSegment> segments) {
        for (LEDSegment segment : segments.values()) {
            if (!segment.fitsOnDevice(this)) {
                throw new IllegalArgumentException(String.format("Segment \"%s\" does not fit on device", segment.getName()));
            }
        }
        this.segments = segments;
    }

    /**
     * Add a segment to the LED
     * @param segment segment to add
     */
    public void addSegment(LEDSegment segment) {
        if (!segment.fitsOnDevice(this)) {
            throw new IllegalArgumentException("Segment does not fit on device");
        }
        segments.put(segment.getName(), segment);
    }

    /**
     * Get the JSON representation of the LED
     * @return JSON representation of the LED
     */
    @Override
    public String toString() {
        return new JSONObject()
                .put("name", this.getName())
                .put("port", this.getPort())
                .put("length", this.getLength())
                .put("type", this.getLEDType().toString())
                .put("segments", this.getSegments().values().stream().map(LEDSegment::toString).toArray())
                .toString();
    }
}
