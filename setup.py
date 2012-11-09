import os

from setuptools import find_packages
from setuptools import setup

version = '0.1'
project = 'kotti_panels'

install_requires = [
    'Kotti',
]

docs_require = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface',
]

tests_require = [
    'WebTest',
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'wsgi_intercept',
    'zope.testbrowser',
]

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

setup(
    name=project,
    version=version,
    description="Reusable units of content for Kotti",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
    ],
    keywords='kotti addon',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/kotti_panels',
    license='bsd',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points={
        'fanstatic.libraries': [
            'kotti_panels = kotti_panels.static:library',
        ],
    },
    extras_require={
        'docs': docs_require,
        'testing': tests_require,
    },
    message_extractors={
        'kotti_panels': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ]
    },
)
