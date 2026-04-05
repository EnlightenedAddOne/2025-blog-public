# 2025-W29

> 来源：Obsidian/日志/周复盘/2025-W29.md

```dataviewjs
// 从当前周记文件名中提取周数信息
let currentNote = dv.current().file.name; // 例：2025-W29
let [year, weekStr] = currentNote.split('-');
let week = parseInt(weekStr.replace('W', ''));

// 使用 moment 来计算该年该周的起止日期（ISO 周一 ~ 周日）
let startOfWeek = moment().isoWeekYear(parseInt(year)).isoWeek(week).startOf('isoWeek');
let endOfWeek = moment().isoWeekYear(parseInt(year)).isoWeek(week).endOf('isoWeek');

// 日记筛选
let files = dv.pages(`"日志/日记"`)
    .where(p => {
        let dateStr = p.file.name.slice(0, 10); // 只取 YYYY-MM-DD
        return moment(dateStr, 'YYYY-MM-DD').isBetween(startOfWeek, endOfWeek, null, '[]');
    })
    .sort(p => p.file.name);

// 标题：显示当前是第几周，起止时间
let weekTitle = `🗓️ 第 ${week} 周（${startOfWeek.format('MM月DD日')} ~ ${endOfWeek.format('MM月DD日')}）`;
dv.header(1, weekTitle);

// 提取汇总内容
await HeaderAggregation(files, ['🎯 任务结算（Quest Summary）']);

async function HeaderAggregation(files, headers) {
    for (let file of files) {
        let contentRaw = await app.vault.readRaw(file.file.path);
        let contents = [];

        for (let header of headers) {
            let section = contentRaw.split(/#+ /).find(p => p.startsWith(header));
            contents.push(section?.slice(header.length) ?? '');
        }

        if (contents.every(p => p.replace(/\s+/, '') === '')) continue;

        dv.header(2, file.file.name);
        contents.forEach((p, i) => {
            if (p.replace(/\s+/, '') === '') return;
            dv.header(3, headers[i]);
            dv.paragraph(p);
        });
    }
}

```

```dataviewjs
// 解析当前周记文件名（例如 2025-W29）
let fileName = dv.current().file.name;
let [year, weekStr] = fileName.split('-');
let week = parseInt(weekStr.replace('W', ''));

// 计算该周的起止日期（ISO 周一 ~ 周日）
let startOfWeek = moment().isoWeekYear(parseInt(year)).isoWeek(week).startOf('isoWeek');
let endOfWeek = moment().isoWeekYear(parseInt(year)).isoWeek(week).endOf('isoWeek');

// 设置标题
let weekTitle = `🗓️ 第 ${week} 周（${startOfWeek.format('MM月DD日')} ~ ${endOfWeek.format('MM月DD日')}）`;
dv.header(1, weekTitle);

// 查找所有该周的日记文件（前提是文件名以 YYYY-MM-DD 开头）
let files = dv.pages('"日志/日记"')
    .where(p => {
        let match = p.file.name.match(/^(\d{4}-\d{2}-\d{2})/);
        if (!match) return false;
        let date = moment(match[1], 'YYYY-MM-DD');
        return date.isBetween(startOfWeek, endOfWeek, null, '[]');
    })
    .sort(p => p.file.name);

// 用表格展示文件名、心情和天气字段
dv.table(
    ["日期", "心情", "天气","温度"],
    files.map(p => {
        // 使用正确的字段名：☁️天气
        let weather = p["☁️ 天气"] || "❔";
        let temperature = p["🌡️ 温度"] || "❔";
        return [
            `[[${p.file.name}]]`, // 显示为链接
            p.emoji || "❔",
            weather,
            temperature
        ];
    })
);
```

<< [[2025-W28]] | [[2025-W30]] >>
