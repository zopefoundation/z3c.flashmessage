# -*- coding: latin-1 -*-
# Copyright (c) 2007 Zope Foundation and Contributors
# See also LICENSE.txt
# $Id$
"""A global message receiver that covers all sources."""

import zope.interface

import z3c.flashmessage.interfaces


@zope.interface.implementer(z3c.flashmessage.interfaces.IMessageReceiver)
class GlobalMessageReceiver(object):

    def receive(self, type=None):
        sources = zope.component.getAllUtilitiesRegisteredFor(
            z3c.flashmessage.interfaces.IMessageSource)
        for source in sources:
            # We need to create a list here, because message.prepare might
            # modify the original source list stop the iteration before
            # all items where consumed:
            for message in list(source.list(type)):
                message.prepare(source)
                yield message
