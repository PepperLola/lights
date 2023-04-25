package com.pigmice.piled.util;

import java.util.Objects;

import com.google.common.base.Function;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableValue;

public class NTValue<T> {
    private NetworkTable table;
    private T value;
    private String name;
    private Function<T, NetworkTableValue> toNTValue;

    /**
     * Creates a new NTValue
     * @param table NetworkTable to store the value in
     * @param name name of the value
     * @param defaultValue default value
     * @param toNTValue function to convert the value to a NetworkTableValue
     * @see NetworkTable
     * @see NetworkTableValue
     */
    public NTValue(NetworkTable table, String name, T defaultValue, Function<T, NetworkTableValue> toNTValue) {
        this.table = table;
        this.name = name;
        this.toNTValue = toNTValue;
        this.setValue(defaultValue);
    }

    /**
     * Get the name of the value
     * @return name of the value
     */
    public String getName() {
        return this.name;
    }

    /**
     * Get the value
     * @return value
     */
    public T getValue() {
        return value;
    }

    /**
     * Set the value
     * @param value value
     */
    public void setValue(T value) {
        if (this.table != null && !Objects.equals(this.value, value)) {
            this.table.getEntry(this.name).setValue(this.toNTValue.apply(value));
        }
        this.value = value;
    }
}
