package com.pigmice.piled.led;

import com.pigmice.piled.PiLED.LEDType;
import com.pigmice.piled.reflection.SerializeField;

import java.util.List;
import java.util.Map;

public class LEDPanel extends LED {
    @SerializeField
    private int width;
    @SerializeField
    private int height;

    /**
     * Creates a new LED panel
     * @param name name of the LED panel
     * @param port port of the LED panel
     * @param width width of the LED panel
     * @param height height of the LED panel
     * @param segments segments of the LED panel
     */
    public LEDPanel(String name, int port, int width, int height, List<LEDSegment> segments) {
        super(name, port, width * height, LEDType.Panel, segments);
        this.width = width;
        this.height = height;
    }

    /**
     * Creates a new LED panel
     * @param name name of the LED panel
     * @param port port of the LED panel
     * @param width width of the LED panel
     * @param height height of the LED panel
     */
    public LEDPanel(String name, int port, int width, int height) {
        this(name, port, width, height, null);
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
}