import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="islpwf",
    version="0.3",
    author="Kurt Rinnert",
    author_email="kurt.rinnert@liverpool.ac.uk",
    description="Datasets and helper functions for Introduction to Statistical Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rinnert/statlearning-python-pwf/tree/master/isl_python_package",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
