==============
Flash messages
==============

Components to display small messages for users.


Sending a message to the current user
=====================================

To send a message to the current user, you can use the session-based message
source. Let's set one up:

>>> from z3c.flashmessage.session import SessionMessageSource
>>> source = SessionMessageSource()

>>> source.send(u'The world will come to an end in 40 seconds!')

Then, the user can receive the message:

>>> m = list(source.receive())
>>> m
[<z3c.flashmessage.message.Message object at 0x...>]
>>> m[0].message
u'The world will come to an end in 40 seconds!'
>>> m[0].type
u'message'

The standard message will remove itself from the source when it was received:

>>> list(source.receive())
[]




