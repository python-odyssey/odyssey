#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Perforce application logic.
"""

import os
import io
import re
import shutil
from enum import Enum
import requests
import lxml.objectify
import semver

PERFORCE_FTP_ROOT = "https://cdist2.perforce.com"
PERFORCE_VERSION_PATH = PERFORCE_FTP_ROOT + "/perforce"
VERSION_REGEX = re.compile(r"r\d+.\d+")


def get_html_text(url) -> str:
    response = requests.get(url)
    return response.text


def html_from_text(html_text):
    html_parser = lxml.etree.HTMLParser()
    return lxml.etree.parse(io.StringIO(html_text), html_parser)


def get_table_in_html(html_etree):
    body_element = html_etree.find("body")
    return body_element.find("table")


class FTPItemType(Enum):
    Directory = 0
    File = 1


class FTPItem:
    def __init__(self, item_type, item_name):
        self.type = item_type
        self.name = item_name

    def __repr__(self):
        return f"({self.type},{self.name})"


def iter_items(table_element):
    for table_row in table_element.iterchildren():
        img_element = table_row.find("td/img")
        if (
            img_element is None
            or img_element.attrib is None
            or "alt" not in img_element.attrib
        ):
            continue

        alt = img_element.attrib["alt"]
        if alt not in ("[DIR]", "[   ]"):
            continue

        a_element = table_row.find("td/a")
        if (
            a_element is None
            or a_element.attrib is None
            or "href" not in a_element.attrib
        ):
            continue

        item_type = None
        if alt == "[DIR]":
            item_type = FTPItemType.Directory
        elif alt == "[   ]":
            item_type = FTPItemType.File

        item_name = a_element.attrib["href"].strip().strip("/")

        yield FTPItem(item_type, item_name)


def iter_versions(items):
    for item in items:
        if item.type == FTPItemType.Directory and VERSION_REGEX.match(item.name):
            yield item.name


def iter_directories(items):
    for item in items:
        if item.type == FTPItemType.Directory:
            yield item.name


def iter_files(items):
    for item in items:
        if item.type == FTPItemType.File:
            yield item.name


def find_version() -> list:
    html_text = get_html_text(PERFORCE_VERSION_PATH)
    html_etree = html_from_text(html_text)
    table_element = get_table_in_html(html_etree)
    return list(iter_versions(iter_items(table_element)))


def find_platform(version) -> list:
    html_text = get_html_text(PERFORCE_VERSION_PATH + "/" + version)
    html_etree = html_from_text(html_text)
    table_element = get_table_in_html(html_etree)
    return list(iter_directories(iter_items(table_element)))


def find_file(version, platform) -> list:
    html_text = get_html_text(PERFORCE_VERSION_PATH + "/" + version + "/" + platform)
    html_etree = html_from_text(html_text)
    table_element = get_table_in_html(html_etree)
    return list(iter_files(iter_items(table_element)))


def download_file(version, platform, file_name, output_path) -> str:
    url = PERFORCE_VERSION_PATH + "/" + version + "/" + platform + "/" + file_name
    temporary_path = output_path + ".tmp"
    with requests.get(url, stream=True) as response:
        with open(temporary_path, "wb") as temp_file:
            shutil.copyfileobj(response.raw, temp_file)
    shutil.move(temporary_path, output_path)
    return os.path.realpath(output_path)
