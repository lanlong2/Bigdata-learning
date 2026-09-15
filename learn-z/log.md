# 错题1（字符）

> 来源：`字符与元组.md` 第二部分 A4 · 清洗一行脏数据
> 日期：2026-09-03　　状态：✅ 已订正通过

---

## 一、题目

```python
raw = "   Zhang San ,  18  \n"
```

把它清洗成 `"zhangsan|18"`。

**难点**：两端有空格和换行、逗号两边有空格、姓名中间有空格、还要转小写、最后要用 `|` 拼起来。

---

## 二、我的版本（最终通过）

```python
raw = "   Zhang San ,  18  \n"
s = raw.strip()
print(s)
s1 = s.split(',')
s11 = s1[0].strip()
s12 = s1[1].strip()
s2 = [s11, s12]
print(s2)
s31 = s2[0].replace(' ', '')
s32 = s2[1].replace(" ", "")
s311 = s31.lower()
s321 = s32.lower()
s3 = [s311, s321]
print(s3)
s4 = "|".join(s3)
print(s4)
```

**输出**

```
Zhang San ,  18
['Zhang San', '18']
['zhangsan', '18']
zhangsan|18
```

✅ 结果正确。优点：每一步都 `print` 出来检查，调试思路清晰。

---

## 三、易错点（我实际踩过的坑）

### 坑1 · 方法忘了写括号 🔴 犯了三次

```python
raw.strip        # ✗ 只是"指了指"这个方法，没有执行
raw.strip()      # ✓ 加括号才是"按下启动键"
```

验证：

```python
print(raw.strip)     # <built-in method strip of str object at 0x...>
print(raw.strip())   # 'Zhang San ,  18'
```

**比喻**：`raw.strip` 是"洗衣机"三个字，`raw.strip()` 才是按下启动键。

---

### 坑2 · 没有用 `=` 接住返回值 🔴

```python
raw.replace(' ', '')        # ✗ 加了括号也白搭，结果被扔了
raw = raw.replace(' ', '')  # ✓ 必须接住
```

**根源**：字符串**不可变**。所有字符串方法都是"重新印一张新字条"，老字条一个字都不会变。
👉 口诀：**字符串的方法全是"返回新的"，后面几乎永远要跟一个 `=`。**

---

### 坑3 · 下标从 0 开始，不是 1 🔴 导致程序崩溃

```python
s1 = s.split(',')     # ['Zhang San ', '  18']   ← 只有 2 段
```

| 写法 | 结果 |
|------|------|
| `s1[0]` | `'Zhang San '` ← **姓名在这里** |
| `s1[1]` | `'  18'` ← **年龄在这里** |
| `s1[2]` | 💥 `IndexError: list index out of range` |

我第一版写的是 `s1[1]` 和 `s1[2]`，等于跳过姓名、又去够一个不存在的第三段，程序直接崩在这行。

👉 死记：**n 个元素，门牌号是 `0` 到 `n-1`。**

---

### 坑4 · 列表没有字符串方法 🔴

```python
s2 = [s11, s12]             # s2 是【列表】
s2.replace(' ', '')         # 💥 AttributeError: 'list' object has no attribute 'replace'
```

`replace` / `lower` / `strip` / `split` 全是**字符串**的方法，**列表用不了**。

**类型追踪表**（卡住时先问自己"手里这个是什么类型"）：

| 变量 | 怎么来的 | 类型 | 能用什么 |
|------|---------|------|---------|
| `raw` | 原始数据 | **str** | strip / split / replace / lower |
| `s` | `raw.strip()` | **str** | 同上 |
| `s1` | `s.split(',')` | **list** ⚠️ | 索引 / len / append，**没有 replace** |
| `s1[0]` | 列表取一个元素 | **str** | 又能用字符串方法了 |
| `s4` | `"|".join(...)` | **str** | ✓ |

**自查神器**：`print(type(x), repr(x))`
`repr` 会把空格和 `\n` 原样显示出来，一眼看出到底洗干净没有。

---

### 坑5 · 变量命名 ⚠️ 唯一没改掉的问题

```python
s11  s12  s2  s31  s32  s311  s321  s3  s4      # ✗ 三个月后自己都看不懂
name  age  parts  result                         # ✓ 一眼知道装的是什么
```

👉 口诀：**变量名要回答"里面装的是什么"，而不是"它是第几个变量"。**

---

## 四、简便版本

### 版本 B · 拆包 + 好名字（推荐现在就用）

```python
raw = "   Zhang San ,  18  \n"

name, age = raw.strip().split(",")     # ⭐ 拆包：split 出 2 段，左边就写 2 个变量
name = name.replace(" ", "").lower()
age = age.strip()
print("|".join([name, age]))           # zhangsan|18
```

**关键**：`name, age = ...` 就是元组拆包（知识点 13），一步顶掉 `s1[0]`、`s1[1]` 两行，还顺手把变量名起好了。

---

### 版本 C · 推导式（练熟推导式后再用）

```python
raw = "   Zhang San ,  18  \n"

parts = [p.replace(" ", "").lower() for p in raw.strip().split(",")]
print("|".join(parts))                 # zhangsan|18
```

**好处**：不管拆出 2 段还是 20 段，代码一个字都不用改。

---

## 五、两条额外发现

**① `strip()` 那一步其实是多余的**

```python
"Zhang San ".replace(" ", "")   # 'ZhangSan'    没 strip 也一样
"  18".replace(" ", "")         # '18'
```

因为 `strip()` 只删两端空格，而 `replace(" ", "")` 是**删掉所有空格**，后者本来就包含前者的活。

⚠️ **但要看目标**：这题目标是 `zhangsan`（姓名连在一起）才能这么干。
如果目标是 `zhang san`（**保留中间空格**），就**必须用 `strip()`，绝不能用 `replace`** —— 会把中间那个空格也吃掉。

**② 开头的 `raw.strip()` 不能省**
它要干掉结尾的 `\n`，而 `\n` **不是空格**，`replace(" ", "")` 治不了它。

---

## 六、一句话总结

> **`.方法` 忘括号 → 没启动；启动了忘 `=` → 白干；`split` 完忘了下标从 0 数 → 直接崩。**
> 这三条的共同根源只有一个：**字符串不可变，所有操作都得"接住新的"。**

---
