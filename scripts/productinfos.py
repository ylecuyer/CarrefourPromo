import requests
import re
import urllib
import pystache
import sys
from bs4 import BeautifulSoup

template = """
{{#products}}
<div class="list card">

	<div class="item">
		<h2>{{name}}</h2>
		<p>{{description}}</p>
	</div>

	<div class="item item-image">
		<img src="img/products/{{src}}.jpg" alt="{{code_barre}}"/>
	</div>

	<div class="item item-icon-left balanced">
		<i class="icon ion-checkmark-circled"></i>
		<strong>{{gain}}€</strong> <small class="right">{{price}}€ <span class="arrow">→</span> {{promo}}€</small>
	</div>

</div>
{{/products}}
"""

data = { 'products': [] }

with open('formated.txt') as f_in:

    for line in f_in:

        [code_barre, produit] = line.rstrip().split(';')

        url = "http://www.carrefour.fr/drive/chercher/"+code_barre
        r = requests.get(url)
        soup = BeautifulSoup(r.text)

        try:
            result = soup.find(class_="product-list").find('li')

            image_url = result.find('img')['src']
            nom = result.find(class_="label").text.strip()
            description = result.find(class_="capacity").text.strip()
            prix_txt = result.find(class_="price").text.strip()
            prix = re.findall(r'\d+,\d+', prix_txt)[0]
            prix_f = float(prix.replace(",", "."))
            promo = round(prix_f*0.95, 2)
            gain = round(prix_f - promo, 2)

            urllib.request.urlretrieve(image_url, "output/img/products/"+code_barre+".jpg")

            data['products'].append({ 'src': code_barre, 'code_barre': code_barre, 'name': nom, 'description': description, 'price': prix_f, 'promo': promo, 'gain': gain })

            print(image_url)
            print(nom)
            print(description)
            print(prix_f)
            print(promo)
            print(gain)
        except:

            #traceback.print_exc(file=sys.stdout)

            data['products'].append({ 'src': 'nopicture', 'code_barre': code_barre, 'name': produit, 'description': '---', 'price': '---', 'promo': '---', 'gain': '---' })

            print(code_barre)
            print(produit)

with open("output/partials/"+sys.argv[1]+".html","wt") as f_out:
    f_out.write(pystache.render(template, data))
