import os.path
from setuptools import setup, find_packages

def read(*path_elements):
    return "\n\n" + file(os.path.join(*path_elements)).read()


setup(
    name = "z3c.flashmessage",
    version='1.2',
    author = "Jasper Op de Coul, Christian Theune",
    author_email = "jasper@infrae.com, ct@gocept.com",
    description = "A package for sending `flash messages` to users.",
    long_description=(
        '.. contents::\n\n' +
        read('src', 'z3c', 'flashmessage', 'README.txt') +
        read('CHANGES.txt')
        ),
    url = 'http://pypi.python.org/pypi/z3c.flashmessage/',
    license = "ZPL 2.1",
    keywords = "zope3 message zope session",
    zip_safe=False,
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['z3c'],
    install_requires = ['setuptools',
                        'ZODB3',
                        'zope.interface',
                        'zope.schema',
                        'zope.session'],
    extras_require=dict(test=[
        'zope.publisher',
        'zope.component',
        'zope.security',
        'zope.app.wsgi'])
)
