import glob
import os
import re
import itertools
from os import path
wd = path.dirname(path.realpath(__file__))
EXCLUDED_FILENAMES = ["importer.py", "led_effect.py", "not_connected.py"] # don't include not_connected, not something user can set
python_effects_dir_path = path.join(wd, "..", "pi", "effects")
effects_glob_path = path.join(python_effects_dir_path, "*.py")
effect_files = map(lambda p: p[p.rfind("/")+1:], glob.glob(effects_glob_path))
effect_python_files = list(filter(lambda f: f[:2] != "__" and f not in EXCLUDED_FILENAMES, effect_files))
java_effects_dir_path = path.join(wd, "..", "robot", "src", "main", "java", "com", "pigmice", "piled", "effects")
java_effects_glob_path = path.join(java_effects_dir_path, "*.java")
effect_java_files = list(map(lambda p: p[p.rfind("/")+1:], glob.glob(java_effects_glob_path)))

# convert python constructor to list of tuple of param name, type, default value
param_pattern = re.compile(r"(\S+): ?([^,)]+)")
EXCLUDED_PARAM_NAMES = ["segment"]
def process_constructor(s: str) -> list[tuple[str, str, str]]:
    names_and_types = list(map(lambda match: match[:2], param_pattern.findall(s)))
    ret = []
    for (n, t) in names_and_types:
        if n in EXCLUDED_PARAM_NAMES:
            continue
        default_val = None
        if "=" in t:
            (t, default_val) = re.split(pattern=" ?= ?", string=t)
        else:
            default_val = ""
        ret.append((n, t, default_val))
    return ret

def python_to_java_value(s: str, within_generic = False) -> str:
    values_dict: dict[str, str] = {
        "None": "null",
        "True": "true",
        "False": "false"
    }
    if s in values_dict.keys():
        return values_dict[s]
    # figure out lists and stuff
    if "list" in s:
        if not "[" in s:
            raise Exception("Need to define type of list")
        first_index = s.index("[")
        last_index = s.rfind("]")
        inner = s[first_index+1:last_index]
        return f"new ArrayList<{python_to_java_type(inner, True)}>{'()' if not within_generic else ''}"
    return s


# convert python to java type, assumes nested lists are java arrays instead of arraylist
def python_to_java_type(s: str, assume_array = False) -> str:
    types_dict: dict[str, str] = {
        "str": "String",
        "int": "int",
        "float": "double",
        "bool": "boolean",
        "LEDEffect": "Effect",
        "LEDSegment": "LEDSegment",
        "ColorRamp": "ColorRamp",
        "Color": "Color",
    }
    if s in types_dict.keys():
        return types_dict[s]
    # figure out lists and stuff
    if "list" in s:
        if not "[" in s:
            raise Exception("Need to define type of list")
        first_index = s.index("[")
        last_index = s.rfind("]")
        inner = s[first_index+1:last_index]
        if "list" in inner:
            s = python_to_java_type(inner, True) + "[]"
        elif assume_array:
            return python_to_java_type(inner, True) + "[]"
        else:
            s = f"List<{python_to_java_type(inner)}>"
        return s
    return ""

def python_to_java_name(s: str) -> str:
    return re.sub(r"_(\S)", lambda m: m.group(1).upper(), s)

# convert python params list to list of tuple with java name, java type, default value
def python_to_java_params(params: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    ret: list[tuple[str, str, str]] = []
    for (name, param_type, default_val) in params:
        name = python_to_java_name(name)
        java_type = python_to_java_type(param_type)
        ret.append((name, java_type, default_val))

    return ret

def gen_additional_imports(java_params: list[tuple[str, str, str]]) -> str:
    import_dict: dict[str, str] = {
        "LEDSegment": "import com.pigmice.piled.led.LEDSegment;",
        "ColorRamp": "import com.pigmice.piled.util.ColorRamp;",
        "Color": "import edu.wpi.first.wpilibj.util.Color;",
        "List": "import java.util.List;",
        "ArrayList": "import java.util.ArrayList;",
        "Map": "import java.util.Map;",
        "HashMap": "import java.util.HashMap;",
        "TreeMap": "import java.util.TreeMap;"
    }
    imports = set()
    for ( key, value ) in import_dict.items():
        for param in java_params:
            if key in param[1]:
                imports.add(value)
    return "\n".join(imports)

def gen_class_name(fname: str) -> str:
    fname = python_to_java_name(fname)
    return fname[0].upper() + fname[1:-3] + "Effect"

def gen_fields(java_params: list[tuple[str, str, str]]) -> str:
    fields = map(lambda p: f"\t@SerializeField\n\tprivate {p[1]} {p[0]};", java_params)
    return "\n\n".join(fields)

CONSTRUCTOR_TEMPLATE = """\t%s
\tpublic %s(%s) {
\t\t%s
%s
\t}"""

def gen_constructor_javadoc(effect_name, class_name: str, java_params: list[tuple[str, str, str]]) -> str:
    ret = f"/**\n\t * {class_name.replace('E', ' E')}"
    for param in java_params:
        ret += f"\n\t * @param {param[0]} {param[0]} for the {effect_name.replace('_', ' ')} effect"
    return ret + "\n\t */"

def gen_constructor(effect_name: str, class_name: str, java_params: list[tuple[str, str, str]]) -> str:
    super_call = f"super(\"{effect_name}\");"
    params = list(map(lambda p: f"{p[1]} {p[0]}", java_params))
    sets = list(map(lambda p: f"\t\tthis.{p[0]} = {p[0]};", java_params))
    javadoc = gen_constructor_javadoc(effect_name, class_name, java_params)
    return CONSTRUCTOR_TEMPLATE % (javadoc, class_name, ", ".join(params), super_call, "\n".join(sets))

def gen_optional_constructor(effect_name: str, class_name: str, java_params: list[tuple[str, str, str]], optional_params: list[tuple[str, str, str]], replaced: list[tuple[str, str, str]]) -> str:
    required_params = list(filter(lambda param: param not in replaced, java_params))
    param_str = ", ".join(list(map(lambda p: f"{p[1]} {p[0]}", required_params)))
    this_required = ', '.join(map(lambda p: p[0], required_params))
    this_optional_params = []
    for optional in optional_params:
        if not optional in replaced:
            this_optional_params.append(optional[0])
        else:
            this_optional_params.append(python_to_java_value(optional[2]))
    this_optional = ""
    if len(optional_params) > 0:
        this_optional = ', ' + ', '.join(this_optional_params)
    this_call = f"\t\tthis({this_required}{this_optional});"
    javadoc = gen_constructor_javadoc(effect_name, class_name, required_params)
    return CONSTRUCTOR_TEMPLATE % (javadoc, class_name, param_str, "", this_call)

def gen_constructors(effect_name: str, class_name: str, java_params: list[tuple[str, str, str]]) -> str:
    optional = list(filter(lambda param: param[2] != "", java_params))
    constructors = [gen_constructor(effect_name, class_name, java_params)]
    for i in range(1, len(optional)+1):
        combinations = itertools.combinations(optional, i)
        for combo in combinations:
            constructors.append(gen_optional_constructor(effect_name, class_name, java_params, optional, list(combo)))
    return "\n\n" + "\n\n".join(constructors)

GETTER_TEMPLATE = """%s
\tpublic %s get%s() {
\t    return this.%s;
\t}"""

def gen_getter_javadoc(effect_name: str, java_param: tuple[str, str, str]) -> str:
    replaced = effect_name.replace('_', ' ')
    return f"\t/**\n\t * Get the {java_param[0]} for the {replaced} effect\n\t * @return {java_param[0]} for the {replaced} effect\n\t */"

def gen_getter(effect_name: str, java_param: tuple[str, str, str]) -> str:
    name = java_param[0]
    uppered = name[0].upper() + name[1:]
    javadoc = gen_getter_javadoc(effect_name, java_param)
    return GETTER_TEMPLATE % (javadoc, java_param[1], uppered, name)

SETTER_TEMPLATE = """%s
\tpublic void set%s(%s %s) {
\t    this.%s = %s;
\t}"""

def gen_setter_javadoc(effect_name: str, java_param: tuple[str, str, str]) -> str:
    replaced = effect_name.replace('_', ' ')
    return f"\t/**\n\t * Set the {java_param[0]} for the {replaced} effect\n\t * @param {java_param[0]} {java_param[0]} for the {replaced} effect\n\t */"

def gen_setter(effect_name: str, java_param: tuple[str, str, str]) -> str:
    name = java_param[0]
    uppered = name[0].upper() + name[1:]
    javadoc = gen_setter_javadoc(effect_name, java_param)
    return SETTER_TEMPLATE % (javadoc, uppered, java_param[1], name, name, name)

def gen_getters_setters(effect_name: str, java_params: list[tuple[str, str, str]]) -> str:
    getters_setters = []
    for param in java_params:
        getter = gen_getter(effect_name, param)
        setter = gen_setter(effect_name, param)
        getters_setters.append(getter + "\n\n" + setter)

    return "\n\n" + "\n\n".join(getters_setters)

# template string format goes additional imports, javadoc, class name, fields, constructors, getters/setters
JAVA_CLASS_TEMPLATE="""package com.pigmice.piled.effects;

import com.pigmice.piled.reflection.SerializeField;
%s

%s
public class %s extends Effect {
%s%s%s
}"""

def gen_class_javadoc(class_name: str) -> str:
    replaced = class_name.replace("E", " E")
    return f"/**\n * {replaced}\n */"

for fname in effect_python_files:
    constructor_pattern = re.compile(r"__init__\(self[^)]+\)")
    with open(path.join(python_effects_dir_path, fname), "r") as f:
        contents = f.read()
        constructors = constructor_pattern.findall(contents)
        class_name = gen_class_name(fname)
        java_file_name = f"{class_name}.java"
        java_file_path = path.join(java_effects_dir_path, java_file_name)
        if os.path.exists(java_file_path):
            print(f"\033[0;34m{java_file_name} found! Skipping...")
            continue

        effect_name = fname[:-3]

        for constructor in constructors:
            params = process_constructor(constructor)
            java_params = python_to_java_params(params)
            additional_imports = gen_additional_imports(java_params)
            javadoc = gen_class_javadoc(class_name)
            fields = gen_fields(java_params)
            java_constructors = gen_constructors(effect_name, class_name, java_params)
            getters_setters = gen_getters_setters(effect_name, java_params)
            java_class = JAVA_CLASS_TEMPLATE % (additional_imports, javadoc, class_name, fields, java_constructors, getters_setters)
            res = input(f"\033[1;31mWrite {java_file_name} (Y/n)? \033[0;31m")
            print("\033[0m", end="\r")
            if res == "Y":
                with open(java_file_path, "w") as f2:
                    f2.write(java_class)
                    f2.close()
        f.close()
