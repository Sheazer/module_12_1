import inspect
import pprint


def introspection_info(obj):

    type_obj = type(obj)
    callable_obj = callable(obj)
    module = inspect.getmodule(obj)
    all_attributes = dir(obj)

    methods = [attr for attr in all_attributes if callable(getattr(obj, attr)) and not attr.startswith("__")]
    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    result = {'type': type_obj,'attributes': attributes, 'methods': methods, 'module': module, 'callable': callable_obj}

    return result


number_info = introspection_info('42')
pprint.pprint(number_info)
