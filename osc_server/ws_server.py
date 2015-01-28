# import tornado.ioloop
# import tornado.web

# from tornado.options import define, options, parse_command_line

# define("port", default=8888, help="run on the given port", type=int)

# class IndexHandler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     def get(self):
#         self.write("This is your response")
#         self.finish()

# app = tornado.web.Application([
#     (r'/', IndexHandler),
# ])

# if __name__ == '__main__':
#     parse_command_line()
#     app.listen(options.port)
#     tornado.ioloop.IOLoop.instance().start()


import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from tornado.ioloop import PeriodicCallback
import time
import datetime
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8052
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, UDP_PORT))

class WSHandler(tornado.websocket.WebSocketHandler):
    # def __init__(self):
    #     self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     self.sock.bind((UDP_IP, UDP_PORT))
    #     print "init"

    def open(self):
        print 'new connection'
        self.write_message("first message from server")
        self.callback = PeriodicCallback(self.send_message, 100)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))
        print "line 50"
        self.callback.start()

    def send_message(self):
        opt = 1
        # print "send message to client"
        if opt == 0:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        else:
            data, addr = self.sock.recvfrom(1024)
            print "server received message: ", data
        print "send message to client"
        self.write_message(data)

    def on_message(self, message):
        print 'message received %s' % message

    def on_close(self):
        print 'connection closed'

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8885)
    tornado.ioloop.IOLoop.instance().start()
