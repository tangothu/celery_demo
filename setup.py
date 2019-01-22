from setuptools import find_packages, setup

docs_require = [
    'sphinx',
]

install_requires = [
    'amqp==1.4.9',
    'anyjson==0.3.3',
    'billiard==3.3.0.23',
    'celery==3.1.26.post2',
    'celery-with-redis==3.0',
    'kombu==3.0.37',
    'pytz==2018.9',
    'redis==3.0.1',
    'vine==1.2.0'
]

setup(
    name='celery_demo',
    version='1.0.0',
    description='',
    author='Kevin Tan',
    author_email='tange116@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
)
