import os

def rename_files():
    """
    重命名当前目录中文件名包含用户输入文本的所有文件。
    """
    try:
        # 获取用户输入
        text_to_remove = input("请输入你想从文件名中删除的文本: ")
        
        # 检查输入是否为空
        if not text_to_remove:
            print("输入不能为空。")
            return
            
        # 获取脚本所在目录
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # 遍历目录中的所有文件
        for filename in os.listdir(current_directory):
            # 检查文件名是否包含用户输入的文本
            if text_to_remove in filename:
                # 构建新的文件名
                new_filename = filename.replace(text_to_remove, '')
                
                # 构建完整的旧路径和新路径
                old_path = os.path.join(current_directory, filename)
                new_path = os.path.join(current_directory, new_filename)
                
                # 重命名文件
                os.rename(old_path, new_path)
                print(f"文件 '{filename}' 已重命名为 '{new_filename}'")
                
        print("\n所有相关文件已成功重命名。")
                
    except Exception as e:
        print(f"发生错误: {e}")

# 运行函数
if __name__ == "__main__":
    rename_files()