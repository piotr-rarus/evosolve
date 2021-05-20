import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="linkage",
    description="Linkage Learning methods.",

    author="Piotr Rarus",
    author_email="piotr.rarus@gmail.com",

    url="https://github.com/piotr-rarus/linkage-learning",
    license="MIT",
    version="0.0.0",

    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(
        exclude=[
            "test"
        ]
    ),
    install_requires=[
        # "evobench==0.4.1"
    ],
    include_package_data=True,
    tests_require=[
        "flake8>=3.8.3",
        "pytest>=5.4.3",
        "pytest-cov>=2.10.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
