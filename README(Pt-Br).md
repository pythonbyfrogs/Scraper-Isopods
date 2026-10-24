# 🐸 🐍 ⚙️

Este 'web scraper' tem como objetivo coletar anúncios de vendedores de isópodes (tatuzinhos-de-jardim) brasileiros, coletando os anúncios e transformando em uma planilha. O sistema entra em diferentes sites e coleta o título e preço dos anúncios, em seguida, permite a escolha entre salvar como .csv ou .xlsx, revise os sites caso haja algum anúncio interessante na planilha :)

# ⚙️ Instalação
### Pré-requisitos
* Python 3.12.3
* pip (pip3 no linux)
* Bibliotecas em 'requirements.txt'

**Passo a passo**
1. Clone o repositório:
 ```bash
git clone https://github.com/pythonbyfrogs/Scraper-Isopods
cd "Scraper de Isópodes"
```
2. Instale as dependências:
```bash
python3 -m pip install -r requirements.txt
```
Windows:
```bash
py -m pip install -r requirements.txt
```
3. Para rodar o scraper:
```bash
python3 main.py
```
Windows:
```bash
py main.py
```
# 👀 Detalhes técnicos
### Estrutura
Os scrapers estão na pasta 'Scrapers', é possível utilizar apenas o scraper individual caso queira verificar os anúncios e a disponibilidade de tatuzinhos-de-jardim, no entanto, os scrapers individuais NÃO GERAM PLANILHAS, caso queira uma planilha geral, utilize o 'main.py' via terminal. Sinta-se à vontade para adaptar os códigos ao seu desejo.
### Sites
Os sites monitorados são:
* https://www.animalpetstorebr.com.br/bioativo/isopodes/
* https://berreterrarios.lojavirtualnuvem.com.br/isopode/
* https://mercadomorph.com.br/product-category/equipe-de-limpeza/

### Beba água. 🥤
![Example of the generated spreadsheet](assets/preview.png)