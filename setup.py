from setuptools import setup
from typing import List

#Decleration variable for setup function
PROJECT_NAME="housing-prediction"
VERSION="0.0.1"
AUTHOR="Vikash Singh"
DESCRIPTION="this is my first fsds project"
PACKAGES=["housing"]
REQUIRMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: this function is going to return list of requirement
    mention in requirements.txt

    return this function is going to return a list which contain name of 
    libraries mention in requirements.txt file
    """
    with open(REQUIRMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()    

)
