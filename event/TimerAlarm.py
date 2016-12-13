# coding:utf-8
from regist import regist_round_timer
from regist import regist_relative_timer
from user_inerface.DialogManagement import DialogManagement

def TimerAlarm(func_para):
    DialogManagement.show_Dialog("Hello word", "DialogAlarm" )

regist_relative_timer("TIMER_ALARM", "10", TimerAlarm, ())