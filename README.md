# 🎯 JD-Resume Interview Coach (岗位面试模拟官)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skill: AI Agent](https://img.shields.io/badge/AI-Skill-blue)]()

一个专为求职者打造的 AI Agent Skill。只需输入你的**个人简历**和目标**岗位 JD（职位描述）**，它就能模拟该岗位的资深面试官，为你量身定制 8-12 道专业面试题，并提供一份可直接执行的面试准备清单。

## ✨ 核心特性

- **高度定制化出题**：拒绝千篇一律的“面经”，所有问题均锚定你的具体经历与 JD 的核心要求。
- **结构化输出**：每道题附带【考察点】【追问链】【优秀回答信号】【风险信号】。
- **精准匹配度诊断**：自动识别你的“强匹配（易被深挖）”与“弱匹配/缺失项（易被挑战）”的能力。
- **保姆级准备清单**：涵盖自我介绍、高危问题预案、反问面试官等 6 大板块，拿到手就能开始复习。
- **跨平台通用**：基于标准 Skill 架构编写，完美兼容 Claude Code、Coze、Dify 等支持本地/云端工具的 AI 平台。

## 📁 目录结构

本项目严格遵循标准 Agent Skill 架构：

```text
jd-resume-interview-coach/
├── SKILL.md              # 【必需】核心元数据与执行 SOP
├── agents/
│   └── openai.yaml       # 【推荐】Agent 配置文件（模型、工具注册）
├── scripts/              # 【工具】稳定代码（如处理 PDF 简历、校验输出格式）
├── references/           # 【知识库】长资料（如岗位题库框架、面试官人设）
└── assets/               # 【模板】静态文件（如输出排版模板、准备事项清单）
