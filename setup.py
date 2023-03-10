from setuptools import find_packages, setup
setup(
    name='LinkedListFunctionsLib',
    packages=find_packages(include=['LinkedListFunctionsLib']),
    version='0.1.0',
    description='Library for linked lists',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)