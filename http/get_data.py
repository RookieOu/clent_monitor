# -*- encoding: utf-8 -*-
"""
@File : get_data.py   
@Contact : 1175774748@qq.com
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/7/19 11:30 上午   yanou      1.0         None
"""
from abc import ABC

import tornado.ioloop
import tornado.web
import json

from main import draw, clear, get_data


class MainHandler(tornado.web.RequestHandler, ABC):
    def post(self):
        body = self.request.body
        body_decode = body.decode()
        body_json = json.loads(body_decode)
        draw(body_json)


class ClearHandler(tornado.web.RequestHandler, ABC):
    def post(self):
        clear()


class IndexHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render('render.html')


class DataHandler(tornado.web.RequestHandler, ABC):
    def post(self):
        self.write(get_data())


application = tornado.web.Application(
    [(r"/draw", MainHandler), (r"/clear", ClearHandler), (r"/show", IndexHandler), (r"/getData", DataHandler)])

if __name__ == "__main__":
    application.listen(4396)
    tornado.ioloop.IOLoop.instance().start()
