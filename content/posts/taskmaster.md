title: Taskmaster
slug: Taskmaster
tags: 42, shell, C, Unix, job-control, daemon, termcaps, python
date: 2019-04-02
modified: 2019-02-02
sortorder: 115

_Tasks Supervisor_

@42Born2Code

In this 42 project we were asked to create a basic version of [supervisor](https://github.com/Supervisor/supervisor).
We were restricted to our language of choice's standard library. Except for the config file parsing.

The script reads the tasks parameters from the yaml file, and executes some kind of user prompt to effectively manage these tasks.

The only argument needed is a config file.
All info about making your own config file is in exampleconfig.yaml.

Partners in this project -> [@toshuomj](https://github.com/toshuomj)

<img src="/images/Taskmaster01.gif" alt="Taskmaster01" width="700"/>

To launch the script, you just need to either:

``` zsh
$/> python3 taskmaster.py config_files/<yourconfig>.yaml
```

or

``` zsh
$/> ./taskmaster.py config_files/<yourconfig>.yaml
```

dependencies: yaml


[Try it on Github!](https://github.com/abguimba/42-taskmaster)

[42sh subject](PDFs/42-taskmaster.en.pdf)

[Norminette subject](https://github.com/Binary-Hackers/42_Subjects/blob/master/04_Norme/norme_2_0_1.pdf)

[Every 42 subject](https://github.com/agavrel/42_Subjects)
