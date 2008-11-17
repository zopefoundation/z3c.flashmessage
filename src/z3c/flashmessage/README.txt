==============
Flash messages
==============

Components to display small messages to users.


Sending a message to the current user
=====================================

To send a message to the current user, you can use the session-based message
source. Let's set one up:

>>> from z3c.flashmessage.sources import SessionMessageSource
>>> source = SessionMessageSource()

>>> source.send(u'The world will come to an end in 40 seconds!')

The source allows to list all current messages:

>>> m = list(source.list())
>>> m
[<z3c.flashmessage.message.Message object at 0x...>]
>>> m[0].message
u'The world will come to an end in 40 seconds!'
>>> m[0].type
u'message'

Receiving messages
==================

The standard message that is generated removes itself from the source when it
is received. The receiver will call `prepare()` on the message before it is
handed out to the code that receives it:

>>> m[0].prepare(source)
>>> list(source.list())
[]

There also is another default message that does not delete itself when being
read:

>>> from z3c.flashmessage.message import PersistentMessage
>>> source.send(PersistentMessage(u'I will stay forever!'))
>>> m = list(source.list())[0]
>>> m.message
u'I will stay forever!'
>>> m.prepare(source)
>>> list(source.list())
[<z3c.flashmessage.message.PersistentMessage object at 0x...>]

Global receiver
===============

There is a global receiver that queries all message sources that are set up as
utilities. Let's set up a session message source as a utility:

>>> from zope.component import provideUtility 
>>> provideUtility(source)
>>> source.send(u'Test!')

>>> from z3c.flashmessage.sources import RAMMessageSource
>>> source2 = RAMMessageSource()
>>> provideUtility(source2, name='other')
>>> source2.send(u'Test 2!')
>>> source2.send(u'Test 3!')

>>> from z3c.flashmessage.receiver import GlobalMessageReceiver
>>> receiver = GlobalMessageReceiver()
>>> m = list(receiver.receive())
>>> len(m)
4
>>> m[0].message
u'I will stay forever!'
>>> m[1].message
u'Test!'
>>> m[2].message
u'Test 2!'
>>> m[3].message
u'Test 3!'

After the receiver handed out the messages, they are gone from the
sources, because the receiver notifies the messages that they were
read:

>>> len(list(receiver.receive()))
1


Filtering message types
=======================

When listing messages from a message source, we can restrict which messages we
see. If we don't give a type, then all messages are returned. The default type
of a message is `message`:

>>> source3 = RAMMessageSource()
>>> source3.send(u'Test 2!')
>>> list(source3.list())
[<z3c.flashmessage.message.Message object at 0x...>]
>>> list(source3.list('message'))
[<z3c.flashmessage.message.Message object at 0x...>]
>>> list(source3.list('somethingelse'))
[]


Performance and Scalability Issues
==================================

By default, messages are stored persistently in the ZODB using
zope.session.  This can be a significant scalability problem; see
design.txt in zope.session for more information.  You should think
twice before using flashmessages for unauthenticated users, as this
can easily lead to unnecessary database growth on anonymous page
views, and conflict errors under heavy load.

One solution is to configure your system to store flashmessages in
RAM. You would do this by configuring a utility providing
z3c.flashmessages.interfaces.IMessageSource with the factory set to
z3c.flashmessages.sources.RAMMessageSource, and a specific name if
your application expects one.

RAM storage is much faster and removes the persistence issues
described above, but there are two new problems.  First, be aware that
if your server process restarts for any reason, all unread
flashmessages will be lost.  Second, if you cluster your application
servers using e.g. ZEO, you must also ensure that your load-balancer
supports session affinity (so a specific client always hits the same
back end server).  This somewhat reduces the performance benefits of
clustering.


Changes
=======

1.0b2
-----

* Bugfix: When there was more than one message in a source not all messages
  would be returned by the receiver.
