package com.pigmice.piled.led;

import edu.wpi.first.math.Pair;
import org.json.JSONObject;

public class LEDStripSegment extends LEDSegment {
    private final Pair<Integer, Integer> range;

    /**
     * Creates a new LEDStripSegment object
     * @param name name of the segment
     * @param range index range of the segment
     */
    public LEDStripSegment(String name, Pair<Integer, Integer> range) {
        super(name);

        if (range.getFirst() < 0 || range.getSecond() < 0) {
            throw new IllegalArgumentException("Range must be positive");
        }

        if (range.getFirst() > range.getSecond()) {
            throw new IllegalArgumentException("Range must be in ascending order");
        }

        this.range = range;
        this.length = range.getSecond() - range.getFirst();
    }

    /**
     * Get the range of the segment
     * @return range of the segment
     */
    public Pair<Integer, Integer> getRange() {
        return this.range;
    }

    @Override
    public boolean fitsOnDevice(LED device) {
        return range.getSecond() < device.getLength();
    }

    @Override
    public String toString() {
        JSONObject obj = new JSONObject();
        obj.put("name", this.getName())
            .put("range", new int[]{this.getRange().getFirst(), this.getRange().getSecond()});
        return obj.toString();
    }
}
