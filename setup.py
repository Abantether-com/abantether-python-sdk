from setuptools import setup
from setuptools import setup, find_packages

version = '0.0.5'

setup(
    name='abantether-python-sdk',
    packages=['abantether'],
    license='MIT',
    version=version,
    author='Iman Mousaei',
    author_email='imanmousaei1379@gmail.com',
    description='A python sdk to trade easily in abantether.com',
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'rt').read(),
    url='https://github.com/Abantether-com/abantether-python-sdk/',
    download_url=f'https://github.com/imanmousaei/coinexpy/archive/refs/tags/v{version}.tar.gz',
    keywords=['abantether', 'sdk', 'python', 'api', 'exchange', 'wrapper', 'trade', 'crypto', 'bitcoin'],
    install_requires=[
        'requests==2.31.0'
    ],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.4',
)
