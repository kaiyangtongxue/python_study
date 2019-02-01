import time
from MyWebServer import HTTPServer

HTML_ROOT_DIR = "html"

class Application(object):
    """框架的核心"""

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO","/")
        if path.startswith("/static"):
            file_name=path[7:]
            print(file_name)
            if "/" == file_name:
                file_name = "/index.html"
            filename = HTML_ROOT_DIR + file_name
            try:
                file = open(filename, "rb")
            except IOError:
                print("文件不存在")
                status = "404 Not Found"
                headers=[
                    ("Content-Type", "text/plain")
                ]
                start_response(status,headers)
                return "not found"
            else:
                file_data = file.read()
                file.close()

                status="200 OK"
                headers = [
                    ("Content-Type", "text/plain")
                ]
                start_response(status,headers)
                return file_data.decode("utf-8")

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)
        # 未找到
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = {
        ("Content-Type", "text/plain")
    }
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = {
        ("Content-Type", "text/plain")
    }
    start_response(status, headers)
    return "hello diango"

urls = [
        ("/",show_ctime),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
    ]

app = Application(urls)

def main():
    urls = [
        ("/",show_ctime),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
    ]
    app = Application(urls)
    http_server = HTTPServer(app)
    http_server.bind(7788)
    http_server.start()


if __name__ == "__main__":
    main()

# def application(env,start_response):
#     # urls = [
#     #     ("/ctime",show_ctime),
#     #     ("/sayhello",say_hello)
#     # ]
#     # status = "200 OK"
#     # headers=[
#     #     ("Content-Type","text/plain")
#     # ]
#     # start_response(status,headers)
#     return time.ctime()
