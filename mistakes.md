# 踩坑记录 mistakes.md

> 规则：每次卡住超过 10 分钟的地方，记一行。格式：症状 → 原因 → 解法。
> 这是全仓库最值钱的文件——面试讲 debug 经历，弹药全在这里。

---

## 环境与 Git

- `git log` 报 `cannot spawn less` → Windows 没有翻页器 → `git --no-pager log` 或 `git config --global core.pager ""`
- push 报 502 → 代理抖动 → 先重试，再查 git/PyCharm 的 proxy 设置
- 提交后 GitHub 没变 → commit 只是本地存档，push 才上传（三段式：改动→commit→push）
- `python python xxx.py` 打重了 → 第二个 python 被当成文件名 → 读报错：`can't open file 'python'`
- 点运行"无事发生" → 命令少了 python 前缀，走了 pythonw（无控制台）→ 永远带 `python` 前缀

## Python 语法与机制

- `"19" + 1` 报 TypeError → `input()` 返回的永远是字符串 → 用 `int()` 转换
- `string()` 报 NameError → Python 没有这个函数，转字符串是 `str()`（string 是模块名）
- `remove('王芳')` 报 ValueError → 列表元素其实是 `['王芳']`（列表套列表）→ 用 `type()` 定位，肉眼靠不住
- `bag=[]` 做默认参数 → 默认值只在 def 时创建一次，跨调用共享 → 用 `None` 哨兵，函数内再造
- 边遍历列表边 remove → 元素前移导致跳过（[1,2,2,3] 删 2 剩 [1,2,3]）→ 重建新列表，或按索引 pop/del
- `kept = i` 以为在收集 → 只是贴标签，每轮覆盖 → 收集用 `kept.append(i)`
- `if x > top[key] or not top` 崩溃 → or 从左往右短路求值 → 保命检查放左边：`if not top or ...`
- `del` 不能当变量名 → 是 Python 关键字；但可以作为字符串命令名注册
- 函数没写 return → 默默返回 None，调用方拿到空 → 忘 return 是高频事故
- `if __name__ == '__main__':` → import 会把整个文件执行一遍，主流程要加门禁，否则 import 即运行

## 调试方法论

- **print() 会骗你，type() 不会** → 怀疑类型时打 `print(type(x), repr(x))`
- **查询"没效果"，先怀疑数据没差异** → 6 行 done 全是 0，WHERE done=0 当然看不出区别
- **"数据消失"，先查是不是被过滤了** → 1 没丢，是 done=1 被 WHERE 筛掉了
- **No such file 时信磁盘不信记忆** → traceback 路径、状态栏、dir 输出三方对质
- **注册了但没生效 = 两层不一致** → argparse 有 del 但 if/elif 没写分支，掉进 else

## 测试（pytest）

- ModuleNotFoundError → 测试和被测代码要同目录（pytest 把测试所在目录加进搜索路径）
- no tests ran → 函数名必须是 `test_` 开头，pytest 只收集这样的函数
- assert 查空气列表 → 测试要验证函数的**真实承诺**（数据库函数就查库，不是查本地变量）
- 第二次跑测试行数翻倍 → 往共享状态写的测试不幂等 → 用 uuid 唯一标记，或测试前清场
- `SELECT *` 导致断言下标错位 → 测试和正式代码要**指定列名**，不依赖列序

## SQL / SQLite

- `IF NOT EXIST` 报 near "EXIST" → 固定搭配 `IF NOT EXISTS`，一个字母不能少
- SQL 报错读法：`near "XXX"` = 数据库读到那个词就懵了
- 第二次运行数据翻倍 → INSERT 没有 IF NOT EXISTS 保护，来者不拒；去重要靠 UNIQUE 或先查
- ~~AUTOINCREMENT 编号只涨不回头~~ **修正**：`INTEGER PRIMARY KEY`（不带 AUTOINCREMENT）会**复用**已删除的最大 id；加了 `AUTOINCREMENT` 才永不复用。订单号/帖子 id 场景必须 AUTOINCREMENT，否则"新订单顶旧订单号"
- 代码里写了 AUTOINCREMENT 但 id 还是被复用 → 磁盘上的旧表是早期版本建的，IF NOT EXISTS 跳过重建（schema 漂移二犯）→ 删库重建；查真相：`SELECT sql FROM sqlite_master WHERE name='表名'` 能看到表实际的建表语句
- 不带 WHERE 的 UPDATE/DELETE = 全表爆炸 → 老手纪律：先写 SELECT 用同样 WHERE 验证，再改
- `table orders has no column named price` → 表是旧结构：`IF NOT EXISTS` 跳过重建，**改建表语句必须删库或 ALTER**
- 列之间漏逗号 → SQLite 不报语法错，把下一列名吞进类型（item TEXT price INTEGER）→ 照妖镜：`PRAGMA table_info(表名)`
- 相对路径 `connect('shop.db')` 落在"运行命令时站的目录"，不是脚本目录 → 用 `__file__` 锚定：
  `os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shop.db')`
- JOIN 输出是 id 不是名字 → ON 负责缝表（用 id），SELECT 负责挑列（想要名字就选 name）
- 名字只存一份、其他地方存 id 引用、JOIN 现场关联 → 改一处处处生效（反冗余，数据库设计第一原理）
- **commit 之后才崩溃 = 写操作已经生效**（del 时 NameError 崩在 commit 后，下次运行 id=1 真没了）→ 程序崩了 ≠ 什么都没发生，写操作以 commit 为界（事务边界意识）
- 界面编号用 enumerate 位置序号，数据库操作却按真实 id → 删行后两者分家，done 会改错行 → 显示也用 `row['id']`，让"看到的编号=操作的编号"（编号空洞恰恰证明身份系统在工作）

---

*持续更新。每次面试前通读一遍，等于把三个月的坑重走一遍。*
