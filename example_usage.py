from client import GeohashEncoder

def main():
    print("=== Testing Geohash Spatial Encoder ===")
    encoder = GeohashEncoder()
    gh = encoder.encode(37.7749, -122.4194, precision=6)
    print("San Francisco geohash:", gh)
    assert len(gh) == 6
    assert gh.startswith("9q8y")
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
