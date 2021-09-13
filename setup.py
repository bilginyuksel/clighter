import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clighter",
    version="0.3.2",
    author="bilginyuksel",
    author_email="bilgin.yuksel96@gmail.com",
    description="Game engine for CLI games.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bilginyuksel/clighter",
    project_urls={
        "Bug Tracker": "https://github.com/bilginyuksel/clighter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
