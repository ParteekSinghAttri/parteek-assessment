import os
from unittest import TestCase

import main


class Test(TestCase):

    def test_parse_xml(self):
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
            actual = main.parse_xml(test_file)
            expected = "http://firds.esma.europa.eu/firds/DLTINS_20210117_01of01.zip"

            assert expected == actual

        finally:
            # test clean up
            os.remove(test_file)