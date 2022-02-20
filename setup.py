from setuptools import setup, find_packages

# This call to setup() does all the work
setup(
    name="aymakan-sdk",
    version="1.0",
    description="AyMakan SDK",
    long_description="This is official Aymakan Python SDK. It can be used to integrate with Aymakan APIs.",
    long_description_content_type="text/markdown",
    url="https://github.com/aymakan/python-sdk/",
    author="Abdullah AlQattan",
    author_email="a.alqattan@aymakan.com.sa",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["requests, python-decouple"],
    include_package_data=True,
    install_requires=[""]
)