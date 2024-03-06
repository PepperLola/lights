package com.pigmice.piled.led;

import com.pigmice.piled.reflection.SerializeField;
import edu.wpi.first.math.Pair;
import org.json.JSONObject;

public class LEDPanelSegment extends LEDSegment {
    @SerializeField
    private final int width;
    @SerializeField
    private final int height;
    @SerializeField
    private final Pair<Integer, Integer> topLeft;
    @SerializeField
    private final Pair<Integer, Integer> bottomRight;

    /**
     * Creates a new LEDPanelSegment object
     * @param name name of the segment
     * @param topLeft top left corner of the segment
     * @param bottomRight bottom right corner of the segment
     */
    public LEDPanelSegment(String name, Pair<Integer, Integer> topLeft, Pair<Integer, Integer> bottomRight) {
        super(name);

        if (topLeft.getFirst() < 0 || topLeft.getSecond() < 0 || bottomRight.getFirst() < 0 || bottomRight.getSecond() < 0) {
            throw new IllegalArgumentException("Points must fit on the device");
        }

        if (topLeft.getFirst() > bottomRight.getFirst() || topLeft.getSecond() > bottomRight.getSecond()) {
            throw new IllegalArgumentException("Top left point must be above and to the left of bottom right point");
        }

        this.length = (bottomRight.getFirst() - topLeft.getFirst()) * (bottomRight.getSecond() - topLeft.getSecond());

        this.topLeft = topLeft;
        this.bottomRight = bottomRight;
        this.width = bottomRight.getFirst() - topLeft.getFirst();
        this.height = bottomRight.getSecond() - topLeft.getSecond();
    }

    @Override
    public boolean fitsOnDevice(LED device) {
        return bottomRight.getFirst() + bottomRight.getSecond() * width < device.getLength();
    }

    /**
     * Get the width of the segment
     * @return width of the segment
     */
    public int getWidth() {
        return width;
    }

    /**
     * Get the height of the segment
     * @return height of the segment
     */
    public int getHeight() {
        return height;
    }

    /**
     * Get the top left corner of the segment
     * @return top left corner of the segment
     */
    public Pair<Integer, Integer> getTopLeft() {
        return topLeft;
    }

    /**
     * Get the bottom right corner of the segment
     * @return bottom right corner of the segment
     */
    public Pair<Integer, Integer> getBottomRight() {
        return bottomRight;
    }

    @Override
    public JSONObject toJson() {
        JSONObject obj = new JSONObject();
        obj.put("name", this.getName())
            .put("topLeft", new int[]{topLeft.getFirst(), topLeft.getSecond()})
            .put("bottomRight", new int[]{bottomRight.getFirst(), bottomRight.getSecond()});
        return obj;
    }
}
