from setuptools import setup

setup(name='GGApp',
      version='1.0',
      description='OpenShift App',
      author='Krishna',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=open('./requirements.txt').readlines(),
     )
