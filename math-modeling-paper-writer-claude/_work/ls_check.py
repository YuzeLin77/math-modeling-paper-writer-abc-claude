# -*- coding: utf-8 -*-
import os
base = r"D:\数学建模自创skill\写论文skill"
for root, dirs, files in os.walk(base):
    depth = root.replace(base, "").count(os.sep)
    if depth <= 2:
        print("DIR(%d):" % depth, root)
        if depth <= 1:
            for f in files[:5]:
                print("   ", f)
