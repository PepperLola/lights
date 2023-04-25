package com.pigmice.piled.effects;

import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONObject;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class EffectTest {
    @Test
    public void toStringTest() {
        BreatheEffect breatheEffect = new BreatheEffect(Color.kPurple, 1);
        JSONObject stripJson = new JSONObject(breatheEffect.toString());
        assertEquals(stripJson.getString("name"), "Breathe");
        assertEquals(stripJson.getInt("color"), 8388736);
        assertEquals(stripJson.getInt("speed"), 1);

        SolidEffect solidEffect = new SolidEffect(Color.kPurple);
        stripJson = new JSONObject(solidEffect.toString());
        assertEquals(stripJson.getString("name"), "Solid");
        assertEquals(stripJson.getInt("color"), 8388736);

        RainbowEffect rainbowEffect = new RainbowEffect(1);
        stripJson = new JSONObject(rainbowEffect.toString());
        assertEquals(stripJson.getString("name"), "Rainbow");
        assertEquals(stripJson.getInt("speed"), 1);
    }
}
