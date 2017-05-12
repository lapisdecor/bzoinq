.. highlight:: shell

============
Installation
============

Dependencies
------------

This package has only been tested on Ubuntu Linux. In order for the sounds
to work you must install the pyaudio dependencies.

.. code-block:: console

    $ sudo apt install portaudio19-dev python-all-dev python-pyaudio python3-pyaudio


Stable release
--------------

To install bzoinq, run this command in your terminal:

.. code-block:: console

    $ pip3 install bzoinq

This is the preferred method to install bzoinq, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for bzoinq can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/lapisdecor/bzoinq

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/lapisdecor/bzoinq/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/lapisdecor/bzoinq
.. _tarball: https://github.com/lapisdecor/bzoinq/tarball/master
