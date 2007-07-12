# -*- coding: latin-1 -*-
# Copyright (c) 2007 Infrae, gocept gmbh & co. kg and Contributors
# See also LICENSE.txt
# $Id$
"""A simple message that can be displayed."""

import persistent
import zope.interface

import z3c.flashmessage.interfaces


class Message(persistent.Persistent):
    """A message that is displayed to the user.

    This is the default message which will delete itself after being received.

    """

    zope.interface.implements(z3c.flashmessage.interfaces.IMessage)

    def __init__(self, message, type=u"message"):
        self.message = message
        self.type = type

    def prepare(self, source):
        """Prepare for being received.

        Messages that get are received get removed from the source.

        """
        source.delete(self)
