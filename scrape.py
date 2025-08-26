from bs4 import BeautifulSoup
import requests
import os


response = requests.get("https://www.maths.cam.ac.uk/postgrad/part-iii/part-iii-guide-courses")
parsed = BeautifulSoup(response.text, "html.parser")

tables = parsed.find_all("table")

os.makedirs("Part III Guide to Courses")
os.chdir("website")

count = 1 # Rename folders once scraping is done
total_courses = 0
for table in tables:
    os.makedirs(str(count))
    sublinks = list(map(lambda x: (x.get_text(strip = True), x.get("href")), table.find_all("a", href = True)))
    for sublink in sublinks:
        os.makedirs(f"{count}\\{sublink[0]}")
        response = requests.get(sublink[1])
        parsed = BeautifulSoup(response.text, "html.parser")
    

        table = parsed.find("table")
        subsublinks = list(map(lambda x: (x.get_text(strip = True), x.get("href")), table.find_all("a", href = True)))
        total_courses += len(subsublinks)
        for link in subsublinks:
            response = requests.get(link[1], stream=True)
            response.raise_for_status()  # Ensure we have a 200 OK

            with open(f"{count}\\{sublink[0]}\\{link[0]}.pdf", "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            pass
    count += 1
print(total_courses)