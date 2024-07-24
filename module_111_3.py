from inspect import isfunction
from pprint import pprint


def introspection_info(obj):
    dict1 = dict()
    dict1['type'] = type(obj).__name__
    dict1['attributes'] = dir(obj)
    dict1['methods'] = [attr for attr in dir(obj) if isfunction(getattr(obj, attr))]
    dict1['module'] = __name__
    dict1['module_path'] = __file__
    return dict1


a = introspection_info(42)
pprint(a)
