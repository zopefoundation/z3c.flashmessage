# -*- coding: latin-1 -*-
# Copyright (c) 2007 Zope Foundation and Contributors
# See also LICENSE.txt
# $Id$
"""A simple message that can be displayed."""

import persistent
import z3c.flashmessage.interfaces
import zope.interface


@zope.interface.implementer(z3c.flashmessage.interfaces.IMessage)
class BaseMessage(persistent.Persistent):
    """A message that is displayed to the user.

    An (abstract) base class.

    """

    def __init__(self, message, type=u"message"):
        self.message = message
        self.type = type


class Message(BaseMessage):
    """A message that is displayed to the user.

    This message will delete itself after being received.

    """

    def prepare(self, source):
        """Prepare for being received.

        Messages that get are received get removed from the source.

        """
        source.delete(self)


class PersistentMessage(BaseMessage):
    """A message that doesn't delete itself when being received."""

    def prepare(self, source):
        pass
