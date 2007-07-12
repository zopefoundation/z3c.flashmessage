from setuptools import setup, find_packages

setup(
    name = "z3c.flashmessage",
    version = "1.0",
    author = "Jasper Op de Coul, Christian Theune",
    author_email = "jasper@infrae.com, ct@gocept.com",
    description = "A package for sending `flash messages` to users.",
    license = "ZPL 2.1",
    keywords = "zope3",
    zip_safe=False,
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['z3c'],
    install_requires = ['setuptools',
                        'ZODB3',
                        'zope.interface',
                        'zope.component',
                        'zope.app.session',
                        'zope.security'],
    extras_require=dict(test=['zope.app.testing',
                              'zope.app.zcmlfiles'])
)
