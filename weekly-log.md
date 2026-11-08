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

---

## 第 11 周（日期：2026-10-28 ~ 11-03，含三天忙人模式）

**做了什么**
- 依赖注入改造：todo_db 四个命令函数全部改收 conn，主流程发通行证；
  cmd_list 不碰库所以不收——该注入的注入，不该注入的不硬塞
- 测试迁移：fresh_db() 用 :memory: 内存库，测试天然幂等、不碰真库；
  3 passed（test_add / test_done / test_done_wrong_id）
- count_by(conn, done_value) 上线：list 末尾新增"未完结 X · 已完成 Y"汇总，
  练习题变产品功能
- summary(conn)：函数调用函数，返回 total/done/todo 字典；
  讨论 total 两种算法（COUNT(*) vs done+todo）的隐藏假设并写注释
- longest_task(conn)：SQL 排序挑选（ORDER BY LENGTH DESC LIMIT 1），
  学会"一件事一台机器干"，去掉冗余的 Python 冠军循环
- 数据搬家 migrate.py：todo.json → todo.db，带完成状态迁移，
  集合判重 + 连跑两遍验证幂等（第二遍新增 0 条）
- pandas 第一课：read_sql 读库、布尔筛选、value_counts、str.len 向量化、
  sort_values；三个一行挑战全过；交叉验证（pandas 与 SQL 统计结果一致）

**卡在哪**
- import todo_db 崩 NameError(conn) → 门禁留缝：conn.close() 在 if 块外；
  凡依赖运行时变量的代码必须缩进进门禁
- Incorrect number of bindings → 几个 ? 给几个值，单元素元组带逗号
- 测"不误伤"先造"在场者"：空表测不出边界行为；rows[98] 是第98行不是 id98
- unable to open database file → dirname 少数一层，practice 叠了两层；
  路径报错第一动作 print(路径)
- Cannot operate on a closed database → conn.close() 跑在后续使用之前，
  关门顺序也是设计
- tuple indices must be integers（两次）→ 默认行是元组只认数字下标；
  其中一次是导师模板里的雷：没设 conn.row_factory = sqlite3.Row 就写 row['text']
  → 教训：谁写的代码都敢怀疑，抄来的模板逐行问"为什么能跑"
- SELECT FORM → FROM 打反；traceback 穿过 pandas 时先看"它手里拿的是什么"，
  第三方库往往只是信使
- pandas 筛选后行号不连续 → index 是标签不是位置：过滤杀死位置，杀不死身份
  （列表下标/数据库id/pandas标签，三个世界同一条规律）

**下周做什么**
- 阶段 2 毕业项目：用 pandas 分析一份真实数据集
  （读取 → 清洗 → 三个业务问题 → 结论报告）
- done_rate(conn)：完成率 + 除零保护（空表 total=0 时除法会怎样）
- LeetCode 数据库简单题开刷（连续三周欠账了 😄😄）
- 忙人模式备忘：每周 1 次 × 1 小时也可，回来的次数才作数

---

## 第 12 周（日期：2026-11-04）

**做了什么**
- done_rate(conn)：完成率 + 除零保护；用 :memory: 空库验证返回 0 不崩
- 阶段 2 毕业项目：解析自己仓库的真实 git 历史（31 次提交 / 1552 行新增）
  → DataFrame → 三个业务问题（星期分布 / Top3 高产日 / 深夜提交数）
- 产出 week12/REPORT.md：三条发现 + 方法自检节（主动交代数据局限）
- 交叉对账：Top3 高产日与 weekly-log 最长三篇互证通过
- 解析器三问自测全过：split('|',3) 保险丝 / 缺统计行=默认值 0 / _ 丢弃手势

**卡在哪**
- done_rate() takes 0 positional arguments but 1 was given → 定义漏 conn 参数；
  更深：函数体偷偷用全局 conn = 隐藏依赖，测试喂不进数据 → 参数写进签名
- 正则那行看不懂 → 果断换成 split+关键词六行版：能解释的代码才属于自己
- "代码跑通了但什么都看不懂" → 停下逐行弄懂 + 三问自测，
  跑通后停下来弄懂才是工程师和粘贴员的分界线

**下周做什么**
- 阶段 3 开门：Flask 第一课（路由 / JSON / 状态码）
- search_tasks(conn, keyword)：LIKE + % 包参数
- LeetCode 数据库题欠账第四周 😄😄😄

---

## 第 13 周（日期：2026-11-07 ~ 11-08）

**做了什么**
- Flask 第一课：server.py 三扇门（/ 、/tasks 、/tasks/<int:id>），
  浏览器亲眼看到程序"站着等敲门"，终端日志每请求一行
- 状态码语言上手：200 看成功 / 201 生成功 / 400 递的没法用 /
  404 查无此门 / 405 门不接这种敲法
- /search 门：query 参数 request.args.get + LIKE '%kw%' 模糊搜索；
  空搜索=全列表（%% 匹配一切）作为设计决定写进注释
- POST /tasks：methods=['GET','POST'] 同门两种敲法；
  get_json(silent=True) + strip 安检 + lastrowid 回传 + 201
- client_test.py：requests 客户端五连验证（201/400/400/200/列表+1），
  API 的 server 与 client 两端都是自己写的
- jsonify 中文：app.json.ensure_ascii = False（json.dump 同款开关）

**卡在哪**
- import todo_db 找不到 → sys.path.append 亲手改搜索清单；
  并认清两张清单：Python 运行时的 sys.path vs PyCharm 静态检查的清单
  （IDE 标红 ≠ 运行报错，终端才是法官）
- sqlite3.connect('todo_db.DB') 带引号 = 打开名叫这串字符的文件（空库雷）
  → 不带引号才是取变量
- home 门牌被写成 /tasks → 根地址 404 + 门牌冲突（先登记的赢）
- {'error', '...'} 逗号写成集合 → jsonify 崩 TypeError；花括号内逗号=集合、冒号=字典
- search 的 get('') 参数名写空 → None 拼字符串崩；fetchone 用在搜索门（下一颗雷，提前排掉）
- ConnectionRefusedError → 服务器没在跑；学会双终端模型（一个站岗一个敲门）
  与排查顺序：活着吗 → 门对吗 → 函数对吗
- r.json() 对纯文本响应崩 JSONDecodeError → .json() 是断言不是转换，文本门用 .text
- 客户端不幂等：每跑一次 client_test 插一条"POST 测试"（id 8/9/10 三条躺库）
  → 下次用 DELETE 门清场

**下周做什么**
- PUT /tasks/<id> 与 DELETE /tasks/<id>：CRUD 全网齐，
  顺手用 DELETE 清掉三条 POST 测试
- 安全三件套意识：验证（已会）/ 认证（待学）/ 关 debug（已知为什么）
- LeetCode 数据库题欠账第五周 😄😄😄😄