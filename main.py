# encoding: utf-8
import __builtin__
from types import ModuleType


class DummyModule(ModuleType):
    def __getattr__(self, key):
        if "register" in key:
            return lambda x: x
        else:
            return object

    __all__ = []  # support wildcard imports


def tryimport(name, globals={}, locals={}, fromlist=[], level=-1):
    try:
        return realimport(name, globals, locals, fromlist, level)
    except ImportError as e:
        return DummyModule(name)
    except Exception as e:
        pass


realimport, __builtin__.__import__ = __builtin__.__import__, tryimport

if __name__ == '__main__':
    from pocs import __all__

    # link: https://michaelheap.com/python-dynamically-load-all-modules-in-a-folder/
    # link: https://stackoverflow.com/a/6077117/8591480
    for i in __all__:
        print "POC: %s :%s" % (__all__[i].TestPOC.name, __all__[i].TestPOC.references)
    pass
