#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
#include <float.h>
/**
 * print_python_list - prints info about python lists
 * @p: the pointer to a python list object
 * Return nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len = 0;
	Py_ssize_t i = 0;
	PyObject *item;

	setbuf(stdout, NULL);
	if (PyList_Check(p))
	{
		len = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", len);
		for (i = 0; i < len; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else if (len < 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
}
/**
 * print_python_bytes - prints info about python byte codes
 * @p: pointer to the python object to print its info
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *str = NULL;
	Py_ssize_t i = 0;
	Py_ssize_t len = 0;

	setbuf(stdout, NULL);
	if (PyBytes_Check(p))
	{
		printf("[*] Python bytes\n");
		str = PyBytes_AsString(p);
		len = PyBytes_Size(p);
		printf("  Bytes string: %s\n", str);
		printf("  Size: %ld\n", len);
		printf("  First 10 bytes: ");
		for (i = 0; i < len && i < 10; i++)
		{
			printf("%02hhx ", str[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - prints info about python float
 * @p: pointer to the python object to print its info
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	double value = 0.0;

	setbuf(stdout, NULL);
	if (PyFloat_Check(p))
	{
		value = PyFloat_AsDouble(p);
		printf("[*] Python float\n");
		printf("  Value: %f\n", value);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
}
