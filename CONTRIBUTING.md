# 贡献指南 · Contributing Guide

> **欢迎 PR!** 这个 Skill 是个开放项目,任何讲师/AI 助手开发者都可以贡献。

[中文](#中文) | [English](#english)

---

## 中文

### 怎么贡献

#### 1. 报告问题(Issue)

发现 bug / 有建议 / 想要新功能:
1. 打开 [GitHub Issues](https://github.com/your-org/lecture-transcript-rewriter/issues)
2. 选对应模板(Bug Report / Feature Request / Question)
3. 详细描述场景和复现步骤

#### 2. 提交代码(PR)

**流程**:
1. Fork 仓库
2. 创建分支:`git checkout -b feature/your-feature`
3. 改代码(参见下面的"贡献方向")
4. 跑测试(如果有)
5. 提交:`git commit -m "feat: 新增 XXX 功能"`
6. Push:`git push origin feature/your-feature`
7. 创建 PR,描述改了什么

**Commit 规范**(参考 Conventional Commits):
- `feat:` 新功能
- `fix:` 修 bug
- `docs:` 文档改动
- `style:` 格式调整(不影响代码)
- `refactor:` 重构
- `test:` 测试
- `chore:` 构建/工具改动

#### 3. 翻译

目前文档以中文为主,需要翻译成:
- [ ] English(优先,GitHub 主流)
- [ ] 日本語
- [ ] 한국어
- [ ] 繁體中文(港台讲师用)

#### 4. 补充实战案例

你有其他课程的逐字稿 + 改写后的口播稿?可以贡献到 `examples/` 目录。

要求:
- 文件名格式:`课程名_讲师_版本_vN.docx`
- 附 1 段说明(100-200 字):讲什么、怎么改的、效果如何
- 涉及真实信息要做脱敏(参考 DEMO.md 化名方案)

---

### 贡献方向(欢迎)

#### 优先级 P0(必做)

| 方向 | 说明 | 工作量 |
|---|---|---|
| 英文版 README | 让海外用户也能用 | 2-3h |
| 英文版 SKILL.md | 完整翻译 | 5-8h |
| 英文版 5 个 templates | 翻译所有模板 | 3-4h |
| GitHub Actions | CI/CD(自动跑测试) | 2-3h |

#### 优先级 P1(欢迎)

| 方向 | 说明 | 工作量 |
|---|---|---|
| 新评估维度 | "幽默感""控场能力""视觉设计" | 1-2h |
| 新漏讲清单 | "互动游戏""AI 工具使用""伦理合规" | 1-2h |
| 实战案例 | 任何课程的改写前后对比 | 2-4h/份 |
| 改进模板 | docx 排版更精美 | 2-3h |
| 视频教程 | 录 5-10 分钟操作视频 | 4-6h |

#### 优先级 P2(进阶)

| 方向 | 说明 | 工作量 |
|---|---|---|
| Web 控制台原型 | 简单的 HTML 表单调用 Skill | 1-2 周 |
| AI 模型路由 | 自动选 Claude/GPT/Qwen | 1 周 |
| 模板市场设计 | 用户上传/下载/分享模板 | 1-2 周 |

---

### 编码规范

#### Python 脚本

- 风格:PEP 8
- 注释:中文(用户主要是讲师群体)
- 错误处理:用 try/except,不要让用户看到 traceback
- 跨平台:macOS / Linux / Windows 都能跑(测试)

#### Markdown 文档

- 中文为主,英文摘要
- 标题层级:最多 4 级(`#` `##` `###` `####`)
- 表格用 markdown 表格(不用 HTML)
- 代码块标语言:` ```bash ` ` ```python ` ` ```markdown `
- 链接用相对路径:`[SKILL.md](SKILL.md)`

#### 文件命名

- 中文文件名(给讲师用)or 英文文件名(给开发者用)都行
- 一致性优先:同类型文件用同一种语言
- 例:`诊断报告模板.md`(中文)而不是 `diagnosis-report.md`(英文)

---

### 测试

#### 手动测试清单

提交 PR 前,确认:

- [ ] `python3 generate_keys.py` 跑得通
- [ ] 生成的邀请码能正确追加到 KEYS.md
- [ ] 分享话术能正常显示
- [ ] 所有 markdown 文件在 GitHub 渲染正常
- [ ] 所有链接都能跳转
- [ ] 化名检查(没有真实姓名/公司名)

#### 自动化测试(将来)

会加:
- Python 单元测试(测试 generate_keys.py)
- Markdown 链接检查(测试所有 .md 文件)
- 化名检查(测试没有"小羊/王老师/协鑫"等真实名)

---

### 联系方式

- **GitHub Issues**: [提交问题](https://github.com/your-org/lecture-transcript-rewriter/issues)
- **GitHub Discussions**: [讨论区](https://github.com/your-org/lecture-transcript-rewriter/discussions)
- **Email**: maintainer@xx.com

---

## English

### How to contribute

#### 1. Report issues

Found a bug / have a suggestion / want a feature:
1. Open [GitHub Issues](https://github.com/your-org/lecture-transcript-rewriter/issues)
2. Pick a template (Bug Report / Feature Request / Question)
3. Describe the scenario + reproduction steps in detail

#### 2. Submit PR

**Workflow**:
1. Fork the repo
2. Create branch: `git checkout -b feature/your-feature`
3. Make changes (see "Contribution directions" below)
4. Run tests (if any)
5. Commit: `git commit -m "feat: add XXX feature"`
6. Push: `git push origin feature/your-feature`
7. Open PR, describe what you changed

**Commit convention** (Conventional Commits):
- `feat:` new feature
- `fix:` bug fix
- `docs:` docs only
- `style:` formatting
- `refactor:` refactoring
- `test:` tests
- `chore:` build/tooling

#### 3. Translate

Currently Chinese-first. Need translations:
- [ ] English (priority — GitHub mainstream)
- [ ] Japanese
- [ ] Korean
- [ ] Traditional Chinese (for Taiwan/HK instructors)

#### 4. Add case studies

Have other course transcripts + rewrites? Contribute to `examples/`.

Requirements:
- Filename format: `course_instructor_version_vN.docx`
- Include a brief description (100-200 words): what the course is about, how it was rewritten, what the results were
- Anonymize all real information (see DEMO.md anonymization scheme)

---

### Contribution directions

#### Priority P0 (essential)

| Direction | Description | Effort |
|---|---|---|
| English README | For international users | 2-3h |
| English SKILL.md | Full translation | 5-8h |
| English templates | Translate all 5 templates | 3-4h |
| GitHub Actions | CI/CD (auto test) | 2-3h |

#### Priority P1 (welcome)

| Direction | Description | Effort |
|---|---|---|
| New evaluation dimensions | "humor", "stage presence", "visual design" | 1-2h |
| New missing-content checklists | "interactive games", "AI tool usage", "ethics" | 1-2h |
| Case studies | Before/after rewrites of any course | 2-4h/each |
| Improved templates | Better docx formatting | 2-3h |
| Video tutorial | 5-10 min walkthrough | 4-6h |

#### Priority P2 (advanced)

| Direction | Description | Effort |
|---|---|---|
| Web console prototype | Simple HTML form calling Skill | 1-2 weeks |
| AI model routing | Auto-select Claude/GPT/Qwen | 1 week |
| Template marketplace | User upload/download/share | 1-2 weeks |

---

### Coding standards

#### Python scripts

- Style: PEP 8
- Comments: Chinese (instructors are the main users)
- Error handling: try/except, don't show tracebacks to users
- Cross-platform: macOS / Linux / Windows

#### Markdown

- Chinese primary, English summary
- Heading levels: max 4 (`#` `##` `###` `####`)
- Use markdown tables (not HTML)
- Code blocks: specify language (` ```bash ` ` ```python ` ` ```markdown `)
- Use relative paths: `[SKILL.md](SKILL.md)`

#### File naming

- Chinese (for instructors) or English (for devs) — both OK
- Consistency first: same type files use same language
- Example: `诊断报告模板.md` (Chinese) vs `diagnosis-report.md` (English)

---

### Testing

#### Manual test checklist

Before submitting PR, confirm:

- [ ] `python3 generate_keys.py` runs OK
- [ ] Generated invite codes correctly append to KEYS.md
- [ ] Share text displays correctly
- [ ] All markdown files render OK on GitHub
- [ ] All links work
- [ ] Anonymization check (no real names/companies)

#### Automated tests (future)

Will add:
- Python unit tests (for generate_keys.py)
- Markdown link checker (for all .md files)
- Anonymization checker (no "小羊/王老师/协鑫" etc.)

---

### Contact

- **GitHub Issues**: [Submit](https://github.com/your-org/lecture-transcript-rewriter/issues)
- **GitHub Discussions**: [Forum](https://github.com/your-org/lecture-transcript-rewriter/discussions)
- **Email**: maintainer@xx.com

---

## 🙏 Code of Conduct

- Be respectful and constructive
- Focus on the issue, not the person
- Welcome newcomers
- Celebrate diverse perspectives

By participating, you agree to abide by these principles.

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
