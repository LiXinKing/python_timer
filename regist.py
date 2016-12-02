from globalDef import g_relative_timer_regist_dict
from globalDef import g_absolute_timer_regist_dict
from globalDef import g_round_timer_regist_dict
from event import *


def regist_relative_timer(timer_name, timer_stamp, timer_func, func_para):
    g_relative_timer_regist_dict[timer_name] = (timer_stamp, timer_func, func_para)


def regist_absolute_timer(timer_name, timer_stamp, timer_func, func_para):
    g_absolute_timer_regist_dict[timer_name] = (timer_stamp, timer_func, func_para)


def regist_round_timer(timer_name, timer_stamp, timer_func, func_para):
    g_round_timer_regist_dict[timer_name] = (timer_stamp, timer_func, func_para)
