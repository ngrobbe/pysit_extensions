.. _install_guide:

************
Installation
************

Dependencies
============

The PySIT extensions example has the following dependencies:

- Python 2.7 (May work with Python 3.X, but is not explicitely compatible)
- PySIT 0.5 (or greater)

Installing Python, PySIT, and  Dependencies
===========================================

See `http://pysit.readthedocs.org/en/latest/install.html
<http://pysit.readthedocs.org/en/latest/install.html>`_

Installing PySIT Extensions: Example
====================================

Installing from source
----------------------

PySIT extensions may use C++ extensions, so you will need a functioning C++
compiler to install from source.  For Windows users, if you are using one of
the pre-built scientific Python distributions, one should be included,
otherwise you will need to install an approprate version of MinGW.  MacOS X
users will need to install XCode.

From Mercurial (hg) clone
>>>>>>>>>>>>>>>>>>>>>>>>>

This is the recommended way to install from source, as it will make it easiest
to keep up with the latest bug fixes.

.. note::

	If you are planning on developing for PySIT, please see the :ref:`dev_guide`.

.. note::

	This section assumes that you have a version of `Mercurial (hg)
	<http://mercurial.selenic.com/>`_ installed for your operating system. 
	Mercurial is a distributed version control system (DVCS).  For an
	introduction to Mercurial and DVCS, see `hginit <http://www.hginit.com>`_.


1. Clone the PySIT extensions example from the master repository, hosted on `bitbucket.org
   <http://www.bitbucket.org>`_::

	hg clone https://bitbucket.org/pysit/pysit_extensions-example

2. From the root of directory of your PySIT Extensions Example clone, run::

	python setup.py install
