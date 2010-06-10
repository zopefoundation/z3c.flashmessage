# -*- coding: latin-1 -*-
# Copyright (c) 2007 Zope Foundation and Contributors
# See also LICENSE.txt
# $Id$
"""Flash message interfaces"""

import zope.interface
import zope.schema


class IMessage(zope.interface.Interface):
    """A message that can be displayed to the user."""

    message = zope.schema.TextLine(title=u"The message itself.")

    type = zope.schema.TextLine(title=u"A classifier for the message",
                                default=u"message")

    def prepare(source):
        """Prepare for being received.

        This method is called by the IMessageSource before the message is
        returned before being displayed to the user.

        Two things are generally reasonable to do here:

            - Decide whether the message should be deleted from the source
            - Update the message

        """


class IMessageSource(zope.interface.Interface):

    def send(message, type=u"message"):
        """Send a message to this source.

        Message can either be a unicode string or an IMessage object.

        """

    def list(type=None):
        """Return all messages of the given type from this source.

        If type is None, all messages will be returned.

        The result is an iterable.

        """

    def delete(message):
        """Remove the given message from the source."""


class IMessageReceiver(zope.interface.Interface):
    """Receive messages.

    Depending on the implementation, this receives messages from various
    sources.

    """

    def receive(type=None):
        """Return all messages of the given type relevant to the current
        request.
        """
