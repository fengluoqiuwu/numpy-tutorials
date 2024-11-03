import argparse
import os
import subprocess
import shutil
import webbrowser

def clear_generate_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md') or file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except subprocess.CalledProcessError as e:
                    print(f"Error deleting {file_path}: {e}")

def clear_folder_contents(folder_path):
    try:
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)  # 删除文件
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # 删除子文件夹及其内容
    except Exception as e:
        print(f"Error clearing contents of {folder_path}: {e}")

def convert_notebooks_to_md(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ipynb'):
                ipynb_file = os.path.join(root, file)
                try:
                    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown', ipynb_file], check=True)
                    subprocess.run(['jupyter', 'nbconvert', '--to', 'pdf', ipynb_file], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {ipynb_file}: {e}")

def copy_md_to_docs(temp_folder, output_folder):
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            if file.endswith('.md'):
                # 计算输出目录
                relative_path = os.path.relpath(root, temp_folder)
                output_dir = os.path.join(output_folder, relative_path)

                # 创建输出目录（如果不存在）
                os.makedirs(output_dir, exist_ok=True)

                # 拷贝文件
                shutil.copy(os.path.join(root, file), os.path.join(output_dir, file))
                print(f"Copied: {file} to {output_dir}")

source_folder = os.path.join(os.getcwd(), '_sources')  # 源文件夹
output_folder = os.path.join(os.getcwd(), 'docs')      # 目标输出文件夹
html_folder = os.path.join(os.getcwd(), 'site')      # 目标输出文件夹

def generate():
    convert_notebooks_to_md(source_folder)
    copy_md_to_docs(source_folder, output_folder)

def clear():
    clear_generate_files(source_folder)
    clear_generate_files(output_folder)
    clear_folder_contents(html_folder)

def build():
    try:
        # 调用 mkdocs build 命令
        subprocess.run(['mkdocs', 'build'], check=True)
        print("MkDocs build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while building MkDocs: {e}")

def serve():
    try:
        # 调用 mkdocs build 命令
        subprocess.run(['mkdocs', 'serve'], check=True)
        print("MkDocs build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while building MkDocs: {e}")

def open():
    # 确保文件路径是绝对路径
    absolute_path = os.path.abspath(os.path.join(html_folder, 'index.html'))
    # 使用默认浏览器打开 HTML 文件
    webbrowser.open(f'file://{absolute_path}')

def main():
    commands = ['auto', 'generate', 'clear', 'build', 'serve', 'open']
    parser = argparse.ArgumentParser(description="A command-line tool.")
    parser.add_argument('command', choices=commands, help="The command to execute.")

    args = parser.parse_args()

    if args.command == 'auto':
        clear()
        generate()
        build()
        open()
    elif args.command == 'generate':
        generate()
    elif args.command == 'clear':
        clear()
    elif args.command == 'build':
        build()
        open()
    elif args.command == 'serve':
        serve()
    elif args.command == 'open':
        open()
    else:
        print(f"Error: unknown command '{args.command}'")

if __name__ == '__main__':
    main()