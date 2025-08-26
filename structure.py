import os

OUTPUT = open("README.md", "w+")

main_dir = "Part III Guide to Courses"
sections = os.listdir(main_dir)

for section in sections:
    OUTPUT.write(f"# {section}\n\n")
    for subsection in os.listdir(f"{main_dir}\\{section}"):
        OUTPUT.write(f"## {subsection}\n")
        for file in os.listdir(f"{main_dir}\\{section}\\{subsection}"):
            OUTPUT.write(f"[ ] {file.replace(".pdf", "")}\n")
        OUTPUT.write("\n")
    OUTPUT.write("\n")