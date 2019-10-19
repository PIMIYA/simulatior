import json
import logging
import socketserver
import sys
import traceback

import click

from action_type import ActionType
from manager import Manager
from setting import setting_logging


class TheTCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        self.mgr = Manager()

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
            name = json_data["id"]
            action_val = json_data["type"]
            args = json_data["args"]
            action = ActionType(action_val)
            self.mgr.do_action(name=name, action=action, args=args)
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


@click.command()
@click.option("--host", default="localhost", show_default=True, help="")
@click.option("--port", default=9999, show_default=True, help="")
def main(host, port):
    """ Run the simulatior server """
    setting_logging(log_level=logging.INFO)
    with socketserver.TCPServer((host, port), TheTCPHandler) as server:
        print(f'Server running on {host}:{port}')
        print('Press Ctrl-C to quit.')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            sys.stdout.write("Server stopped.\n\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
