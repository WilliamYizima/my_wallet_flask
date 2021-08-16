from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip() 
        for req 
        in open(filename).readlines()
        ]

setup(
    name="wallet",
    version="0.1.0",
    description="wallet app integrate React-app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)