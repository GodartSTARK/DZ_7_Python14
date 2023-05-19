from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Sorted folders',
    author='Volodymyr Dobrovolskyi',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean_folder=clean_folder.clean:main'
        ]
    }
)