from setuptools import setup, find_packages
import os

setup(
    name='diagramskor',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'diagramskor': ['*.png'],  # 패키지 내에 데이터 파일을 포함하지 않음
    },
    install_requires=['diagrams'],
    author='Jung Jin Young',
    author_email='bungker@gmail.com',
    description='Diagrams extend for Korean cloud services',
    url='https://github.com/jyjung/diagramskor',
)