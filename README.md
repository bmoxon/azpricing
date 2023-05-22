# Azure Pricing work

Started with published information on the Azure pricing apis.

[Azure Retail Prices overview](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices)

# Pull from the api for further investigation and testing

```bash
$ curl -o allprices.json https://prices.azure.com/api/retail/prices?api-version=2023-01-01-preview --insecure

$ ls -l allprices.json
-rw-r--r-- 1 bmoxon bmoxon 61441 Apr 28 07:25 allprices.json

# prettyprint
$ jq . < allprices.json
```

# python query tool

Start with the python listing at the end of the Azure Retail Prices overview article (link above).

examples

```
$ ./azpricing.py --help
usage: azpricing.py [-h] [-r REGION] [-f FAMILY] [-v VERSION] [-m METER]

Query Azure pricing API for VM pricing information

optional arguments:
  -h, --help            show this help message and exit
  -r REGION, --region REGION
                        Azure region to query, e.g. eastus
  -f FAMILY, --family FAMILY
                        VM family to query, e.g. ND, ND96asr
  -v VERSION, --version VERSION
                        VM family version, e.g. v4
  -m METER, --meter METER
                        Meter, e.g. "Spot" or "Low Priority"

$ ./azpricing.py -r eastus2 -f ND -v 4
+---------------------------+---------------+-----------------+-------------------------------+
| armSkuName                |   retailPrice | armRegionName   | meterName                     |
|---------------------------+---------------+-----------------+-------------------------------|
| Standard_ND96amsr_A100_v4 |        6.554  | eastus2         | ND96amsr A100 v4 Low Priority |
| Standard_ND96amsr_A100_v4 |       14.4188 | eastus2         | ND96amsr A100 v4 Spot         |
| Standard_ND96amsr_A100_v4 |       32.77   | eastus2         | ND96amsr A100 v4              |
+---------------------------+---------------+-----------------+-------------------------------+
```
```
