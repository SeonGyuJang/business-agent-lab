#!/usr/bin/env python3
"""Simulated booking service for the Week 02 classroom demonstration.

Every reply is fictional. Nothing here contacts an artist, an agency, or the internet.

Usage:
  python booking.py quote "aespa"
  python booking.py availability "BLACKPINK" 2027-04-17
  python booking.py list
"""
import sys

EVENT_DATE = "2027-04-17"

# Fictional event quotes in USD, availability on EVENT_DATE, and the hours the act can play.
# SEVENTEEN can only play late, so a lineup with them has to be ordered and timed.
# Quotes for acts with a public CTI range sit inside that range.
# ponytail: fixed table, edit here to change the run's outcome.
TABLE = {
    "BLACKPINK":   {"quote": 4_200_000, "available": False, "window": None},
    "CORTIS":      {"quote":   350_000, "available": True,  "window": ("19:00", "22:30")},
    "aespa":       {"quote":   620_000, "available": True,  "window": ("19:00", "22:30")},
    "ATEEZ":       {"quote": 2_200_000, "available": True,  "window": ("19:00", "22:30")},
    "NewJeans":    {"quote": 1_100_000, "available": False, "window": None},
    "TWICE":       {"quote": 3_800_000, "available": True,  "window": ("19:00", "22:30")},
    "SEVENTEEN":   {"quote":   700_000, "available": True,  "window": ("21:30", "22:30")},
    "LE SSERAFIM": {"quote":   900_000, "available": True,  "window": ("19:00", "22:30")},
}

TAG = "SIMULATED booking service reply."


def find(name):
    key = name.strip().lower()
    for artist in TABLE:
        if artist.lower() == key:
            return artist
    return None


def quote(name):
    artist = find(name)
    if artist is None:
        return f"{TAG} No record for '{name}'. Known acts: {', '.join(TABLE)}."
    return f"{TAG} Quote for {artist}, one 45-minute set on {EVENT_DATE}: USD {TABLE[artist]['quote']:,}. Fee only; travel and production not included."


def availability(name, date):
    artist = find(name)
    if artist is None:
        return f"{TAG} No record for '{name}'. Known acts: {', '.join(TABLE)}."
    if date != EVENT_DATE:
        return f"{TAG} This service only answers for {EVENT_DATE}."
    row = TABLE[artist]
    if not row["available"]:
        return f"{TAG} {artist} is not available on {date}."
    a, b = row["window"]
    return f"{TAG} {artist} is available on {date} from {a} to {b}."


def main(argv):
    if len(argv) >= 2 and argv[1] == "quote" and len(argv) == 3:
        print(quote(argv[2]))
    elif len(argv) >= 2 and argv[1] == "availability" and len(argv) == 4:
        print(availability(argv[2], argv[3]))
    elif len(argv) == 2 and argv[1] == "list":
        print(f"{TAG} Known acts: {', '.join(TABLE)}.")
    elif len(argv) == 2 and argv[1] == "--selftest":
        assert "4,200,000" in quote("blackpink")
        assert "not available" in availability("NewJeans", EVENT_DATE)
        assert "from 19:00 to 22:30" in availability("aespa", EVENT_DATE)
        assert "from 21:30 to 22:30" in availability("SEVENTEEN", EVENT_DATE)
        assert "No record" in quote("MAMAMOO")
        assert "only answers" in availability("TWICE", "2027-04-18")
        print("selftest ok")
    else:
        print(__doc__.strip())
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
