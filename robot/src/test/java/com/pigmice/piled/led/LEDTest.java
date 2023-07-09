package com.pigmice.piled.led;

import com.pigmice.piled.led.LED;
import static org.junit.Assert.assertEquals;

import org.json.JSONObject;
import org.junit.Test;

public class LEDTest {
    @Test
    public void toStringTest() {
        LED ledStrip = new LEDStrip("test", 1, 2);
        JSONObject stripJson = new JSONObject(ledStrip.toString());
        assertEquals(stripJson.getString("name"), "test");
        assertEquals(stripJson.getInt("port"), 1);
        assertEquals(stripJson.getInt("length"), 2);
        assertEquals(stripJson.getString("type"), "Strip");

        LED ledPanel = new LEDPanel("test", 1, 2, 3);
        JSONObject panelJson = new JSONObject(ledPanel.toString());
        assertEquals(panelJson.getString("name"), "test");
        assertEquals(panelJson.getInt("port"), 1);
        assertEquals(panelJson.getInt("width"), 2);
        assertEquals(panelJson.getInt("height"), 3);
        assertEquals(panelJson.getString("type"), "Panel");
    }
}
