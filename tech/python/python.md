# Python

## Installing Dependencies
* pip directly
  * install via pip: **py -m pip install <library>**
    * pip comes packaged with python by default after python version 3.4
  * upgrade via pip: **py -m pip install --upgrade <library>**
* requirements.txt
  * install from requirements.txt: **py -m pip install -r requirements.txt**
  * if you want to create a requirements.txt for a project that already has dependencies installed: **pip freeze > requirements.txt**
* pipenv
  * manage dependencies using 'pipenv': **py -m pip install --user pipenv**
    * if pipenv isnt avail after installation, need to add [user base's](https://docs.python.org/3/library/site.html#site.USER_BASE) binary directory to **PATH**
  * install via pipenv: **pipenv install <library>**
    * this installs the library and creates a Pipfile in project's root directory.
* poetry
  * install via powershell: 
  ```
  (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
  ```
  * configuration:
    * in a new project: **poetry new <project name>**
    * in an existing project: **poetry init**
    * updating [configuration](https://python-poetry.org/docs/configuration/): **poetry config <config var> <config var value [--local]**
      * poetry, by default, creates virtual env in {cache-dir}/virtualenvs.  
        * cache-dir on windows: C:\Users\<username>\AppData\Local\pypoetry\Cache
      * config var: **cache-dir=<string file location>** in config.toml file to set it to a different location
      * config var: **virtualenvs.in-project=true** in config.toml to create virtual env in project root directory in a folder named **.venv**
      * if "--local" is used, then it creates a local config file named "poetry.toml" that stores configuration overrides
    * view current configuration: **poetry config --list**        
  * "pyproject.toml" file for dependency list
  * adding dependencies: 
    * add them to tool.poetry.dependencies section of pyproject.toml file
    * use **poetry add <library>**  
  * has two types of dependencies: production and development
  * "poetry.lock" should be in source control as it contains locked dependency versions
* running: **poetry run python <script>.py**
* running tests: **poetry run pytest**

## Virtual Environments
* virtual environments allow packages to be in an isolated location for a particular application rather than installed globally (i.e. node_modules folder)
* create: py -m venv <name of env>
  * this creates a subdirectory of the name of env chosen.  
  * It configures the current shell to use that venv as the default python environment
* configure shell for a project with an existing venv by running the "activate" script: <name of env in project directory>\Scripts\activate

