import asyncio

from tornado.websocket import websocket_connect


async def do_main():
    conn = await websocket_connect("ws://localhost:12349/ws/echo")
    await conn.write_message("webソケットのテスト")
    print("メッセージを送信")
    from_server = await conn.read_message()
    print("メッセージを受信: %s" % from_server)
    conn.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_main())
