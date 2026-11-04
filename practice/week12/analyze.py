import re
import pandas as pd

rows = []
cur = None
for line in open('git_log_raw.txt',encoding='utf-8'):
    line = line.rstrip()
    if line.startswith('COMMIT'):
        _,h,t,msg = line.split('|',3)
        cur = {'hash':h,'time':t,'message':msg,'files':0,'insertions':0,'deletions':0}
        rows.append(cur)
    elif line.strip() and cur:
        m = re.search(r'(\d+) files? changed(?:, (\d+) insertions?\(\+\))?(?:, (\d+) deletions?\(-\))?', line)
        if m:
            cur['files'] = int(m.group(1))
            cur['insertions'] = int(m.group(2) or 0)
            cur['deletions'] = int(m.group(3) or 0)

df = pd.DataFrame(rows)
df['time'] = pd.to_datetime(df['time'])
print(len(df))
print(df.head())
# Q1 你星期几最爱提交？
print(df['time'].dt.day_name().value_counts())

# Q2 哪三天写的代码最多？
print(df.groupby(df['time'].dt.date)['insertions'].sum()
        .sort_values(ascending=False).head(3))

# Q3 深夜提交（22 点及以后）有几次？
print((df['time'].dt.hour >= 22).sum())