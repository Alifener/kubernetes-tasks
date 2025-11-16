import os
import requests
import re
import json

# Root of your repo
REPO_ROOT = os.getcwd()
SCENARIOS_DIR = os.path.join(REPO_ROOT, "scenarios")

# Kubernetes website raw markdown base URL
BASE_RAW_URL = "https://raw.githubusercontent.com/kubernetes/website/main/content/en/docs/tasks/"

# GitHub API base for content listing
GITHUB_API_BASE = "https://api.github.com/repos/kubernetes/website/contents/content/en/docs/tasks"


def slugify(text):
    """Create folder-friendly names"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def get_task_files_recursive(path="content/en/docs/tasks"):
    """Recursively get all markdown files in tasks folder and subfolders, skipping index.md"""
    api_url = f"https://api.github.com/repos/kubernetes/website/contents/{path}"
    resp = requests.get(api_url)
    resp.raise_for_status()
    data = resp.json()

    md_files = []
    for item in data:
        if item['type'] == 'file' and item['name'].endswith(".md") and item['name'] != "index.md":
            relative_path = os.path.relpath(item['path'], "content/en/docs/tasks")
            md_files.append(relative_path)
        elif item['type'] == 'dir':
            md_files.extend(get_task_files_recursive(item['path']))
    return md_files


def extract_commands(md_text):
    """Extract commands from markdown code blocks (fenced and indented)"""
    commands = []

    # Fenced code blocks ``` or ```bash
    fenced_blocks = re.findall(r'```(?:bash|sh|shell)?\n(.*?)```', md_text, re.DOTALL)
    for block in fenced_blocks:
        for line in block.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                commands.append(line)

    # Indented code blocks (4+ spaces)
    indented_blocks = re.findall(r'(?:\n {4,}.*)+', md_text)
    for block in indented_blocks:
        for line in block.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                commands.append(line)

    # Filter only likely executable commands
    filtered = []
    for cmd in commands:
        if cmd.startswith(("kubectl", "helm", "docker", "./", "minikube", "kind")):
            filtered.append(cmd)
    return filtered


def create_scenario(md_file):
    """Generate a KillerCoda scenario folder for a task"""
    title = md_file.replace(".md", "").replace("-", " ").title()
    folder_name = slugify(title)
    scenario_path = os.path.join(SCENARIOS_DIR, folder_name)
    os.makedirs(scenario_path, exist_ok=True)

    # index.json
    index_data = {
        "title": title,
        "description": f"Auto-generated scenario from Kubernetes task: {title}",
        "duration": 15,
        "backend": {"imageid": "kubernetes-kubeadm-1node"}
    }
    with open(os.path.join(scenario_path, "index.json"), "w") as f:
        json.dump(index_data, f, indent=2)

    # intro.md
    intro_md = f"# {title}\n\nThis scenario is based on the Kubernetes task: {title}.\nFollow the steps below to practice this task in a real cluster."
    with open(os.path.join(scenario_path, "intro.md"), "w") as f:
        f.write(intro_md)

    # step1.md
    md_raw_url = BASE_RAW_URL + md_file
    resp = requests.get(md_raw_url)
    resp.raise_for_status()
    md_text = resp.text

    commands = extract_commands(md_text)
    step_lines = []
    if commands:
        for i, cmd in enumerate(commands, start=1):
            step_lines.append(f"### Step {i}\n`{cmd}`{{{{exec}}}}")
    else:
        step_lines.append("No executable steps detected automatically.")

    with open(os.path.join(scenario_path, "step1.md"), "w") as f:
        f.write("\n\n".join(step_lines))

    # finish.md
    finish_md = "You have completed this Kubernetes task."
    with open(os.path.join(scenario_path, "finish.md"), "w") as f:
        f.write(finish_md)

    print(f"Scenario created: {folder_name}")


def main():
    os.makedirs(SCENARIOS_DIR, exist_ok=True)
    task_files = get_task_files_recursive()
    print(f"Found {len(task_files)} task markdown files.")
    for md_file in task_files:
        try:
            create_scenario(md_file)
        except Exception as e:
            print(f"Failed {md_file}: {e}")


if __name__ == "__main__":
    main()
