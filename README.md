CommitWise
===========
CommitWise is a smart and simple tool for generating clean Git commit messages.
It can create commit messages from a text file or using AI models.

**With CommitWise, your commits are always:**
- **Clean and readable**
- **Following Git best practices**
- **Well-structured and informative**
<br>

Features
--------
- Generate commits from text files, preserving exact formatting, spacing, and paragraphs

- Generate commits using AI (local with Ollama or OpenAI API)

- Simple and easy-to-use CLI with only a few flags

- Works seamlessly in any Git project
<br>

Requirements
------------
- Python >= **`3.9`**

- For local AI : **`Ollama`** installed and the desired model downloaded

- For online AI : **`OpenAI API Key`** (if using OpenAI)
<br>

Installation
------------
```
$> pip install commitwise
```
<br>

AI Configuration
----------------
CommitWise supports two AI modes:
- Local AI using Ollama (recommended)

- OpenAI API

**You only need to configure ONE of them**.

<br>

>Local AI (Ollama)
>----------------
>
>1. Install Ollama:
>   https://ollama.com
>
>2. Download a model :
>    ```
>    $> ollama pull llama3
>    ```
>
>3. Make sure Ollama is running:
>    ```
>    $> ollama serve
>    ```
>
>CommitWise will automatically detect Ollama at :
> `http://localhost:11434`
>
>**No additional configuration is required.**

<br>

>OpenAI Configuration
>--------------------
>
>- If you prefer using OpenAI instead of local AI, set your `API-KEY` as an environment variable.
>
>   - Windows :
>       ``` 
>        $> setx OPENAI_API_KEY "your_api_key_here"
>       ```
>
>   - Linux / macOS :
>       ```
>       $> export OPENAI_API_KEY="your_api_key_here"
>       ```
>
>**CommitWise will automatically use OpenAI when the API key is available.**

<br>

Usage
-----
Generate commit from AI (local or OpenAI):
```
$> commitwise --ai
```

Generate commit from a text file:
```
$> commitwise --file ./my_commit.txt
```

Show help:
```
$> commitwise --help
```

<br>

Professional Note
-----------------
CommitWise ensures that AI-generated commit messages are clean and Git-ready,
without extra explanations, markdown, or educational text.
This is guaranteed through strict prompting and output cleaning.

<br>

Links
-----

[GitHub](https://github.com/hasssan-hasssan/commitwise "GitHub repository") | 
[PyPi](https://pypi.org/project/commitwise)

<br>

Support
-------
If CommitWise is helpful, please give it a star on [GitHub](https://github.com/hasssan-hasssan/commitwise "GitHub repository") so others can find it!

<br>