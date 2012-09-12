"""
Express extreme, possibly religious enthusiasm whenever the topic of
smaller-than-average equine creatures comes up.

~ Corbin Simpson <simpsoco@osuosl.org>
"""

from zope.interface import implements
from twisted.plugin import IPlugin
from hackabot.plugin import IHackabotPlugin

class Honeybadger(object):
    implements(IPlugin, IHackabotPlugin)

    @staticmethod
    def msg(conn, event):
        if event["sent_by"] == conn.nickname:
            return

        message = event["text"].lower()

        if "don't care" in message or "give a shit" in message:
            conn.msg(event["reply_to"], "Honey Badger don't care! Honey Badger don't give a shit!!")

    me = msg

honeybadger = Honeybadger()
