from setuptools import setup

setup(
    name='notefall',
    version="0.0.01-alpha",
    description='Fallingnote mania style game that can load osu!mania beatmaps',
    url='https://github.com/notefall/notefall',
    author='ExhaustedBiped',
    author_email='exhaustedbiped5@gmail.com',
    license='Apache 2.0',
    packages=['notefall'],
    #install_requires=['pygame>=1.9.1'],
    zip_safe=False,
    include_package_data=True
)
