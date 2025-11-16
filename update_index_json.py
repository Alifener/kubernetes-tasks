import os
import json

# Root of your repo
REPO_ROOT = os.getcwd()
SCENARIOS_DIR = os.path.join(REPO_ROOT, "scenarios")

def update_index_json(scenario_folder):
    """
    Update index.json with the 'details' block pointing to intro.md and step1.md
    """
    index_path = os.path.join(scenario_folder, "index.json")
    if not os.path.exists(index_path):
        print(f"No index.json found in {scenario_folder}, skipping...")
        return

    # Load existing index.json
    with open(index_path, "r") as f:
        try:
            index_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Invalid JSON in {index_path}, skipping...")
            return

    # Update details block
    details = {
        "intro": {"text": "intro.md"},
        "steps": []
    }

    # Automatically detect step files
    step_files = sorted([
        f for f in os.listdir(scenario_folder)
        if f.startswith("step") and f.endswith(".md")
    ])

    for step_file in step_files:
        details["steps"].append({"text": step_file})

    index_data["details"] = details

    # Write back updated index.json
    with open(index_path, "w") as f:
        json.dump(index_data, f, indent=2)

    print(f"Updated index.json in {scenario_folder}")


def main():
    if not os.path.exists(SCENARIOS_DIR):
        print(f"No scenarios folder found at {SCENARIOS_DIR}")
        return

    # Iterate over scenario folders
    for scenario_name in os.listdir(SCENARIOS_DIR):
        scenario_path = os.path.join(SCENARIOS_DIR, scenario_name)
        if os.path.isdir(scenario_path):
            update_index_json(scenario_path)

if __name__ == "__main__":
    main()

