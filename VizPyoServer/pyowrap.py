# pyo_wrap.py
#
# Builds on top of pyo functions



import inspect
import pyo

to_wrap = [pyo.Sine,
           pyo.Noise]

wrappers = {}


def get_declared_class_names():
    names = [pyo_class.__name__ for pyo_class in to_wrap]
    return names


class PyoClassWrap:

    def __init__(self, pyo_class):
        # retain arguments
        self.pyo_class = pyo_class
        # get the list of argument names for the function
        self.arg_names = list(inspect.signature(self.pyo_class.__init__).parameters.keys())
        self.arg_names.remove("self")

    def arg_default(self, arg_name):
        default = inspect.signature(self.pyo_class.__init__).parameters[arg_name].default
        if default == inspect.Parameter.empty:
            return None
        else:
            return default


def _wrap_pyo():
    global wrappers
    wrappers = {pyo_class.__name__:PyoClassWrap(pyo_class) for pyo_class in to_wrap}


def get_class(pyo_class_name):
    return wrappers[pyo_class_name]


def get_classes():
    return list(wrappers.keys())


_wrap_pyo()










