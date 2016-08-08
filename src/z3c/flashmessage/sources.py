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


@zope.interface.implementer(z3c.flashmessage.interfaces.IMessageSource)
class ListBasedMessageSource(object):
    """An (abstract) base class that stores messages
    in a list.

    Sub-classes have to define the method
    `_get_storage(self, for_write=False)`.

    """

    def send(self, message, type=u"message"):
        """Send a message to this source."""
        if not z3c.flashmessage.interfaces.IMessage.providedBy(message):
            # The programmer has passed in not a message, so we create a
            # message for him. This is allowed by the API for convenience.
            message = z3c.flashmessage.message.Message(message, type=type)
        message.source = self
        self._get_storage(for_write=True).append(message)

    def list(self, type=None):
        """Return all messages of the given type from this source."""
        for message in self._get_storage(for_write=False):
            if type is None or message.type == type:
                yield message

    def delete(self, message):
        """Remove the given message from the source."""
        self._get_storage(for_write=True).remove(message)

    def _get_storage(self, for_write=False):
        """Return the storage which must have a list API.

        When `for_write` is True the caller want's to write to the storage.

        To be implemented in concreate sub classes

        """


class SessionMessageSource(ListBasedMessageSource):
    """Source which stores its data in the session of the user."""

    _pkg_id = 'z3c.flashmessage'

    def _get_storage(self, for_write=False):
        request = zope.security.management.getInteraction().participations[0]
        session = zope.session.interfaces.ISession(request)
        if for_write:
            # Creating a new session when it does not exist yet.
            session_data = session[self._pkg_id]
        else:
            # Making sure we do *not* create a new session when it not exists:
            session_data = session.get(self._pkg_id, {})
        return session_data.setdefault('messages',
                                       persistent.list.PersistentList())


@zope.interface.implementer(z3c.flashmessage.interfaces.IMessageSource)
class RAMMessageSource(ListBasedMessageSource):
    """Source which stores its data in RAM.

    Caution: This source is not able to store messages for individual users.

    """

    def __init__(self):
        super(RAMMessageSource, self).__init__()
        self._storage = []

    def _get_storage(self, for_write=False):
        return self._storage
