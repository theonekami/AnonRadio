##
##Alrighty then.
##i don't trust you all so i'd rather say this fast
##this is MY bot..ANd it's a HE
##

from random import randint, choice
import bdtest
import math # For funsies

from invoker import ReplyObject, Command

from data.tiers import tiers, formats
from data.links import Links, YoutubeLinks
from data.pokedex import Pokedex
from data.types import Types
from data.replies import Lines

from user import User


usageLink = r'http://www.smogon.com/stats/2017-08/'

def URL(): return 'https://github.com/QuiteQuiet/PokemonShowdownBot/'

def get(robot, cmd, params, user):
    if user.isOwner():
        res = str(eval(params))
        return ReplyObject(res if not res == None else '', True)
    return ReplyObject('You do not have permisson to use this command. (Only for owner)')

def forcerestart(robot, cmd, params, user):
    if user.hasRank('#'):
        # Figure out how to do this
        robot.closeConnection()
        return ReplyObject('')
    return ReplyObject('You do not have permisson to use this command. (Only for owner)')

def savedetails(robot, cmd, params, user):
    """ Save current robot.details to details.yaml (moves rooms to joinRooms)
     Please note that this command will remove every comment from details.yaml, if those exist."""
    if user.hasRank('#'):
        robot.saveDetails()
        return ReplyObject('Details saved.', True)
    return ReplyObject("You don't have permission to save settings. (Requires #)")

def newautojoin(robot, cmd, params, user):
    if user.hasRank('#'):
        # Join the room before adding it to list of autojoined rooms
        robot.joinRoom(params)
        robot.saveDetails(True)
        return ReplyObject("New autojoin ({room}) added.".format(room = params))
    return ReplyObject("You don't have permission to save settings. (Requires #)")

def setbroadcast(robot, cmd, params, user):
    params = robot.removeSpaces(params)
    if params in User.Groups or params in ['off', 'no', 'false']:
        if user.hasRank('#'):
            if params in ['off', 'no', 'false']: params = ' '
            if robot.details['broadcastrank'] == params:
                return ReplyObject('Broadcast rank is already {rank}'.format(rank = params if not params == ' ' else 'none'), True)
            robot.details['broadcastrank'] = params
            return ReplyObject('Broadcast rank set to {rank}. (This is not saved on reboot)'.format(rank = params if not params == ' ' else 'none'), True)
        return ReplyObject('You are not allowed to set broadcast rank. (Requires #)')
    return ReplyObject('{rank} is not a valid rank'.format(rank = params if not params == ' ' else 'none'))


def hi(robot, cmd,params):
    return ReplyObject("/me HI There " + params,True)

def Hello(robot,cmd,params):
    return ReplyObject("__Hello there i am kAmi's idea of automating BD. Yorshikune__",True)

def Broadcast(robot,cmd,params):
    msg=params.split(',')
    robot.rooms


def regp(robot,cmd,params):
    msg=params.split(',')
    w=open('players.txt','a')
    w.write(params+'\n')
    return ReplyObject("Ok then "+msg[0]+ " is registered")

def stats(robot,cmd,params):
    params=params.split(',')
    res1,temp1=bdtest.ret_stats(params[0])
    try:
        res2,temp2=bdtest.ret_stats(params[1])
    except:
        temp2=str("")
        res2=dict()
        res2[temp2]=(0,0)
    A=res1[temp1][0]+res2[temp2][0]
    M=res1[temp1][1]+res2[temp2][1]
    temp=temp1+" "+temp2
    x="The stats for " + temp +" are Attack:" + str(A) + " Magic:" +str(M)
##    print(tempp)
    return ReplyObject(x)  
##def hiback(robot,cmd):
##    robot.say("battledome","hi there")
##    return ReplyObject('')
##    

commands = [
    # The easy stuff that can be done with a single lambda expression
    Command(['source', 'git'], lambda: ReplyObject('Source code can be found at: {url}'.format(url = URL()), True)),
    Command(['credits'], lambda: ReplyObject('Credits can be found: {url}'.format(url = URL()), True)),
    Command(['owner'], lambda s: ReplyObject('Owned by: {owner}'.format(owner = s.owner), True)),
    Command(['commands', 'help'], lambda: ReplyObject('Read about commands here: {url}blob/master/COMMANDS.md'.format(url = URL()), reply = True, pmreply = True)),
    Command(['explain'], lambda: ReplyObject("BB-8 is the name of a robot in the seventh Star Wars movie :)", True)),
    Command(['ask'], lambda: ReplyObject(Lines[randint(0, len(Lines) - 1)], True)),
    Command(['squid'], lambda: ReplyObject('\u304f\u30b3\u003a\u5f61', True)),
    Command(['seen'], lambda: ReplyObject("This is not a command because I value other users privacy.", True)),
    Command(['broadcast'], lambda s: ReplyObject('Rank required to broadcast: {rank}'.format(rank = s.details['broadcastrank']), True)),
    Command(['usage'], lambda: ReplyObject(usageLink, reply = True, pmreply = True)),
    Command(['pick'], lambda s, c, p: ReplyObject(choice(p.split(',')), True)),

    # Generate the command list on load
    Command([link for link in YoutubeLinks], lambda s, c: ReplyObject(YoutubeLinks[c], True)),
    Command([f for f in formats], lambda s, c: ReplyObject('Format: http://www.smogon.com/dex/sm/formats/{tier}/'.format(tier = c), True)),

    # Commands with dedicated functions because of their complexity (need more than a single expression)
    Command(['get'], get),
    Command(['forcerestart'], forcerestart),
    Command(['savedetails'], savedetails),
    Command(['newautojoin'], newautojoin),
    Command(['setbroadcast'], setbroadcast),
    Command(['hi'],hi),
    Command(['regp'],regp),
##    Command(["hiback"],hiback),
    Command(["hello"],Hello),
    Command(['stats'],stats)

]
