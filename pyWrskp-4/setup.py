from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package, does not do much, so far just a random number, this is the first time ' \
                   'I have done this'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="pyWrskp",
    version="V6",
    author="Jonah",
    author_email="jonah@makowski.ca",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
