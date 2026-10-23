# 认识Java与第一个程序

对应J00的第一节。**在大模型应用路线结束后学习本篇**，现在只作为已备材料，不代表已经进入Java阶段。Java路线450小时包含语言、框架、基础能力和独立业务项目，不能把本篇读完等同于Java基础学完。

本篇目标：区分JDK、编译和运行；独立保存、编译、运行一个程序；理解最初的变量、输出和计算。已有Python知识可以帮助理解，但Java语法在这里从零解释。

## 1. Java代码如何运行

Python一般由解释器直接执行`.py`。Java常见的入门过程分为两步：

1. 用编译器`javac`把`.java`源码转换成`.class`字节码，编译时检查语法与很多类型错误。
2. 用`java`启动Java虚拟机（JVM）执行字节码。JVM是运行Java程序的程序，不是需要自己另外写的机器。

**JDK**是Java开发工具包，包含编译、运行等开发工具。只有运行环境却没有编译器时，可能出现`java`可用、`javac`不可用。建议以JDK 21 LTS为本路线教学起点；LTS表示长期支持版本线，具体供应商、安装包与维护更新在实际开学时核对[官方入门](https://dev.java/learn/getting-started/)，不把现在的版本选择推断为未来已经安装。

环境准备好后，在PowerShell逐行执行：

```powershell
java -version
javac -version
Get-Command java
Get-Command javac
```

前两行看版本，后两行看终端实际找到的命令路径。PATH是系统搜索可执行程序的目录列表；安装后终端找不到命令时，先开一个新终端，再核对JDK的`bin`目录是否在PATH中。多套JDK共存时，确认`java`与`javac`来自同一JDK；不要因一个命令报错就不断重复安装。

本篇只使用JDK 21已有语法。后续IDE可以减少重复操作，但第一遍先理解终端中的编译与运行。框架具体版本在J04开始前再按官方兼容要求选择。

## 2. 保存第一个完整程序

在自己的Java练习目录，新建名为`HelloJava.java`的UTF-8文本文件。不要保存为`HelloJava.java.txt`。手写：

```java
public class HelloJava {
    public static void main(String[] args) {
        System.out.println("你好，Java！");
        System.out.println("我将学习后端开发。");
    }
}
```

这段代码第一次出现的结构如下：

- `class`声明一个类。类是Java组织代码的一种基本单位，后面会系统学习对象；当前先把它理解为程序的外层结构。
- `public`表示这个类可以被外部访问。顶层公共类的名字`HelloJava`必须与文件名`HelloJava.java`一致，大小写也一致。
- 大括号`{}`表示代码块，必须成对出现，缩进帮助人阅读，但不能替代括号。
- `main`是本程序的启动入口。`static`表示不必先创建对象即可调用，`void`表示这个方法不返回一个值。方法与Python函数相似，用于组织操作。
- `String[] args`表示一个字符串数组参数，用来接收命令行参数。本篇不读取它；数组在后续章节学习，不要求现在修改入口签名。
- `System.out.println(...)`把括号里的内容输出，并在结尾换行。双引号包住一段字符串，即文本。
- 每条输出语句结尾需要英文分号`;`，源码中的标点使用英文半角字符。

进入保存该文件的目录，逐行执行：

```powershell
javac -encoding UTF-8 HelloJava.java
java -cp . HelloJava
```

第一行成功时一般没有输出，会生成`HelloJava.class`。`-encoding UTF-8`明确告诉编译器源码编码。第二行运行类，`-cp .`表示在当前目录查找类，最后写类名而不是文件名。

预期结果：

```text
你好，Java！
我将学习后端开发。
```

Java也支持某些单文件源码直接启动方式，但本节统一练习“先编译、后运行”，便于分清两个阶段。每次改源码都要重新编译，否则可能运行旧的`.class`。

## 3. 保存数据：变量、类型与赋值

**变量**是用名字保存和读取数据的位置。Java声明变量时通常先写类型，再写名字：

```java
String learner = "同学";
int studyDays = 6;
double hoursPerDay = 1.5;
double weeklyHours = studyDays * hoursPerDay;
```

`String`表示字符串；`int`表示一定范围内的整数；`double`表示浮点数，可以保存小数近似值。`=`是把右边计算结果保存到左边变量，不能把它当作数学等式。变量要先声明、赋值，再读取。

Java的`int`不能直接保存`1.5`，`String`也不能直接保存不带引号的数字。变量名可以自行选，只要符合语法并能清楚表达含义，不要求与示例一致。

新建`StudyCard.java`，写完整程序：

```java
public class StudyCard {
    public static void main(String[] args) {
        String learner = "同学";
        int studyDays = 6;
        double hoursPerDay = 1.5;
        double weeklyHours = studyDays * hoursPerDay;

        System.out.println("学习者：" + learner);
        System.out.println("每天小时：" + hoursPerDay);
        System.out.println("每周小时：" + weeklyHours);
    }
}
```

编译运行：

```powershell
javac -encoding UTF-8 StudyCard.java
java -cp . StudyCard
```

输出：

```text
学习者：同学
每天小时：1.5
每周小时：9.0
```

`*`是乘法；整数与`double`相乘，本例结果是`double`。当`+`有一边是字符串时，会进行字符串拼接，所以`"每周小时：" + weeklyHours`得到一段文本。

## 4. 计算中的边界

把下面的语句放在`main`内部，一次预测一行再运行：

```java
System.out.println(7 / 2);
System.out.println(7.0 / 2);
System.out.println("结果：" + 2 + 3);
System.out.println("结果：" + (2 + 3));
```

输出：

```text
3
3.5
结果：23
结果：5
```

两个整数相除是整数除法，本例舍去小数部分。至少一个数是`double`时采用浮点除法。`+`按这里的从左到右顺序执行，所以第三行先拼接`"结果："`与`2`再拼接`3`；第四行括号先完成数字相加。

`double`存在近似误差，不能把它直接作为后续精确金额计算的默认方案。金额类型在数据库和业务项目阶段再学，不要求现在提前掌握。整数除以0会失败，具体异常在后续章节学习；本篇先记住除数必须检查。

注释可以写`// 这一行后面是说明`，编译器不会执行注释。用注释解释原因，不能用“预期输出”注释替代实际运行。

## 5. 常见错误怎样定位

| 现象 | 解释与处理 |
|---|---|
| `javac`不是可识别命令 | 终端没有找到编译器；核对JDK和PATH，检查新终端 |
| `class HelloJava is public...` | 公共类名与文件名不一致，改为同名且大小写一致 |
| 提示缺少`;`或括号 | 从报错行往前检查标点；真正遗漏位置可能在上一行 |
| `cannot find symbol` | 名字不存在或大小写不同，例如把`System`写成`system` |
| `incompatible types` | 赋值类型不匹配，例如`int hours = 1.5;` |
| 找不到主类 | 核对所在目录、编译是否成功、类名和`-cp .`；运行时不加`.class` |
| 改完代码，运行还是旧内容 | 重新执行`javac`，并检查编译有没有失败 |
| 中文乱码 | 确认源码保存为UTF-8并按本节命令编译；再核对终端编码 |

一次只修一个明确问题，重新编译再观察。不因为某个旧文件成功编译就假定当前文件也成功。

## 6. 就地练习与完成检查

完成[入门练习V01—V06](../../02_习题册/Java/00_入门练习.md)，对应本篇已教过的语法。先独立做，再查看分离的参考答案；练习不要求输入、判断、循环或自定义方法，这些尚未在本篇教授。

- [ ] 能说出`.java`、`.class`、`javac`、`java`各自的作用。
- [ ] 能从空文件写出入口，解释类名与文件名一致的要求。
- [ ] 能声明字符串、整数、小数变量，并说明类型错误的原因。
- [ ] 能预测整数除法和字符串拼接结果。
- [ ] 能改动源码、重新编译并确认新结果。

本篇练习完成后，下一步是输入输出、条件与循环、数组和方法，再进入类与对象；对应中文分节教材与练习待按学习进度展开。按自己的实际学习情况更新记录，不把材料已备记成已学。

[Java路线](README.md) · [官方阅读](../../09_官方文档阅读/Java/README.md)
