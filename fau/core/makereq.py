import os 
import sys
import importlib.metadata

def reqFile():
    files = [f for f in os.listdir('.') if f.endswith('.py') and f != os.path.basename(__file__)]

    libs_need = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith("from "):
                    parts = line.split()
                    if len(parts) > 1 and f"{parts[1].split('.')[0]}.py" not in files:
                        libs_need.append(parts[1].split('.')[0])
                        
                elif line.startswith("import "):
                    parts = line.split()
                    if len(parts) > 1 and f"{parts[1].split('.')[0]}.py" not in files:
                        libs_need.append(parts[1].split('.')[0])

    cleaned_libs = [lib.split('.')[0] for lib in libs_need]
    unique_libs = list(set(cleaned_libs))
    standard_libs = set(sys.builtin_module_names) | getattr(sys, "stdlib_module_names", set())
    external_packages = [lib for lib in unique_libs if lib not in standard_libs]

    libs = []
    try:
        for lib in external_packages:
            version = importlib.metadata.version(lib)
            libs.append(f"{lib}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print("Package is not installed in the local environment.")
        libs.append(lib)


    with open('requirements.txt', 'w', encoding='utf-8') as f:
        for i in libs:
            f.write(i+"\n")