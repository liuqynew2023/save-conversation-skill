# save-conversation（Codex Skill）

一个给 [Codex](https://openai.com/codex) 使用的「对话归档」技能：输入 `【生成文档】`，自动把当前对话（问题、回答、提问时间）整理成 Markdown + Word，按「主题文件夹」存进你的知识库目录。

## 功能

- **触发词**：`【生成文档】`（可带标题，例如 `【生成文档】提示词学习心得`）
- **统一归档**：默认存到 `~/Desktop/AI agent学习/`（可在 `SKILL.md` 顶部修改）
- **按主题建文件夹**：自动根据对话主题创建子文件夹，同名主题复用、不覆盖
- **文件命名**：取「本次提问」的前 10 个字
- **双格式输出**：`.md`（给 AI 复用 / 喂知识库）+ `.docx`（给人阅读）

## 仓库结构

```
save-conversation-skill/
├── README.md
└── save-conversation/          # 技能本体
    ├── SKILL.md                # 指令：触发词、流程、文档模板
    ├── agents/openai.yaml      # 技能显示信息
    └── scripts/archive.py      # 归档脚本（生成 .md 与 .docx）
```

## 安装

方式一（用 skill-installer）：
```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo liuqynew2023/save-conversation-skill \
  --path save-conversation
```

方式二（手动）：
把 `save-conversation/` 文件夹复制到 `~/.codex/skills/` 即可。

安装后，在新对话里输入 `【生成文档】` 即可触发。

## 自定义修改

| 想改什么 | 改哪里 |
|----------|--------|
| 触发词 / 存档流程 / 文档模板 | `save-conversation/SKILL.md` |
| 存档根目录 | `SKILL.md` 顶部「存储根目录」 |
| Word 格式（字体 / 颜色 / 表格） | `save-conversation/scripts/archive.py` |
| 技能显示名 | `save-conversation/agents/openai.yaml` |

## 依赖

归档脚本需要 `python-docx`。在 Codex 环境里通过「工作区依赖」的 Python 运行即可，无需额外安装。
