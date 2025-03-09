import os
from datetime import datetime

# ⚠️ 这里修改为你的 Markdown 文件夹路径
directory = r"C:\Users\23968\Desktop\hugo\myblog\content\post\blog"

# YAML Front Matter 模板
yaml_template = """---
title: "{title}"
date: "{date}"
draft: false
---
"""

# 遍历指定文件夹下的所有 Markdown 文件
for filename in os.listdir(directory):
    if filename.endswith(".md"):  # 只处理 Markdown 文件
        file_path = os.path.join(directory, filename)

        # 读取文件内容
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()

        # 检查文件是否已经有 YAML Front Matter
        if content and content[0].strip() == "---":
            print(f"跳过：{filename}，已有 YAML Front Matter")
            continue  # 跳过已有 Front Matter 的文件

        # 生成 YAML Front Matter
        yaml_content = yaml_template.format(
            title=filename.replace(".md", ""), 
            date=datetime.today().strftime("%Y-%m-%d")
        )

        # 写回文件
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(yaml_content + "\n" + "".join(content))

        print(f"✅ 处理完成：{filename}")

print("\n🎉 批量添加 Front Matter 完成！")
