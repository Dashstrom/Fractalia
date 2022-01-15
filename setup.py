from sys import stderr
from setuptools import setup, find_packages


def read(path: str) -> str:
    try:
        with open(path, "r", encoding="utf8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"warning: No {path!r} found", file=stderr)
        return ""


REQUIREMENTS = [i.strip() for i in read("requirements.txt").split('\n')]

setup(
    name='fractalia',
    version="1.0.0",
    author="***REMOVED*** ***REMOVED*** - William MADIE",
    author_email='***REMOVED***',
    url='https://github.com/Dashstrom/Fractalia',
    license=read("LICENSE"),
    packages=find_packages(exclude=('tests', 'docs')),
    long_description=read("README.md"),
    install_requires=REQUIREMENTS,
    description=('Tkinter application for generate landscapes '
                 'composed of fractals.')
)
