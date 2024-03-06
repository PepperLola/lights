package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
import org.json.JSONObject;

import java.util.Map;

public class CustomEffect extends Effect {
    @SerializeField
    private Map<String, Object> props;

    public CustomEffect(String name, Map<String, Object> props) {
        super(name);
        this.props = props;
    }

    /**
     * Get the properties of the custom effect
     * @return properties of the custom effect
     */
    public Map<String, Object> getProps() {
        return this.props;
    }

    /**
     * Get a single prop from the effect
     * @param key key of the property
     * @return value of the property
     */
    public Object getProp(String key) {
        return this.props.get(key);
    }

    /**
     * Overwrite properties for the custom effect
     * @param props properties for the custom effect
     */
    public void setProps(Map<String, Object> props) {
        this.props = props;
    }

    /**
     * Add a single property to the custom effect
     * @param key key of the property
     * @param value value of the property
     */
    public void addProp(String key, Object value) {
        this.props.put(key, value);
    }

    @Override
    public JSONObject toJson() {
        JSONObject obj = new JSONObject()
                .put("name", this.getName());
        this.props.forEach(obj::put);;
        return obj;
    }
}
