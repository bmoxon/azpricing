#!/usr/bin/env python3

""" np20scusex.py
NP20 availability in SCUS example from end of
https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices

pip requirements
tabulate
response
"""

import requests
import json
from tabulate import tabulate 


def build_pricing_table(json_data, table_data):
    for item in json_data['Items']:
        meter = item['meterName']
        if not 'Windows' in item['productName']:
            table_data.append([item['armSkuName'], item['retailPrice'], item['unitOfMeasure'], item['armRegionName'], meter, item['productName']])
            # table_data.append([item['armSkuName'], item['retailPrice'], item['unitOfMeasure'], item['armRegionName'], meter, item['productName']])
        # table_data.append([item['armSkuName'], item['retailPrice'], item['unitOfMeasure'], item['armRegionName'], meter, item['productName']])
        
def main():
    table_data = []
    table_data.append(['SKU', 'Retail Price', 'Unit of Measure', 'Region', 'Meter', 'Product Name'])
    
    api_url = "https://prices.azure.com/api/retail/prices?api-version=2021-10-01-preview"
    # query = "armRegionName eq 'southcentralus' and armSkuName eq 'Standard_NP20s' and priceType eq 'Consumption' and contains(meterName, 'Spot')"
    # query = "armRegionName eq 'eastus' and skuName contains 'NDv4'"
    query = "armRegionName eq 'eastus' and contains(skuName, 'HB')
    response = requests.get(api_url, params={'$filter': query})
    json_data = json.loads(response.text)
   
    build_pricing_table(json_data, table_data)
    nextPage = json_data['NextPageLink']
    
    while(nextPage):
        response = requests.get(nextPage)
        json_data = json.loads(response.text)
        nextPage = json_data['NextPageLink']
        build_pricing_table(json_data, table_data)

    print(tabulate(table_data, headers='firstrow', tablefmt='psql'))
    
if __name__ == "__main__":
    main()