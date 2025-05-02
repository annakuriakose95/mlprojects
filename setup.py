# why setup.py - Consider your entire machine learning project as a package

from setuptools import find_packages, setup # type: ignore
from typing import List
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
        
# Considered as meta data information of the entire project
setup(
    name='mlproject',
    version='0.0.1',
    author='Anna',
    author_email='annakuriakose1611@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    
    
)

