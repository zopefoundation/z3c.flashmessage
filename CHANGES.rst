=======
CHANGES
=======

3.1 (2025-04-03)
================

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


3.0 (2023-02-08)
================

- Drop support for Python 2.7, 3.4, 3.5, 3.6.

- Add support for Python 3.8, 3.9, 3.10, 3.11.

- Ensure all objects have consistent resolution orders.


2.1 (2018-11-12)
================

- Claim support for Python 3.6, 3.7, PyPy and PyPy3.

- Drop support for Python 3.3.

- Drop support for ``python setup.py test``.


2.0 (2016-08-08)
================

- Standardize namespace ``__init__``.

- Claim compatibility for Python 3.3, 3.4, and 3.5.

1.3 (2010-10-28)
================

- ``SessionMessageSource`` implicitly created sessions when the client was
  reading the messages from the source. Changed internal API so reading no
  longer creates a session when it not yet exists.

1.2 (2010-10-19)
================

* Removed test dependency on `zope.app.zcmlfiles`.


1.1 (2010-10-02)
================

* Removed test dependency on `zope.app.testing`.


1.0 (2007-12-06)
================

* Updated dependency to `zope.session` instead of `zope.app.session` to get
  rid of deprecation warnings.


1.0b2 (2007-09-12)
==================

* Bugfix: When there was more than one message in a source not all messages
  would be returned by the receiver.

1.0b1 (2007-08-22)
==================

* Initial public release.
