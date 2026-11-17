
import pandas as pd
from datetime import datetime
from pathlib import Path

from Scrapers import berre_terrarios
from Scrapers import animal_pet_store
from Scrapers import mercado_morph

# Saving in "Dataframes" folder
data_folder = Path("Dataframes")
data_folder.mkdir(exist_ok=True)

date = datetime.now().strftime("%Y-%m-%d")


def main():
    all_products = []

    scrapers = [
        ("berre_terrarios", berre_terrarios.scraper),
        ("animal_pet_store", animal_pet_store.scraper),
        ("mercado_morph", mercado_morph.scraper)
    ]

    for store_name, scraper_function in scrapers:
        print(f"\nScraping {store_name}...")

        try:
            products = scraper_function()

            for product in products:
                all_products.append({
                    "Store": store_name,
                    "Product": product["Product"],
                    "Price": product["Price"],
                })

            print(f"Products collected: {len(products)}")

        except Exception as error:
            print(f"Error scraping {store_name}: {error}")

    if not all_products:
        print("\nNo products were collected.")
        return

    dataframe = pd.DataFrame(all_products)

    print("\nChoose the export format:")
    print("1 - CSV")
    print("2 - Excel (.xlsx)")

    choice = input("Your choice (1/2): ").strip()

    if choice == "1":
        filename = data_folder / f"Isopods_{date}.csv"

        dataframe.to_csv(
            filename,
            index=False,
            sep=";",
            encoding="utf-8-sig"
        )

        print(f"\nData exported to {filename}")

    elif choice == "2":
        filename = data_folder / f"Isopods_{date}.xlsx"

        dataframe.to_excel(
            filename,
            index=False
        )

        print(f"\nData exported to {filename}")

    else:
        print("\nInvalid option. No file was exported.")


if __name__ == "__main__":
    main()
