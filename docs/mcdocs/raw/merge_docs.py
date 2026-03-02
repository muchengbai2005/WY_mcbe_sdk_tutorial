# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = r"c:\Users\26010\Downloads\doc4\mcdocs"
OUTPUT_DIR = os.path.join(BASE_DIR, "new")

def remove_frontmatter(content):
    """移除markdown文件的frontmatter"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content

def merge_folder(folder_path, output_title, output_filename):
    """合并一个文件夹内的所有md文件"""
    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        return
    
    md_files = []
    for f in os.listdir(folder_path):
        if f.endswith('.md') and f != '索引.md':
            md_files.append(f)
    
    if not md_files:
        print(f"文件夹内没有md文件: {folder_path}")
        return
    
    md_files.sort()
    
    output_content = f"# {output_title}\n\n"
    output_content += "## 目录\n\n"
    
    for f in md_files:
        name_without_ext = os.path.splitext(f)[0]
        anchor = re.sub(r'[^\w\u4e00-\u9fff-]', '', name_without_ext).lower()
        output_content += f"- [{name_without_ext}](#{anchor})\n"
    
    output_content += "\n---\n\n"
    
    for f in md_files:
        file_path = os.path.join(folder_path, f)
        name_without_ext = os.path.splitext(f)[0]
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = remove_frontmatter(content)
        
        output_content += f"## {name_without_ext}\n\n"
        output_content += content
        output_content += "\n\n"
    
    output_file = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_content)
    
    print(f"已生成: {output_file}")

def merge_events():
    """合并事件文档"""
    events_dir = os.path.join(BASE_DIR, "1-ModAPI", "事件")
    if not os.path.exists(events_dir):
        print("事件文件夹不存在")
        return
    
    md_files = sorted([f for f in os.listdir(events_dir) if f.endswith('.md')])
    
    output_content = "# ModAPI 事件\n\n"
    output_content += "## 目录\n\n"
    
    for f in md_files:
        name = os.path.splitext(f)[0]
        anchor = re.sub(r'[^\w\u4e00-\u9fff-]', '', name).lower()
        output_content += f"- [{name}](#{anchor})\n"
    
    output_content += "\n---\n\n"
    
    for f in md_files:
        file_path = os.path.join(events_dir, f)
        name = os.path.splitext(f)[0]
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = remove_frontmatter(content)
        output_content += f"## {name}\n\n{content}\n\n"
    
    output_file = os.path.join(OUTPUT_DIR, "1-ModAPI-事件.md")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_content)
    print(f"已生成: {output_file}")

def merge_interfaces():
    """合并接口文档"""
    interfaces_dir = os.path.join(BASE_DIR, "1-ModAPI", "接口")
    if not os.path.exists(interfaces_dir):
        print("接口文件夹不存在")
        return
    
    subfolders = []
    single_files = []
    
    for item in os.listdir(interfaces_dir):
        item_path = os.path.join(interfaces_dir, item)
        if os.path.isdir(item_path):
            subfolders.append((item, item_path))
        elif item.endswith('.md'):
            single_files.append((item, item_path))
    
    for folder_name, folder_path in sorted(subfolders):
        merge_folder(folder_path, f"ModAPI 接口-{folder_name}", f"1-ModAPI-接口-{folder_name}.md")
    
    for filename, filepath in sorted(single_files):
        name = os.path.splitext(filename)[0]
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        content = remove_frontmatter(content)
        output_content = f"# ModAPI 接口-{name}\n\n{content}"
        output_file = os.path.join(OUTPUT_DIR, f"1-ModAPI-接口-{name}.md")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(output_content)
        print(f"已生成: {output_file}")

def merge_enums():
    """合并枚举值文档"""
    enums_dir = os.path.join(BASE_DIR, "1-ModAPI", "枚举值")
    if not os.path.exists(enums_dir):
        print("枚举值文件夹不存在")
        return
    
    md_files = sorted([f for f in os.listdir(enums_dir) if f.endswith('.md')])
    
    output_content = "# ModAPI 枚举值\n\n"
    output_content += "## 目录\n\n"
    
    for f in md_files:
        name = os.path.splitext(f)[0]
        anchor = re.sub(r'[^\w\u4e00-\u9fff-]', '', name).lower()
        output_content += f"- [{name}](#{anchor})\n"
    
    output_content += "\n---\n\n"
    
    for f in md_files:
        file_path = os.path.join(enums_dir, f)
        name = os.path.splitext(f)[0]
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = remove_frontmatter(content)
        output_content += f"## {name}\n\n{content}\n\n"
    
    output_file = os.path.join(OUTPUT_DIR, "1-ModAPI-枚举值.md")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_content)
    print(f"已生成: {output_file}")

def merge_updates():
    """合并更新信息文档"""
    updates_dir = os.path.join(BASE_DIR, "1-ModAPI", "更新信息")
    if not os.path.exists(updates_dir):
        print("更新信息文件夹不存在")
        return
    
    md_files = sorted([f for f in os.listdir(updates_dir) if f.endswith('.md')])
    
    output_content = "# ModAPI 更新信息\n\n"
    
    for f in md_files:
        file_path = os.path.join(updates_dir, f)
        name = os.path.splitext(f)[0]
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = remove_frontmatter(content)
        output_content += f"## {name}\n\n{content}\n\n"
    
    output_file = os.path.join(OUTPUT_DIR, "1-ModAPI-更新信息.md")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_content)
    print(f"已生成: {output_file}")

def merge_apollo():
    """合并Apollo文档"""
    apollo_dir = os.path.join(BASE_DIR, "2-Apollo")
    if not os.path.exists(apollo_dir):
        print("Apollo文件夹不存在")
        return
    
    for item in os.listdir(apollo_dir):
        item_path = os.path.join(apollo_dir, item)
        if os.path.isdir(item_path):
            merge_folder(item_path, f"Apollo {item}", f"2-Apollo-{item}.md")
        elif item.endswith('.md'):
            name = os.path.splitext(item)[0]
            with open(item_path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = remove_frontmatter(content)
            output_content = f"# Apollo {name}\n\n{content}"
            output_file = os.path.join(OUTPUT_DIR, f"2-Apollo-{name}.md")
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(output_content)
            print(f"已生成: {output_file}")

def merge_preset():
    """合并PresetAPI文档"""
    preset_dir = os.path.join(BASE_DIR, "3-PresetAPI")
    if not os.path.exists(preset_dir):
        print("PresetAPI文件夹不存在")
        return
    
    for item in os.listdir(preset_dir):
        item_path = os.path.join(preset_dir, item)
        if os.path.isdir(item_path):
            merge_folder(item_path, f"PresetAPI {item}", f"3-PresetAPI-{item}.md")
        elif item.endswith('.md'):
            name = os.path.splitext(item)[0]
            with open(item_path, 'r', encoding='utf-8') as file:
                content = file.read()
            content = remove_frontmatter(content)
            output_content = f"# PresetAPI {name}\n\n{content}"
            output_file = os.path.join(OUTPUT_DIR, f"3-PresetAPI-{name}.md")
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(output_content)
            print(f"已生成: {output_file}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    print("=" * 60)
    print("开始合并文档...")
    print("=" * 60)
    
    print("\n[1/6] 合并事件文档...")
    merge_events()
    
    print("\n[2/6] 合并接口文档...")
    merge_interfaces()
    
    print("\n[3/6] 合并枚举值文档...")
    merge_enums()
    
    print("\n[4/6] 合并更新信息文档...")
    merge_updates()
    
    print("\n[5/6] 合并Apollo文档...")
    merge_apollo()
    
    print("\n[6/6] 合并PresetAPI文档...")
    merge_preset()
    
    print("\n" + "=" * 60)
    print("所有文档合并完成!")
    print(f"输出目录: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
