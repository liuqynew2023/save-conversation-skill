#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""save-conversation 存储位置配置：get/set 根目录，set 时自动创建文件夹。

用法:
  python3 config.py get                     # 读取已配置的根目录（未配置输出 NOT_CONFIGURED）
  python3 config.py set --root "完整路径"    # 创建文件夹并保存配置
"""
import os, sys, json, argparse

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.environ.get("SAVE_CONVERSATION_CONFIG", os.path.join(SKILL_DIR, "config.json"))

def load():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("get")
    s = sub.add_parser("set")
    s.add_argument("--root", required=True)
    s.add_argument("--no-create", action="store_true")
    args = ap.parse_args()
    if args.cmd == "get":
        root = load().get("root")
        print("ROOT=" + root if root else "NOT_CONFIGURED")
    else:
        root = args.root
        if not args.no_create:
            os.makedirs(root, exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump({"root": root}, f, ensure_ascii=False, indent=2)
        print("ROOT=" + root)

if __name__ == "__main__":
    main()
