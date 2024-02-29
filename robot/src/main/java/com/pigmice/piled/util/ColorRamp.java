package com.pigmice.piled.util;

import edu.wpi.first.math.Pair;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONArray;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

public class ColorRamp {
    private List<Pair<Color, Double>> colors;

    /**
     * Color Ramp interpolates between colors at positions
     * @param colors list of pairs of color and position (0.0 - 1.0)
     */
    public ColorRamp(List<Pair<Color, Double>> colors) {
        this.colors = colors;
    }

    /**
     * Get color positions
     * @return a list of pairs of color and position
     */
    public List<Pair<Color, Double>> getColors() {
        return colors;
    }

    /**
     * Set color positions
     * @param colors a list of pairs of color and position
     */
    public void setColors(List<Pair<Color, Double>> colors) {
        this.colors = colors;
    }

    /**
     * Get the JSON representation of the ColorRamp
     * @return JSON representation of the ColorRamp
     */
    @Override
    public String toString() {
        JSONArray arr = new JSONArray();
        for (Pair<Color, Double> pair : this.getColors()) {
            Color color = pair.getFirst();
            double pos = pair.getSecond();
            JSONArray pairArr = new JSONArray();
            JSONArray colorArr = new JSONArray();
            colorArr.put((int) (color.red * 255))
                    .put((int) (color.green * 255))
                    .put((int) (color.blue * 255));

            pairArr.put(colorArr).put(pos);
            arr.put(pairArr);
        }
        return arr.toString();
    }
}
