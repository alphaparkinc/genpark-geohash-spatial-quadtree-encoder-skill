class GeohashEncoder:
    """
    Base32 Geohash Encoder mapping latitude/longitude coordinates
    into hierarchical string tokens.
    """
    BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

    def encode(self, lat, lon, precision=6):
        lat_range = [-90.0, 90.0]
        lon_range = [-180.0, 180.0]
        geohash = []
        bits = [16, 8, 4, 2, 1]
        bit = 0
        ch = 0
        even = True

        while len(geohash) < precision:
            if even:
                mid = (lon_range[0] + lon_range[1]) / 2.0
                if lon > mid:
                    ch |= bits[bit]
                    lon_range[0] = mid
                else:
                    lon_range[1] = mid
            else:
                mid = (lat_range[0] + lat_range[1]) / 2.0
                if lat > mid:
                    ch |= bits[bit]
                    lat_range[0] = mid
                else:
                    lat_range[1] = mid

            even = not even
            if bit < 4:
                bit += 1
            else:
                geohash.append(self.BASE32[ch])
                bit = 0
                ch = 0

        return "".join(geohash)
