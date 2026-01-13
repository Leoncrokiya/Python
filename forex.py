try:
    from forex_python.converter import CurrencyRates
    from forex_python.bitcoin import BtcConverter
    FOREX_AVAILABLE = True
except Exception as e:
    CurrencyRates = None
    BtcConverter = None
    FOREX_AVAILABLE = False
    IMPORT_ERROR = e

from decimal import Decimal, InvalidOperation

def currency_converter():

    print("=== Currency Converter ===")
    print("Example currency codes: USD, EUR, GBP, ZAR, JPY, BTC")
    print("Type 'exit' at any time to quit.\n")

    while True:
        try:
            if not FOREX_AVAILABLE:
                print("Required package 'forex-python' is not installed or could not be imported.")
                print("Install it with: python -m pip install forex-python")
                if 'IMPORT_ERROR' in globals():
                    print("Import error:", IMPORT_ERROR)                
                return None
            c = CurrencyRates()
            btc = BtcConverter()
            # Get amount
            amount_str = input("Enter amount: ").strip()
            if amount_str.lower() == "exit":
                print("Goodbye!")
                break

            try:
                amount = Decimal(amount_str)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
            except InvalidOperation:
                print("Invalid amount. Please enter a numeric value.")
                continue

            # Get source currency
            from_currency = input("From currency (e.g., USD): ").strip().upper()
            if from_currency.lower() == "exit":
                break

            # Get target currency
            to_currency = input("To currency (e.g., EUR): ").strip().upper()
            if to_currency.lower() == "exit":
                break

            # Perform conversion
            if from_currency == "BTC" or to_currency == "BTC":
                # Bitcoin conversion
                if from_currency == "BTC":
                    result = btc.convert_btc_to_cur(float(amount), to_currency)
                else:
                    result = btc.convert_to_btc(float(amount), from_currency)
            else:
                result = c.convert(from_currency, to_currency, float(amount))
            # Safely format numeric results; fall back to plain printing otherwise
            try:
                result_num = float(result)
                print(f"{amount} {from_currency} = {result_num:.2f} {to_currency}\n")
            except Exception:
                print(f"{amount} {from_currency} = {result:.2f} {to_currency}\n")

        except Exception as e:
            print(f"Error: {e}\n")
            
    return to_currency

if __name__ == "__main__":
    currency_converter()