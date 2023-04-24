package com.pigmice.piled.led;

import com.pigmice.piled.PiLED.LEDType;

public class LEDStrip extends LED {

    /**
     * Creates a new LED strip
     * @param name name of the LED strip
     * @param port port of the LED strip
     * @param length length of the LED strip
     */
    public LEDStrip(String name, int port, int length) {
        super(name, port, length, LEDType.Strip);
    }
}
