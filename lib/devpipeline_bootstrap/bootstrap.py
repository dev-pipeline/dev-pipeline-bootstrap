#!/usr/bin/python3
"""This module does a checkout and build of the packages given in the config file."""
import devpipeline_core.command

import devpipeline_build.builder
import devpipeline_scm.scm


def main(args=None):
    # pylint: disable=bad-continuation,missing-docstring
    builder = devpipeline_core.command.make_command([
        devpipeline_scm.scm.scm_task,
        devpipeline_build.builder.build_task
    ],
        prog="dev-pipeline bootstrap",
        description="Checkout and build packages")
    devpipeline_core.command.execute_command(builder, args)


if __name__ == '__main__':
    main()
