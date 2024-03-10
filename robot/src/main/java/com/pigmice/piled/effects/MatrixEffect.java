package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import com.pigmice.piled.util.ColorRamp;
import edu.wpi.first.wpilibj.util.Color;

/**
 * Matrix Effect
 */
public class MatrixEffect extends Effect {
	@SerializeField
	private ColorRamp color;

	@SerializeField
	private int speed;

	@SerializeField
	private double interval;

	@SerializeField
	private int rainLength;

	/**
	 * Matrix Effect
	 * @param color color for the matrix effect
	 * @param speed speed for the matrix effect
	 * @param interval interval for the matrix effect
	 * @param rainLength rainLength for the matrix effect
	 */
	public MatrixEffect(ColorRamp color, int speed, double interval, int rainLength) {
		super("matrix");
		this.color = color;
		this.speed = speed;
		this.interval = interval;
		this.rainLength = rainLength;
	}

	/**
	 * Get the color for the matrix effect
	 * @return color for the matrix effect
	 */
	public ColorRamp getColor() {
	    return this.color;
	}

	/**
	 * Set the color for the matrix effect
	 * @param color color for the matrix effect
	 */
	public void setColor(ColorRamp color) {
	    this.color = color;
	}

	/**
	 * Get the speed for the matrix effect
	 * @return speed for the matrix effect
	 */
	public int getSpeed() {
	    return this.speed;
	}

	/**
	 * Set the speed for the matrix effect
	 * @param speed speed for the matrix effect
	 */
	public void setSpeed(int speed) {
	    this.speed = speed;
	}

	/**
	 * Get the interval for the matrix effect
	 * @return interval for the matrix effect
	 */
	public double getInterval() {
	    return this.interval;
	}

	/**
	 * Set the interval for the matrix effect
	 * @param interval interval for the matrix effect
	 */
	public void setInterval(double interval) {
	    this.interval = interval;
	}

	/**
	 * Get the rain length for the matrix effect
	 * @return rain length for the matrix effect
	 */
	public int getRainLength() {
	    return this.rainLength;
	}

	/**
	 * Set the rain length for the matrix effect
	 * @param rain length rainLength for the matrix effect
	 */
	public void setRainLength(int rainLength) {
	    this.rainLength = rainLength;
	}
}