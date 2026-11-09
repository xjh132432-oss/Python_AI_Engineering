# 学习工作流

## Day 01：Python 模块与异常处理

### 一、完成内容

- 创建成绩计算模块。
- 实现 `calculate_average()`。
- 实现 `find_highest()`。
- 实现 `find_lowest()`。
- 实现 `count_passed()`。
- 在主程序中导入成绩计算模块。
- 使用 `if __name__ == "__main__"` 设置程序入口。
- 为成绩列表为空的情况添加 `ValueError` 异常处理。

### 二、运行验证

#### 1. 正常输入测试

输入：

    scores = [90, 85, 92, 88]

预期结果：

- Average: 88.75
- Highest: 92
- Lowest: 85
- Passed: 4

测试结果：通过。

#### 2. 空列表测试

输入：

    scores = []

测试结果：

- 成功捕获 `ValueError`。
- 程序输出错误提示。
- 没有出现未处理的异常终止。

### 三、建议提交信息

    learn: practice Python modules and exception handling