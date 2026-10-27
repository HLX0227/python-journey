# 每周复盘

> 规则：每周日晚 15 分钟。写了才算数，哪怕只有三行。
> 这份 log 是懈怠时的证据链，也是以后简历和面试的素材库。

---

## 第 1 周

**做了什么**
- 搭好环境：PyCharm + Python 3.12 + Git，GitHub 仓库建立并打通推送
- Python 基础：变量、数据类型、f-string、字符串方法（strip/split/upper）
- input() 接收输入 + int() 类型转换，写了一个个人信息卡片程序
- 列表：索引、负索引、切片、append/remove/del、for 遍历、enumerate、反转
- 学会看报错：TypeError / NameError / ValueError
- 学会调试：用 type() 和 repr() 定位问题，而不是靠猜

**卡在哪**
- input() 返回字符串，`"19" + 1` 报 TypeError → 用 int() 解决
- 误用 string() 转字符串 → Python 里是 str()，没有 string() 这个函数
- remove('王芳') 报 ValueError → 排查发现列表里套了列表（元素是 ['王芳'] 不是 '王芳'），用 type() 定位后修正
- git push 报 502 → 代理问题，重试后恢复

**下周做什么**
- 字典（dict）基础，把 card.py 改造成字典版本
- while 循环 + break
- 函数定义与调用
- LeetCode 简单题每天 1 道

---

## 第 2 周

**做了什么**
- 字典、字典套列表、平均分/找最大/查找三个经典算法、
         学会 break、标志位、None

**卡在哪**
- >= 和 > 的并列行为、else continue 空转（已解决）

**下周做什么**
- 函数——把今天这些代码全部重构成函数

---

## 第 3 周

**做了什么**
- 函数定义与重构、把 roster 拆成 4 个函数

**卡在哪**
- return 类型错、忘写 return、静默 f-string bug
         ——全部用 repr/诊断代码定位解决

**下周做什么**
- 函数进阶（默认参数、多返回值）+ 文件读写

---

## 第 4 周

**做了什么**
- 默认参数、可变默认值陷阱(None哨兵)、json文件读写、
         给 roster 加上持久化（加载→操作→存盘）

**卡在哪**
- 忘 return 重演、def 位置、浮点长尾（已解决）

**下周做什么**
- 异常处理 try/except、把 add_student 做成完整 CRUD

---

## 第 5 周

**做了什么**
- 函数与重构、默认参数、可变默认值陷阱(None哨兵)、
         json持久化、try/except、完整CRUD、种子数据、重启验证法
**卡在哪**
- return类型错、忘return、边遍历边删、kept=i贴标签
         ——全部定位并修复

**下周做什么**
- argparse + TODO 工具

---

## 第 6 周

**做了什么**
- argparse：位置参数 vs 可选参数、default、type=int 自动校验、--help 自动生成
- 读懂 usage 行：方括号=可选，无方括号=必填
- 子命令 subparsers：add/list/del/done 命令路由（if/elif args.command）
- 完成 TODO 工具 todo_app.py：字典列表存任务、json 持久化、异常处理、边界检查
- 补写了 week06/README.md（功能、用法、技术要点、踩坑日志）
- 验收：done 99 不崩溃、重启后勾选状态还在（持久化验证通过）

**卡在哪**
- 命令少了 python 前缀 → pythonw 无控制台，"无事发生"之谜
- `python python ...` 打重了 → 读报错发现把 python 当成了文件名
- 注册了 del 但没写 elif 分支 → "两层不一致"：--help 里有它、跑起来掉进 else
- 差一错误：id < len(tasks) 应为 <=，导致最后一项无法操作
- del 是 Python 关键字不能当变量名，但可以作为字符串命令名

**下周做什么**
- 给 todo_app 写 pytest 单元测试（阶段 1 最后一块拼图）
- 开始阶段 2：SQL 基础 + LeetCode 数据库题
- 补 LeetCode：数组/字符串简单题每天 1 道（这两周欠账了 😄）

## 第 7 周

**做了什么**
- 安装 pytest（第一次用 pip 装第三方库），给 TODO 工具写了 4 个单元测试
- 学会 assert 断言：测试"不崩溃"和"不改坏数据"两种检查
- 理解 import 机制：import 会把整个文件执行一遍
- 给 todo_app.py 加上 `if __name__ == '__main__':` 门禁，
  让代码"直接运行"和"被 import"两种用法互不干扰
- 搞懂 pytest 两个规则：只收集 test_ 开头的函数；
  测试文件要和被测代码同目录（import 搜索范围）
- 阶段 1 结业：命令行 TODO 工具 + 测试 + README ✅

**卡在哪**
- ModuleNotFoundError：测试放 week07、代码在 week06，隔壁楼看不见
  → 把测试移到代码旁边解决
- SystemExit: 2：import todo_app 时主流程的 parse_args() 被连带执行
  → 加 __name__ 门禁解决
- no tests ran：函数名写成 tasks_add，pytest 不认
  → 改名 test_add（只收集 test_ 开头的）
- 路径打错：命令里写 week07 实际在 week06 → not found 就是字面意思

**下周做什么**
- 阶段 2 开始：SQL 基础（SELECT/WHERE/JION/GROUP BY）
- LeetCode 数据库题库，每天 1-2 题
- 补上欠的算法题（数组/字符串简单题）
- 了解：把 todo.json 的数据搬进 SQLite 数据库（SQL 第一课的实战）

---

## 第 8 周

**做了什么**
- 第一次盲写测试（top_by 通用找最大）：算法主干全对，
  暴露出 or 短路顺序和初始值语义两个缺口
- SQL 第一课（sqlite3，零安装真数据库）：
  CREATE TABLE IF NOT EXISTS / INSERT + ? 占位符 / commit / SELECT / UPDATE
- 观察并理解了三个数据库特性：
  ① 数据跨运行持久存在（第二次跑变 4 行，INSERT 不幂等）
  ② AUTOINCREMENT 编号只涨不回头（id 从 3 继续）
  ③ UPDATE 的效果永久改变后续查询（"1 不见了"= 被 WHERE done=0 过滤，
     数据没丢，状态变了）
- 建立 SQL 记忆策略：背 20% 思维（CRUD 四动作、? 防注入、commit 纪律），
  查 80% 语法（拼写忘了就查文档，查得快也是职业技能）

**卡在哪**
- IF NOT EXIST 少个 S → 学会读 SQL 报错：near "XXX" = 读到这个词就懵了
- 文件夹建错位置（week08 建在根目录不在 practice 里）→ No such file 时
  信 traceback/dir 的磁盘真相，不信记忆；相对路径认"站在哪运行"不认"文件在哪"
- 项目里出现两个 mydb.db → 工作目录决定数据库落在哪，删掉多余的
- "查询没区别" → 因为 6 行数据 done 全是 0，没有可过滤的差异；
  先怀疑数据没差异，再怀疑代码有 bug
- UPDATE 语句混搭：写死了 id=2 却还挂着参数 (1,) → 口诀：几个 ? 给几个值

**下周做什么**
- SQL 第二课：DELETE + 多表 JOIN 初步
- 实战：把 todo_app 的 json 存储改造成 SQLite 存储（阶段 2 里程碑）
- LeetCode 数据库题开刷（简单 10 题）
- 盲写题：add_task(text)（sqlite3 插入函数）

---

## 第 9 周

**做了什么**
- 第二次盲写：add_task(text) 结构全对，lastrowid 拿到新行 id
- 给数据库函数写 pytest：确立"先执行→再查询→后断言"三段式，
  用 uuid 唯一标记解决测试幂等，用指定列名解决 SELECT * 错位
- SQL 第二课：DELETE + rowcount、lastrowid、UPDATE 改名实验
- JOIN 多表查询跑通：users + orders 两表，ON user_id = id 缝合
- 亲手验证数据库设计第一原理：名字只存一份、其他地方存 id 引用、
  JOIN 现场关联 → UPDATE 一处改名，所有订单显示自动跟着变
- 建立 mistakes.md 踩坑本（环境/语法/调试/测试/SQL 五类归档）

**卡在哪**
- 参数收了却没用：add_task 里 INSERT 写死 ('任务1',) → 测试查库当场抓获
  "静默说谎"bug；口诀：几个 ? 给几个值
- 测试第二次跑 rows=2 → 往共享状态写的测试不幂等 → uuid 唯一标记
- SELECT * 让断言下标错位（拿到 id 不是 text）→ 测试要指定列名
- CREATE TABLE 列间漏逗号 → SQLite 不报语法错，把 price 吞进类型 →
  照妖镜 PRAGMA table_info；改表结构必须删库重建（IF NOT EXISTS 不更新旧表）
- 删了 shop.db 还报旧结构 → 相对路径认"站在哪运行"不认脚本位置，
  真库在项目根 → 用 __file__ 锚定路径，永久解决
- JOIN 输出是 id 不是名字 → 自己 SELECT 挑错了列；ON 负责缝，SELECT 负责挑

**下周做什么**
- 大项目：todo_app 从 json 换成 SQLite 存储（函数签名不变，命令行体验不变，
  换发动机 = 第一次"重构不改行为"实战）
- 迁移时同步改造 pytest（查库断言版）
- LeetCode 数据库简单题开刷（本周欠账 😄）
- 盲写题预告：del_task(task_id)，用 rowcount 返回删除行数

---

## 第 10 周（日期：2026-10-27）

**做了什么**
- 第三次盲写：del_task(task_id) 一次写通核心（DELETE+commit+close+rowcount）
- 大项目完成：TODO 工具 2.0——存储引擎从 JSON 迁移到 SQLite，
  命令行体验保持不变（argparse 子命令、if/elif 路由一行没改）
- 数据层重写：init_db 建表 / load_tasks 用 sqlite3.Row 按列名取值 /
  cmd_add·done·del 改为即时 INSERT·UPDATE·DELETE+commit
- 用 rowcount 做诚实报告：操作 0 行时告知"没有该任务"，替代手动 len 边界检查
- cmd_list 显示真实 id：界面编号=数据库主键，杜绝删行后改错目标
- 实验验证 AUTOINCREMENT：删掉 id=2 后新任务领到 id=3，编号出现"空洞"
  ——空洞恰恰证明身份系统在工作
- 更新 week10/README.md（1.0 vs 2.0 对比表、技术要点、迁移踩坑清单）

**卡在哪**
- connect() 漏传 DB → 盲写时写熟了，迁移时反而漏（肌肉记忆也会偷懒）
- 主流程 tasks 未定义 → 换发动机时忘了取消 load_tasks() 的注释
- SELECT FROM 漏列清单 → near "FROM": syntax error，用读 SQL 报错法秒定位
- schema 漂移二犯：代码加了 AUTOINCREMENT 但 id 仍被复用 →
  旧表是早期版本建的，IF NOT EXISTS 跳过重建 → 删库重建；
  新武器：SELECT sql FROM sqlite_master 查表真实建表语句
- 修正旧认知：INTEGER PRIMARY KEY 不带 AUTOINCREMENT 会复用最大 id
- 事务边界首体验：del 时 NameError 崩在 commit 之后 → 删除已生效，
  "程序崩了"≠"什么都没发生"
- f-string 漏 f：print('没有id为{id}的任务') 原样吐花括号

**下周做什么**
- 给 todo_db 写迁移版 pytest（查库断言 + 测试专用内存库 :memory:）
- 把旧 todo.json 的数据搬进 todo.db（数据迁移实战）
- LeetCode 数据库简单题开刷（连续两周欠账了 😄😄）
- 阶段 2 后半程：pandas 数据处理入门