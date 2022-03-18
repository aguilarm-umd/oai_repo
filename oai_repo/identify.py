"""
Implementation of Identify verb
"""
from .exceptions import OAIErrorBadArgument
from .request import OAIRequest
from .response import OAIResponse


class IdentifyRequest(OAIRequest):
    """
    raises:
        OAIErrorBadArgument
    """
    def __init__(self):
        super().__init__()


class IdentifyResponse(OAIResponse):
    """
    """
