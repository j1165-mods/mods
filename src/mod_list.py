import time

from googlesearch import search

input_file = "../README.md"
output_file = "mod_list.md"

# Open the input file and read its contents
with open(input_file, "r") as file:
    lines = file.readlines()

# Create a new file for writing the search results
with open(output_file, "w") as file:
    # Loop through each line
    for line in lines:

        # Markdown table
        # Columns: | Mod Name | Version | Notes |
        # Ignore notes column for now

        # Example
        # | Mod Name                 |    Version    | Notes                 |
        # |:-------------------------|:-------------:|:----------------------|

        if not line.startswith("|") or line.startswith("|:") or line.startswith("| Mod Name"):
            continue

        # Split the line into columns
        columns = line.split("|")

        mod_name = columns[1].strip()
        mod_version = columns[2].strip()

        print(f"Searching for {mod_name} {mod_version}...")

        # Search for the mod
        search_results = search(f"{mod_name} {mod_version} minecraft 1.18.2 curseforge", num_results=3)
        total_results = 0
        file.write(f"# {mod_name} | {mod_version} ")
        file.write("\n")

        # Write the search results
        for result in search_results:
            file.write("\n")
            total_results += 1
            result_title = result.split("/")[-1]
            result_title = result_title.replace("-", " ")
            file.write(f"- [{result_title}]({result})")

        print(f"- Found {total_results} results")

        file.write("\n\n\n")
        time.sleep(0.5)
