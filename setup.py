from setuptools import setup

setup(
    name="timedotc",
    version="0.1.0",
    url="https://github.com/markmelnic/timedotc",
    license="MIT License",
    author="Mark Melnic",
    author_email="me@markmelnic.com",
    description="Time relative one time computed code",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[],
    packages=["timedotc"],
    platforms=["MacOS X", "Posix"],
    zip_safe=False,
    test_suite="test",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)