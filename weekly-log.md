# 每周复盘

> 规则：每周日晚 15 分钟。写了才算数，哪怕只有三行。
> 这份 log 是懈怠时的证据链，也是以后简历和面试的素材库。

---

## 第 1 周（日期：____）

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

## 第 2 周（日期：____）

**做了什么**
- 字典、字典套列表、平均分/找最大/查找三个经典算法、
         学会 break、标志位、None

**卡在哪**
- >= 和 > 的并列行为、else continue 空转（已解决）

**下周做什么**
- 函数——把今天这些代码全部重构成函数

---

## 第 3 周（日期：____）

**做了什么**
- 函数定义与重构、把 roster 拆成 4 个函数

**卡在哪**
- return 类型错、忘写 return、静默 f-string bug
         ——全部用 repr/诊断代码定位解决

**下周做什么**
- 函数进阶（默认参数、多返回值）+ 文件读写

---

## 第 4 周（日期：____）

**做了什么**
- 默认参数、可变默认值陷阱(None哨兵)、json文件读写、
         给 roster 加上持久化（加载→操作→存盘）

**卡在哪**
- 忘 return 重演、def 位置、浮点长尾（已解决）

**下周做什么**
- 异常处理 try/except、把 add_student 做成完整 CRUD

---

## 第 5 周（日期：____）

**做了什么**
- 函数与重构、默认参数、可变默认值陷阱(None哨兵)、
         json持久化、try/except、完整CRUD、种子数据、重启验证法
**卡在哪**
- return类型错、忘return、边遍历边删、kept=i贴标签
         ——全部定位并修复

**下周做什么**
- argparse + TODO 工具