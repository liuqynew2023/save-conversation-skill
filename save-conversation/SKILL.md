---
name: save-conversation
description: Save the current conversation (the user's question, the assistant's answer, and the time the question was asked) into a topic folder under the user's "AI agent学习" knowledge base, as Markdown and Word files. Trigger when the user types 【生成文档】 (optionally followed by a custom title) or otherwise asks to save / archive / 归档 / 生成文档 the current conversation. All archives go under one common folder and are organized by conversation topic.
metadata:
  short-description: 把对话存成 Markdown + Word，按主题归档到「AI agent学习」文件夹
---

# Save Conversation（按主题归档对话到「AI agent学习」文件夹）

把当前对话保存成 Markdown + Word 两份文档，统一存到用户的「AI agent学习」知识库文件夹下，按「主题文件夹」组织。

## 存储根目录（可在此修改）
默认根目录固定为：
```
/Users/liuqingyuan05/Desktop/AI agent学习/
```
想换地方时，只改这一处即可。

## 触发条件
- 用户输入 `【生成文档】`（可带可选标题，例如 `【生成文档】提示词学习心得`）
- 或用户用自然语言说「保存/归档本次对话、把这段对话存成文档」等相近意思。

## 执行步骤
1. **确定根目录**：`/Users/liuqingyuan05/Desktop/AI agent学习/`（若不存在则创建；若该目录不可写，先向用户申请写入权限再执行）。
2. **确定主题文件夹**：根据本次对话主题，起一个简洁主题名（2~12 个字，去掉 `/ \ : * ? " < > |` 等非法字符）。在根目录下创建该文件夹；**同名文件夹已存在则复用（追加文件，不覆盖）**。
3. **确定文件名**：取「本次核心提问」的**前 10 个字**作为文件名。
   - 清理规则：去掉 `【】`、空格、换行，以及常见中英文标点（`？。，、！：；""''…—` 等）。
   - 不足 10 个字 → 用全部；清理后为空 → 退回用主题文件夹名。
4. **回顾当前对话**，提取有价值内容：用户原始问题/诉求、我的回答要点、关键结论、本次产生的文件路径。
5. **记录时间**：`提问时间` 尽量取用户提问发生的日期（对话上下文中可用当前日期；能明确到时分就写时分，否则只写日期）。`归档时间` 用当前时间。
6. **生成 Markdown 内容**（模板见下），并把 `主题文件夹名` 写进模板的「主题」字段。
7. **调用脚本生成文件**：用工作区依赖的 Python 运行 `scripts/archive.py`，传入 `--root`、`--folder`、`--name`，脚本会自动生成 `<root>/<folder>/<name>.md` 和 `<name>.docx`。
8. **回复用户**：告知已保存，并给出两个文件的绝对路径链接。

## 标题规则（仅用于可选标题，不改变存储结构）
- 用户输入了标题 → 可作为文档内标题使用，但**文件夹仍按主题、文件名仍按提问前 10 字**。
- 未输入标题 → 用「本次核心提问」作为文档标题。

## 归档范围
- 默认归档「本次对话」。
- 用户若说明只归档某一部分（如「只要关于提示词的那段」），按用户指定范围提取。

## Markdown 模板
```
# {标题}

> 主题：{主题文件夹名}
> 提问时间：{YYYY-MM-DD HH:mm}
> 归档时间：{YYYY-MM-DD HH:mm}

## 一、原始问题 / 诉求
{用户提出的问题或目标}

## 二、回答 / 核心内容
{我的回答要点、方法、结论}

## 三、关键结论 / 可复用要点
- {要点}

## 四、相关产出文件
- {文件路径或链接}
```

## 工具调用
```bash
# 用工作区依赖的 python3（保证有 python-docx），从 stdin 读 Markdown
python3 /Users/liuqingyuan05/.codex/skills/save-conversation/scripts/archive.py \
  --root "/Users/liuqingyuan05/Desktop/AI agent学习" \
  --folder "主题文件夹" \
  --name "提问前10字"
```
脚本会自动在 `<root>/<folder>/` 下生成 `{提问前10字}.md` 和 `{提问前10字}.docx`。

## 注意
- 只链接实际生成、位于「AI agent学习」文件夹下的文件。
- 不要把本技能的 scripts/ 内部文件暴露给用户。
