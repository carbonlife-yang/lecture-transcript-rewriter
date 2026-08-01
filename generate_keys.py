#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
邀请码生成器 - 一键生成 + 自动填表 + 分享话术
零依赖:只用 Python 标准库

用法:
  python3 generate_keys.py
  python3 generate_keys.py 5    # 直接生成 5 个(跳过询问)
  python3 generate_keys.py 5 --share-to "zhang@xx.com"    # 生成 5 个并指定分享对象
'''

import random
import sys
import os
from datetime import datetime

# 邀请码字符集(去掉易混淆的 0/O/1/I/L)
CHARS = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'

KEYS_FILE = 'KEYS.md'


def generate_one():
    """生成 1 个邀请码,格式:SKL-XXXX-XXXX"""
    part1 = ''.join(random.choices(CHARS, k=4))
    part2 = ''.join(random.choices(CHARS, k=4))
    return f'SKL-{part1}-{part2}'


def generate_n(n):
    """生成 N 个不重复的邀请码"""
    codes = set()
    while len(codes) < n:
        codes.add(generate_one())
    return list(codes)


def check_duplicate(codes):
    """检查 KEYS.md 里是否已经有这些码(避免重复)"""
    if not os.path.exists(KEYS_FILE):
        return []

    with open(KEYS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    duplicates = [c for c in codes if c in content]
    return duplicates


def append_to_keys_md(codes, share_to=None):
    """自动追加到 KEYS.md 的"待激活邀请码"表"""
    if not os.path.exists(KEYS_FILE):
        print(f'⚠️  找不到 {KEYS_FILE},请先创建 KEYS.md(从 KEY_MANAGEMENT.md 复制结构)')
        return False

    with open(KEYS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # 找到"待激活邀请码"表的行
    today = datetime.now().strftime('%Y-%m-%d')
    new_rows = []
    for code in codes:
        share_info = f'已发给 {share_to}' if share_to else '—'
        new_rows.append(f'| {code} | {today} | 待激活 | {share_info} |')

    # 找到表头"| 邀请码 | 生成时间 | 状态 | 给谁了 |"之后的位置
    target_line = '| 邀请码 | 生成时间 | 状态 | 给谁了 |'
    lines = content.split('\n')
    insert_idx = None
    for i, line in enumerate(lines):
        if target_line in line:
            # 找到表头后的第一行(可能是表头分隔符),在它之后插入
            insert_idx = i + 2
            break

    if insert_idx is None:
        print(f'⚠️  在 {KEYS_FILE} 里找不到"待激活邀请码"表的表头')
        print(f'   请手动编辑 {KEYS_FILE},把邀请码加到对应表里')
        return False

    # 插入新行
    for row in reversed(new_rows):
        lines.insert(insert_idx, row)
    new_content = '\n'.join(lines)

    with open(KEYS_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def print_share_template(codes, share_to=None):
    """打印分享话术(可以直接复制粘贴)"""
    print()
    print('=' * 70)
    print('📋 分享话术(直接复制发给同事):')
    print('=' * 70)
    print()

    codes_text = ' / '.join(codes)

    if share_to:
        recipient = share_to
    else:
        recipient = '[填入同事邮箱或称呼]'

    template = f"""Hi {recipient} 👋

我有个讲课逐字稿改写的 skill,你拿去用。

邀请码:{codes_text}

用法(第一次用):
  1. 把 skill 装到你常用的 AI 助手(Claude/Codex/GPT 都行)
  2. 第一次用时,跟 AI 说:"用 lecture-transcript-rewriter skill,我的邀请码是 {codes[0]},我的邮箱是 {recipient}"
  3. 以后直接用,不用再填邀请码

用途:把别人的培训录音/逐字稿改成你自己的版本,40 分钟出第一版。

有问题找我 👋"""

    print(template)
    print()
    print('=' * 70)
    print('✅ 复制上面的话术 → 微信/邮件/飞书发给同事')
    print('=' * 70)


def main():
    # 解析参数
    n = None
    share_to = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == '--share-to' and i + 1 < len(args):
            share_to = args[i + 1]
            i += 2
        elif arg.isdigit():
            n = int(arg)
            i += 1
        elif arg in ['-h', '--help']:
            print(__doc__)
            sys.exit(0)
        else:
            print(f'⚠️  未知参数:{arg}')
            print(__doc__)
            sys.exit(1)

    # 问生成几个
    if n is None:
        try:
            user_input = input('🔑 要生成几个邀请码? [默认 5]: ').strip()
            n = int(user_input) if user_input else 5
        except (ValueError, KeyboardInterrupt):
            print('已取消')
            sys.exit(0)

    if n < 1:
        print('⚠️  至少生成 1 个')
        sys.exit(1)

    if n > 100:
        print('⚠️  最多生成 100 个(避免太多)')
        sys.exit(1)

    # 问发给谁
    if share_to is None and n > 0:
        try:
            share_to_input = input('👤 这批码发给谁?(邮箱/工号/微信名,留空可跳过): ').strip()
            share_to = share_to_input if share_to_input else None
        except KeyboardInterrupt:
            share_to = None

    print()
    print('⏳ 正在生成邀请码...')
    codes = generate_n(n)

    # 检查重复
    duplicates = check_duplicate(codes)
    if duplicates:
        print(f'⚠️  发现 {len(duplicates)} 个码与 KEYS.md 重复,重新生成...')
        codes = generate_n(n)
        duplicates = check_duplicate(codes)
        if duplicates:
            print(f'❌ 仍有 {len(duplicates)} 个重复(运气不好),请重试')
            sys.exit(1)

    # 输出邀请码
    print()
    print(f'✅ 成功生成 {n} 个邀请码:')
    print()
    for i, code in enumerate(codes, 1):
        print(f'  {i}. {code}')

    # 追加到 KEYS.md
    print()
    if append_to_keys_md(codes, share_to):
        print(f'✅ 已自动追加到 {KEYS_FILE}')
        if share_to:
            print(f'   并标记"已发给 {share_to}"')
    else:
        print(f'⚠️  没自动追加,请手动编辑 {KEYS_FILE}')

    # 显示分享话术
    print_share_template(codes, share_to)


if __name__ == '__main__':
    main()
