# First Steps for installing and using the software

This guide will walk you through the steps to install and use the `Notes2LaTeX` software.

## Clone this repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/lealmilton/notes2latex.git
```

## Create a virtual environment `venv`
On your local machine, create a virtual environment `venv` using the following command:

```bash
python3 -m venv venv
```

After creating the virtual environment, activate it using the following command:

```bash
venv\Scrips\activate
```

## Poppler

Poppler is a PDF rendering library that is used by the `Notes2LaTeX` software to convert PDFs to images. To install Poppler, follow the instructions for your operating system below.

> **Note**: These must be well handled in the future. For now, we will use the `poppler` folder in the repository.

Download the latest version of Poppler from this [Github repo](https://github.com/oschwartz10612/poppler-windows/releases/tag/v23.11.0-0). Extract the contents of the zip file to the `venv`, which should be organized as the following representation:

```bash
venv
├───Include
|	└───...
├───Lib
|	└───...
├───poppler-23.11.0
│	└───...
├───Scripts
|	└───...
└───pyenv.cfg
```

## Install the required packages
...

## Create the `OPENAI_API_KEY` ambient variable

On your ambient variables, create a new variable named `OPENAI_API_KEY` and set its value to your OpenAI API key.