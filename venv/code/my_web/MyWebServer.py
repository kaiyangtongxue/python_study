# coding=utf-8
import socket
from multiprocessing import Process
import re
import sys

HTML_ROOT_DIR = "html"

WSGIPYTHON_DIR = "wsgipython"


class HTTPServer(object):
    """"""

    def __init__(self, application):
        """构造函数"""
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = application

    def bind(self, port):
        self.serverSocket.bind(("", port))

    def start(self):
        self.serverSocket.listen(10)
        while True:
            clientSocket, clientAddr = self.serverSocket.accept()
            clientP = Process(target=self.handleClient, args=(clientSocket,))
            clientP.start()
            clientSocket.close()

    def handleClient(self, clientSocket):
        """用一个新的进程，为一个客户端进行服务"""
        recvData = clientSocket.recv(2014)
        if len(recvData) == 0:
            clientSocket.close()
            return
        requestHeaderLines = recvData.splitlines()
        # GET /index.html HTTP /1.1
        first_line = requestHeaderLines[0].decode('utf-8')
        file_name = re.search(r"\w+ +(/[^ ]*) ", first_line).group(1)
        method = re.search(r"(\w+) +/[^ ]* ", first_line).group(1)
        print(file_name)
        for line in requestHeaderLines:
            linestr = line.decode('UTF-8')
            print(linestr)

        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }

        response_body = self.app(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body
        clientSocket.send(response.encode('UTF-8'))
        clientSocket.close()

    def start_response(self, status, headers):
        """
            status = "200 OK"
            headers=[
                ("Content-Type","text/plain")
            ]
            start_response(status,headers)
        """
        response_headers = "HTTP/1.1 " + status
        print(response_headers)
        for headers in headers:
            response_headers += "%s: %s\r\n" % headers
        self.response_headers = response_headers


def main():
    sys.path.insert(1, WSGIPYTHON_DIR)
    if len(sys.argv) <2:
        sys.exit("python MyWebServer.py Moudle:app")
    moudle_name,app_name = sys.argv[1].split(":")
    m=__import__(moudle_name)
    app=getattr(m,app_name)
    http_server = HTTPServer(app)
    http_server.bind(7788)
    http_server.start()


if __name__ == '__main__':
    main()
