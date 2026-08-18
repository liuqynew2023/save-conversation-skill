# save-conversation（Codex Skill）

一个给 [Codex](https://openai.com/codex) 使用的「对话归档」技能：把有价值的 AI 对话一键存成 Markdown + Word，按主题自动归档。

> 一句话：输入 `【生成文档】`，自动把当前对话（问题、回答、提问时间）整理成 `.md` + `.docx`，存进你配置的文件夹。

## 功能

- 📁 **一键归档**：`【生成文档】` → `.md` + `.docx` 两份
- 🗂 **按主题归类**：自动建子文件夹，同名主题合并、不覆盖
- ✏️ **自定义命名**：`【生成文档】周会纪要`；不填默认「提问前 10 字」
- 🔀 **切换存储位置**：`【切换存储位置】[1.文件夹名=..] [2.路径=..]`
- 🧭 **零基础上手**：首次使用欢迎引导 + `【存档帮助】` 速查卡

## 快速上手

```
【生成文档】                                    → 默认命名存档
【生成文档】周会纪要                             → 自定义命名存档
【切换存储位置】[1.文件夹名=产品调研] [2.路径=/Users/xxx/Desktop]
【存档帮助】                                    → 查看速查卡
```

## 仓库结构

```
save-conversation-skill/
├── README.md
└── save-conversation/          # 技能本体
    ├── SKILL.md                # 指令：触发词、流程、文档模板
    ├── README.md               # 技能说明
    ├── agents/openai.yaml      # 技能显示信息
    └── scripts/
        ├── config.py           # 存储位置配置（首次使用自动建文件夹）
        └── archive.py          # 归档脚本（生成 .md 与 .docx）
```

## 安装

方式一（用 skill-installer）：
```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo liuqynew2023/save-conversation-skill \
  --path save-conversation
```

方式二（手动）：
```bash
cp -r save-conversation ~/.codex/skills/
```

安装后，新开一个 Codex 对话，首次使用按提示配置存储位置即可。

## 依赖

归档脚本需要 `python-docx`。在 Codex 环境里通过「工作区依赖」的 Python 运行即可，无需额外安装。
