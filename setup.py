from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    "Function will return the list of requirements"

    requirements=[]
    with open (file_path) as file_obj:
        requirements+file_obj.readlines()

setup(
name='dsproject',
version='0.0.1',
author='Pedro Gomes',
author_email='pedrogomes_140@hotmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)