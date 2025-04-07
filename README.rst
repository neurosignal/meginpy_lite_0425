.. -* mode: rst -*-
================
meginpy_lite_0425
================

A module to convert string type digitization into extra type headshape points.

It is a temporary workaround until the string gets support by mne-tools. 
It utilizes MEGIN's ***show_fiff*** utility to correctly read all digitization types and then feed back to the file. 
Optionally the file with the denser digitization points can be written. 
If show_fiff is not available on the same machine, provide hostname, username, and password for a computer where show_fif is installed.
The module seamlessly connect to the host machine and perform the task, if the data is readable to the host machine. 

How to use
===========

There are two ways to use the module: i) by installing, ii) adding it to your script

i) Installation
------------

Download the software and install it:

.. code-block:: bash

    git clone https://github.com/neurosignal/meginpy_lite_0425.git
    cd meginpy_lite_0425
    python setup.py install
    
Usage:

.. code-block:: bash

    from meginpy_lite_0425.digitization import string2extra
    raw = string2extra(fname, hostname=ip_adr, username=uname, password=pswrd, raw_new_fname=False)


ii) Adding its path into your script
------------

.. code-block:: bash

    import sys
    sys.path.append(..../meginpy_lite_0425/)
    
    from digitization import string2extra
    raw = string2extra(fname, hostname=ip_adr, username=uname, password=pswrd, raw_new_fname=False)

For better usage clarity, please check out `test_usage.py <https://github.com/neurosignal/meginpy_lite_0425/blob/main/test_usage.py>`_ file.
  
Requirements
============
 - `Numpy <https://www.numpy.org/>`_
 - `MNE-Python <https://mne.tools/stable/index.html>`_
 - `Paramiko==3.5.0 <https://mne.tools/stable/index.html>`_