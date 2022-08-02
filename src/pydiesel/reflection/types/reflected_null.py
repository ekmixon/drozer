from pydiesel.api.protobuf_pb2 import Message
from pydiesel.reflection.exceptions import ReflectionException
from pydiesel.reflection.types.reflected_type import ReflectedType

class ReflectedNull(ReflectedType):
    """
    A ReflectedType that represents Java null.
    """
    
    def _pb(self):
        """
        Get an Argument representation of the null, as defined in the drozer
        protocol.
        """
        return Message.Argument(type=Message.Argument.NULL)

    def __eq__(self, other):
        return True if (other == None) else ReflectedType.__eq__(self, other)

    def __ne__(self, other):
        return False if (other == None) else ReflectedType.__ne__(self, other)

    def __str__(self):
        return "null"
        