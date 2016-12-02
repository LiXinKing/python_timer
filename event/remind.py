# coding:utf-8
from regist import regist_round_timer

def timer_remind(func_para):
    print "timer_remind"


regist_round_timer("TIMER_REMIND", "01:53:30", timer_remind, ())
