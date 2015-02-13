from __future__ import unicode_literals
 
from willie.tools import Ddict, Identifier, get_timezone, format_time
from willie.module import commands, event, rule
import time
import random

seen_dict = Ddict(dict)
 
@event('JOIN')
@rule('.*')
def greet(bot, trigger):
    absent_threshold_in_seconds = 3600
    greets = ['hello','ello','hihi','welcome','hi']
    puncs = [':)',':)',':)','<3','<3',':D','^.^','^.^',':3']
    nick = trigger.nick
    if nick in seen_dict:
        timestamp = seen_dict[nick]['timestamp']
        timenow = time.time()
        if timenow - timestamp < absent_threshold_in_seconds:
            return
    time.sleep(3)
    bot.say('{}, {} {}'.format(nick, random.choice(greets), random.choice(puncs)))
    
@event('PART','QUIT','NICK')
@rule('.*')
def user_part(bot, trigger):
    nick = Identifier(trigger.nick)
    channel = trigger.sender
    update_seen(nick, channel)
    
@event('KICK')
@rule('.*')
def user_kick(bot, trigger):
    nick = Identifier(trigger.args[1])
    channel = trigger.sender
    update_seen(nick, channel)
    
def update_seen(nick, channel):
    seen_dict[nick]['timestamp'] = time.time()
    
    
