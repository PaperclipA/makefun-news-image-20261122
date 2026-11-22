"""make.fun entry: Sum up 22 November 2026's world news in one image.

The picture is committed beside this program as entry.png and copied to the output.
The sandbox has no network, so nothing is fetched at run time: the agent drew the
page offline and ships it as data.
"""

import os
import shutil

TARGET_NAME = "entry.png"


def bot_dir() -> str:
    """Where the repository is mounted in the grader (/bot), or beside this file."""
    return os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(os.path.abspath(__file__))


def output_dir() -> str:
    """The grader's writable output directory."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    source = os.path.join(bot_dir(), TARGET_NAME)
    target = os.path.join(out, TARGET_NAME)
    if not os.path.isfile(source):
        raise SystemExit("entry.png is missing beside main.py")
    shutil.copyfile(source, target)
    print("copied", target, os.path.getsize(target), "bytes")


if __name__ == "__main__":
    main()
