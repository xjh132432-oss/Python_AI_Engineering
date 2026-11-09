# Python 模块与包

## 一、学习目标

- 理解 Python 模块与包的概念。
- 掌握模块的导入方式。
- 理解 `__name__` 变量的作用。
- 学会分离功能实现与程序入口。
- 理解不同模块之间的异常处理。

## 二、模块（Module）

模块是一个 Python 文件，可以包含函数、类和变量，
用于组织和复用代码。

示例：

    module_demo/
    ├── main.py
    └── score.py

其中：

- `score.py`：负责成绩计算功能。
- `main.py`：负责导入模块、调用函数和输出结果。

## 三、模块导入方式

### 1. 导入整个模块

    import score

    score.calculate_average(scores)

通过模块名访问其中的函数。

### 2. 导入指定函数

    from score import calculate_average

    calculate_average(scores)

直接导入指定函数，调用时不需要添加模块名前缀。

### 3. 导入方式的选择

当 `main.py` 和 `score.py` 位于同一目录，
并且从该目录运行 `main.py` 时，可以直接使用：

    import score

同一个项目中应尽量保持导入风格一致。

## 四、程序入口

    if __name__ == "__main__":
        main()

当 Python 文件被直接运行时，
其 `__name__` 的值为 `"__main__"`。

当文件被其他模块导入时，
其 `__name__` 通常为模块名称。

因此可以使用该条件控制主程序的执行，
避免模块被导入时自动执行入口逻辑。

## 五、异常处理

当函数接收到不符合要求的数据时，
可以主动抛出异常。

    if not scores:
        raise ValueError("Scores cannot be empty")

由调用方决定如何处理异常：

    try:
        result = score.calculate_average(scores)
    except ValueError as error:
        print(error)

这种设计可以将错误检测与错误展示分离。

## 六、函数职责划分

`score.py` 负责提供以下功能：

- `calculate_average(scores)`：计算平均分。
- `find_highest(scores)`：查找最高分。
- `find_lowest(scores)`：查找最低分。
- `count_passed(scores)`：统计及格人数。

`main.py` 负责：

- 准备输入数据。
- 调用功能函数。
- 展示计算结果。
- 处理预期异常。

## 七、注意事项

- 避免使用 `sum`、`max`、`min` 等内置函数名作为变量名。
- 在访问列表元素或进行除法前检查空列表。
- 将可复用功能与程序入口分离。
- 在同一项目中保持导入方式一致。