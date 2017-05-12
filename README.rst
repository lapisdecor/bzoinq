===============================
bzoinq
===============================


.. image:: https://img.shields.io/pypi/v/bzoinq.svg
      :target: https://pypi.python.org/pypi/bzoinq
      :alt: Pypi


.. image:: https://img.shields.io/travis/lapisdecor/bzoinq.svg
      :target: https://travis-ci.org/lapisdecor/bzoinq
      :alt: Travis CI


.. image:: https://readthedocs.org/projects/bzoinq/badge/?version=latest
      :target: https://bzoinq.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status


.. image:: https://pyup.io/repos/github/lapisdecor/bzoinq/shield.svg
      :target: https://pyup.io/repos/github/lapisdecor/bzoinq/
      :alt: Updates


Run a task and/or play a sound alarm at a given datetime



* Free software: MIT license
* Documentation: https://bzoinq.readthedocs.io.


Features
--------

* Create tasks that run functions and/or play a sound alarm
* Bzoinq object is like a task list
* Monitor object has it's own thread and watches for new tasks and sorts tasks
according to task alarm time
* Tasks will load automatically when you start your program but you must save
 your tasks when you exit.


Dependencies
------------

This package has only been tested on Ubuntu Linux. In order for the sounds
to work you must install the Linux pyaudio dependencies.

.. code-block:: console

    $ sudo apt install portaudio19-dev python-all-dev python-pyaudio python3-pyaudio

Credits
---------
Bzoinq is by Luis Louro and contributers are welcome
