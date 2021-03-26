# Powershell Commands

* Switch to ENV folder: cd Env:
* List all env variables: get-item -path Env:
* List all user env variables: get-item -path Env:user*
* Get an environment variable value: (get-item -path Env:<variablename>).Value
* Create an env variable: Set-Item -Path Env:<variablename> -Value "<variablevalue>"
    * if <variablevalue> is '' then it deletes the environment variable
    * can also use the shortcut $env:<variablename> = "<variablevalue>"
    * 