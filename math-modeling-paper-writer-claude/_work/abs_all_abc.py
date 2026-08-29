# -*- coding: utf-8 -*-
"""抽35篇ABC论文摘要前480字, 供方法索引"""
import os, re, glob
D = r"D:\数学建模自创skill\写论文skill\_work\ocr_full"
out = []
for f in sorted(glob.glob(os.path.join(D, "*.txt"))):
    b = os.path.basename(f)
    m = re.search(r'_([ABC])\d', b)
    if not m or "progress" in b:
        continue
    t = re.sub(r'[ \t]+', '', open(f, encoding='utf-8').read())
    mm = re.search(r'摘\s*要(.*?)(关键词|关\s*键\s*词)', t, re.S)
    ab = mm.group(1) if mm else t[:800]
    ab = re.sub(r'-{5}PAGE\d+-{5}', '', ab)
    ab = re.sub(r'\n+', '', ab)
    tag = re.search(r'(\d{4}).*?([ABC]\d{3})', b)
    label = (tag.group(1)+tag.group(2)) if tag else b[:20]
    out.append("### %s\n%s\n" % (label, ab[:480]))
open(r"D:\数学建模自创skill\写论文skill\_work\abs_all_abc.txt","w",encoding="utf-8").write("\n".join(out))
print("篇数:", len(out), "字符:", len("\n".join(out)))
