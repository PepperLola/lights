package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;


/**
 * Demo Effect
 */
public class DemoEffect extends Effect {
	@SerializeField
	private int interval;

	/**
	 * Demo Effect
	 * @param interval interval for the demo effect
	 */
	public DemoEffect(int interval) {
		super("demo");
		this.interval = interval;
	}

	/**
	 * Get the interval for the demo effect
	 * @return interval for the demo effect
	 */
	public int getInterval() {
	    return this.interval;
	}

	/**
	 * Set the interval for the demo effect
	 * @param interval interval for the demo effect
	 */
	public void setInterval(int interval) {
	    this.interval = interval;
	}
}