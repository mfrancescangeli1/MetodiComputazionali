import numpy
import ctypes

# Carico la lireria libsomme (libsomme.so) che è presente nella cartella di lavoro  ('.')
_libserie = numpy.ctypeslib.load_library('libserie', '.')

# definizoine tipi di input (argtypes) e di output (restypes) per la funzione sum_n di libsomme 
_libserie.fibonacci.argtypes = [ctypes.c_int]
_libserie.fibonacci.restype  = ctypes.c_int

# definizoine tipi di input (argtypes) e di output (restypes) per la funzione sum_sqrtn di libsomme 
_libserie.rapporto.argtypes = [ctypes.c_int]
_libserie.rapporto.restype  = ctypes.c_double

# utilizzo di _libsomme.sum_n
# il parametro n va necessariamente convertito in int
def fibonacci(n):
    return _libserie.fibonacci(int(n))


# utilizzo di _libsomme.sum_sqrtn
# il parametro n va necessariamente convertito in int
def rapporto(n):
    return _libserie.rapporto(int(n))


