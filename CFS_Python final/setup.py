from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["pandas", "numpy"],
                     "include_files": ["processes.xlsx"],
                     "excludes": 
                         ["tkinter", "tensorflow","tensorboard","theano", "PyQt5",
                          'adodbapi', 'alabaster', 'asn1crypto', 'asyncio', 'babel',
                          'backports', 'bottleneck', 'bs4', 'certifi', 'cffi', 'chardet',
                          'cloudpickle', 'colorama', 'concurrent', 'cryptography', 'ctypes',
                          'curses', 'Cython', 'cytoolz', 'dask', 'dbm', 'dill', 'distributed',
                          'docutils', 'et_xmlfile', 'folders.py', 'h5py', 'html', 'html5lib', 
                          'idna', 'imagesize', 'ipykernel', 'IPython', 'ipython_genutils', 
                          'ipywidgets', 'jedi', 'jinja2', 'jsonschema', 'jupyter_client', 
                          'jupyter_core', 'keras', 'lib2to3', 'locket', 'lxml', 'markupsafe',
                          'matplotlib', 'mpi4py', 'msgpack', 'multiprocessing', 'mysql', 
                          'nbconvert', 'nbformat', 'nose', 'notebook', 'numexpr', 'numpydoc',
                          'openpyxl', 'OpenSSL', 'pandas_datareader', 'partd', 'patsy', 'PIL',
                          'pkg_resources', 'prompt_toolkit', 'psutil', 'py', 'pycparser',
                          'pydoc_data', 'pygments', 'pyreadline', 'pywin', 'pyximport',
                          'requests', 'requests_ftp', 'scipy', 'setuptools', 'sklearn', 
                          'sortedcontainers', 'sphinx', 'sphinxcontrib', 'sqlalchemy', 
                          'sqlite3', 'statsmodels', 'tables', 'tblib', 'testpath', 'toolz',
                          'tornado', 'traitlets', 'wcwidth', 'win32com', 'win_unicode_console', 
                          'xlsxwriter', 'xlwt', 'xmlrpc', 'yaml', 'zict', 'zmq']
}

#"bokeh", "cloudpickle", "cryptography","crypto","email","jinja2", "mpi4py"

setup(  name = "scheulder",
        version = "1",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Input.py", base=None)])




