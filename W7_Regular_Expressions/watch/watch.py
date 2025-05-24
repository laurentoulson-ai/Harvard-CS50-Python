"""
Task: Take a HTML Youtube embed as input, and output direct Youtube link
example input: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
example output: https://youtu.be/xvFZjo5PgG0
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Check if it's an iframe tag
    if not s.strip().startswith("<iframe"):
        return None

    """
    Regex needs to check that:
    1) link preceded by src=
    2) valid youtube link, no typos
    3) valid video ID chars - len checked later
    """
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11}))"'
    match = re.search(pattern, s)

    if match:
        video_id = match.group(2)
        if len(video_id) == 11:  # Standard YouTube video ID length
            return f"https://youtu.be/{video_id}"

    else:
        None


if __name__ == "__main__":
    main()
