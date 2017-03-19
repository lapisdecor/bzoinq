# -*- coding: utf-8 -*-

from __future__ import print_function


import datetime
import pickle
import os
from functools import total_ordering
from bzoinq.playit import playit
import time
import threading


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
        assert type(alarm) is datetime.datetime
        self.task_id += 1
        # create the task
        new_task = Task(self.task_id, description, alarm)
        # add task to task list
        self.task_list.append(new_task)
        # sort the task list
        self.task_list = sorted(self.task_list)
        print("new task created")

    def remove_task(self, id_to_remove):
        """Removes task with given id"""
        for task in self.task_list[:]:
            if task.id == id_to_remove:
                try:
                    self.task_list.remove(task)
                except:
                    print("couldn't remove task")

    def remove_all_tasks(self):
        """Clears all the tasks"""
        self.task_list = []
        self.task_id = 0
        print("All tasks have been cleaned")

    def get_task_list(self):
        return self.task_list

    def save_tasks(self):
        """Saves current tasks to file"""
        with open('outfile.p', 'wb') as fp:
            pickle.dump(self.task_list, fp)
        print("Tasks have been saved")

    def change_alarm(self, id_to_change, new_time):
        """
        Changes the alarm time of a task.
        new_time must be a datetime object
        """
        assert type(new_time) is datetime.datetime
        # time on a task can only be changed if the task still exists
        for task in self.task_list()[:]:
            if task.id == id_to_change:
                task.alarm = new_time
        print("alarm with id {} changed".format(id_to_change))


class Monitorthread(threading.Thread):
    def __init__(self, name=None, target=None):
        super().__init__(name=name, target=target)

    # def run(self):
    #     pass


class Monitor():
    """Defines a monitor that keeps checking a task list for changes"""
    def __init__(self, task_list):
        self.stopit = False
        self.task_list = task_list

    def stop(self):
        """stops the monitor thread"""
        self.stopit = True

    def start(self):
        """Starts the monitor thread"""
        t = Monitorthread(target=self.keep_checking)
        t.start()
        print("Monitor thread has started")

    def keep_checking(self):
        """Keeps checking time and sorts the task_list"""
        while True:
            time.sleep(1)
            if self.stopit:
                break
            if len(self.task_list) > 0:
                # make sure task_list is sorted
                self.task_list = sorted(self.task_list)
                # check the time
                current_time = datetime.datetime.now()
                if current_time >= self.task_list[0].alarm:
                    print(self.task_list[0].alarm)
                    # play the sound
                    playit(r"alarm-clock-elapsed.wav")
                    # remove current alarm from the task_list
                    done_alarm = self.task_list.pop(0)
                    print("alarm is done {}".format(done_alarm))


# help function
def to_datetime(sometime):
    """converts Y-M-D 00:00:00 (string) time input to datetime"""
    try:
        my_datetime = datetime.datetime.strptime(sometime, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print("Incorrect time. Please use Y-M-D 00:00:00 format.")
        raise ValueError
    return my_datetime
