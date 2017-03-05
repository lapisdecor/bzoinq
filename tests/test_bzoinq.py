#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bzoinq
----------------------------------

Tests for `bzoinq` module.
"""

import pytest


from bzoinq import bzoinq


# @pytest.fixture
# def response():
#     """Sample pytest fixture.
#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
#
#
# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument.
#     """
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_task():
    a = bzoinq.Task(1, "lalala", datetime.datetime(2017, 10, 1, 10, 10))
    assert a.id == 1
