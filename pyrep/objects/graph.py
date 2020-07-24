from pyrep.objects.object import Object
from pyrep.const import ObjectType
from pyrep.backend import vrep


class Graph(Object):
    """A point with orientation.

    Dummies are multipurpose objects that can have many different applications.
    """


    def _get_requested_type(self) -> ObjectType:
        return ObjectType.GRAPH
