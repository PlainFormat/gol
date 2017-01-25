# Gol
Command line tool for Chronolog.

## Install

```
pip install .
```

## Usage

Append today's heading to the start of the chronolog file.

```bash
gol init                                  # Create empty chronolog file in current folder.
gol act  -m 'My first activity.'          # Log my activity.
gol act  -m 'My second activity.'         # Log next activity.
gol head                                  # Close my today's log.
```

Result (content of 'chronolog.md'):
```

## 2017-01-18
* 16.02: My second activity.
* 15.55: My first activity.
```

### Global and local config

There are two ways how to specify `gol` output file.

1. Firstly `.gol/config.yaml` file is searched in folder where `gol` command is called.
It enabels you to edit multiple separated chronolog files using `gol`.
2. Secondly `~/.golconfig.yaml` file is searched when there is no local config.
It enables you to access your 'global' chronolog file from any location.
