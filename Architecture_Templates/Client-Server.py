import os

project_name = 'my_project'
base_files = ["README.md", ".env", "requirements.txt"]

structure = {
    project_name : {'client': {'components': ['Navbar.jsx', 'Input.jsx'],
                                'pages': ['Home.jsx', 'Login.jsx', 'Dashboard.jsx'],
                                'services' : ['authService.js', 'modelService.js', 'api.js'],
                                'assets': ['styles/'],
                                '.': ['main.js']
                                },
                    'server': {'controllers' : ['modelController.js', 'authController.js'],
                               'services': ['service.js', 'authService.js'],
                               'models' : ['model.js'],
                               'routes': ['modelRoutes.js'],
                               'config': ['logger.js', 'db_connection.js'],
                               '.': ['server.js']
                                }
                    }
}

def create_file(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# File: {os.path.basename(path)}\n")


def create_structure_recursive(base_path, structure):
    for name, content in structure.items():
        current_path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(current_path, exist_ok=True)
            create_structure_recursive(current_path, content)

        elif isinstance(content, list):
            os.makedirs(current_path, exist_ok=True)
            for item in content:
                if isinstance(item, str):
                    item_path = os.path.join(current_path, item)
                    if item.endswith("/"):
                        os.makedirs(item_path, exist_ok=True)
                    else:
                        create_file(item_path)
                elif isinstance(item, dict):
                    create_structure_recursive(current_path, item)


if __name__ == "__main__":
    base_dir = os.path.join(".", project_name)
    create_structure_recursive(".", structure)

    for file in base_files:
        create_file(os.path.join(base_dir, file))

    print("Structure generated successfully.")