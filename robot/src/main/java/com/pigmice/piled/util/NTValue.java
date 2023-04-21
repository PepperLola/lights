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

    public NTValue(NetworkTable table, String name, T defaultValue, Function<T, NetworkTableValue> toNTValue) {
        this.table = table;
        this.name = name;
        this.toNTValue = toNTValue;
        this.setValue(defaultValue);
    }

    public String getName() {
        return this.name;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        if (!Objects.equals(this.value, value)) {
            this.table.getEntry(this.name).setValue(this.toNTValue.apply(value));
        }
        this.value = value;
    }
}
