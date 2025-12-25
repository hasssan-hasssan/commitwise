CommitWise
===========

CommitWise is a smart and simple tool for generating clean Git commit messages.
It can create commit messages from a text file or using AI models.

With CommitWise, your commits are always:
- Clean and readable
- Following Git best practices
- Well-structured and informative

Features
--------

- Generate commits from text files, preserving exact formatting, spacing, and paragraphs
- Generate commits using AI (local with Ollama or OpenAI API)
- Simple and easy-to-use CLI with only a few flags
- Works seamlessly in any Git project

Installation
------------

pip install commitwise

Usage
-----

Generate commit from AI (local or OpenAI):
commitwise --ai

Generate commit from a text file:
commitwise --file ./my_commit.txt

Show help:
commitwise --help

Requirements
------------

- Python >= 3.9
- For local AI: Ollama installed and the desired model downloaded
- For online AI: OpenAI API Key (if using OpenAI)

Professional Note
-----------------

CommitWise ensures that AI-generated commit messages are clean and Git-ready,
without extra explanations, markdown, or educational text.
This is guaranteed through strict prompting and output cleaning.

Links
-----

GitHub Repository: https://github.com/hasssan-hasssan/commitwise

PyPI: https://pypi.org/project/commitwise

Support
-------

If CommitWise is helpful, please give it a star on GitHub so others can find it!

GitHub About Section
-------------------

CommitWise: Generate clean Git commit messages from files or AI.

Supports local AI (Ollama) or OpenAI API for automatic commit generation.

Simple CLI with --ai and --file modes.

