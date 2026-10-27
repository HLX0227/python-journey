# TODO 工具 2.0（SQLite 版）

命令行待办事项工具。1.0 版用 JSON 文件存储，本版完成 **存储引擎迁移：JSON → SQLite**，命令行体验保持不变——一次"重构不改行为"的实战。

## 与 1.0 的区别

| | 1.0（json 版） | 2.0（SQLite 版） |
|---|---|---|
| 存储 | `todo.json` 全量读写 | `todo.db`，按行增删改 |
| 编号 | 列表位置（删一行全体前移） | 数据库主键 id（永不混淆） |
| 保存 | 结束时整体写回 | 每条命令即时 commit |
| 错误处理 | 手动边界检查 `id > len` | `rowcount` 报告实际影响行数 |

## 用法

```bash
python todo_db.py add "买牛奶"      # 添加
python todo_db.py list              # 查看（显示真实 id + 完成勾选）
python todo_db.py done 1            # 按 id 标记完成
python todo_db.py del 2             # 按 id 删除
python todo_db.py --help            # 自动说明书
```

## 技术要点

- `sqlite3` 标准库，零依赖；`?` 参数占位符防 SQL 注入
- `conn.row_factory = sqlite3.Row`：查询结果支持按列名取值，业务代码零改动
- `INTEGER PRIMARY KEY AUTOINCREMENT`：id 永不复用（删过的编号不会发给新任务）
- `__file__` 锚定数据库路径：无论从哪个目录运行，todo.db 都在脚本旁边
- `rowcount` 诚实报告：操作 0 行时明确告知"没有该任务"，不假装成功
- 分层设计：数据层（init/load）与命令层（cmd_*）分离，迁移时驾驶舱原封不动

## 迁移中踩过的坑（详见根目录 mistakes.md）

- **schema 漂移**：改了 CREATE TABLE 但旧表还在，IF NOT EXISTS 跳过重建 → 删库重建；`SELECT sql FROM sqlite_master` 查表真实结构
- **id 复用之谜**：不带 AUTOINCREMENT 的 INTEGER PRIMARY KEY 会回收最大 id
- **事务边界**：commit 之后才崩溃 = 写操作已生效，"程序崩了"≠"什么都没发生"
- **编号脱钩**：界面用位置序号、操作用主键 → 删行后改错目标 → 显示统一用真实 id

## 环境

Python 3.10+，仅标准库（sqlite3 / argparse / os）。

## 下一步

- [ ] pytest 查库断言版测试（迁移到 2.0）
- [ ] 截止日期字段（TEXT 存日期 + WHERE 过滤）
- [ ] 多用户支持（users 表 + JOIN，练习已就绪）
