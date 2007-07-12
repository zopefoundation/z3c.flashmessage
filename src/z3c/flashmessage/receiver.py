# -*- coding: latin-1 -*-
# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$
"""A global message receiver that covers all sources."""

import zope.interface

import z3c.flashmessage.interfaces


class GlobalMessageReceiver(object):

    zope.interface.implements(z3c.flashmessage.interfaces.IMessageReceiver)

    def receive(self, type=None):
        sources = zope.component.getAllUtilitiesRegisteredFor(
            z3c.flashmessage.interfaces.IMessageSource)
        for source in sources:
            for message in source.list(type):
                message.prepare(source)
                yield message
