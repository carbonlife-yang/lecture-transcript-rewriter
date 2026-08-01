# Lecture Transcript Rewriter Skill

> **把任何一份讲课逐字稿,改写成你自己的版本。**
> **Convert any lecture transcript into your own version — in 25-40 minutes.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.4.1-blue.svg)](CHANGELOG.md)
[![Models](https://img.shields.io/badge/Claude%20%7C%20GPT%20%7C%20Codex%20%7C%20Qwen-compatible-green.svg)](SKILL.md)

[中文](#中文) | [English](#english)

---

## 中文

### 这是什么?

一个面向讲师/培训师的 AI Skill,把别人的讲课实录(带时间戳的逐字稿)快速改写成你自己的版本。

**核心能力**:
- ⏱️ **25-40 分钟** 完成一份 1-2 万字逐字稿的改写
- 🎯 **6 阶段互动对话** — AI 主动问你 4 个关键问题(目标时长/学员/保留删除/风格)
- 📊 **10 维度评估体系** — 知识覆盖度/时间分配/案例演示/结构清晰度/互动设计/语言流畅/重点突出/答疑/收尾/学员友好度
- 📝 **5 个配套模板** — 诊断报告/口播稿结构/讲师档案/评分表/问题分析表
- 🔑 **轻量级钥匙机制** — 邀请码 + 白名单 + 使用日志,实现"分享+追踪+权限"0 依赖
- 🌍 **跨模型兼容** — Claude/Codex/GPT/Qwen/任何支持 system prompt 的 LLM 都能用

### 解决什么问题?

讲师拿到一份好的逐字稿(比如前辈的实战实录),通常有 3 个痛点:
1. **判断难**:这场讲得好不好?漏了什么?超时了哪些?
2. **改写难**:按目标时长、目标框架,怎么快速变成自己的版本?
3. **风格难**:怎么把别人的风格变成自己的风格,而不是照搬?

这个 Skill 把"判断→改写→风格化"标准化,**让任何讲师 5 分钟上手,40 分钟出第一版**。

### 5 分钟上手

#### 1. 安装 Skill(30 秒)

```bash
git clone https://github.com/your-org/lecture-transcript-rewriter.git
cd lecture-transcript-rewriter
```

#### 2. 启动 AI 助手(30 秒)

把你最常用的 AI 助手打开(Claude/Codex/GPT 都行),贴入以下 prompt:

```
你是一个讲课逐字稿改写助手。详细 SOP 见 lecture-transcript-rewriter/SKILL.md。
我会给你一份讲课录音/逐字稿,请按 6 阶段帮我改写成我自己的版本:
1. 开场 + 问 4 个关键问题
2. 读我的稿,拆时间轴、找漏讲
3. 输出诊断报告
4. 按我的目标框架重写
5. 风格化(加我的口头禅/案例/修口误)
6. 交付 docx + pdf
要求 25-40 分钟出第一版。
```

#### 3. 第一次分享给同事(可选,2 分钟)

```bash
# 生成 5 个邀请码
python3 generate_keys.py 5 --share-to zhang@xx.com
```

脚本会输出可复制的分享话术,直接微信发给同事。

### 真实效果

**实战案例**:某讲师(化名 A 老师)用本 Skill 把自己 1h26m 的实战稿改写为 80min 标准版。

| 指标 | 改写前 | 改写后 |
|---|---|---|
| 讲课能力评分 | 2.85 / 5(需重做) | **4.35 / 5(良好)** |
| 漏讲清单 | 12 项 | 12 项全部补全 |
| 时长 | 86.5min | 80min(目标) |
| 强调词 | 0 | 47 个(加粗+下划线) |

完整演示见 [DEMO.md](DEMO.md)。

### 文件结构

```
lecture-transcript-rewriter/
├── README.md              ← 你正在看的
├── SKILL.md               ← 完整方法论(20K,含 6 阶段对话+10 维度评估)
├── DEMO.md                ← 完整 6 阶段对话演示
├── CHANGELOG.md           ← 版本日志
├── CONTRIBUTING.md        ← 贡献指南
├── LICENSE                ← MIT 协议
├── KEYS.md                ← 邀请码+白名单
├── USAGE_LOG.md           ← 使用日志
├── KEY_MANAGEMENT.md      ← 5 分钟上手 SOP
├── generate_keys.py       ← 一键生成邀请码脚本
├── templates/             ← 5 个配套模板
│   ├── 问题分析表模板.md
│   ├── 诊断报告模板.md
│   ├── 讲师口播稿模板.md
│   ├── 讲师档案模板.md
│   └── 讲课能力评分表.md
└── examples/              ← 实战案例
    └── 多维表格培训_A老师标准版_v1.docx
```

### 贡献

欢迎 PR!详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

可以贡献的方向:
- 新增评估维度(比如"幽默感""控场能力")
- 新增漏讲清单(比如"互动游戏""AI 工具使用")
- 翻译成其他语言(英文/日文/韩文)
- 改进模板(让 docx 更易生成)
- 补充实战案例(其他课程的改写)

### License

MIT — 随便用,可以改,商用 OK。

---

## English

### What is this?

An AI Skill for instructors/trainers to quickly rewrite someone else's lecture transcript (with timestamps) into your own version.

**Core capabilities**:
- ⏱️ **25-40 minutes** to rewrite a 10K-20K character transcript
- 🎯 **6-stage interactive dialogue** — AI proactively asks you 4 key questions (target duration/audience/what to keep-remove/style)
- 📊 **10-dimension evaluation system** — Knowledge coverage/time allocation/case demos/structure clarity/interaction/language fluency/key emphasis/Q&A/closing/learner-friendliness
- 📝 **5 templates** — Diagnosis report/lecture script structure/instructor profile/scorecard/problem analysis
- 🔑 **Lightweight key mechanism** — Invite codes + whitelist + usage log, zero-dependency "share+track+permission"
- 🌍 **Cross-model compatible** — Claude/Codex/GPT/Qwen/any LLM supporting system prompts

### What problem does it solve?

Instructors with a good transcript (e.g., a senior's actual session) typically face 3 pain points:
1. **Hard to judge** — Was this session good? What's missing? Where did it run over?
2. **Hard to rewrite** — How to fit target duration + framework?
3. **Hard to stylize** — How to make it feel like YOUR voice, not a copy?

This Skill standardizes "judge → rewrite → stylize" so **any instructor can get started in 5 minutes, ship first version in 40 minutes**.

### Quick Start (5 minutes)

#### 1. Install (30 seconds)

```bash
git clone https://github.com/your-org/lecture-transcript-rewriter.git
cd lecture-transcript-rewriter
```

#### 2. Launch your AI assistant (30 seconds)

Open your favorite AI (Claude/Codex/GPT work), paste:

```
You are a lecture transcript rewriting assistant. See lecture-transcript-rewriter/SKILL.md for full SOP.
I will give you a lecture transcript. Help me rewrite it in 6 stages:
1. Opening + ask 4 key questions
2. Read my transcript, split timeline, find missing content
3. Output diagnosis report
4. Rewrite per my target framework
5. Stylize (add my catchphrases/cases/fix stutters)
6. Deliver docx + pdf
Target: 25-40 minutes for first version.
```

#### 3. Share with colleagues (optional, 2 minutes)

```bash
# Generate 5 invite codes
python3 generate_keys.py 5 --share-to colleague@xx.com
```

Script outputs copy-paste share text — send via WeChat/email.

### Real Results

**Case study**: An instructor (alias "A 老师") used this Skill to rewrite their 1h26m actual session into an 80min standard version.

| Metric | Before | After |
|---|---|---|
| Lecture quality score | 2.85 / 5 | **4.35 / 5** |
| Missing items | 12 | 12 fully covered |
| Duration | 86.5min | 80min (target) |
| Emphasized keywords | 0 | 47 (bold + underline) |

Full demo: [DEMO.md](DEMO.md)

### File Structure

```
lecture-transcript-rewriter/
├── README.md              ← You're here
├── SKILL.md               ← Full methodology (20K)
├── DEMO.md                ← Complete 6-stage dialogue demo
├── CHANGELOG.md           ← Version log
├── CONTRIBUTING.md        ← Contribution guide
├── LICENSE                ← MIT
├── KEYS.md                ← Invite codes + whitelist
├── USAGE_LOG.md           ← Usage log
├── KEY_MANAGEMENT.md      ← 5-min onboarding SOP
├── generate_keys.py       ← One-click invite code generator
├── templates/             ← 5 templates
│   ├── 问题分析表模板.md
│   ├── 诊断报告模板.md
│   ├── 讲师口播稿模板.md
│   ├── 讲师档案模板.md
│   └── 讲课能力评分表.md
└── examples/              ← Case studies
    └── 多维表格培训_A老师标准版_v1.docx
```

### Contributing

PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

You can contribute:
- New evaluation dimensions (e.g., "humor", "stage presence")
- New missing-content checklists (e.g., "interactive games", "AI tool usage")
- Translations 
- Improved templates (easier docx generation)
- Case studies (rewrites of other courses)

### License

MIT — use freely, modify freely, commercial use OK.

---

## 🌟 Star History

If this skill has helped you, **give it a star ⭐** — it will really encourage me to build more.

## 📞 Contact

- **Maintainer**: [Your Name](https://github.com/carbonlife-yang)

---

## 🙏 Acknowledgments

This Skill was born from real lecture-transcript rewriting work with internal corporate trainers. Thanks to all the instructors who tested early versions and gave feedback.

特别感谢最初参与测试的讲师团队 — 你们的实战反馈让这个 Skill 从"理论"变成"能跑起来的方法"。
