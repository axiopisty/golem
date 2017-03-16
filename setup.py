#!/usr/bin/env python

from setuptools import setup

from setup.setup_commons import *
from setup.taskcollector_builder import TaskCollectorBuilder
from sys import argv

if 'bdist_wheel' in argv:
    ui_err = generate_ui()
requirements, dependencies = parse_requirements(path.dirname(__file__))
docker_err = try_pulling_docker_images()
task_collector_err = TaskCollectorBuilder().build()
setup(
    name='golem',
    version=get_golem_version('bdist_wheel' in argv),
    description='Global, open sourced, decentralized supercomputer',
    long_description=get_long_description(path.abspath(path.dirname(__file__))),
    url='https://golem.network',
    author='Golem Team',
    author_email='contact@golemproject.net',
    license="GPL-3.0",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
    keywords='golem',
    packages=find_required_packages(),
    install_requires=requirements,
    dependency_links=dependencies,
    # @todo remove test dependencies from requirements.txt and add here
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    include_package_data=True,
    cmdclass={'test': PyTest},
    test_suite='tests',
    tests_require=['mock', 'pytest'],
    entry_points={
        'gui_scripts': [
            'golemapp = golemapp:start',
        ],
        'console_scripts': [
            'golemcli = golemcli:start',
        ]
    },
    data_files=get_files()
)

if 'bdist_wheel' not in argv:
    ui_err = generate_ui()

print_errors(ui_err, docker_err, task_collector_err)
