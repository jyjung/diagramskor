from setuptools import setup, find_packages
import os

setup(
    name='diagramskor',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'my_package': [],  # 패키지 내에 데이터 파일을 포함하지 않음
    },
    data_files= [],  # /site-packages에 복사할 파일    
    install_requires=['diagrams'],
    author='Jung Jin Young',
    author_email='bungker@gmail.com',
    description='Diagrams extend for Korean cloud services',
    url='https://github.com/jyjung/diagramskor',
)