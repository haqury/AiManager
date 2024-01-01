from setuptools import setup

setup(
    name='AiManager',
    version='1.0',
    description='A useful module',
    author='Author Name',
    author_email='haqury@gmail.com',
    packages=['AiManager'],  # same as name
    install_requires=['PyQt5', 'openai', 'win32api'],  # external packages as dependencies
)