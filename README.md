# 🐸 🐍 ⚙️

This 'web scraper' aims to collect ads from Brazilian isopod (roly polys) sellers, collecting the ads and turning them into a spreadsheet. The system goes into different sites and collects the title and price of ads, then allows the choice between saving as .csv or .xlsx, review the sites if there is any interesting ad in the spreadsheet :)

# ⚙️ Installation
### Prerequisites
* Python 3.12.3
* pip (pip3 in linux)
* Libraries in 'requirements.txt'

**How to do**
1. Clone the repository:
 ```bash
git clone https://github.com/pythonbyfrogs/Scraper-Isopods
cd "Scraper de Isópodes"
```
2. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```
Windows:
```bash
py -m pip install -r requirements.txt
```
3. Running the scraper:
```bash
python3 main.py
```
Windows:
```bash
py main.py
```
# 👀 Tech stack
### Estructure
The scrapers are in the 'Scrapers' folder. You can only use the individual scraper if you want to check the ads and availability of pillbugs. However, the individual scrapers DO NOT GENERATE SPREADSHEETS. If you want a general spreadsheet, use 'main.py' via the terminal. Feel free to adapt the codes to your needs.
### Sites
The monitored sites are:
* https://www.animalpetstorebr.com.br/bioativo/isopodes/
* https://berreterrarios.lojavirtualnuvem.com.br/isopode/
* https://mercadomorph.com.br/product-category/equipe-de-limpeza/

### Drink more water. 🥤
![Example of the generated spreadsheet](assets/preview.png)