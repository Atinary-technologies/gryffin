
#!/usr/bin/env python

import numpy as np

from distutils.core      import setup
from distutils.extension import Extension
from Cython.Build        import cythonize

ext_modules = [
        Extension(
                        'kernel_evaluations', ['kernel_evaluations.pyx'],
                         include_dirs       = [np.get_include(), '.'],
                         extra_compile_args = ['-fopenmp'], 
                         extra_link_args = ['-fopenmp'],
                ),
        Extension(
                        'kernel_prob_reshaping', ['kernel_prob_reshaping.pyx'],
                         include_dirs       = [np.get_include(), '.'],
                         extra_compile_args = ['-fopenmp'], 
                         extra_link_args = ['-fopenmp'],
                ),
]

setup(
        name = 'Phoenics',
        ext_modules  = cythonize(ext_modules)
)
