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

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import datetime
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
    murica = wrap(britain)

    def whatislove(self, irc, msg, args):
        """ what is love?
        """
        irc.reply("Baby don't hurt me")
        irc.reply("Don't hurt me")
        irc.reply('No more')
    whatislove = wrap(whatislove)

    @internationalizeDocstring
    def stab(self, irc, msg, args, usern):
        """ Stab function to stab your enemies
        """
        #usern="brakos"
        irc.reply("o()xxxx[{::::::*%s*::::::>" % usern)
    stab = wrap(stab, ['text'])


    @internationalizeDocstring
    def kinematic1(self, irc, msg, args, usern):
        """ impersonate kinematic1
        """
        irc.reply("hiyooooooooooooooo %s !" % usern)

    kinematic1= wrap(kinematic1, ['text'])


Class = MNFHRules


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
