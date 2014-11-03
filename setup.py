from os.path import join, dirname
from distutils.core import setup

try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-static-jquery',
    version='2.1.1',
    url="https://github.com/Haos616/django-static-jquery",
    description='jQuery packaged in an handy django app to speed up new applications and deployment.',
    long_description=long_description,
    author='Denis',
    author_email='haos616@gmail.com',
    license='BSD',
    keywords='django jquery staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_static_jquery'],
     include_package_data=True,
)