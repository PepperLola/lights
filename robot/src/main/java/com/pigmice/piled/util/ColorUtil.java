package com.pigmice.piled.util;

import edu.wpi.first.wpilibj.util.Color;

public class ColorUtil {
    public static int toInt(Color color) {
        return toInt(color.red, color.green, color.blue);
    }

    public static int toInt(double r, double g, double b) {
        return toInt((int) (r * 255), (int) (g * 255), (int) (b * 255));
    }

    public static int toInt(int r, int g, int b) {
        return (r << 16) + (g << 8) + b;
    }
}
