import os
from rich.tree import Tree
from rich.console import Console
from io import StringIO
import pyperclip

def generate_rich_tree(target_dir):
    tree = Tree(f":file_folder: [bold blue]{os.path.basename(target_dir)}[/bold blue]")
    
    paths_dict = {target_dir: tree}

    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        current_node = paths_dict[root]
        
        for d in sorted(dirs):
            dir_path = os.path.join(root, d)
            paths_dict[dir_path] = current_node.add(f":open_file_folder: [bold green]{d}[/bold green]")
            
        for f in sorted(files):
            if not f.startswith('.'):
                current_node.add(f":page_facing_up: {f}")
                
    return tree

def copy():
    structure = generate_rich_tree(os.getcwd())

    buffer = StringIO()
    Console(file=buffer, force_terminal=False).print(structure)
    pyperclip.copy(buffer.getvalue())
    print("Folder tree structure copied!")