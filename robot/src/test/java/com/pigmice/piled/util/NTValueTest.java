package com.pigmice.piled.util;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableValue;
import org.junit.Test;

import java.util.Optional;

import static org.junit.Assert.assertEquals;

public class NTValueTest {
    @Test
    public void nameTest() {
        NTValue<String> stringValue = new NTValue<>(null, "test_string", "default value", String -> NetworkTableValue.makeString("test string"));
        NTValue<Integer> intValue = new NTValue<>(null, "test_int", 2733, String -> NetworkTableValue.makeDouble(2733));
        NTValue<Double> doubleValue = new NTValue<>(null, "test_double", 3.1415D, String -> NetworkTableValue.makeDouble(3.1415D));

        assertEquals(stringValue.getName(), "test_string");
        assertEquals(intValue.getName(), "test_int");
        assertEquals(doubleValue.getName(), "test_double");
    }

    @Test
    public void valueTest() {
        NTValue<String> stringValue = new NTValue<>(null, "test_string", "default value", String -> NetworkTableValue.makeString("test string"));
        NTValue<Integer> intValue = new NTValue<>(null, "test_int", 2733, String -> NetworkTableValue.makeDouble(2733));
        NTValue<Double> doubleValue = new NTValue<>(null, "test_double", 3.1415D, String -> NetworkTableValue.makeDouble(3.1415D));

        assertEquals(stringValue.getValue(), "default value");
        assertEquals((int) intValue.getValue(), 2733);
        assertEquals(doubleValue.getValue(), 3.1415D, 1E-10);

        stringValue.setValue("changed value");
        intValue.setValue(3636);
        doubleValue.setValue(2.71828D);

        assertEquals(stringValue.getValue(), "changed value");
        assertEquals((int) intValue.getValue(), 3636);
        assertEquals(doubleValue.getValue(), 2.71828D, 1E-10);
    }

    // TODO figure out a good way of simulating or hosting a network table for testing?
}
