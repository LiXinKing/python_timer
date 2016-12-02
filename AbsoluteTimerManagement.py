# coding:utf-8
from TimerManagement import TimerManagement
import time
from MacroDef import M_MILSECOND_PER_DAY
from TraceLog import TraceLog


class AbsoluteTimerManagement(TimerManagement):
    def batch_regist(self, timer_dict):
        for timer_name, timer_info in timer_dict.items():
            time_array = time.strptime(timer_info[0], "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(time_array))
            time_now = int(time.time())
            if time_stamp - time_now > 0 and time_stamp - time_now < 5:
                self.regist(timer_name, time_stamp - time_now, timer_info[1], timer_info[2])
