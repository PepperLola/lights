package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;
import java.util.List;

/**
 * ColorCycleBlink Effect
 */
public class ColorCycleBlinkEffect extends Effect {
	@SerializeField
	private List<Color> colors;

	@SerializeField
	private int interval;

	/**
	 * ColorCycleBlink Effect
	 * @param colors colors for the color cycle blink effect
	 * @param interval interval for the color cycle blink effect
	 */
	public ColorCycleBlinkEffect(List<Color> colors, int interval) {
		super("color_cycle_blink");
		this.colors = colors;
		this.interval = interval;
	}

	/**
	 * Get the colors for the color cycle blink effect
	 * @return colors for the color cycle blink effect
	 */
	public List<Color> getColors() {
	    return this.colors;
	}

	/**
	 * Set the colors for the color cycle blink effect
	 * @param colors colors for the color cycle blink effect
	 */
	public void setColors(List<Color> colors) {
	    this.colors = colors;
	}

	/**
	 * Get the interval for the color cycle blink effect
	 * @return interval for the color cycle blink effect
	 */
	public int getInterval() {
	    return this.interval;
	}

	/**
	 * Set the interval for the color cycle blink effect
	 * @param interval interval for the color cycle blink effect
	 */
	public void setInterval(int interval) {
	    this.interval = interval;
	}
}