import json
import sys
import pathlib

target = pathlib.Path(sys.argv[1])

with open(target, encoding="utf-8") as f:
    data = json.loads(f.read())

out_filename = target.stem + ".min.json"
with open(out_filename, "w", encoding="utf-8") as f:
    json.dump(
        data,
        f,
        separators=(",", ":"), # Remove space
        ensure_ascii=False # Don't use escape sequence for unicode chars
    )
