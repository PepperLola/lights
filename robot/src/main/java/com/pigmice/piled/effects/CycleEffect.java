package com.pigmice.piled.effects;

import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONArray;
import org.json.JSONObject;

import java.util.List;

public class CycleEffect extends Effect {
    private List<Effect> effects;
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

    @Override
    public JSONObject toJson() {
        return new JSONObject()
                .put("name", this.getName())
                .put("interval", this.getInterval())
                .put("effects", new JSONArray(this.getEffects().stream().map(Effect::toJson).toArray()));
    }
}
