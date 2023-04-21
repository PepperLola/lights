package com.pigmice.piled;

import java.util.HashMap;
import java.util.Map;

import com.pigmice.piled.util.NTValue;

import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.networktables.NetworkTableValue;
import edu.wpi.first.wpilibj.DriverStation;

public class NTValues {
    private NetworkTable gameInfoTable;

    public NTValues() {
        this.gameInfoTable = NetworkTableInstance.getDefault().getTable("GameInfo");
    }

    private final NTValue<DriverStation.Alliance> ALLIANCE_VALUE = new NTValue<>(gameInfoTable,
            "alliance",
            DriverStation.Alliance.Invalid, alliance -> NetworkTableValue.makeString(alliance.name().toLowerCase()));

    private final NTValue<GameStage> GAME_STAGE_VALUE = new NTValue<>(gameInfoTable,
            "stage",
            GameStage.Disabled, gameStage -> NetworkTableValue.makeString(gameStage.name().toLowerCase()));

    /**
     *
     */
    private final Map<String, NTValue<?>> OTHER_VALUES = new HashMap<>();

    public void addValue(NTValue<?> value) {
        OTHER_VALUES.put(value.getName(), value);
    }

    public NTValue<?> getValue(String name) {
        return OTHER_VALUES.get(name);
    }

    void setStage(GameStage stage) {
        GAME_STAGE_VALUE.setValue(stage);
    }

    void setAlliance(DriverStation.Alliance alliance) {
        ALLIANCE_VALUE.setValue(alliance);
    }

    public enum GameStage {
        Auto,
        TeleOp,
        Test,
        Disabled
    }
}
