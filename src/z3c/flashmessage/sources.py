# -*- coding: latin-1 -*-
# Copyright (c) 2007 Zope Foundation and Contributors
# See also LICENSE.txt
# $Id$
"""A message source that stores messages in the session."""

import zope.interface

import zope.session.interfaces

import persistent.list

import z3c.flashmessage.interfaces
import z3c.flashmessage.message


class ListBasedMessageSource(object):
    """An (abstract) base class that stores messages
    in a list.

    Sub-classes have to define the attribute `_storage`.

    """

    zope.interface.implements(z3c.flashmessage.interfaces.IMessageSource)

    def send(self, message, type=u"message"):
        """Send a message to this source."""
        if not z3c.flashmessage.interfaces.IMessage.providedBy(message):
            # The programmer has passed in not a message, so we create a
            # message for him. This is allowed by the API for convenience.
            message = z3c.flashmessage.message.Message(message, type=type)
        message.source = self
        self._storage.append(message)

    def list(self, type=None):
        """Return all messages of the given type from this source."""
        for message in self._storage:
            if type is None or message.type == type:
                yield message

    def delete(self, message):
        """Remove the given message from the source."""
        self._storage.remove(message)


class SessionMessageSource(ListBasedMessageSource):

    @property
    def _storage(self):
        request = zope.security.management.getInteraction().participations[0]
        session = zope.session.interfaces.ISession(
            request)['z3c.flashmessage']
        messages = session.setdefault('messages',
                                      persistent.list.PersistentList())
        return messages


class RAMMessageSource(ListBasedMessageSource):

    zope.interface.implements(z3c.flashmessage.interfaces.IMessageSource)

    def __init__(self):
        super(RAMMessageSource, self).__init__()
        self._storage = []
