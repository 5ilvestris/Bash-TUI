import subprocess
import os

def run_tui_checklist():
    try:
        options = [
            ["AAA", "Choice 1", "off"],
            ["BBB", "Choice 2", "off"],
            ["CCC", "Choice 3", "off"],
            ["DDD", "Choice 4", "off"],
        ]
        
        dialog_args = [item for sublist in options for item in sublist]
        output_filepath = "/tmp/checklist_choices.txt"

        # Commands
        command = [
            "dialog",
            "--title", "Feature Selection",
            "--checklist", "Select features to enable:",
            "15", "50", "4",  # Height, Width, List Height
            *dialog_args
        ]
        # Run everything
        result = subprocess.run(
            command,
            stderr=subprocess.PIPE,
        )
        with open(output_filepath, 'w') as f:
            f.write(result.stderr.decode('utf-8'))
        # Execute
        if result.returncode == 0:
            with open(output_filepath, 'r') as f:
                raw_choices = f.read().strip()
            # List results
            selected_choices = raw_choices.replace('"', '').split()
            # Write output
            os.system("clear")
            print("\n--------- SONUC ---------")
            if selected_choices:
                print(f" You selected {len(selected_choices)} of them.")
                for choice in selected_choices:
                    print(f"- {choice}")
            else:
                os.system("clear")
                print("Nothing selected.")
        else:
            os.system("clear")
            print("\nCancelled by user.")
        # Remove old file
        if os.path.exists(output_filepath):
            os.remove(output_filepath)
    exceot:
        print("An error just happened or operation cancelled by user.")
run_tui_checklist()
