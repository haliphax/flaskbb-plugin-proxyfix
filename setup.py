'Adds the Werzeug ProxyFix middleware to FlaskBB.'

from setuptools import setup

setup(
    name='flaskbb-plugin-proxyfix',
    packages=['proxyfix'],
    version='1.0',
    author='haliphax',
    author_email='haliphax@github.com',
    description='Werkzeug ProxyFix',
    url='https://github.com/haliphax/flaskbb-plugin-proxyfix',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    entry_points={'flaskbb_plugins':
                  ['proxyfix = proxyfix']},
    classifiers=[
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
