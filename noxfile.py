# -*- coding: utf-8 -*-
"""Nox sessions

This module contains Nox sessions automating tasks and workflows.

Example:
    From the project's root, run:
        $ nox -s isort
        $ nox -s black

"""

import nox


@nox.session(python="3.11")
def isort(session):
    session.install("isort==5.12.0")
    session.run("isort", "src", "tests")


@nox.session(python="3.11")
def black(session):
    session.install("black==23.7.0")
    session.run("black", "src", "tests")
