-- 第1步：创建学生成绩表，只需执行一次
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    score INTEGER NOT NULL
);

-- 第2步：添加三条练习数据，只需执行一次
INSERT INTO students (id, name, score)
VALUES (1, '小明', 80),
       (2, '小红', 95),
       (3, '小华', 88);

-- 第3步：查询数据，可以反复执行
SELECT id, name, score
FROM students
ORDER BY id;