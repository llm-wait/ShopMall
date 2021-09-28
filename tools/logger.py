# -*- coding: utf-8 -*- 
# @Time : 2021/9/24 10:19 
# @Author : Corn
# @File : logger.py
import logging.handlers

from Review.Week9.apiFrame import config


class GetLog:
    logger=None
    @classmethod
    def get_logger(cls):
        if cls.logger ==None:
           cls.logger=logging.getLogger()
           cls.logger.setLevel(logging.INFO)
           fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
           fm=logging.Formatter(fmt)
           tf=logging.handlers.TimedRotatingFileHandler(filename=config.DIR_NAME+"/log/test.log",
                                                        when='H',
                                                        interval=1,
                                                        backupCount=3,
                                                        encoding='utf-8'
                                                        )
           tf.setFormatter(fm)
           cls.logger.addHandler(tf)
        return  cls.logger