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

def test_to_datetime():
    import datetime
    mytime = "2017-10-1 10:20:00"
    assert bzoinq.to_datetime(mytime) == datetime.datetime(2017, 10, 1, 10, 20, 0)

def test_sound_and_task():
    a = bzoinq.Bzoinq()
    a.create_task()
    # test that the first id is 1
    assert a.task_id == 1

def test_monitor():
    import time
    a = bzoinq.Bzoinq()
    a.create_task("First task")
    b = bzoinq.Monitor(a)
    b.start()
    time.sleep(5)
    b.stop()

def test_two_tasks():
    import datetime
    import time
    current_time = datetime.datetime.now()
    time_in_10 = current_time + datetime.timedelta(seconds=10)
    time_in_5 = current_time + datetime.timedelta(seconds=5)
    a = bzoinq.Bzoinq()
    a.create_task("10 seconds task", time_in_10)
    a.create_task("5 seconds task", time_in_5)
    b = bzoinq.Monitor(a)
    b.start()
    time.sleep(15)
    b.stop()

def test_monitor_again():
    import time
    a = bzoinq.Bzoinq()
    b = bzoinq.Monitor(a)
    b.start()
    a.create_task("Task to test the Monitor")
    time.sleep(3)
    a.create_task("Second task to test the Monitor")
    time.sleep(3)
    b.stop()


def testfunction():
    def printme():
        print("function run ok")

    import time
    a = bzoinq.Bzoinq()
    b = bzoinq.Monitor(a)
    b.start()
    a.create_task("Testing a function", function=printme)
    time.sleep(2)
    b.stop()
