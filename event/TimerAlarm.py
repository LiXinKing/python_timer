# coding:utf-8
from regist import regist_round_timer
from user_inerface.DialogManagement import DialogManagement

def TimerAlarm(func_para):
    DialogManagement.show_Dialog("Hello word", "DialogAlarm" )

regist_round_timer("TIMER_ALARM", "22:39:10", TimerAlarm, ())