#from distutils.core import setup
#from Cython.Build import cythonize

#setup(ext_modules = cythonize('day11_cython_gmp.pyx',compiler_directives={'language_level' : "3"}))
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import sys

ext = Extension("day11_cython_gmp2", ["day11_cython_gmp2.pyx"], include_dirs=sys.path, libraries=['gmp', 'mpfr', 'mpc'])

setup(
    name="day11_cython_gmp2",
    ext_modules=cythonize([ext], include_path=sys.path)
)