#!/usr/bin/python3

"""
This module does a checkout and build of the packages given in the config file.
"""

import devpipeline_core.command
import devpipeline_configure.load

import devpipeline_build.builder
import devpipeline_scm.scm

_MAJOR = 0
_MINOR = 5
_PATCH = 0

_STRING = "{}.{}.{}".format(_MAJOR, _MINOR, _PATCH)


def _configure(parser):
    devpipeline_core.command.setup_task_parser(parser)
    devpipeline_core.command.add_version_info(parser, _STRING)


def _execute(arguments):
    devpipeline_core.command.process_tasks(
        arguments,
        [devpipeline_scm.scm.CHECKOUT_TASK, devpipeline_build.builder.BUILD_TASK],
        devpipeline_configure.load.update_cache,
    )


_BOOTSTRAP_COMMAND = (
    "Checkout and build a project.  This is most useful right after a fresh configure.",
    _configure,
    _execute,
)
