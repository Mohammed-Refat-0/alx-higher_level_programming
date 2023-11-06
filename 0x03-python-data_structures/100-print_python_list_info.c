#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - Print info about Python's lists
 * @p: Pyobjext pointer
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t count;
	Py_ssize_t length = PyList_Size(p);
	PyListObject *pyObj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", length);
	printf("[*] Allocated = %ld\n", pyObj->allocated);
	for (count = 0; count < length; count++)
	{
		printf("Element %ld: %s\n", count, Py_TYPE(pObj->ob_item[count])->tp_name);
	}
}
