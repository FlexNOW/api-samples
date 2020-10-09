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

A csv file `execution_report.csv` containing the current day's executions, one per line.
```
parent_load_time,parent_client_order_id,parent_notes,street_id,street_symbol,street_load_time,street_size,exec_id,exec_size,exec_price,exec_last_market,exec_transaction_time
2020-09-14T10:04:14.15Z,12345,BCDF2U6-20201001,notes,OEZ0 Comdty,2020-09-14T11:14:37.874416,2.0,execid02394,2,135.0,XEUR,2020-10-01T12:37:33
2020-09-14T10:04:14.15Z,12346,AABB2U6-20201001,note2,OEZ0 Comdty,2020-09-14T11:14:37.874416,2.0,execid390342,0,0.0,XEUR,2020-10-01T12:33:27
2020-09-14T10:04:14.15Z,12347,BBCC2U7-20201001,note3,OEZ0 Comdty,2020-09-14T11:14:50.948208,2.0,execid1234,0,0.0,XEUR,2020-10-01T11:14:52.64
```