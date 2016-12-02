from TimerManagement import TimerManagement
from AbsoluteTimerManagement import AbsoluteTimerManagement
from RoundTimerManagement import RoundTimerManagement
"""
#    Timer regist example
#    "MOVE_TIMER": (10, move, ()),
#    "MOVE_TIMER": ("2016-12-3 17:53:00", move, ()),
"""
g_relative_timer_instance = TimerManagement()
g_absolute_timer_instance = AbsoluteTimerManagement()
g_round_timer_instance = RoundTimerManagement()
g_relative_timer_regist_dict = {}
g_absolute_timer_regist_dict = {}
g_round_timer_regist_dict = {}
