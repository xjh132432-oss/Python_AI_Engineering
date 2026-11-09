# 学习踩坑记录

## 一、混用模块导入方式

### 问题

最初同时使用：

    import score

和：

    from module_demo.score import calculate_average

这两种导入路径依赖实际目录结构和程序运行位置，
混用后容易造成导入路径混乱。

### 解决方法

将 `main.py` 和 `score.py` 放在同一目录下，
统一使用：

    import score

调用函数时使用：

    score.calculate_average(scores)

## 二、空列表处理

### 问题

当成绩列表为空时，可能出现：

- 计算平均分时发生 `ZeroDivisionError`。
- 使用 `scores[0]` 时发生 `IndexError`。

### 解决方法

在计算和访问列表之前进行检查：

    if not scores:
        raise ValueError("Scores cannot be empty")

由调用方捕获并处理异常。

## 三、变量名覆盖内置函数

### 问题

使用 `sum`、`max`、`min` 作为变量名，
会覆盖当前作用域中对应的 Python 内置函数。

### 解决方法

使用具有明确含义的变量名：

- `total`
- `highest`
- `lowest`