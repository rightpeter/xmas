#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop

from tornado.options import define, options

define("port", default=8120, help="run on the given port", type=int)

nameDict = {'rightpeter': ['女神', '平安夜']}

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
            (r'/([A-Za-z0-9]+$)', ZhufuHandler),
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        self.set_header("Content-Type", "text/plain")

        try:
            name_boy = self.get_argument("boy")
        except:
            self.write("没有输入你自己的名字")
            return

        try:
            name_girl = self.get_argument("girl")
        except:
            self.write("没有输入女神的名字")
            return


        try:
            name_festival = self.get_argument("festival")
        except:
            self.write("没有输入节日")
            return 

        if ( nameDict.has_key(name_boy) ):
            self.write("已有人使用了%s" % name_boy.encode('gbk')) 
        else:

            nameDict[name_boy] = [name_girl, name_festival]
            self.write("Create Successfully!")


class ZhufuHandler(tornado.web.RequestHandler):
    def get(self, name_boy):
    
        self.render('testMain.html', name=nameDict[name_boy][0], festival=nameDict[name_boy][1])

def main():
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
