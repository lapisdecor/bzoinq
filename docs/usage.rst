=====
Usage
=====

To use bzoinq in a project::

    from bzoinq import bzoinq
    import datetime

    # create a bzoinq instance
    mybzoinq = bzoinq.Bzoinq()

    # create a task
    mybzoinq.create_task("Buy Milk", datetime.datetime(2017,3,30, 19,0))

    # create a Monitor a pass the task list
    mymonitor = bzoinq.Monitor(mybzoinq.get_task_list())

    # start the Monitor
    mymonitor.start()

    you can now add more tasks and hopefuly they will sound on the datetime you
    define on them
