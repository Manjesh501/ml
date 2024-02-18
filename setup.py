from setuptools import find_packages,setup
from typing import List


hyphen ='-e .'
def get_requirement(filepath :str)->List[str]:
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[ req.replace("\n", " ")for req in requirements]

        if hyphen in requirements:
          requirements.remove(hyphen)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Manjesh',
author_email='manjesht78@gmail.com',
packages= find_packages(),
install_requires=get_requirement('requirements.txt')


)