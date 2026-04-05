> 来源：Obsidian/日志/日记/2025-07-16-星期三.md

> [!quote] 🎯 今日箴言
> 为你明灯三千，为你花开满城，为你所向披靡。 —— 《天官赐福》 · 佚名

---

# 🏰【今日考研冒险日志】

## 🗡️ 每日任务（Daily Quests）

- [x] 👹 战胜「英语单词」 (+100 EXP)
- [x] 👺 击败「政治大纲」(暂跳) (+80 EXP)
- [x] 🐉 挑战「高数基础」 (+170 EXP)

## 💻 计算机408任务（CS408 Quests）

- [ ] 🧮 数据结构特训 (+85 EXP)
- [ ] 📜 计算机组成原理副本 (+75 EXP)
- [ ] 🖧 操作系统Boss战 (+85 EXP)
- [ ] 🌐 计算机网络攻略 (+55 EXP)

## ⏳ 活动任务（Activities Quests）

- [x] 🚗 驾照科目一刷题 (+80 EXP)
- [x] 🧘 每日冥想10分钟 (+50 EXP)
- [x] 📚 法律法规学习 (+70 EXP)

## 🧩 支线任务（Side Quests）

- [x] 🍵 喝杯茶Buff，恢复体力 (+40 EXP)
- [x] 🗃️ 整理桌面装备 (+40 EXP)
- [ ] 🚶‍♂️ 拉伸走动，回复状态 (+70 EXP)

---

## ⚔️ 今日战斗记录（Battle Log）

### 副本1

- 📚 科目/章节：高数
- 🎁 战利品（今日收获）：
  - 🪄 收获1： 高数第一部分基础入门测试题做完了
  - 🪄 收获2：
  - 🪄 收获3：
- 👹 Boss难点：数列极限还不会
- 🛡️ 击败策略：

---

### 副本2

- 📚 科目/章节：科一
- 🎁 战利品（今日收获）：
  - 🪄 收获1：科一题目刷完了
  - 🪄 收获2： 模拟考试今日最高92
  - 🪄 收获3：
- 👹 Boss难点：
- 🛡️ 击败策略：

---

## 🎯 任务结算（Quest Summary）

```dataviewjs
// ⭐ 自动读取当前文件的复选框
let tasks = dv.current().file.tasks

// ⭐ 只保留已完成
let doneTasks = tasks.where(t => t.checked)

// ⭐ 通过正则提取 (+10 EXP) 里的数字
let totalExp = 0
for (let t of doneTasks) {
    let match = t.text.match(/\+\s*(\d+)\s*EXP/i)
    if (match) {
        totalExp += parseInt(match[1])
    }
}

// ⭐ 自动生成评价
let comment = ""
if (totalExp >= 900) {
    comment = "🏆 完美通关！经验满满，状态爆表！"
} else if (totalExp >= 700) {
    comment = "👍 表现优异，继续冲刺满分！"
} else if (totalExp >= 400) {
    comment = "⚔️ 还不错，保持战斗力，明天再战！"
} else if (totalExp > 100) {
    comment = "🛡️ 状态一般，注意休息调整！"
} else {
    comment = "💤 今天需要充电，明天加油！"
}

// ⭐ 输出结果
dv.paragraph(`- 📝 今日评价：${comment}`)
dv.paragraph(`- ⚡️ 今日获得经验值：${totalExp} EXP`)
```

- 🗂️总结：科一题目刷完，科一模拟考试最高92

---

## ✨ 每日激励

> 「考研路上，每一步都是英雄的成长。」

---

<< [2025-07-15-星期二](2025-07-15-星期二.md) | [2025-07-17-星期四](2025-07-17-星期四.md) >>
