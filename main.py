import sys
import requests

BASE_API_URL = "https://api.frankfurter.dev/v1/"
SUPPORTED_CURRENCIES_URL = BASE_API_URL + "currencies"
CONVERSION_URL = BASE_API_URL + "latest"


def get_supported_currencies():
    try:
        response = requests.get(SUPPORTED_CURRENCIES_URL)
        data = response.json()
        if data:
            return data
        else:
            print("Error getting supported currencies: ", data)
            return None
    except Exception as e:
        print("Error:", str(e))
        return None


def get_converesion(base_currency, target_currency):
    try:
        response = requests.get(CONVERSION_URL, params={
            "base": base_currency,
            "symbols": target_currency
        })
        data = response.json()
        if data.get("rates"):
            return data.get("rates")
        else:
            print("Error in conversion: ", data)
            return None
    except Exception as e:
        print("Error:", str(e))
        return None


if __name__ == "__main__":
    currencies = get_supported_currencies()
    if len(sys.argv) != 3:
        print("Usage: python main.py <base_currency> <target_currency>")
        print("Supported currencies:")
        for code, name in currencies.items():
            print(f"{code} - {name}")
    else:
        base_currency = sys.argv[1]
        target_currency = sys.argv[2]
        if base_currency not in currencies:
            print(f"Base currency '{base_currency}' is not supported.")
        if target_currency not in currencies:
            print(f"Target currency '{target_currency}' is not supported.")
        if base_currency in currencies and target_currency in currencies:
            print(f"Converting from {base_currency} to {target_currency}")
            rate = get_converesion(base_currency, target_currency)
            print("Conversion rate: ", rate.get(target_currency))
