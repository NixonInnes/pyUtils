import warnings

class Objectify(object):
    def __init__(self, dic, force=False):
        if not isinstance(dic, dict):
            raise TypeError("Unsupported type: dic must be a dict()")
        for key in dic:
            if isinstance(key, (int, float)):
                if force:
                    warnings.warn("dictionary key '{}' is a number.".format(key), UserWarning)
                else:
                    raise TypeError("dictionary key '{}' is a number. Using a number as an attribute name is not permitted.\
                                    \r\n You may define parameter 'force=True' to override this behaviour.".format(key))
            if isinstance(dic[key], dict):
                setattr(self, str(key), type(self)(dic[key]))
            else:
                setattr(self, str(key), dic[key])
