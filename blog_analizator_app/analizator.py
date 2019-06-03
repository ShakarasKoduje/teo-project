import asyncio
import datetime

from web_scraper import modelScraper


async def ZebranieStron():

        await asyncio.sleep(1)
        print("Zebranie Stron Umieszczam przedmiot w kolejce")
        z = modelScraper.zbieraczStronBloga()
        return z

async def PrzetworzenieStron(a):
        await asyncio.sleep(1)
        print("Otrzymuje przedmiot z kolejki Przetworzenie Stron")

        z = modelScraper.ekstraktorStronWpisow(a)
        return z

async def PrzetworzenieWpisow(a):
        await asyncio.sleep(1)
        print("Przetworzenie Wpisow Otrzymuje przedmiot z kolejki")

        z = modelScraper.tworzenieModeli(a)
        return z

async def WypisanieModeli(item):
        await asyncio.sleep(1)
        for i in item:
            print(f"{i['title']}")




async def main():
    while True:
        print(f"Próba rozpoczęta w {datetime.datetime.now()}")
        try:
            strony = await ZebranieStron()
            przetworzenieStron = await PrzetworzenieStron(strony)
            przetworzenieWpisow = await PrzetworzenieWpisow(przetworzenieStron)
            await WypisanieModeli(przetworzenieWpisow)
        except:
            print("BŁĄD")
            break

        await asyncio.sleep(60)
        print(f"Koniec próby w  {datetime.datetime.now()}")
        print("====================================")
asyncio.run(main())
print("KONIEC WSZYSTKICH PROCESÓW.")