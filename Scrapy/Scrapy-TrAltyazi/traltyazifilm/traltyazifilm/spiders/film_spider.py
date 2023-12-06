import scrapy
import json


class FilmSpider(scrapy.Spider):
    name = 'film_spider'
    start_urls = ['https://www.turkcealtyazi.org/imdb250.html']

    def parse(self, response):
        film_verileri = []

        film_adi_tr = response.css('td.rowbeyaz a span::text').extract()
        film_adi_orginal = response.css(
            'td.rowbeyaz span:nth-child(3)::text').extract()
        imdb_oy_sayisi = response.css(
            'td.rowbeyaz span:nth-child(2)::text').extract()
        imdb_oy_ortalamasi = response.css('td.rowbeyaz span b::text').extract()
        tra_oy_sayisi = response.css('td.rowbeyaz div span::text').extract()
        tra_oy_ortalamasi = response.css(
            'td.rowbeyaz div span strong::text').extract()

        for i in range(len(film_adi_tr)):
            film = {
                "Film Adı (TR)": film_adi_tr[i],
                "Film Adı (Orijinal)": film_adi_orginal[i],
                "IMDb Oy Sayısı": imdb_oy_sayisi[i],
                "IMDb Oy Ortalaması": imdb_oy_ortalamasi[i],
                "TRAltazi Oy Sayısı": tra_oy_sayisi[i],
                "TRAltazi Oy Ortalaması": tra_oy_ortalamasi[i]
            }
            film_verileri.append(film)

        # Verileri JSON formatında bir dosyaya yaz
        with open('film_verileri.json', 'w', encoding='utf-8') as json_dosya:
            json.dump(film_verileri, json_dosya, ensure_ascii=False, indent=4)

        # Verileri metin dosyasına yaz
        with open('film_verileri.txt', 'w', encoding='utf-8') as txt_dosya:
            for i, film in enumerate(film_verileri, start=1):
                txt_dosya.write("*************************\n")
                txt_dosya.write(f"{i}. Film\n")
                txt_dosya.write("Film Adı (TR): " +
                                film["Film Adı (TR)"] + "\n")
                txt_dosya.write("Film Adı (Orijinal): " +
                                film["Film Adı (Orijinal)"] + "\n")
                txt_dosya.write("IMDb Oy Sayısı: " +
                                film["IMDb Oy Sayısı"] + "\n")
                txt_dosya.write("IMDb Oy Ortalaması: " +
                                film["IMDb Oy Ortalaması"] + "\n")
                txt_dosya.write("TRAltazi Oy Sayısı: " +
                                film["TRAltazi Oy Sayısı"] + "\n")
                txt_dosya.write("TRAltazi Oy Ortalaması: " +
                                film["TRAltazi Oy Ortalaması"] + "\n")
                txt_dosya.write("*************************\n")
                txt_dosya.write("\n")

        self.log(
            'Veriler "film_verileri.json" ve "film_verileri.txt" dosyalarına yazıldı.')
