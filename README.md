# Matopeli

Pieni Pythonilla tehty klassinen matopeli.  
Toteutettu `pygame`-kirjastolla ja julkaistu `.exe`-muodossa automaattisesti GitHub Actionsin avulla.

[Lataa uusin versio]([https://github.com/nilenos/super-matopeli/releases/tag/auto-latest](https://github.com/nilenos/matopeli/releases)

[![GitHub release](https://img.shields.io/github/v/tag/nilenos/super-matopeli?label=versio)](https://github.com/nilenos/super-matopeli/releases)

---

## Näyttökuva

![Matopeli-näyttökuva](screenshots/matopeli.png)

> Lisää `screenshots/matopeli.png`-kuvatiedosto projektiisi, jotta se näkyy GitHubissa.

---

## 🎮 Ohjeet

- Käynnistä peli tuplaklikkaamalla `matopeli.exe`
- Ohjaa matoa nuolinäppäimillä
- Syö punaiset ruuat kasvattaaksesi matoa
- Älä törmää seinään tai itseesi!

---

## Testaus

Projektissa käytetään `pytest`-yksikkötestejä ja `pytest-cov`-kattavuusraportointia.  
Testit ajetaan automaattisesti GitHub Actionsin CI-putkessa jokaisen commitin yhteydessä.

```bash
pytest --cov=. --cov-report=html
```

---

## ⚙️ Kehittäjille

### Asenna riippuvuudet:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Aja peli:

```bash
python matopeli.py
```

### Rakenna .exe-tiedosto (vaatii PyInstaller):

```bash
pyinstaller --onefile matopeli.py
```

---

##  Kehittäjä

[GitHub: nilenos](https://github.com/nilenos)

Ota yhteyttä parannusehdotusten tai kysymysten osalta!

---

© 2025 Super Matopeli – avoin lähdekoodi MIT-lisenssillä
