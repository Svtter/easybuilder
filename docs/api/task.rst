Task
======

We create task api to define the task of easybuilder.

预定义的 task 是 :class:`CheckCleanTask`。如果想要替换预定义的 task，可以修改 Worker 的 ``default_tasks``。

Usage
-----------

如果想要定义自己的 task，可以通过以下方式进行。

.. code-block:: python

    from easybuilder.task import Task

    class MyTask(Task):
        pass


    class MyWorker(Worker):
        prev_tasks = [MyTask]
        def main(self):
            pass

