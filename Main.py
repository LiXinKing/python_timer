# coding:utf-8
from globalDef import g_absolute_timer_instance
from globalDef import g_relative_timer_instance
from globalDef import g_round_timer_instance
from globalDef import g_absolute_timer_regist_dict
from globalDef import g_relative_timer_regist_dict
from globalDef import g_round_timer_regist_dict
from event import *
import time


def main():

    g_relative_timer_instance.batch_regist(g_relative_timer_regist_dict)
    while True:
        time.sleep(0.1)
        g_absolute_timer_instance.batch_regist(g_absolute_timer_regist_dict)
        g_round_timer_instance.batch_regist(g_round_timer_regist_dict)
        g_absolute_timer_instance.do()
        g_relative_timer_instance.do()
        g_round_timer_instance.do()


if __name__ == "__main__":
    main()
