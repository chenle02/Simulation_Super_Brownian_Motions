from setuptools import setup, find_packages

setup(
    name='your_package',
    version='1.0',
    packages=find_packages(),
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Le Chen',
    author_email='chenle02@gmail.com',
    url='https://github.com/chenle02/Simulation_Super_Brownian_Motions',
    install_requires=[
        # Any dependencies your package needs, e.g.,
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        # Choose your license as you wish
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
