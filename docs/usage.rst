Usage
=====

easybuilder 是一个简单的构建工具，主要包含以下几个组件：

**Builder**: 用于构建 Docker 镜像
-----------------------------------
.. code-block:: python

   from easybuilder.builder import Builder

   builder = Builder("myapp")
   builder.build_img("latest")  # 构建镜像
   builder.build_venv()  # 构建虚拟环境镜像

**Worker**: 用于执行构建任务
-----------------------------------
.. code-block:: python

   from easybuilder.worker import Worker

   class MyWorker(Worker):
       def main(self):
           # 实现你的构建逻辑
           pass

   worker = MyWorker()
   worker.run()  # 执行构建

**TempFolder**: 临时文件夹工具
-----------------------------------
.. code-block:: python

   from easybuilder.temputils import TempFolder

   with TempFolder() as tmp:
       # 在临时文件夹中进行操作
       pass

**checker**: 检查工具
-----------------------------------
.. code-block:: python

   from easybuilder.checker import check_clean

   check_clean()  # 检查 git 仓库是否干净