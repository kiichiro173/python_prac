
import logging

def getMyLogger(name):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('./log/project.log')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s  %(asctime)s  [%(name)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = getMyLogger("ここはモジュール名")

for i in range(100):
    data = i
    if i % 30 == 0:
        logger.error(f"30の倍数でエラーが発生: {data}")
    elif i % 10 == 0:
        logger.warning(f"10の倍数でwarningが発生: {data}")
    elif i % 2 == 0:
        logger.debug(f"2の倍数でdebugが発生: {data}")
    else:
        logger.info("infoが発生")