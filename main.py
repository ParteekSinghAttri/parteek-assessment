# importing the required modules
import csv
import logging
import os
import xml.etree.ElementTree as ET
import zipfile

import boto3
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(solr_url):

    logger.info("Step 1: Download the xml from the link")
    downloaded_xml = download_xml(solr_url)
    logger.info('File downloaded: %s', downloaded_xml)

    logger.info("Step 2: From the xml, please parse through to the first download link whose file_type is DLTINS")
    url_to_download = parse_xml(downloaded_xml)
    logger.info('URL for download: %s', url_to_download)

    logger.info("Step 2: and download the zip")
    downloaded_zip = download_zip(url_to_download)
    logger.info('Downloaded ZIP: %s', downloaded_zip)

    logger.info("Step 3 Extract the xml from the zip")
    extracted_xml = extract_zip(downloaded_zip)
    logger.info('Extracted XML: %s', extracted_xml)

    logger.info("Step 4 Convert the contents of the xml into a CSV")
    csv_file = xml_to_csv(extracted_xml)
    logger.info('Converted CSV: %s', csv_file)

    logger.info("Step 5 Store the csv from step 4) in an AWS S3 bucket")
    s3_link = upload_to_s3(csv_file)
    logger.info('File uploaded. S3 link: %s', s3_link)


def extract_zip(file_path):
    extracted_xml = 'step3_extracted.xml'

    with zipfile.ZipFile(file_path, 'r') as zf:
        for name in zf.namelist():
            if 'xml' in name:
                f = zf.open(name)
                with open(extracted_xml, 'wb') as out:
                    out.write(f.read())

    return extracted_xml


def download_xml(xml_url):
    # creating HTTP response object from given url
    resp = requests.get(xml_url)

    downloaded_xml = "step1_downloaded.xml"
    # saving the xml file
    with open(downloaded_xml, 'wb') as f:
        f.write(resp.content)

    return downloaded_xml


def download_zip(zip_url):
    # creating HTTP response object from given url
    r = requests.get(zip_url, stream=True)

    downloaded_zip = "step2_downloaded.zip"

    # saving the zip file
    with open(downloaded_zip, "wb") as zip_file:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to pdf file
            if chunk:
                zip_file.write(chunk)
    return downloaded_zip


def parse_xml(xml_file):
    # create element tree object
    tree = ET.parse(xml_file)

    # get the result element
    result = list(tree.iter('result'))[0]

    found = False
    url_to_download = ""
    for doc in result:
        for child in doc:
            if child.get("name") == "file_type" and child.text == "DLTINS":
                found = True
            if child.get("name") == "download_link":
                url_to_download = child.text

        # find the first element
        if found:
            break

    if found:
        return url_to_download

    raise Exception("Didn't find any DLTINS file type")


def xml_to_csv(xml_file):
    csv_file = "step4_csv_file.csv"

    # parse XML
    xml = ET.parse(xml_file)

    # create CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:

        csvfile_writer = csv.writer(csvfile)

        # add the header to csv file
        csvfile_writer.writerow([
            'FinInstrmGnlAttrbts.Id',
            'FinInstrmGnlAttrbts.FullNm',
            'FinInstrmGnlAttrbts.ClssfctnTp',
            'FinInstrmGnlAttrbts.CmmdtyDerivInd',
            'FinInstrmGnlAttrbts.NtnlCcy',
            'Issr',
        ])

        path = "./{urn:iso:std:iso:20022:tech:xsd:head.003.001.01}Pyld/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Document/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrmRptgRefDataDltaRpt/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrm/"

        for termntd_rcrd in xml.findall(path):

            if termntd_rcrd:
                # extract details
                fin_instrm_gnl_attrbts = termntd_rcrd.find(
                    "./{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrmGnlAttrbts")
                issr = termntd_rcrd.find("./{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Issr")
                csv_line = [
                    fin_instrm_gnl_attrbts.find('{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Id').text,
                    fin_instrm_gnl_attrbts.find('{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FullNm').text,
                    fin_instrm_gnl_attrbts.find('{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}ClssfctnTp').text,
                    fin_instrm_gnl_attrbts.find('{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}CmmdtyDerivInd').text,
                    fin_instrm_gnl_attrbts.find('{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}NtnlCcy').text,
                    issr.text
                ]

                # add a new row to CSV file
                csvfile_writer.writerow(csv_line)

    return csv_file


def upload_to_s3(csv_file):
    s3 = boto3.client("s3")

    bucket = 'parteek-assessment'
    filename = 'extracted.csv'

    s3.upload_file(
        Filename=csv_file,
        Bucket=bucket,
        Key=filename,
    )

    return s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': filename
        }
    )


if __name__ == "__main__":
    # calling main function

    url = """https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"""
    logger.info('Start processing from url: %s', url)
    main(url)


def test():
    # test setup
    test_file = '.temp-test.xml'
    try:
        dom = ("""<?xml version="1.0" encoding="UTF-8"?>
    <response>
    
    <lst name="responseHeader">
      <int name="status">0</int>
      <int name="QTime">0</int>
      <lst name="params">
        <str name="q">*</str>
        <str name="indent">true</str>
        <str name="start">0</str>
        <str name="fq">publication_date:[2021-01-17T00:00:00Z TO 2021-01-19T23:59:59Z]</str>
        <str name="rows">100</str>
        <str name="wt">xml</str>
      </lst>
    </lst>
    <result name="response" numFound="4" start="0">
      <doc>
        <str name="checksum">852b2dde71cf114289ad95ada2a4e406</str>
        <str name="download_link">http://firds.esma.europa.eu/firds/DLTINS_20210117_01of01.zip</str>
        <date name="publication_date">2021-01-17T00:00:00Z</date>
        <str name="published_instrument_file_id">46015</str>
        <str name="id">46015</str>
        <str name="_root_">46015</str>
        <str name="file_name">DLTINS_20210117_01of01.zip</str>
        <str name="file_type">DLTINS</str>
        <long name="_version_">1727871449962643484</long>
        <date name="timestamp">2022-03-21T01:37:03.881Z</date></doc>
      <doc>
        <str name="checksum">3533fe597fc721ed139198503fe87910</str>
        <str name="download_link">http://firds.esma.europa.eu/firds/DLTINS_20210119_01of02.zip</str>
        <date name="publication_date">2021-01-19T00:00:00Z</date>
        <str name="published_instrument_file_id">46051</str>
        <str name="id">46051</str>
        <str name="_root_">46051</str>
        <str name="file_name">DLTINS_20210119_01of02.zip</str>
        <str name="file_type">DLTINS</str>
        <long name="_version_">1727871449986760712</long>
        <date name="timestamp">2022-03-21T01:37:03.904Z</date></doc>
      <doc>
        <str name="checksum">4edec7a18a04a8a11c2735f4405acbaf</str>
        <str name="download_link">http://firds.esma.europa.eu/firds/DLTINS_20210119_02of02.zip</str>
        <date name="publication_date">2021-01-19T00:00:00Z</date>
        <str name="published_instrument_file_id">46052</str>
        <str name="id">46052</str>
        <str name="_root_">46052</str>
        <str name="file_name">DLTINS_20210119_02of02.zip</str>
        <str name="file_type">DLTINS</str>
        <long name="_version_">1727871449986760713</long>
        <date name="timestamp">2022-03-21T01:37:03.904Z</date></doc>
      <doc>
        <str name="checksum">f88a84bd2423c5016476577d2c2f4687</str>
        <str name="download_link">http://firds.esma.europa.eu/firds/DLTINS_20210118_01of01.zip</str>
        <date name="publication_date">2021-01-18T00:00:00Z</date>
        <str name="published_instrument_file_id">46032</str>
        <str name="id">46032</str>
        <str name="_root_">46032</str>
        <str name="file_name">DLTINS_20210118_01of01.zip</str>
        <str name="file_type">DLTINS</str>
        <long name="_version_">1727871450003537944</long>
        <date name="timestamp">2022-03-21T01:37:03.920Z</date></doc>
    </result>
    </response>
    """)

        with open(test_file, 'w') as f:
            f.write(dom)

        # test execution
        actual = parse_xml(test_file)
        expected = "http://firds.esma.europa.eu/firds/DLTINS_20210117_01of01.zip"

        assert expected == actual

    finally:
        # test clean up
        os.remove(test_file)
