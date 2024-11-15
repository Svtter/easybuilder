import os


def check_clean():
    # 检查git仓库是否有未提交的更改
    result = os.popen("git status --porcelain").read()
    if not os.path.exists(".git"):
        print("错误: 当前目录不是git仓库")
        exit(1)
    if result:
        print("错误: git仓库不干净,请先提交所有更改")
        print("未提交的更改:")
        print(result)
        exit(1)
    print("git仓库状态检查通过")
