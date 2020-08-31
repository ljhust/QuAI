"""
QUANTAXIS Log Module
@yutiansut

util_log_x is under [QAStandard#0.0.2@602-x] Protocol
util_log_info()
util_log_debug()
util_log_expection()
"""

import configparser
import datetime
import os
import sys
from zenlog import logging
from QUANTAXIS.QASetting.QALocalize import log_path, setting_path

from QUANTAXIS.QAUtil.QASetting import QA_Setting

"""2019-01-03  升级到warning级别 不然大量别的代码的log会批量输出出来
2020-02-19 默认使用本地log 不再和数据库同步
"""

try:
    _name = '{}{}quai_{}-{}-.log'.format(
        log_path,
        os.sep,
        os.path.basename(sys.argv[0]).split('.py')[0],
        str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    )
except:
    _name = '{}{}quai-{}-.log'.format(
        log_path,
        os.sep,
        str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    )

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s QuAI>>> %(message)s',
    datefmt='%H:%M:%S',
    filename=_name,
    filemode='w',
)
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter('QuAI>> %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# logging.info('start QUANTAXIS')


def util_log_debug(logs, ui_log=None, ui_progress=None):
    """
    explanation:
        QUANTAXIS DEBUG级别日志接口

    params:
        * logs ->:
            meaning: log信息
            type: null
            optional: [null]
        * ui_log ->:
            meaning:
            type: null
            optional: [null]
        * ui_progress ->:
            meaning:
            type: null
            optional: [null]

    return:
        None

    demonstrate:
        Not described

    output:
        Not described
    """
    logging.debug(logs)


def util_log_info(logs, ui_log=None, ui_progress=None, ui_progress_int_value=None):
    """
    explanation:
        QUANTAXIS INFO级别日志接口

    params:
        * logs ->:
            meaning: 日志信息
            type: null
            optional: [null]
        * ui_log ->:
            meaning:
            type: null
            optional: [null]
        * ui_progress ->:
            meaning:
            type: null
            optional: [null]
        * ui_progress_int_value ->:
            meaning:
            type: null
            optional: [null]

    return:
        None

    demonstrate:
        Not described

    output:
        Not described
    """

    """
    QUANTAXIS Log Module
    @yutiansut

    QA_util_log_x is under [QAStandard#0.0.2@602-x] Protocol
    """
    logging.warning(logs)

    # 给GUI使用，更新当前任务到日志和进度
    if ui_log is not None:
        if isinstance(logs, str):
            ui_log.emit(logs)
        if isinstance(logs, list):
            for iStr in logs:
                ui_log.emit(iStr)

    if ui_progress is not None and ui_progress_int_value is not None:
        ui_progress.emit(ui_progress_int_value)


def util_log_expection(logs, ui_log=None, ui_progress=None):
    """
    explanation:
        QUANTAXIS ERROR级别日志接口

    params:
        * logs ->:
            meaning: 日志信息
            type: null
            optional: [null]
        * ui_log ->:
            meaning:
            type: null
            optional: [null]
        * ui_progress ->:
            meaning:
            type: null
            optional: [null]

    return:
        None

    demonstrate:
        Not described

    output:
        Not described
    """

    logging.exception(logs)
