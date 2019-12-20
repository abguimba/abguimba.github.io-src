title: Taskmaster
slug: Taskmaster
tags: 42, shell, C, Unix, job-control, daemon, termcaps, python
date: 2019-04-02
modified: 2019-02-02
sortorder: 115

_Tasks Supervisor_

@42Born2Code

In this 42 project we were asked to create a basic version of [supervisor](https://github.com/Supervisor/supervisor).

Basic task manager that reads from a config.json file and supervises a number of processes.
We were restricted to our language of choice’s standard library. Except for the config file parsing.

The script reads the tasks parameters from the json file, and executes some kind of user prompt to effectively manage these tasks.

The only argument needed is a config file. All info about making your own config file is in exampleconfig.json.

## Project partners

- [Abraham Gimbao](https://github.com/abguimba)
- [Marc Jose](https://github.com/mjose-portfolio)

## Install

- Not needed.

## Configuration

- Create a file in json format with the following characteristics:

<img src="/images/Taskmaster05.png" alt="Taskmaster05" width="700"/>

## Launching method

- `python3 taskmaster.py config_files/<yourconfig>.json`

## Commands

- `help`: List available commands with "help" or detailed help with "help cmd".
- `help <command>`: Prints the description and the method of use of the command.
- `start <program>`: Starts desired program(s). Usage -> start <program name(s)>
- `stop <program>`: Stops desired program(s). Usage -> stop <program name(s)>
- `restart <program>`: Restarts desired program(s) that has already been launched. Usage -> restart <program name(s)>
- `reload`: Reloads the whole configuration. Usage -> reload
- `display`: Opens a window that shows the pre-loaded configuration and the status of the programs to be monitored.

## Examples

<img src="/images/Taskmaster01.gif" alt="Taskmaster01" width="700"/>
<img src="/images/Taskmaster02.gif" alt="Taskmaster02" width="700"/>
<img src="/images/Taskmaster03.gif" alt="Taskmaster03" width="700"/>
<img src="/images/Taskmaster04.gif" alt="Taskmaster04" width="700"/>

[Try it on Github!](https://github.com/abguimba/42-taskmaster)

[42sh subject](PDFs/42-taskmaster.en.pdf)

[Norminette subject](https://github.com/Binary-Hackers/42_Subjects/blob/master/04_Norme/norme_2_0_1.pdf)

[Every 42 subject](https://github.com/agavrel/42_Subjects)
