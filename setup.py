import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RMinimum-Algorithm", # Replace with your own username
    version="0.0.1",
    author="Julian Lorenz",
    author_email="jfk.lorenz@gmail.com",
    description="Package for the RMinimum algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfklorenz/RMinimum-Algorithm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
