package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;

import java.util.List;

public class CycleEffect extends Effect {
    @SerializeField
    private List<Effect> effects;
    @SerializeField
    private int interval;

    /**
     * Effect to cycle through other effects
     * @param effects list of effects to cycle through
     * @param interval seconds between effect changes
     */
    public CycleEffect(List<Effect> effects, int interval) {
        super("cycle");
        this.effects = effects;
        this.interval = interval;
    }


    /**
     * Get the list of effects to cycle through
     * @return list of effects to cycle through
     */
    public List<Effect> getEffects() {
        return effects;
    }

    /**
     * Set the list of effects to cycle through
     * @param effects list of effects to cycle through
     */
    public void setEffects(List<Effect> effects) {
        this.effects = effects;
    }

    /**
     * Get the interval between effect changes
     * @return interval between effect changes
     */
    public int getInterval() {
        return interval;
    }

    /**
     * Set the interval between effect changes
     * @param interval interval between effect changes
     */
    public void setInterval(int interval) {
        this.interval = interval;
    }
}
