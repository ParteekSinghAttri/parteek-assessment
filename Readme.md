# parteek-assessment

TODO description

### Sample run

Please see the logs for sample run.

```commandline
C:\Users\Parteek\PycharmProjects\assessment\venv\Scripts\python.exe C:/Users/Parteek/PycharmProjects/assessment/main.py
INFO:__main__:Start processing from url: https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100
INFO:__main__:Step 1: Download the xml from the link
INFO:__main__:File downloaded: step1_downloaded.xml
INFO:__main__:Step 2: From the xml, please parse through to the first download link whose file_type is DLTINS
INFO:__main__:URL for download: http://firds.esma.europa.eu/firds/DLTINS_20210117_01of01.zip
INFO:__main__:Step 2: and download the zip
INFO:__main__:Downloaded ZIP: step2_downloaded.zip
INFO:__main__:Step 3 Extract the xml from the zip
INFO:__main__:Extracted XML: step3_extracted.xml
INFO:__main__:Step 4 Convert the contents of the xml into a CSV
INFO:__main__:Converted CSV: step4_csv_file.csv
INFO:__main__:Step 5 Store the csv from step 4) in an AWS S3 bucket
INFO:botocore.credentials:Found credentials in environment variables.
INFO:__main__:File uploaded. S3 link: https://parteek-assessment.s3.amazonaws.com/extracted.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWZO76XEUNAFSAPE7%2F20220321%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220321T073705Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=4b491588295b450b2837b05975414a7e20fc67b4571134bb88f1bc6b13e3e306
```

Please see the processed file [here](https://parteek-assessment.s3.amazonaws.com/extracted.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWZO76XEUNAFSAPE7%2F20220321%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220321T073705Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=4b491588295b450b2837b05975414a7e20fc67b4571134bb88f1bc6b13e3e306).

Please see the logs for sample test run

```commandline
C:\Users\Parteek\PycharmProjects\assessment\venv\Scripts\python.exe F:\Installed\JetBrains\Toolbox\apps\PyCharm-C\ch-0\212.5457.59\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py --target main.py::test
Testing started at 13:26 ...
Launching pytest with arguments main.py::test in C:\Users\Parteek\PycharmProjects\assessment

============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-3.10.1, py-1.11.0, pluggy-1.0.0 -- C:\Users\Parteek\PycharmProjects\assessment\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Parteek\PycharmProjects\assessment, inifile:
plugins: cov-2.9.0, mock-1.13.0, xdoctest-0.9.1
collecting ... collected 1 item

main.py::test PASSED                                                     [100%]

========================== 1 passed in 0.31 seconds ===========================

Process finished with exit code 0
```