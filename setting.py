import logging


def setting_logging(log_level=logging.INFO):
    logging.basicConfig(
        format='%(asctime)-22s %(levelname)-8s %(message)s',
        level=log_level)
