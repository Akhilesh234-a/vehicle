import urllib.request
import json
titles = ['Mahindra_Thar', 'Hyundai_Creta', 'Toyota_Innova', 'Suzuki_Swift', 'Royal_Enfield_Classic', 'Honda_Activa', 'KTM_200_Duke', 'Bajaj_Pulsar']
images = {}
for t in titles:
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={t}&prop=pageimages&format=json&pithumbsize=800"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            pages = data['query']['pages']
            val = list(pages.values())[0]
            if 'thumbnail' in val:
                images[t] = val['thumbnail']['source']
    except Exception as e:
        pass
print(json.dumps(images, indent=2))
