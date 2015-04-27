from setuptools import setup, find_packages

requires = open('requirements.txt').read().split('\n')

setup(
    name='Timesync CLI',
    version='0.1.0',
    description='Submits time to a timesync instance [http://github.com/osuosl/timesync].',
    install_requires=requires,
    author='Dean Johnson',
    author_email='deanjohnson222@gmail.com',
    url='https://www.github.com/dean/timesync-cli-python',
    scripts=['timesync'],
)
