from xdress.utils import apiname

package = 'slicer'     # top-level python package name
packagedir = 'slicer'  # loation of the python package

#plugins = ('xdress.stlwrap', 'xdress.cythongen', 
#           'xdress.autodescribe', 'xdress.autoall')

extra_types = 'xdress_extra_types'

stlcontainers = [
    ('vector', 'int'),
    ('vector', ('vector', 'int')),
    ('vector', 'float'),
    ('vector', ('vector', 'float')),
    ]

classes = [apiname('Dag_Slicer', ('src/dag_slicer.hpp','src/dag_slicer.cpp'), incfiles = 'dag_slicer.hpp'),]


