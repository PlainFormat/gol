# Gol
Command line tool for Chronolog.

## Install

```
pip install .
```

## Usage

Append today's heading to the start of the chronolog file.

```bash
touch mylog.md                            # Create testing chronolog file.
gol act mylog.md -m 'My first activity.'  # Log my activity.
gol act mylog.md -m 'My second activity.' # Log next activity.
gol head mylog.md                         # Close my today's log.
```

Result:
```
## 2017-01-18
* 16.02: My second activity.
* 15.55: My first activity.
```
