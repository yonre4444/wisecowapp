import re

logfile = "access.log"

def analyze_log(file):
    with open(file, "r") as f:
        logs = f.readlines()

    errors_404 = [line for line in logs if "404" in line]
    most_requested = {}
    for line in logs:
        match = re.search(r'GET (.*?) ', line)
        if match:
            page = match.group(1)
            most_requested[page] = most_requested.get(page, 0) + 1

    print(f"Total 404 errors: {len(errors_404)}")
    print("Top requested pages:")
    for page, count in sorted(most_requested.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{page} -> {count} times")

if __name__ == "__main__":
    analyze_log(logfile)
