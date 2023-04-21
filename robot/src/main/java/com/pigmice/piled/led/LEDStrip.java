package com.pigmice.piled.led;

import com.pigmice.piled.PiLED.LEDType;

public class LEDStrip extends LED {

    public LEDStrip(String name, int port, int length) {
        super(name, port, length, LEDType.Strip);
    }
}
