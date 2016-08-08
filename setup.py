import os.path
from setuptools import setup, find_packages


def read(*path_elements):
    with open(os.path.join(*path_elements), 'rt') as f:
        return "\n\n" + f.read()

TEST_REQUIREMENTS = [
    'zope.publisher',
    'zope.component',
    'zope.security',
    'zope.app.wsgi[testlayer] >= 4.0',
    'Webtest',
]

setup(
    name="z3c.flashmessage",
    version='2.0',
    author="Jasper Op de Coul, Christian Theune",
    author_email="jasper@infrae.com, mail@gocept.com",
    description="A package for sending `flash messages` to users.",
    long_description=(
        '.. contents::\n\n' +
        read('src', 'z3c', 'flashmessage', 'README.txt') +
        read('CHANGES.txt')
    ),
    url='http://pypi.python.org/pypi/z3c.flashmessage/',
    license="ZPL 2.1",
    keywords="zope3 message zope session",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3',
    ],
    zip_safe=False,
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    namespace_packages=['z3c'],
    install_requires=[
        'setuptools',
        'ZODB',
        'zope.interface',
        'zope.schema',
        'zope.session'
    ],
    extras_require=dict(test=TEST_REQUIREMENTS),
    setup_requires=[
        'eggtestinfo',  # captures testing metadata in EGG-INFO
        'zope.testrunner'
    ],
    tests_require=TEST_REQUIREMENTS,
    test_suite='z3c.flashmessage.tests.test_suite',
    test_loader='zope.testrunner.eggsupport:SkipLayers',
)
