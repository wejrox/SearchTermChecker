import requests
import re
import sys

endpoint = "https://www.pccasegear.com/category/416/new-products"
desired_product = "Ryzen 9 3950X".encode()
test_product = "PCCG Void 590".encode()

def run():
    r = requests.get(url=endpoint)
    content_text = r.content

    if re.search(desired_product, content_text, re.IGNORECASE):
        print(f"Desired product '{desired_product.decode()}' has been released!")
    else:
        print(f"Failed to find product '{desired_product.decode()}'.")
        sys.exit(1)

if __name__ == '__main__':
    run()
