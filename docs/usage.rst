=====
Usage
=====

To use bzoinq in a project::

    from bzoinq import bzoinq
    import datetime

    # create a Bzoinq instance (you can see it as a task manager)
    a = bzoinq.Bzoinq()

    # create a task
    a.create_task("Buy Milk", datetime.datetime(2017,3,30, 19,0))

    # create a Monitor a pass the task list
    b = bzoinq.Monitor(a)  # you need to pass your Bzoinq instance

    # start the Monitor (keeps watching for new tasks)
    b.start()

    You can now add more tasks and they will sound on the datetime you
    define on them

    a.create_task() # creates a sample task that will sound right now

    # you can also convert a "Y-M-D H:M:S" string
    a.create_task("Cook the Turkey", bzoinq.to_datetime("2017-04-07 10:00:00"))

    # you may save the tasks on disk for later use if you want to quit
    b.stop() # stops monitoring for new tasks

    # this saves the tasks in a file that will be loaded when monitor is started
    a.save_tasks()

    You are not limited to sounds, you can run any function at a given datetime.

    # define a function
    def f():
        print("Function running")

    # define a datetime
    my_date = datetime.datetime(2017, 05, 12, 12, 00, 00)

    # create a task that stores the function, this one has no sound
    a.create_task("My Function", alarm=my_date, sound=False, function=f)

    at the given datetime the function will run.

    If you need to shut down the computer, remember to save tasks with a.save_tasks().
    The saved file will be deleted after it's loaded when you start the program again.
