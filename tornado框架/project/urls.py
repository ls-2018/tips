import tornado.web
from views import index


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', index.IndexHandler)

        ]
        super(Application, self).__init__(handlers)
