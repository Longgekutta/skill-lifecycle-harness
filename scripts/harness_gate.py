#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
harness_gate.py: 快速代理脚本，方便智能体在不同工作区快速调用底层 tool-lifecycle-harness
"""
import sys
import subprocess
from pathlib import Path

HARNESS_CORE = Path("D:/github/tool-lifecycle-harness/main.py").resolve()

def main():
    if not HARNESS_CORE.exists():
        print(f"[ERROR] 找不到底层 tool-lifecycle-harness: {HARNESS_CORE}", file=sys.stderr)
        sys.exit(1)
    
    cmd = [sys.executable, str(HARNESS_CORE)] + sys.argv[1:]
    res = subprocess.run(cmd)
    sys.exit(res.returncode)

if __name__ == "__main__":
    main()
