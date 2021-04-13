#!/usr/bin/env python

# import versioneer
# import numpy as np

from setuptools import setup, find_packages
from distutils.extension import Extension
from distutils.command.build import build as build_orig

#===============================================================================

def readme():
    with open('README.md', 'r') as content:
        return content.read()

#===============================================================================

ext_modules = [
        Extension('gryffin.bayesian_network.kernel_evaluations',
                ['src/gryffin/bayesian_network/kernel_evaluations.c']),
        Extension('gryffin.bayesian_network.kernel_prob_reshaping',
                ['src/gryffin/bayesian_network/kernel_prob_reshaping.c']),]

# Preinstall numpy
from setuptools import dist
dist.Distribution().fetch_build_eggs(['numpy>=1.10'])
import numpy as np


#===============================================================================

setup(name='gryffin',
        version='0.1.1',
        # cmdclass=versioneer.get_cmdclass(),
        description='Bayesian optimization for categorical variables',
        long_description=readme(),
        long_description_content_type='text/markdown',
        classifiers=[
                'Intended Audience :: Science/Research',
                'Operating System :: Unix',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering',
        ],
        url='https://github.com/Atinary-technologies/gryffin',
        packages=find_packages('./src'),
        package_dir={'': 'src'},
        zip_safe=False,
        ext_modules=ext_modules,
        tests_require=['pytest'],
        include_dirs=np.get_include(),
        install_requires = [
            "Cython==0.29.22",
            "edward2 @ git+https://github.com/google/edward2.git@a06c3abd8ec9aa4928aad6ae336e7c0324edcbc7",
            "matplotlib==3.4.1",
            "numpy==1.19.2",
            "pandas==1.2.3",
            "seaborn==0.11.1",
            "SQLAlchemy==1.4.6",
            "tensorflow==2.4.0",
            "tensorflow-probability==0.12.0"
        ],
        python_requires='>=3.6',
)
