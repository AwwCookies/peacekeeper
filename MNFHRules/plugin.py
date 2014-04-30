###
# Copyright (c) 2014, scornflakes
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###


# -*- coding: utf-8 -*-

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import datetime
import random
from random import randint
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('MNFHRules')

class MNFHRules(callbacks.Plugin):
    """Add the help for "@plugin help MNFHRules" here
    This should describe *how* to use this plugin."""
    pass

    @internationalizeDocstring
    def isitfriday(self, irc, msg, args):
        """Tells you if it's Friday or not.
        """
        if datetime.datetime.now().weekday()==4:
            irc.reply("\x0313 YOU'RE DAMN RIGHT IT'S FRIDAY!!!")
        else:
            irc.reply("It's not Friday, You can pretend it is, but it just won't be the same.") 
    isitfriday = wrap(isitfriday)
    
    @internationalizeDocstring
    def isitmonday(self, irc, msg, args):
        """Tells you if it's Monday or not.
        """
        if datetime.datetime.now().weekday()==0:
            irc.reply("Please no, don't let it be so. Please.")
        else:
            irc.reply("*sigh of relief* it's not monday.") 
    isitmonday = wrap(isitmonday)
    
    def welcome(self, irc, msg, args, newusername):
        """Welcomes the user to the chan!!
        """
        irc.reply("Welcome to #mnfh {0}! We look forward to getting to know you! Please read more about the chat and rules here: http://goo.gl/dh08Gr".format(newusername))
    welcome = wrap(welcome, ['text'])

    @internationalizeDocstring
    def dance(self, irc, msg, args):
        """ Tells bot to dance!
        """
        irc.reply('\x03%s\\o/' % str(randint(0, 16)).zfill(1))
        irc.reply('\x03%s/o/' % str(randint(0, 16)).zfill(1))
        irc.reply('\x03%s\\o\\' % str(randint(0, 16)).zfill(1))
    dance = wrap(dance)
    
    @internationalizeDocstring
    def murica(self, irc, msg, args):
        """Murica!!!
        """
        irc.reply('Fuck YEAH!')
    murica = wrap(murica)
    
    @internationalizeDocstring
    def britain(self, irc, msg, args):
        """Britain!!!
        """
        irc.reply('Would you care for a spot of tea?')
    britain = wrap(britain)

    @internationalizeDocstring
    def whatislove(self, irc, msg, args):
        """ what is love?
        """
        irc.reply("Baby don't hurt me")
        irc.reply("Don't hurt me")
        irc.reply('No more')
    whatislove = wrap(whatislove)

    @internationalizeDocstring
    def snuggle(self, irc, msg, args, usern):
        """ snuggle...
        """
        irc.reply("(\xe3\x81\xa3\xe2\x8c\x92\xe2\x80\xbf\xe2\x8c\x92)\xe3\x81\xa3 %s" % usern)

    snuggle = wrap(snuggle, ['text'])

    @internationalizeDocstring
    def stab(self, irc, msg, args, usern):
        """ Stab function to stab your enemies
        """
        if 'brakos' in msg.nick or random.random()<0.15:
		irc.reply("%s tries to stab %s, but instead they slip and accidentally stab themself!" % (msg.nick, usern))
		irc.reply("\x0308o()\x0304xxxx\x0308[{\x0315::::::*\x0300%s*\x0315::::::>"% msg.nick)
	elif 'Peacekeeper' in usern:
		irc.reply("%s tries to stab Peacekeeper, instead Peacekeeper dodges the blow and draws his peacekeeper and fires."% msg.nick)
		irc.reply(u'\u003d\u03b5\u002f\u0335\u0347\u033f\u033f\u002f\u0027\u033f\u0027\u033f\u033f  BANG!  X_X {0}' .format(msg.nick))
	else:
		irc.reply("\x0308o()\x0304xxxx\x0308[{\x0315::::::*\x0300%s*\x0315::::::>"% usern)
    stab = wrap(stab, ['text'])
    
    @internationalizeDocstring
    def eyeroll(self, irc, msg, args, usern):
        """ eyeroll
        """

        irc.reply("\xe2\x97\x94\xcc\xaf\xe2\x97\x94 %s"% usern)
    eyeroll = wrap(eyeroll, ['text'])


    @internationalizeDocstring
    def kinematic1(self, irc, msg, args, usern):
        """ impersonate kinematic1
        """
        irc.reply("hiyooooooooooooooo %s!" % usern)

    kinematic1= wrap(kinematic1, ['text'])


Class = MNFHRules


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
