from .index import IndexHandler

HTTP_HANDLERS = [
    (r"/", IndexHandler)
]