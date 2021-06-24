import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="evosolve",
    description="Metaheuristics solvers.",

    author="Piotr Rarus",
    author_email="piotr.rarus@gmail.com",

    url="https://github.com/piotr-rarus/evosolve",
    license="MIT",
    version="0.0.1",

    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(
        exclude=[
            "test",
            "examples"
        ]
    ),
    install_requires=[
        "evobench>=0.5.2"
    ],
    include_package_data=True,
    tests_require=[
        "flake8>=3.8.3",
        "pytest>=5.4.3",
        "pytest-cov>=2.10.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
