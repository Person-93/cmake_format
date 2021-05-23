import io
from setuptools import setup

GITHUB_URL = "https://github.com/cheshirekow/cmakelang"

VERSION = None
with io.open("cmakelang/__init__.py", encoding="utf-8") as infile:
  for line in infile:
    line = line.strip()
    if line.startswith("__version__ ="):
      VERSION = line.split("=", 1)[1].strip().strip("'\"")

assert VERSION is not None


with io.open("cmakelang/doc/README.rst", encoding="utf-8") as infile:
  long_description = infile.read()

setup(
    name="cmakelang",
    version=VERSION,
    packages=[
        "cmakelang",
        "cmakelang.format",
        "cmakelang.lex",
        "cmakelang.lint",
        "cmakelang.parse",
        "cmakelang.parse.funs",
    ],
    description="Language tools for cmake (format, lint, etc)",
    long_description=long_description,
    author="Josh Bialkowski",
    author_email="josh.bialkowski@gmail.com",
    url=GITHUB_URL,
    download_url="{}/archive/{}.tar.gz".format(GITHUB_URL, VERSION),
    keywords=["cmake", "format"],
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    include_package_data=True,
    package_data={
        "cmakelang": [
            "templates/*"
        ]
    },
    entry_points={
        "console_scripts": [
            "cmake-annotate=cmakelang.annotate:main",
            "cmake-format=cmakelang.format.__main__:main",
            "cmake-lint=cmakelang.lint.__main__:main",
            "cmake-genparsers=cmakelang.genparsers:main",
            "ctest-to=cmakelang.ctest_to:main"
        ],
    },
    extras_require={
        "YAML": ["pyyaml>=5.4"],
        "html-gen": ["jinja2==2.10.3"]
    },
    install_requires=["six>=1.13.0"]
)
