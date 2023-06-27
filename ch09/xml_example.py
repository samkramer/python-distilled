# 9.15.29 xml Package
from xml.etree.ElementTree import ElementTree

if __name__ == "__main__":
    doc = ElementTree(file="data/recipe.xml")
    title = doc.find('title')
    print(title.text)
    
    # Alternative (just get element text)
    print(doc.findtext('description'))
    
    # Iterate over multiple elements
    for item in doc.findall('ingredients/item'):
        num = item.get('num')
        units = item.get('units', '')
        text = item.text.strip()
        num_units = f"{num} {units}"
        print(f'{num_units:>10s} {text}')