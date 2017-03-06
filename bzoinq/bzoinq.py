# -*- coding: utf-8 -*-

from __future__ import print_function


import datetime
import pickle
import os
from functools import total_ordering
from playit import playit
import time


@total_ordering
class Task():
    """Defines tasks, their representation and ordering."""
    def __init__(self, id, description, alarm):
        self.id = id
        self.description = description
        self.alarm = alarm

    def __repr__(self):
        return '{}: {} {} {}'.format(self.__class__.__name__,
                                     self.id,
                                     self.description,
                                     self.alarm)

    def __lt__(self, other):
        if hasattr(other, 'alarm'):
            return self.alarm.__lt__(other.alarm)

    def __eq__(self, other):
        if hasattr(other, 'alarm'):
            return self.alarm.__eq__(other.alarm)


class Bzoinq():
    """Creates a running Bzoinq."""
    def __init__(self):
        self.task_id = 0
        self.task_list = []
        # load the saved tasks
        try:
            with open('outfile.p', 'rb') as fp:
                self.task_list = pickle.load(fp)
            print("tasks loaded from file")
            # remove the pickle file
            os.remove('outfile.p')

        except IOError:
            print("could't load task list file")

        # make task_id equal to the greatest of all task_id's
        bigger = 0
        for task in self.task_list:
            if task.id > bigger:
                bigger = task.id
        self.task_id = bigger
        print("new task id = {}".format(self.task_id))

    def __repr__(self):
        return '{}'.format(self.task_list)

    def create_task(self, description="Sample task",
                    alarm=datetime.datetime.now()):
        """Creates a new task"""
        self.task_id += 1
        # create the task
        new_task = Task(self.task_id, description, alarm)
        # add task to task list
        self.task_list.append(new_task)
        # sort the task list
        self.task_list = sorted(self.task_list)
        print("new task created")

    def remove_task(self, id):
        """Removes task with given id"""
        for task in self.task_list[:]:
            if task.id == id:
                try:
                    self.task_list.remove(task)
                except:
                    print("couldn't remove task")

    def remove_all_tasks(self):
        """Clears all the tasks"""
        self.task_list = []
        self.task_id = 0
        print("All tasks have been cleaned")

    def save_tasks(self):
        """Saves current tasks to file"""
        with open('outfile.p', 'wb') as fp:
            pickle.dump(self.task_list, fp)
        print("Tasks have been saved")

    def change_alarm(self, id):
        """Changes the alarm time of a task"""
        # this in practice creates a new task
        # it should cancel any alarm thread currently running
        pass

    def monitor(self):
        # TODO this has to be done in a thread otherwise no task is created
        stopit = False
        while True:
            time.sleep(1)
            if stopit:
                return
            current_time = datetime.datetime.now()
            if len(self.task_list) > 0:
                # check the time
                if current_time >= self.task_list[0].alarm:
                    print(self.task_list[0].alarm)
                    playit(r"alarm-clock-elapsed.wav")
                    done_alarm = self.task_list.pop(0)
                    print("alarm is done {}".format(done_alarm))
                    break


# help function
def to_datetime(sometime):
    """converts 00:00:00 (string) time input to datetime"""
    year, month, day, hours, minutes, seconds = map(int, sometime.split(':'))
    return datetime.datetime(year, month, day, hours, minutes, seconds)
