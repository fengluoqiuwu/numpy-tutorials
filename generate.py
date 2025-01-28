import argparse
import os
import shutil
import subprocess
import webbrowser
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

def clear_generate_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
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

def convert_notebook(ipynb_file):
    try:
        subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown', ipynb_file], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {ipynb_file}: {e}")

def convert_notebooks(folder_path, recursion: bool = True):
    print(folder_path)
    ipynb_files = []

    if recursion:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.ipynb'):
                    ipynb_files.append(os.path.join(root, file))
    else:
        for file in os.listdir(folder_path):
            if file.endswith('.ipynb'):
                ipynb_files.append(os.path.join(folder_path, file))

    # 使用 tqdm 显示进度条
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(convert_notebook, ipynb_file): ipynb_file for ipynb_file in ipynb_files}
        with tqdm(total=len(futures), desc="Converting Notebooks") as pbar:
            for _ in as_completed(futures):
                pbar.update(1)

def copy_md_to_docs(source_folder, output_folder, recursion: bool = True):
    if recursion:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith(('.md', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
                    # 计算输出目录
                    relative_path = os.path.relpath(root, source_folder)
                    output_dir = os.path.join(output_folder, relative_path)

                    # 创建输出目录（如果不存在）
                    os.makedirs(output_dir, exist_ok=True)

                    # 拷贝文件
                    shutil.copy(os.path.join(root, file), os.path.join(output_dir, file))
    else:
        for file in os.listdir(source_folder):
            if file.endswith(('.md', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):

                # 创建输出目录（如果不存在）
                os.makedirs(output_folder, exist_ok=True)

                # 拷贝文件
                shutil.copy(os.path.join(source_folder, file), os.path.join(output_folder, file))

source_folder = os.path.join(os.getcwd(), '_sources')  # 源文件夹
output_folder = os.path.join(os.getcwd(), 'docs')      # 目标输出文件夹
html_folder = os.path.join(os.getcwd(), 'site')      # 目标输出文件夹

def generate(path):
    if path == None:
        convert_notebooks(source_folder)
        copy_md_to_docs(source_folder, output_folder)
    elif path == '.':
        convert_notebooks(source_folder, recursion=False)
        copy_md_to_docs(source_folder, output_folder, recursion=False)
    else:
        convert_notebooks(source_folder+path)
        copy_md_to_docs(source_folder+path, output_folder+path)

def clear():
    clear_generate_files(source_folder)
    clear_generate_files(output_folder)
    clear_folder_contents(html_folder)

def build():
    clear_folder_contents(html_folder)
    try:
        # 调用 mkdocs build 命令
        subprocess.run(['mkdocs', 'build'], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
    parser.add_argument('--path', type=str, help="An optional string parameter.")

    args = parser.parse_args()

    if args.command == 'auto':
        if args.path is None:
            clear()
        generate(args.path)
        build()
        open()
    elif args.command == 'generate':
        generate(args.path)
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