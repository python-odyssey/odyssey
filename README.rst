🚣 ⛵ odyssey ⛵ 🚣
=====================

odyssey is a cross-platform cross-architecture cross-scm workspace management tool. It is designed from the ground up to support multi-repository workflows, and is easily extended to work with any scm or package management tool out there. Although odyssey is written in python, it will work for multi-repository projects in any programming language, even ones that use multiple languages.

*Even if it will take ten years, it will have been worth it.*

.. image:: https://img.shields.io/badge/platform-windows%20%7C%20osx%20%7C%20ubuntu%20%7C%20alpine-lightgrey
    :alt: Supported Platforms

.. image:: https://img.shields.io/badge/architecture-x86%20%7C%20amd64%20%7C%20arm64-lightgrey
    :alt: Supported CPU Architectures

.. image:: https://img.shields.io/github/v/release/python-odyssey/odyssey
    :target: https://github.com/python-odyssey/odyssey/releases
    :alt: GitHub Release

.. image:: https://img.shields.io/pypi/v/odyssey
    :target: https://pypi.org/project/odyssey/
    :alt: PyPI

.. image:: https://img.shields.io/travis/com/python-odyssey/odyssey/master?label=travis
    :target: https://travis-ci.com/python-odyssey/odyssey
    :alt: Travis

.. image:: https://img.shields.io/appveyor/build/GodwinneLorayne/odyssey/master?label=appveyor
    :target: https://ci.appveyor.com/project/GodwinneLorayne/odyssey
    :alt: AppVeyor

.. image:: https://img.shields.io/circleci/build/github/python-odyssey/odyssey/master?label=circleci
    :target: https://circleci.com/gh/python-odyssey/odyssey/tree/master
    :alt: CircleCI

.. image:: https://img.shields.io/github/workflow/status/python-odyssey/odyssey/Python%20package/master?label=github
    :target: https://github.com/python-odyssey/odyssey/actions?query=workflow%3A%22Python+package%22
    :alt: GitHub Workflow

.. image:: https://img.shields.io/codeship/9d611200-8038-0138-868a-7e7dbe13f4dd/master?label=codeship
    :target: https://app.codeship.com/projects/9d611200-8038-0138-868a-7e7dbe13f4dd
    :alt: Codeship

.. image:: https://readthedocs.org/projects/python-odyssey/badge/?version=latest
    :target: https://python-odyssey.readthedocs.io/en/latest/index.html
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://coveralls.io/repos/github/python-odyssey/odyssey/badge.svg?branch=master
    :target: https://coveralls.io/github/python-odyssey/odyssey?branch=master

.. image:: https://img.shields.io/github/languages/code-size/python-odyssey/odyssey
    :alt: GitHub code size in bytes

.. image:: https://img.shields.io/github/issues-raw/python-odyssey/odyssey
    :alt: GitHub issues

.. image:: https://img.shields.io/github/license/python-odyssey/odyssey
    :alt: GitHub

.. image:: https://img.shields.io/github/stars/python-odyssey/odyssey
    :alt: GitHub stars

.. image:: https://img.shields.io/discord/714011709794418698
    :target: https://discord.com/channels/714011709794418698

Problem Space
-------------

odyssey is the answer to the question "How can my project use multiple types of version control, where different types of files can be stored in the system most approproiate them?"

A practical use case from real-world experience: In the video game industry, projects have large amounts of both code and binary files. Projects can have tens, hundreds, or thousands of GBs of development assets and hundreds of thousands or even millions of lines of code. Most teams at present choose between git and perforce. This leads to all kinds of problems in either case. odyssey is built so that teams can choose to use git for their source files (code, documentation, scripts, asset manifests, etc.) and use perforce for their asset files (images, sounds, models, animations, etc.)

Goals
-----

Usefulness: odyssey should be useful to a wide variety of teams in a wide variety of industries. Both open source projects and enterprise projects should find something they love here.

Gradual Adoption: odyssey should not force an all or nothing scenario where only new teams can use it. Many teams have decades of effort invested in their existing setup, and they need to be able to adopt odyssey usage gradually for it to stand a chace of success.

Reproducibility: odyssey should make it easier to reproduce workflows for both developer workstations and build pipelines.

Speed: odyssey should execute as fast as possible, but no faster. You'll know it when you see it.

Related Tools
-------------

Yarn_: Yarn is a package manager that doubles down as project manager. Whether you work on one-shot projects or large monorepos, as a hobbyist or an enterprise user, we've got you covered.

.. _Yarn: https://yarnpkg.com/

Yarn has excellent design around reproducibility, and consequently is very useful to teams with a lot of investment on the line. Unfortunately yarn seems only designed for npm and git packages, and primarily supports monorepos.

meta_: meta is a tool for managing multi-project systems and libraries. It answers the conundrum of choosing between a mono repo or many repos by saying "both", with a meta repo!

.. _meta: https://www.npmjs.com/package/meta

meta seems really useful at the outset. It allows you to create a meta-repo, which allows sharing of workspaces. This is an essential feature. meta also has support for plugins which can extend its functionality in many ways. Unfortunately, at time of writing meta-repos are not recursive, meta itself cannot be distributed without node and npm, and the current meta design doesn't seem to leave room for perforce sub-repos.
