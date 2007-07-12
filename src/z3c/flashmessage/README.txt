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

>>> from z3c.flashmessage.receiver import GlobalMessageReceiver
>>> receiver = GlobalMessageReceiver()
>>> m = list(receiver.receive())
>>> len(m)
3
>>> m[0].message
u'I will stay forever!'
>>> m[1].message
u'Test!'
>>> m[2].message
u'Test 2!'

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
