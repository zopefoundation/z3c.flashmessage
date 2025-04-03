import os.path

from setuptools import find_packages
from setuptools import setup


def read(*path_elements):
    with open(os.path.join(*path_elements)) as f:
        return "\n\n" + f.read()


TEST_REQUIREMENTS = [
    'zope.publisher',
    'zope.component',
    'zope.security',
    'zope.testrunner',
    'zope.app.wsgi[testlayer] >= 4.0',
    'Webtest',
]

setup(
    name="z3c.flashmessage",
    version='3.1',
    author="Jasper Op de Coul, Christian Theune",
    author_email="jasper@infrae.com, mail@gocept.com",
    description="A package for sending `flash messages` to users.",
    long_description=(
        '.. contents::\n\n' +
        read('src', 'z3c', 'flashmessage', 'README.rst') +
        read('CHANGES.rst')
    ),
    url='https://github.com/zopefoundation/z3c.flashmessage',
    license="ZPL-2.1",
    keywords="zope3 message zope session",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope :: 3',
    ],
    zip_safe=False,
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    namespace_packages=['z3c'],
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
        'ZODB',
        'zope.interface',
        'zope.schema',
        'zope.session'
    ],
    extras_require=dict(test=TEST_REQUIREMENTS),
)
