# parteek-assessment

Python Engineer Assessment Test for steel-eye

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
INFO:__main__:Step 3: Extract the xml from the zip
INFO:__main__:Extracted XML: step3_extracted.xml
INFO:__main__:Step 4: Convert the contents of the xml into a CSV
INFO:__main__:Converted CSV: step4_csv_file.csv
INFO:__main__:Step 5: Store the csv from step 4) in an AWS S3 bucket
INFO:botocore.credentials:Found credentials in environment variables.
INFO:__main__:File uploaded. S3 link: https://parteek-assessment.s3.amazonaws.com/extracted.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWZO76XEUNAFSAPE7%2F20220321%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220321T073705Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=4b491588295b450b2837b05975414a7e20fc67b4571134bb88f1bc6b13e3e306
```

Please see the processed file [here (valid for 7 days)](https://parteek-assessment.s3.eu-west-2.amazonaws.com/extracted.csv?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCmFwLXNvdXRoLTEiSDBGAiEA50PKQnqhkBWnq7OgF%2B956xjQWGBvGCK4WzFITfpOntwCIQDTza%2BlRvp35tlm80UdMpLZ8NxTUXsMM8J1szcv7nKj8yr7AggUEAIaDDQ2NzAxMDUwMDkwNCIMIfFh0rWLLfQKa9ERKtgCFY4Db9NHzra2c5JSHgMtvc5L6%2Bc3e4S7pAUZhyQuyXYzy103gGgv%2FMg6fkMYbbkH%2BkBUbjz7KjieFdiLKgjCaSBInVISo3eEvOK2HpfPhUAKswcYaRtmXUfLITdsAV49GlOKf1E43We2P1oKty7TrtGN%2BlnxGraej2CADpynZK557DkAfsMWihcCr3XyH3C1IokePSAi9qSH3IUavWO%2BxBLqDNu68fowWShPf5sV8Wr3lNXMLninVmqDkFJYckxR1F67064ISj81a0KbDeX6Z0vudsHtuzsCgdvzcY4g8TgdEJ0%2BD1L9wb8NPaKG%2FBS0Xrnd4acXH3gRsiA1%2Fr2238cHbWLnxRZMwpLT%2FhkV1PG7ClIkVAy52CdjGnGY19a8yhp%2BlRKCCOh82XakwISW7hEvShcZ5oKSjViIDUSIQ99%2Fd%2BYzJDP5aju%2FHZsrCABaTCNzeEg%2BPIIw1q7hkQY6sgKdOz6ZLx1Lq7p3TrVWOpG2CFm0prPuXpzDyWUssUanEumNyjhmjvgbk%2BA3h6QaYD2jGKdi%2BQEYDrDp6Iht9MC%2F6UnpzkrXD4uj4bt87AXPSLRfq%2ByWY9%2BUs2n1bl0gf5r7qT2KOJf52yRU2d5XfHX5vCup5bUSMoMmH0ehwEPa2TmOXSYkzrArJ%2BpGIItLPSED%2Bg04PY1FgcJF6TCYPGyniGCgoepLo89yCYYVSWvXX0g6aW7jAE0S31DxoNo1%2BrzsCIsfysgMbI3cFpbNl9x1JTRer6QSV1stQOdgnJbn1fwX1tQA%2Fs3y%2FLSOWXdPP%2FuGSjBtn1VqZUxAxe2hXnX1gY6NigOb8Qz1%2FgoGMAwZwxohiTsDptvH63cgIIDvmRvkmqo3q%2FmYWF%2FBe31gDVeVHoQ%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220321T104624Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604800&X-Amz-Credential=ASIAWZO76XEUOTYY4GRZ%2F20220321%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Signature=1a7dd2ba982d63993eab2a410b39dd891c3af980ae1dc589033039c6706e83e6).

Please see the logs for sample test run

```commandline
C:\Users\Parteek\PycharmProjects\assessment\venv\Scripts\python.exe F:\Installed\JetBrains\Toolbox\apps\PyCharm-C\ch-0\212.5457.59\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py --target test_main.py::Test.test_parse_xml
Testing started at 15:57 ...
Launching pytest with arguments test_main.py::Test::test_parse_xml in C:\Users\Parteek\PycharmProjects\assessment

============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-3.10.1, py-1.11.0, pluggy-1.0.0 -- C:\Users\Parteek\PycharmProjects\assessment\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Parteek\PycharmProjects\assessment, inifile:
plugins: cov-2.9.0, mock-1.13.0, xdoctest-0.9.1
collecting ... collected 1 item

test_main.py::Test::test_parse_xml PASSED                                [100%]

========================== 1 passed in 0.31 seconds ===========================

Process finished with exit code 0
```