## Execution report

This sample project will connect to the FlexNOW API and generate a report containing all of the current day's executions. The examples below should all be run on a Unix filesystem with a bash shell.

### Setup

Python 3 is required (`python3 --version` should display the version).

In the root of the project, install the requirements:

```console
$ pip3 install -r requirements.txt

```

### Inputs

* An environment variable `FLEXNOW_API_CLIENT_ID` which contains your FlexNOW-provided client ID.
* An environment variable `FLEXNOW_API_SECRET_TOKEN` which contains your FlexNOW-provided secret API token.
* (optionally) an environment variable `FLEXNOW_API_BASE_URL` which will specify the address of the API. This defaults to the UAT V3 API, https://flexnow-uat.eu.flextrade.com/api/v3.

### Usage

Export environments and run the script from the shell:

```console
$ export FLEXNOW_API_CLIENT_ID="your-client-id"
$ export FLEXNOW_API_SECRET_TOKEN="your-secret-token"
$ export FLEXNOW_API_BASE_URL="https://flexnow-uat.eu.flextrade.com/api/v3" # (default)

$ ./create_execution_report.py
```

### Output

A csv file `create_execution_report.csv` containing the current day's orders in OATS format.
```
```