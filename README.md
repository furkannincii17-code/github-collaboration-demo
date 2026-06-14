# GitHub Collaboration Demo

Basit bir hesap makinesi (calculator) kutuphanesi. Bu depo, iki kisilik bir
ekibin GitHub uzerindeki **Pull Request**, **Code Review** ve
**GitHub Actions (CI)** is akisini gostermek icin olusturulmustur.

## Roller
- **Furkan Inci** — Reviewer / Maintainer (depo sahibi, CI kurulumu, PR inceleme ve merge)
- **Barash Vatansever** — Developer / Author (ozellik gelistirme, Pull Request, test)

## Calistirma
```bash
pip install -r requirements.txt
pytest -v
```

## CI
Her `push` ve `pull_request` olayinda GitHub Actions testleri otomatik calistirir.
