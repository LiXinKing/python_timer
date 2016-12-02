# coding:utf-8

from SingleTon import Singleton
import time
import sched
from TraceLog import TraceLog
import threading


class TimerManagement(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.__timer_dict = {}
        self.__schedule = sched.scheduler(time.time, time.sleep)
        self.__timer_ticking = {}

    def batch_regist(self, timer_dict):
        self.__timer_dict.update(timer_dict)

    def regist(self, timer_name, timer_stamp, timer_func, func_para):
        if timer_name not in self.__timer_dict and timer_name not in self.__timer_ticking:
            self.__timer_dict[timer_name] = (timer_stamp, timer_func, func_para)

    def push_timer(self, timer_name):
        if timer_name not in self.__timer_ticking:
            self.__timer_ticking[timer_name] = None

    def pop_timer(self, timer_name):
        if timer_name in self.__timer_ticking:
            self.__timer_ticking.pop(timer_name)

    def timer_ticking(self, timer_name, timer_func, func_para):
        print "in timer_ticking"
        timer_func(func_para)
        self.pop_timer(timer_name)

    def batch_unregist(self):
        self.__timer_dict = {}

    def get_timer_dict(self):
        return self.__timer_dict

    def get_timer_schedule(self):
        return self.__schedule

    def relative_timer(self, timer_name, timer_stamp, timer_func, func_para):
        schedule = self.get_timer_schedule()
        self.push_timer(timer_name)
        schedule.enter(int(timer_stamp), 0, self.timer_ticking, (timer_name, timer_func, func_para))
        thread = threading.Thread(target = schedule.run, args = ())
        thread.start()
        # thread.join()

    def do(self):
        for timer_name, timer_info in self.get_timer_dict().items():
            # adsolutely ?
            self.relative_timer(timer_name, timer_info[0], timer_info[1], timer_info[2])
        self.batch_unregist()
