# -*- coding: utf-8 -*-
import sys
from .loghandle import creatlog


####################################################################
# Script    : BaseObject
# PURPOSE   : Parent class for all objects
#
# CREATED:    2014-12-22    EnfangQI
#
#
# MODIFIED
# DATE        AUTHOR            DESCRIPTION
# -------------------------------------------------------------------
#
#####################################################################
class DefaultLogger(object):
    def fatal(self, msg=''):
        print('**fatal**: %s' % msg)

    def error(self, msg=''):
        print('**error**: %s' % msg)

    def warn(self, msg=''):
        print('**warn**: %s' % msg)

    def info(self, msg=''):
        print('**info**: %s' % msg)

    def debug(self, msg=''):
        print('**debug**: %s' % msg)


class BaseObject(object):
    __logger = None

    def fatal(self, msg=''):
        msg = self.format_msg(msg)
        self.get_logger().fatal(msg)

    def error(self, msg=''):
        msg = self.format_msg(msg)
        self.get_logger().error(msg)

    def warn(self, msg=''):
        msg = self.format_msg(msg)
        self.get_logger().warn(msg)

    def info(self, msg=''):
        msg = self.format_msg(msg)
        self.get_logger().info(msg)

    def debug(self, msg=''):
        msg = self.format_msg(msg)
        self.get_logger().debug(msg)

    def format_msg(self, msg):
        if msg is None:
            msg = 'None'

        return self.get_log_msg(msg.__str__())

    def get_logger(self):
        if self.__logger is None:
            if creatlog is not None and not self.get_use_default_logger():
                self.__logger = creatlog.getLogger(appname=self.get_sys_name(), screen_only=self.get_screen_log_only())
            else:
                self.__logger = DefaultLogger()

        return self.__logger

    def get_log_msg(self, msg=''):
        if len(msg) > 10000:
            msg = msg[:10000]
        return "%s: %s() || %s" % (self.class_name, self.function_name(4), msg)

    def get_sys_name(self):
        return "DEFAULT"

    def get_screen_log_only(self):
        return False

    def get_use_default_logger(self):
        return False

    # Get function name
    def function_name(self, trace=1):
        return sys._getframe(trace).f_code.co_name

    @staticmethod
    def create_dynamic_object(class_full_name, *args):
        # self.info('class_full_name = %s, args = %s' % (class_full_name, args) )

        # Dynamically load a module
        __import__(class_full_name)
        mod = sys.modules[class_full_name]

        # Dynamically create an object
        package_name, class_name = BaseObject.parse_class_name(class_full_name)
        package_name
        dyn_class = getattr(mod, class_name)

        return dyn_class(*args)

    # Parse class name
    # One rule is that class name is the same as the last part of the module name
    @staticmethod
    def parse_class_name(class_full_name):
        # self.info('class_full_name = %s' % (class_full_name) )

        parts = class_full_name.split('.')
        class_name = parts.pop()

        return '.'.join(parts), class_name

    @property
    def class_name(self):
        return self.__class__.__name__

    @property
    def full_class_name(self):
        return self.__class__.__module__

    @property
    def package_name(self):
        package_name, class_name = self.parse_class_name(self.full_class_name)
        class_name
        return package_name

    def setattr(self, key, value):
        setattr(self, key, value)
