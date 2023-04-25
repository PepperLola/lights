package com.pigmice.piled;

import java.util.HashMap;
import java.util.Map;

import com.pigmice.piled.util.NTValue;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.networktables.NetworkTableValue;
import edu.wpi.first.wpilibj.DriverStation;

public class NTValues {
    private final NetworkTable gameInfoTable = NetworkTableInstance.getDefault().getTable("GameInfo");

    /**
     * Creates a new NTValues object.
     */
    public NTValues() {
    }

    /**
     * The alliance value.
     */
    private final NTValue<DriverStation.Alliance> ALLIANCE_VALUE = new NTValue<>(gameInfoTable,
            "alliance",
            DriverStation.Alliance.Invalid, alliance -> NetworkTableValue.makeString(alliance.name().toLowerCase()));

    /**
     * The game stage value.
     */
    private final NTValue<GameStage> GAME_STAGE_VALUE = new NTValue<>(gameInfoTable,
            "stage",
            GameStage.Disabled, gameStage -> NetworkTableValue.makeString(gameStage.name().toLowerCase()));

    /**
     *  A map of custom values.
     */
    private final Map<String, NTValue<?>> OTHER_VALUES = new HashMap<>();

    /**
     * Add a value to the map of custom values
     * @param value value to add
     */
    public void addValue(NTValue<?> value) {
        OTHER_VALUES.put(value.getName(), value);
    }

    /**
     * Get a value from the map of custom values
     * @param name name of the value
     * @return value
     */
    public NTValue<?> getValue(String name) {
        return OTHER_VALUES.get(name);
    }

    /**
     * Set the game stage
     * @param stage stage to set
     */
    void setStage(GameStage stage) {
        GAME_STAGE_VALUE.setValue(stage);
    }

    /**
     * Set the alliance
     * @param alliance alliance to set
     */
    void setAlliance(DriverStation.Alliance alliance) {
        ALLIANCE_VALUE.setValue(alliance);
    }

    /**
     * The game stage.
     */
    public enum GameStage {
        Auto,
        TeleOp,
        Test,
        Disabled
    }
}
