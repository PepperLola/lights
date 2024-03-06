package com.pigmice.piled.effects;

import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;

public class EffectTest {
    @Test
    public void toStringTest() {
        BreatheEffect breatheEffect = new BreatheEffect(Color.kPurple, 1d);
        JSONObject effectJson = new JSONObject(breatheEffect.toString());
        assertEquals(effectJson.getString("name"), "breathe");
        assertEquals(effectJson.getInt("color"), 8388736);
        assertEquals(effectJson.getInt("speed"), 1d, 0.00001);

        SolidEffect solidEffect = new SolidEffect(Color.kPurple);
        effectJson = new JSONObject(solidEffect.toString());
        assertEquals(effectJson.getString("name"), "solid");
        assertEquals(effectJson.getInt("color"), 8388736);

        RainbowEffect rainbowEffect = new RainbowEffect(1, 0.01);
        effectJson = new JSONObject(rainbowEffect.toString());
        assertEquals(effectJson.getString("name"), "rainbow");
        assertEquals(effectJson.getInt("speed"), 1);
        assertEquals(effectJson.getDouble("increment"), 0.01, 0.00001);

        Map<String, Object> props = new HashMap<>();
        props.put("step", 1);
        props.put("speed", 0.0025);
        props.put("text", "TEST");
        props.put("reverse", false);
        CustomEffect customEffect = new CustomEffect("custom", props);
        effectJson = new JSONObject(customEffect.toString());
        assertEquals(effectJson.getString("name"), "custom");
        assertEquals(effectJson.getInt("step"), 1);
        assertEquals(effectJson.getDouble("speed"), 0.0025, 0.00001);
        assertEquals(effectJson.getString("text"), "TEST");
        assertEquals(effectJson.getBoolean("reverse"), false);
    }
}
