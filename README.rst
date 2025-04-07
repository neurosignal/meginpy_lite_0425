.. -* mode: rst -*-
================
meginpy_lite_0425
================

A module to convert string type digitization into extra type headshape points.

How to use
===========

There are two ways to use the module: i) by installing, ii) adding it to your script

i) Installation
------------

Download the software:

.. code-block:: bash

    git clone https://github.com/neurosignal/meginpy_lite_0425.git

Get into directory:

.. code-block:: bash

    cd meginpy_lite_0425

Install it:

.. code-block:: bash

    python setup.py install

ii) Adding the path into you script

.. code-block:: bash

    import sys
    sys.path.append(..../meginpy_lite_0425/)
    from digitization import string2extra
    
Run to check and install all dependencies for the pseudo-MRI engine:

.. code-block:: bash

    pip install -r requirements.txt

Check the installation: 

.. code-block:: bash

    python pseudoMRI_engine.py --help