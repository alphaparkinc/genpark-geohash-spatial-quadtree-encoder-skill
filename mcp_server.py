import sys
import json
from client import GeohashEncoder

def main():
    encoder = GeohashEncoder()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "encode":
            gh = encoder.encode(params.get("lat", 0.0), params.get("lon", 0.0), params.get("precision", 6))
            res = {"geohash": gh}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
