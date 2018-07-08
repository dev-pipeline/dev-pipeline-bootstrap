bootstrap
=========

Synopsis
--------
::

    dev-pipeline bootstrap [-h] [--dependencies DEPENDENCIES]
                           [--executor EXECUTOR]
                           [targets [targets ...]]


Description
-----------
This tool checks out and builds packages in a configuration with proper
dependency ordering.  The result is similar to running
:code:`dev-pipeline checkout` followed by :code:`dev-pipeline build`, but the
steps are mixed instead of performing all checkouts followed by all builds.

If no targets are specified, all targets will be used.


Options
-------
  -h, --help            show this help message and exit
  --dependencies DEPENDENCIES
                        Control how build dependencies are handled. (default:
                        deep)
  --executor EXECUTOR   The method to execute commands. (default: quiet)


Config Options
--------------
No extra options are consumed.
