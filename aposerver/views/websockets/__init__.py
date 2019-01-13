from .chat import ChatSocketHandler
from .round import RoundSocketHandler


SOCKET_HANDLERS = [
    (r"/chatsocket", ChatSocketHandler),
    (r"/round/([0-9]+)", RoundSocketHandler)
]