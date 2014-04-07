from abc import ABCMeta, abstractmethod, abstractproperty
# TODO cover with tests

class AllowedValueType:
    VALUE = 0
    RANGE = 1

class RangeClosureType:
    OPEN = 0
    CLOSED = 1
    OPENCLOSED = 2
    CLOSEDOPEN = 3

class AllowedValueAbstract:

    allowed_type = None
    values = None
    minval = None
    maxval = None
    spacing = None
    range_closure = None


class LiteralValidatorAbstract(object):
    """LiteralObject validator
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self, inpt):
        """Make sure, given value is ok according to LiteralInput definition
        """
        return True

class AllowedValuesValidator(LiteralValidatorAbstract):
    """AllowedValue validator
    """

    def validate(self, inpt):
        """
        """

        # TODO this is where I ended
        allowed = inpt.allowed_value
        allowed.interval
