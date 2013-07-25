import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-cms-events',
    version=__import__('cmsplugin_events').__version__,
    author='Viktor Nagy',
    author_email='viktor.nagy@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/nagyv/django-cms-events',
    download_url='https://github.com/nagyv/django-cms-events/zipball/master',
    description=u' '.join(__import__('cmsplugin_events').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    test_suite="runtests.runtests",
    zip_safe=False,
    install_requires=[
        'Django>=1.4,<1.6',
    ]
)
