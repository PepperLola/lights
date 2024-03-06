package com.pigmice.piled.led;

import com.pigmice.piled.PiLED.LEDType;
import edu.wpi.first.math.Pair;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LEDStrip extends LED {

    /**
     * Creates a new LED strip
     * @param name name of the LED strip
     * @param port port of the LED strip
     * @param length length of the LED strip
     * @param segments segments of the LED strip
     */
    public LEDStrip(String name, int port, int length, List<LEDSegment> segments) {
        super(name, port, length, LEDType.Strip, segments);
    }

    /**
     * Creates a new LED strip
     * @param name name of the LED strip
     * @param port port of the LED strip
     * @param length length of the LED strip
     */
    public LEDStrip(String name, int port, int length) {
        this(name, port, length, null);
    }
}
