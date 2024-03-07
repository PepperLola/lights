package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import com.pigmice.piled.util.ColorRamp;
import edu.wpi.first.math.Pair;
import edu.wpi.first.wpilibj.util.Color;

import java.util.List;

public class SolidEffect extends Effect {
    @SerializeField
    private ColorRamp color;

    /**
     * Solid effect
     * @param color color of solid effect
     */
    public SolidEffect(Color color) {
        super("solid");
        this.color = new ColorRamp(List.of(new Pair<>(color, 0d), new Pair<>(color, 1d)));
    }

    /**
     * Solid effect
     * @param colorRamp color ramp of solid effect
     */
    public SolidEffect(ColorRamp colorRamp) {
        super("solid");
        this.color = colorRamp;
    }

    /**
     * Get the color ramp of the solid effect
     * @return the color ramp of the solid effect
     * @see ColorRamp
     */
    public ColorRamp getColorRamp() {
        return color;
    }

    /**
     * Set the color ramp of the solid effect
     * @param colorRamp the color ramp of the solid effect
     * @see ColorRamp
     */
    public void setColorRamp(ColorRamp colorRamp) {
        this.color = colorRamp;
    }
}
