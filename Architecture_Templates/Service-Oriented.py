import os

project_name = 'my_project'
base_files = ["main.py", "README.md", ".env", "requirements.txt"]
number_modules = 3

def create_struture(num_module):
    module = f"module_{num_module}"
    structure = {
        project_name : {'services': { module : {'api': ['billing_controller.py', 'schemas.py', 'routes.py'],
                                    'logic': ['service.py'],
                                    'data': ['repository.py', 'model.py', 'db_connection.py']
                                  }
                        },
                        'commons' : ['exceptions.py', 'helpers.py', 'constants.py', 'dto.py', 'config.py'],
                        'integration' : ['adapter.py', 'provider.py', 'connector.py'],
                        'gateway' : ['api_gateway.py', 'routes/', 'auth_middleware.py', 'rate_limiter.py']
                        }
    }
    return structure

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

    for i in range(0, number_modules):
        structure = create_struture(i)
        create_structure_recursive(".", structure)

    for file in base_files:
        create_file(os.path.join(base_dir, file))

    print("Structure generated successfully.")