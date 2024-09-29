from config import *
import logging

from src.case import CaseTest
from src.common.global_data import g
from src.common.result import init_result
from src.common.utils import read_yaml
import os
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DATE_FORMAT = "%m/%d/%Y %H:%M:%S"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

if not os.path.exists('log'):
    os.makedirs('log')
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('log/result.log')

fh.setLevel(logging.CRITICAL)
logger.addHandler(fh)


if __name__ == "__main__":
    env = '_qa2'

    from src.callback.callback_vsoc import CallBack

    chewang = CallBack()
    init_result()
    config_data = read_yaml(f"config/default{env}.yaml")
    g.set_value('config', config_data)
    for case_item in case_list:
        a = CaseTest(case_item, chewang)
        a.start()
