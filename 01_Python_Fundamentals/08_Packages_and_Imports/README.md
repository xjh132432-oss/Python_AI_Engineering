# Day 02 - Python Package 与模块导入机制

## 一、学习目标

理解 Python Module 和 Package 的区别，掌握包的基本结构、模块导入方式，以及通过 `python -m` 执行 Python 包。

## 二、Module 与 Package

### 1. Module（模块）

Module 通常指一个 Python 文件。

例如：

- `score.py`
- `validation.py`

模块用于组织相关函数、类和变量。

### 2. Package（包）

Package 用于组织多个模块，形成更清晰的代码结构。

本次使用普通 Python 包，其目录包含 `__init__.py`。

项目结构：

- `score_manager/`
  - `__init__.py`
  - `__main__.py`
  - `score.py`
  - `validation.py`

## 三、文件职责

### 1. validation.py

负责输入数据验证。

通过 `validate_scores()` 检查成绩列表是否为空。

如果为空，抛出 `ValueError`。

### 2. score.py

负责成绩统计业务逻辑。

实现：

- `calculate_average()`：计算平均分。
- `find_highest()`：查找最高分。
- `find_lowest()`：查找最低分。
- `count_passed()`：统计及格人数。

通过相对导入调用 `validation.py` 中的验证函数。

### 3. __init__.py

负责包初始化和公开接口管理。

通过 `from .score import ...` 将业务函数导入包的命名空间。

`__all__` 用于指定使用 `from score_manager import *` 时公开的名称。

### 4. __main__.py

负责包的程序执行入口。

通过 `python -m score_manager` 执行时，Python 会运行该文件。

## 四、导入机制

### 1. 绝对导入

例如：

`from score_manager import calculate_average`

通过包名访问公开接口。

### 2. 相对导入

例如：

`from .validation import validate_scores`

其中 `.` 表示当前包。

相对导入依赖包上下文，不能直接将包含相对导入的模块当作普通脚本运行。

### 3. __init__.py 的导入过程

当执行 `from score_manager import calculate_average` 时：

1. Python 查找 `score_manager` 包。
2. 执行包的 `__init__.py`。
3. `__init__.py` 从 `score.py` 导入函数。
4. 调用方获得 `calculate_average` 接口。

## 五、使用 python -m 执行包

必须从包所在目录的父目录执行。

进入 `08_Packages_and_Imports` 后运行：

`python -m score_manager`

Python 会查找并执行：

`score_manager/__main__.py`

不要直接使用 `python score_manager/__main__.py`，因为这种方式不会以相同的包上下文启动程序。

## 六、特殊文件名

Python 对特殊文件名有明确约定：

- `__init__.py`：包初始化文件。
- `__main__.py`：包执行入口。

注意文件名前后各有两个下划线，不能写成 `_init_.py` 或 `_main_.py`。

## 七、本次学习成果

- 理解 Module 和 Package 的区别。
- 掌握普通 Python 包的基本结构。
- 理解 `__init__.py` 的作用。
- 掌握相对导入的基本写法。
- 理解 `__all__` 的作用。
- 掌握 `python -m` 的基本使用。
- 将成绩统计程序拆分为多个职责清晰的模块。