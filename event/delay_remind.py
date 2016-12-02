# coding:utf-8
from regist import regist_relative_timer

def delay_remind(func_para):
    print "delay_remind"


regist_relative_timer("RELATIVE_TIMER_REMIND", "50", delay_remind, ())