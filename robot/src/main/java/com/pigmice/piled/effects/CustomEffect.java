package com.pigmice.piled.effects;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class CustomEffect extends Effect {
    private Map<String, Object> props = new HashMap<>();

    public CustomEffect(String name, Map<String, Object> props) {
        super(name);
        this.props = props;
    }

    @Override
    public String toString() {
        JSONObject obj = new JSONObject()
                .put("name", this.getName());
        for (Map.Entry<String, Object> entry : this.props.entrySet()) {
            obj.put(entry.getKey(), entry.getValue());
        }

        return obj.toString();
    }
}
