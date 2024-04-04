import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "EC2_Machine_Learning"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "saijaideep111@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=saijaideep10,
    author_email=saijaideep111@gmail.com,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/saijaideep10/EC2_Machine_Learning",
    project_urls={
        "Bug Tracker": f"https://github.com/saijaideep10/EC2_Machine_Learning/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)