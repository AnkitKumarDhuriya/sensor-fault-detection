from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        requirements = file.read().splitlines()

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements




setup(
    name="sensor-fault-detection",
    version="0.0.1",
    author="Ankit Kumar Dhuriya",
    author_email="ankit.iit9090@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages = find_packages()
)
