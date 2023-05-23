import importlib.util
import sys

def import_effect(name, device, data):
    spec = importlib.util.spec_from_file_location(name, f"effects/{name}.py")
    if spec == None or spec.loader == None:
        return None
    effect = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(effect)
    return effect.parse(device, data)
