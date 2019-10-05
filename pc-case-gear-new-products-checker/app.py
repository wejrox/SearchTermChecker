#! /usr/bin/env python
import requests
import re
import sys
import argparse
import time
from datetime import datetime

endpoint = "https://www.pccasegear.com/category/416/new-products"

def run(desired_product, check_interval_sec):
    r = requests.get(url=endpoint)
    content_text = r.content

    while True:
        if re.search(desired_product, content_text, re.IGNORECASE):
            dt_current = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(f"Desired product '{desired_product.decode()}' has been released. When: {dt_current}")
            sys.exit(0)
        time.sleep(check_interval_sec)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wait until a new product is released from Pc Case Gear.")
    parser.add_argument("desired_product", type=str, help="The product which you are awaiting the release of.")
    parser.add_argument("check_interval_min", type=int, help="The time in minutes to wait before checking again.")
    args = parser.parse_args()

    run(args.desired_product.encode(), args.check_interval_min * 60)
