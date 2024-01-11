import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='CodeChallenge.py',
    version='0.1.0',
    description='Code Challenge',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/krishnamanchikalapudi/CodingChallenge.py',
    classifiers=[
        'Development Status :: 0.1',
        'Programming Language :: Python :: 3.11'
    ],
    author='Krishna Manchikalapudi',
    license='MIT License',
    packages=setuptools.find_packages(),
    install_requires=[

    ],
    zip_safe=False
)