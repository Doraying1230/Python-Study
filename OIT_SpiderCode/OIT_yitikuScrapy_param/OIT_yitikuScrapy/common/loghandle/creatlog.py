# -*- coding: utf-8 -*-
####################################################################
# Script    : logutil
# PURPOSE   : A loghandle class to create log
#
# CREATED:    2016-12-27   EnfangQI
#
#
# MODIFIED
# DATE        AUTHOR            DESCRIPTION
# -------------------------------------------------------------------
#
#####################################################################

from datetime import datetime
import logging
import sys
import time
import os
logger = None


def getLogger(appname, level=logging.INFO, screen_only=False):
    global logger
    if logger is not None:
        return logger

    formatter = logging.Formatter('%(name)s#%(levelname)s#%(asctime)s -- %(message)s')

    file_handler = None
    if not screen_only:
        # Add a file log handler
        # dt = datetime.today().strftime('%Y%m%d')
        path = 'd:\\OITData\\zujuan\\log\\{}\\'.format(appname)
        isEixct = os.path.exists(path)
        if isEixct:
            pass
        else:
            os.makedirs(path)
        log_file_name = path+"{}.log".format(time.strftime('%Y%m%d',time.localtime()));
        file_handler = logging.FileHandler(log_file_name)
        file_handler.setFormatter(formatter)

    # Add a stream log handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    # Create a logger
    logger = logging.getLogger(appname)
    # logger.addHandler(stream_handler)
    if file_handler is not None:
        logger.addHandler(file_handler)
    logger.setLevel(level)

    return logger