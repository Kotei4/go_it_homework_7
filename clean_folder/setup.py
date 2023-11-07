from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Sort, transliterate, files in folder by type.',
    url='https://github.com/Kotei4/Go_IT_sorter',
    author='Kostiantyn.K',
    author_email='mynewtestacc@gmail.com',
    license='MIT',
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.main:ruun']} #1 узнать что сюда прописівать

)