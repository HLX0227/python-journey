# 我的 TODO 工具

一个用纯 Python 标准库写的命令行待办事项工具。零第三方依赖，开箱即用。

## 功能

- ✅ 添加任务（`add`）
- ✅ 查看任务列表，带完成状态勾选（`list`）
- ✅ 标记任务完成（`done`）
- ✅ 删除任务（`del`）
- ✅ 数据持久化到 `todo.json`，关闭程序不丢数据
- ✅ 异常处理：文件不存在自动创建、数据损坏自动恢复、越界编号友好提示

## 快速开始

```bash
python todo_app.py add "学Python"
python todo_app.py add "买牛奶"
python todo_app.py list
# 1. [ ] 学Python
# 2. [ ] 买牛奶

python todo_app.py done 2
python todo_app.py list
# 1. [ ] 学Python
# 2. [✓] 买牛奶

python todo_app.py del 1
python todo_app.py done 99
# 没有第 99 项，好好说话，不崩溃
```

## 数据结构

每条任务是一个字典，存在列表里，编号即位置：

```json
[
  {"text": "学Python", "done": false},
  {"text": "买牛奶", "done": true}
]
```

## 技术要点

| 模块 | 用途 |
|---|---|
| `argparse` 子命令 | `add/list/del/done` 命令路由，自动参数校验与 `--help` |
| `json` + `with open` | 数据读写，`ensure_ascii=False` 保证中文正常 |
| `try/except` | 捕获 `FileNotFoundError` / `JSONDecodeError`，优雅降级 |
| 边界检查 | `id < 1 or id > len(tasks)`，防 IndexError |

## 开发日志（踩过的坑）

- 差一错误（off-by-one）：`id < len` 应为 `id <= len`，导致最后一项无法操作
- 忘写 `return`：函数默默返回 `None`，调用方拿到空数据
- 边遍历边删除会漏元素：改用"重建列表"或 `pop`/`del` 按索引删
- 可变默认参数陷阱：`def f(bag=[])` 会跨调用共享，用 `None` 哨兵

## 环境

Python 3.10+（开发于 3.12），仅使用标准库。

## 后续计划

- [ ] pytest 单元测试
- [ ] 任务截止日期
- [ ] 按状态过滤（`list --todo` / `list --done`）
