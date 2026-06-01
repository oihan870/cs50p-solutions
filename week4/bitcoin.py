import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "YOUR_API_KEY"

    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        )
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Request failed")

    total = n * price

    print(f"{total:,.4f}")


if __name__ == "__main__":
    main()
