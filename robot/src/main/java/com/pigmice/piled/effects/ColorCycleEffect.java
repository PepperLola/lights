package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.wpilibj.util.Color;

import java.util.List;


/**
 * ColorCycle Effect
 */
public class ColorCycleEffect extends Effect {
	@SerializeField
	private List<Color> colors;

	@SerializeField
	private int interval;

	/**
	 * ColorCycle Effect
	 * @param colors colors for the color cycle effect
	 * @param interval interval for the color cycle effect
	 */
	public ColorCycleEffect(List<Color> colors, int interval) {
		super("color_cycle");
		this.colors = colors;
		this.interval = interval;
	}

	/**
	 * Get the colors for the color cycle effect
	 * @return colors for the color cycle effect
	 */
	public List<Color> getColors() {
	    return this.colors;
	}

	/**
	 * Set the colors for the color cycle effect
	 * @param colors colors for the color cycle effect
	 */
	public void setColors(List<Color> colors) {
	    this.colors = colors;
	}

	/**
	 * Get the interval for the color cycle effect
	 * @return interval for the color cycle effect
	 */
	public int getInterval() {
	    return this.interval;
	}

	/**
	 * Set the interval for the color cycle effect
	 * @param interval interval for the color cycle effect
	 */
	public void setInterval(int interval) {
	    this.interval = interval;
	}
}