## OATS report

This sample project will connect to the FlexNOW API and generate an OATS report. The examples below should all be run on a Unix filesystem with a bash shell.

### Setup

Python 3.7 is required (`python3 --version` should display the version).

In the root of the project, install the requirements:

```console
$ pip3 install -r requirements.txt

```

### Inputs

* A broker configuration file which contains a map of FlexNOW broker names to MPID/destination codes. See [example.broker.ini](example.broker.ini) for an example.
* An environment variable `FLEXNOW_API_CLIENT_ID` which contains your FlexNOW-provided client ID.
* An environment variable `FLEXNOW_API_SECRET_TOKEN` which contains your FlexNOW-provided secret API token.
* (optionally) an environment variable `FLEXNOW_API_BASE_URL` which will specify the address of the API. This defaults to the UAT V3 API, https://flexnow-uat.eu.flextrade.com/api/v3.

### Usage

Export environments and run the script from the shell:

```console
$ export FLEXNOW_API_CLIENT_ID="your-client-id"
$ export FLEXNOW_API_SECRET_TOKEN="your-secret-token"
$ export FLEXNOW_API_BASE_URL="https://flexnow-uat.eu.flextrade.com/api/v3" # (default)

$ ./create_oats_report.py
```

### Output

A csv file `oats_report.csv` containing the current day's orders in OATS format.
```
#OE#,RT,N,,,,BROC,parent-order-tag-60,parent-order-tag-11,FNBA,AMUB000-20200807,VOD LN Equity,2020-08-07T13:46:56.325972,100.0,E,,,M,L,,,,,,
#OE#,RT,N,,,,BROC,parent-order-tag-60,parent-order-tag-11,FNBB,AR2I000-20200807,BARC LN Equity,2020-08-07T13:56:04.240544,450000.0,E,,,M,L,,,,,,
```
