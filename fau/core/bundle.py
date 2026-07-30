import os
import zipfile
import time
import subprocess

def copy_file_to_clipboard(file_path):
    """Copies a file to the clipboard by safely invoking the native Windows Shell."""
    abs_path = os.path.abspath(file_path)
    subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", "Set-Clipboard", "-Path", abs_path],
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    time.sleep(0.5)

def count_valid_files(root_dir, extensions, exclude_dirs):
    """Counts files matching the extension criteria to enforce the 1000-file limit."""
    count = 0
    for _, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for file in filenames:
            if file.lower().endswith(extensions):
                count += 1
    return count

def create_copy_and_clean_bundle():
    current_dir = os.getcwd()
    dir_name = os.path.basename(current_dir) if os.path.basename(current_dir) else "project"
    
    output_zip_path = os.path.join(current_dir, f"{dir_name}_bundle.zip")
    temp_text_name = "CODEBASE_CONTEXT.txt"
    temp_text_path = os.path.join(current_dir, temp_text_name)
    
    extensions = ('.py', '.txt', '.png', '.jpg', '.jpeg', '.gif', '.ttf', '.mp3', '.mp4')
    text_extensions = ('.py', '.pyw', '.txt', '.cs', '.rs', '.cpp', '.html', '.css', '.js', '.dart', '.c', '.java', '.md', '.ipynb')
    exclude_dirs = ('.git', '__pycache__', 'venv', '.vscode')

    total_files = count_valid_files(current_dir, extensions, exclude_dirs)
    print(f"Current Directory: {current_dir}")
    print(f"Found {total_files} matching files.")
    
    if total_files >= 1000:
        print(f"Execution Aborted: Directory contains {total_files} files, exceeding the 1000 file threshold.")
        return

    try:
        with open(temp_text_path, 'w', encoding='utf-8') as outfile:
            outfile.write("=== CODEBASE TEXT CONTEXT ===\n")
            outfile.write("Files: ")
            outfile.write(", ".join(file for _, _, filenames in os.walk(current_dir) for file in filenames if file.endswith(('.py', '.pyw', '.txt', '.cs', '.rs', '.cpp', '.html', '.css', '.js', '.dart', '.c', '.java', '.md', '.ipynb')) and file != 'CODEBASE_CONTEXT.txt'))
            outfile.write("\n")
            for dirpath, dirnames, filenames in os.walk(current_dir):
                dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
                for file in filenames:
                    if file.lower().endswith(text_extensions) and file != temp_text_name:
                        file_path = os.path.join(dirpath, file)
                        relative_path = os.path.relpath(file_path, current_dir)
                        outfile.write(f"\n{'='*20}\n")
                        outfile.write(f"File Content: {relative_path}\n")
                        outfile.write(f"{'='*20}\n\n")
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='replace') as infile:
                                outfile.write(infile.read())
                        except Exception as e:
                            outfile.write(f"Error reading file: {e}\n")
                        outfile.write("\n\n")

        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(temp_text_path, temp_text_name)
            for dirpath, dirnames, filenames in os.walk(current_dir):
                dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
                for file in filenames:
                    if file.lower().endswith(extensions) and file != temp_text_name and file != os.path.basename(output_zip_path) and not file.lower().endswith(text_extensions):
                        file_path = os.path.join(dirpath, file)
                        relative_path = os.path.relpath(file_path, current_dir)
                        zipf.write(file_path, relative_path)
        print(f"ZIP package staged at: {output_zip_path}")
        copy_file_to_clipboard(output_zip_path)
        print("Success! File copied to clipboard. You can now press Ctrl+V directly into your browser.")
    finally:
        if os.path.exists(temp_text_path):
            os.remove(temp_text_path)

if __name__ == "__main__":
    create_copy_and_clean_bundle()
