import logging
import time
from twisted.internet import task, reactor

from common import ActionData, setting_logging
from actions import Actor


def get_tick(last_tick: float, precision: int) -> float:
    """ return the tick """
    return round(time.time() - last_tick, precision)


def do_work(action_data: ActionData):
    global _lastTick, _precision
    tick = get_tick(_lastTick, _precision)
    action_data.add_duration_time(tick)
    # print(f'{currentTime}')
    # main loop
    step = action_data.get_next_action()
    if step is not None:
        logging.info(f'trigger {step}')
        if not _actor.do_action(step):
            logging.warning(f'Can not complete {step}')
    # reset action if ended
    action_data.reset_if_all_action_executed()
    # record time
    _lastTick = time.time()


_precision = 4
_interval = 0.1
_lastTick = time.time()
_actionData = ActionData(path="actions.yaml")
_actor = Actor()
setting_logging()

runner = task.LoopingCall(do_work, _actionData)
runner.start(_interval)
print('Start running...')
print('Press CTRL+C to stop.')
reactor.run()
