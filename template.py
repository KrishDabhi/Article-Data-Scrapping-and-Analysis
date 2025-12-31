import os

def create_folder_structure():
    base_dir = "D:\Work\Project - 5"
    
    # Create main directories
    os.makedirs(base_dir, exist_ok=True)
    os.makedirs(os.path.join(base_dir, "input"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "output"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "articles"), exist_ok=True)
    
    # Create empty files
    open(os.path.join(base_dir, "input", "Input.xlsx"), 'w').close()
    open(os.path.join(base_dir, "requirements.txt"), 'w').close()
    open(os.path.join(base_dir, "README.md"), 'w').close()
    
    # Create Python files with basic structure
    py_files = ["scraper.py", "analysis.py", "main.py"]
    for py_file in py_files:
        with open(os.path.join(base_dir, py_file), 'w') as f:
            f.write('"""\nBlackCoffer task - {} \n"""\n'.format(py_file.replace('.py', '').title()))

    print(f"Project structure created in '{base_dir}/'")
    print("\n Structure:")
    print("blackcoffer-task/")
    print("├── input/")
    print("│   └── Input.xlsx")
    print("├── output/")
    print("├── articles/")
    print("├── scraper.py")
    print("├── analysis.py")
    print("├── main.py")
    print("├── requirements.txt")
    print("└── README.md")

if __name__ == "__main__":
    create_folder_structure()