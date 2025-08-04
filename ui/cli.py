
import argparse
from app.trend_parser import generate_outfit

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("trend", nargs="?", default="quiet luxury", help="Enter a fashion trend to translate")
    args, unknown = parser.parse_known_args()

    outfit = generate_outfit(args.trend)
    print("\n👗 Suggested Outfit:\n")
    print(outfit)

if __name__ == "__main__":
    main()
