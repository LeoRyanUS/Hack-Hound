from setuptools import setup, find_packages

# Hack Hound Setup
# Developed by Leo Ryan
# GitHub: https://github.com/LeoRyanUS/Hack-Hound
# GitHub Username: LeoRyanUS
# Email: leoryanus@gmail.com

setup(
    name="hackhound",
    version="1.0.0",
    author="Leo Ryan",
    author_email="leoryanus@gmail.com",
    description="A Python-based web security tool for professionals",
    url="https://github.com/LeoRyanUS/Hack-Hound",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.10.0",
        "colorama==0.4.4",
        "requests==2.26.0"
    ],
)
