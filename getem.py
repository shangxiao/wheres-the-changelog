import requests
import re


def write_file(package, url):
    with open(f"./pypi/{package}.html", "w") as fh:
        fh.write(f'<meta http-equiv="refresh" content="0;URL=\'{url}\'" />\n')


def getem(packages):
    for package in packages:
        print(package)
        response = requests.get("https://pypi.python.org/pypi/" + package + "/json/")
        json = response.json()
        if info := json.get("info"):
            if project_urls := info.get("project_urls"):
                if changes := project_urls.get("Changes"):
                    print("    pypi: " + changes)
                    write_file(package, changes)
                    continue
                elif changelog := project_urls.get("Changelog"):
                    print("    pypi: " + changelog)
                    write_file(package, changelog)
                    continue

                elif homepage := project_urls.get("Homepage"):
                    hp_response = requests.get(homepage)
                    hp = hp_response.text
                    result = re.search('"defaultBranch":"([^"]*)"', hp)
                    if result:
                        branch = result.groups()[0]

                        result2 = re.search(
                            '"path":"((CHANGELOG|CHANGES)[^"]*)"', hp, re.IGNORECASE
                        )
                        if result2:
                            path = result2.groups()[0]
                            url = homepage + "/blob/" + branch + "/" + path
                            print("    hp: " + url)
                            write_file(package, url)
                            continue

        print("    not found")
