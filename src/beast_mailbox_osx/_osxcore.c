
#include <Python.h>
#include <sys/utsname.h>

static PyObject* osx_info(PyObject* self, PyObject* args) {
    struct utsname u;
    if (uname(&u) != 0) {
        Py_RETURN_NONE;
    }
    PyObject* dict = Py_BuildValue("{s:s,s:s,s:s}",
        "platform", u.sysname,
        "arch", u.machine,
        "version", "0.1.0"
    );
    return dict;
}

static PyObject* index(PyObject* self, PyObject* args) {
    const char* path;
    if (!PyArg_ParseTuple(args, "s", &path)) return NULL;
    // TODO: implement macOS fast path (e.g., FSEvents/metadata) here.
    Py_RETURN_NONE;
}

static PyMethodDef Methods[] = {
  {"osx_info", osx_info, METH_NOARGS, "Return basic platform info for sanity checks."},
  {"index", index, METH_VARARGS, "OSX-specific mailbox index fast path (stub)."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mod = { PyModuleDef_HEAD_INIT, "_osxcore", NULL, -1, Methods };
PyMODINIT_FUNC PyInit__osxcore(void) { return PyModule_Create(&mod); }
