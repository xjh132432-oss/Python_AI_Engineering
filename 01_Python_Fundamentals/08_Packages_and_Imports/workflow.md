# Day 02 - 学习工作流

## 一、创建项目结构

创建 `08_Packages_and_Imports/score_manager/` 目录。

包含以下文件：

- `__init__.py`
- `__main__.py`
- `score.py`
- `validation.py`

## 二、实现模块功能

### validation.py

实现 `validate_scores()`，检查成绩列表是否为空。

### score.py

实现四个成绩统计函数：

- `calculate_average()`
- `find_highest()`
- `find_lowest()`
- `count_passed()`

通过相对导入调用数据验证函数。

### __init__.py

从 `score.py` 导入业务函数，并使用 `__all__` 定义公开接口。

### __main__.py

实现程序入口，通过包公开接口调用成绩统计函数。

## 三、运行验证

在 `08_Packages_and_Imports` 目录执行：

`python -m score_manager`

实际输出：

- Average: 88.75
- Highest: 92
- Lowest: 85
- Passed: 4

运行成功。

## 四、实际问题与修复

运行初期出现：

`No module named score_manager.__main__`

检查目录后发现特殊文件名下划线数量错误。

原文件名：

- `_init_.py`
- `_main_.py`

修正为：

- `__init__.py`
- `__main__.py`

修正后重新运行，程序成功执行。

## 五、Git 提交

建议提交信息：

`learn: practice Python packages and import mechanisms`

提交前检查流程：

1. `git status`
2. `git diff`
3. `git add`
4. `git diff --cached`
5. `git commit`
6. `git status`
7. `git push`

以上为建议流程，不代表已经执行提交。