from flask import Flask, render_template
import os
import importlib
import json

app = Flask(__name__)

def get_project_info(project_dir):
    config_path = os.path.join(project_dir, 'project_config.json')
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            return config.get('display_name', os.path.basename(project_dir))
    return os.path.basename(project_dir)

@app.route('/')
def home():
    projects_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects')
    projects = []
    for project in os.listdir(projects_dir):
        project_path = os.path.join(projects_dir, project)
        if os.path.isdir(project_path):
            display_name = get_project_info(project_path)
            projects.append({"name": display_name, "url": f"/{project}"})
    
    return render_template('home.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html', is_home=True)

# Dynamically import and register project routes
projects_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'projects')
for project in os.listdir(projects_dir):
    project_path = os.path.join(projects_dir, project)
    if os.path.isdir(project_path):
        try:
            module = importlib.import_module(f'projects.{project}.routes')
            if hasattr(module, 'bp'):
                app.register_blueprint(module.bp, url_prefix=f'/{project}')
        except ImportError as e:
            print(f"Could not import routes for project: {project}. Error: {e}")

# At the end of app.py
if __name__ == '__main__':
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")
    app.run(debug=True)