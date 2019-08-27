/*
 * Undefine macros defined by SWIG
 */
#ifdef PyInt_Check
#undef PyInt_Check
#endif

static int __pyfile_check_guard(PyObject *x)
{
    return 0;
}
#define PyFile_Check(x) __pyfile_check_guard((x))
static int __pyinstance_check_guard(PyObject *x)
{
    return 0;
}
#define PyInstance_Check(x) __pyinstance_check_guard((x))

#include "numpy/npy_3kcompat.h"
