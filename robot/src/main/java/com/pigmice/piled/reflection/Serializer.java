package com.pigmice.piled.reflection;

import com.pigmice.piled.PiLED;
import com.pigmice.piled.effects.*;
import com.pigmice.piled.led.LED;
import com.pigmice.piled.led.LEDSegment;
import com.pigmice.piled.led.LEDStrip;
import com.pigmice.piled.led.LEDStripSegment;
import com.pigmice.piled.util.ColorRamp;
import com.pigmice.piled.util.ColorUtil;
import edu.wpi.first.math.Pair;
import edu.wpi.first.wpilibj.util.Color;
import org.json.JSONArray;
import org.json.JSONObject;

import java.lang.annotation.Annotation;
import java.lang.reflect.Field;
import java.util.*;

public class Serializer {
    private static String transformFieldName(String name) {
        return name.replaceAll("([A-Z])", "_$1").toLowerCase();
    }

    private static <T> Object serializeObject(T object) {
        if (object instanceof String) {
            return object;
        } else if (object instanceof Integer) {
            return object;
        } else if (object instanceof Double) {
            return object;
        } else if (object instanceof Float) {
            return object;
        } else if (object instanceof Long) {
            return object;
        } else if (object instanceof Boolean) {
            return object;
        } else if (object instanceof PiLED.LEDType) {
            return object.toString();
        } else if (object instanceof Color) {
            return ColorUtil.toInt((Color) object);
        } else if (object instanceof Pair<?, ?> pair) {
            return new JSONArray(List.of(pair.getFirst(), pair.getSecond()));
        } else if (object instanceof Effect) {
            return serialize((Effect) object);
        } else if (object instanceof LED) {
            return serialize((LED) object);
        } else if (object instanceof LEDSegment) {
            return serialize((LEDSegment) object);
        } else if (object instanceof List<?> list) {
            List<Object> jsonList = new ArrayList<>();
            for (Object item : list) {
                jsonList.add(serializeObject(item));
            }
            return jsonList;
        } else if (object instanceof Map<?, ?> map) {
            JSONObject jsonMap = new JSONObject();
            for (Map.Entry<?, ?> entry : map.entrySet()) {
                jsonMap.put(entry.getKey().toString(), serializeObject(entry.getValue()));
            }
            return jsonMap;
        } else if (object instanceof ColorRamp) {
            return ((ColorRamp) object).toJson();
        }
        return serialize(object);
    }

    public static <T> JSONObject serialize(T object) {
        List<Field> annotatedFields = getAnnotatedFields(object, SerializeField.class);
        JSONObject obj = new JSONObject();
        for (Field field : annotatedFields) {
            try {
                field.setAccessible(true);
                String name = transformFieldName(field.getName());
                obj.put(name, serializeObject(field.get(object)));
            } catch (IllegalAccessException e) {
                e.printStackTrace();
            }
        }
        return obj;
    }

    private static <T> List<Field> getAnnotatedFields(T object, Class<? extends Annotation> annotationClass) {
        List<Field> annotatedFields = new ArrayList<>();
        Class<?> superclass = object.getClass().getSuperclass();
        Class<?> currentClass = object.getClass();
        do {
            Field[] fields = currentClass.getDeclaredFields();
            for (Field field : fields) {
                if (field.isAnnotationPresent(annotationClass)) {
                    annotatedFields.add(field);
                }
            }
            currentClass = superclass;
            superclass = currentClass.getSuperclass();
        } while (superclass != null);
        return annotatedFields;
    }
}
