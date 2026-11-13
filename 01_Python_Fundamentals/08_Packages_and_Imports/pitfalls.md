# Day 02 - 问题记录

## 1. 特殊文件名下划线数量错误

### 问题现象

执行：

`python -m score_manager`

出现错误：

`No module named score_manager.__main__; 'score_manager' is a package and cannot be directly executed`

### 原因

实际文件名为：

- `_init_.py`
- `_main_.py`

而 Python 识别的特殊文件名是：

- `__init__.py`
- `__main__.py`

文件名前后各需要两个下划线。

### 解决方法

将文件重命名：

- `_init_.py` 改为 `__init__.py`
- `_main_.py` 改为 `__main__.py`

重新执行：

`python -m score_manager`

程序正常运行。

### 经验

特殊文件名必须严格遵循 Python 的命名约定，少一个下划线也会导致 Python 无法识别对应功能。

## 2. 本次其他问题

暂无新增。