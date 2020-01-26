from typing import Union, Optional, Awaitable

from tornado.websocket import WebSocketHandler
from tornado.web import Application
from tornado.ioloop import IOLoop


class EchoWebSocket(WebSocketHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def on_message(self, message):
        print("メッセージ受信")

        def reply():
            self.write_reply(message)

        IOLoop.instance().call_later(3, reply)

    def write_reply(self, original_message: Union[str, bytes]):
        print("クライアントに変身")
        self.write_message("サーバーからの応答" + original_message)

    def on_close(self):
        print("クライアントが切断")


app = Application(handlers=[
    (r"/ws/echo", EchoWebSocket)
])

if __name__ == '__main__':
    app.listen(12349)
    IOLoop.current().start()
