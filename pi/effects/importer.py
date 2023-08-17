import importlib.util

def import_effect(name, device, data):
    spec = importlib.util.spec_from_file_location(name, f"effects/{name.lower()}.py")
    if spec is None:
        spec = importlib.util.spec_from_file_location(name, f"custom_effects/{name.lower()}.py")
    if spec is None or spec.loader is None:
        return None
    effect = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(effect)
    e = effect.parse(device, data)
    e.set_name(data["name"])
    return e
