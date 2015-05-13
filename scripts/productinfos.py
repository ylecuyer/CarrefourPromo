import requests
import re
import urllib
import pystache
import sys
from bs4 import BeautifulSoup

template = """
<table>
    <tbody>
        {{#products}}
        <tr>
            <td><img src="img/{{src}}.jpg" alt="{{code_barre}}"/></td>
            <td>{{name}}</td>
            <td>{{description}}</td>
            <td>{{price}} ({{promo}})</td>
        </tr>
        {{/products}}
    </tbody>
</table>
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
            promo = round(float(prix.replace(",", "."))*0.95, 2)

            urllib.request.urlretrieve(image_url, "output/img/"+code_barre+".jpg")

            data['products'].append({ 'src': code_barre, 'code_barre': code_barre, 'name': nom, 'description': description, 'price': prix, 'promo': promo })

            print(image_url)
            print(nom)
            print(description)
            print(prix)
            print(promo)
        except:

            #traceback.print_exc(file=sys.stdout)

            data['products'].append({ 'src': 'nopicture', 'code_barre': code_barre, 'name': produit, 'description': '---', 'price': '---', 'promo': '---' })

            print(code_barre)
            print(produit)

with open("output/"+sys.argv[1]+".html","wt") as f_out:
    f_out.write(pystache.render(template, data))
