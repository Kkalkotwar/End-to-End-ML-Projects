from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'  # It should run the setup also when we are reading the requirements.txt file

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines from the file
        requirements = [req.strip() for req in requirements]  # Strip newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# This is basically META DATA of the project.
setup(
    name='ML Project',
    version='0.0.1',
    author='Kunal.N.Kalkotwar',
    author_email='KUNALKALKOTWAR21@GMAIL.COM',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
