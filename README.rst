elevate
=======

I find it upsetting that so many Windows developers launch their Command Prompt as
Administrator out of habit, because so much Windows software falls over if you 
don't have admin rights. And yet there's no decent analogue to Unix's ``sudo``.

So I'm writing one. In Python. It's *very* rough around the edges at the moment, however.

Usage
-----

.. code::

    elevate cmd...


This will pop up a Windows UAC prompt, and proceed to launch ``cmd`` with elevated priviledges. 
Unlike the built-in ``runas.exe`` tool, you'll get ``cmd``'s standard output in the *current*
console window, instead of launching an extra cmd.exe window.
