package com.pigmice.piled.led;

import com.pigmice.piled.reflection.SerializeField;
import com.pigmice.piled.reflection.Serializer;
import org.json.JSONObject;

import com.pigmice.piled.PiLED.LEDType;

import javax.annotation.Nullable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public abstract class LED {
    @SerializeField
    private String name;
    @SerializeField
    private int port;
    @SerializeField
    private int length;
    @SerializeField
    private LEDType type;
    @SerializeField
    private List<LEDSegment> segments;

    /**
     * Creates a new LED object
     * @param name name of the LED
     * @param port port of the LED
     * @param length length of the LED
     * @param type type of the LED
     * @param segments segments of the LED
     * @see LEDType
     * @see LEDSegment
     */
    public LED(String name, int port, int length, LEDType type, @Nullable List<LEDSegment> segments) {
        this.name = name;
        this.port = port;
        this.length = length;
        this.type = type;

        if (segments == null) {
            this.segments = new ArrayList<>();
        } else {
            for (LEDSegment segment : segments) {
                if (!segment.fitsOnDevice(this)) {
                    throw new IllegalArgumentException(String.format("Segment \"%s\" does not fit on device", segment.getName()));
                }
            }
            this.segments = segments;
        }
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
        return type;
    }

    /**
     * Set the type of the LED
     * @param type type of the LED
     * @see LEDType
     */
    public void setLEDType(LEDType type) {
        this.type = type;
    }

    /**
     * Get the segments of the LED
     * @return segments of the LED
     */
    public List<LEDSegment> getSegments() {
        return segments;
    }

    /**
     * Set the segments of the LED
     * @param segments segments of the LED
     */
    public void setSegments(List<LEDSegment> segments) {
        for (LEDSegment segment : segments) {
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
        segments.add(segment);
    }

    /**
     * Get the JSONObject representing the effect
     * @return JSONObject representing the effect
     */
    protected JSONObject toJson() {
        return Serializer.serialize(this);
    }

    /**
     * Get the JSON representation of the LED
     * @return JSON representation of the LED
     */
    @Override
    public String toString() {
        return this.toJson().toString();
    }
}
