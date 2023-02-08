# Copyright (c) 2007 Zope Foundation and Contributors
# See also LICENSE.txt
# $Id$
"""Test harness"""

import doctest

import zope.app.wsgi.testlayer
import zope.publisher.browser
import zope.security.management

import z3c.flashmessage


FlashMessageLayer = zope.app.wsgi.testlayer.BrowserLayer(
    z3c.flashmessage, allowTearDown=True)


def setUp(test):
    request = zope.publisher.browser.TestRequest()
    zope.security.management.newInteraction()
    interaction = zope.security.management.getInteraction()
    interaction.add(request)


def test_suite():
    suite = doctest.DocFileSuite(
        'README.rst',
        optionflags=doctest.ELLIPSIS,
        setUp=setUp)
    suite.layer = FlashMessageLayer
    return suite
