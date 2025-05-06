from setuptools import setup, find_packages

setup(
    name="geometry-lib",
    version="0.1.0",
    description="Library for calculating the areas of geometric shapes",
    author="Artem Pervovsky",
    author_email="artyomperv@mail.ru",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)