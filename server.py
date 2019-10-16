import json
import logging
import socketserver
import sys
import traceback

from common import setting_logging


class TheTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        logging.info(self.data)
        json_data = json.loads(self.data)
        response = {
            "status": 0,
            "msg": ""
        }
        try:
            action = json_data["action"]
            args = json_data["args"]
            logging.info(f"Action: {action}, Args: {args}")
            # TODO: do action
        except Exception as e:
            error_class = e.__class__.__name__
            detail = e.args[0]
            cl, exc, tb = sys.exc_info()
            last_call_stack = traceback.extract_tb(tb)[-1]
            file_name = last_call_stack[0]
            line_num = last_call_stack[1]
            func_name = last_call_stack[2]
            err_msg = f"File \"{file_name}\", " \
                      f"line {line_num}, " \
                      f"in {func_name}: [{error_class}] {detail}"
            logging.error(err_msg)
            response = {
                "status": -1,
                "msg": err_msg
            }
        finally:
            self.request.sendall(bytes(json.dumps(response), "utf-8"))


if __name__ == "__main__":
    setting_logging()
    HOST, PORT = "localhost", 1999
    with socketserver.TCPServer((HOST, PORT), TheTCPHandler) as server:
        print(f'Server running on {HOST}:{PORT}')
        print('Press Ctrl-C to quit.')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            sys.stdout.write("Server stopped.\n\n")
            sys.stdout.flush()
