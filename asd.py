import a
import os

tags = ["AAA", "BBB", "CCC"]
texts = ["Choice 1 (Açıklama)", "Choice 2 (Açıklama)", "Choice 3 (Açıklama)"]

selected = a.run_tui_checklist(tags, texts)

os.system("clear")
print(selected)
