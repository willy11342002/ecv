# Basic Info
* Cloud Server：[GCP](https://ascendant-chain-296306.uc.r.appspot.com/)
* DB：SQLite
* Framework：Django

# DB Schema
| Table | Column | Type | Require | Check | Index |
| :---: | :---: | :---: | :---: | :---: | :---: |
| LineItem | bill_id | Interger | N | N | Foreign Key References Bill |
| LineItem | product_id | Interger | N | N | Foreign Key References Product |
| LineItem | UsageAccountId | Interger | Y | >=0 | Index |
| LineItem | LineItemType | VarChar(28) | Y | N | N |
| LineItem | UsageStartDate | DateTime | Y | N | N |
| LineItem | UsageEndDate | DateTime | Y | N | N |
| LineItem | UsageType | VarChar(64) | Y | N | N |
| LineItem | Operation | VarChar(64) | N | N | N |
| LineItem | AvailabilityZone | VarChar(16) | N | N | N |
| LineItem | ResourceId | VarChar(128) | N | N | N |
| LineItem | UsageAmount | Float | Y | N | N |
| LineItem | NormalizationFactor | Float | N | N | N |
| LineItem | NormalizedUsageAmount | Float | N | N | N |
| LineItem | UnblendedRate | Float | N | N | N |
| LineItem | UnblendedCost | Float | Y | N | N |
| LineItem | LineItemDescription | VarChar(512) | Y | N | N |
| Bill | InvoiceId | Interger | Y | >=0 | Index |
| Bill | BillingEntity | VarChar(16) | Y | N | N |
| Bill | BillType | VarChar(16) | Y | N | N |
| Bill | PayerAccountId | Interger | Y | >=0 | Index |
| Bill | BillingPeriodStartDate | Date | Y | N | Index |
| Product | ProductName | VarChar(128) | N | N | N |
| Product | cacheEngine | VarChar(16) | N | N | N |
| Product | databaseEdition | VarChar(16) | N | N | N |
| Product | databaseEngine | VarChar(32) | N | N | N |
| Product | deploymentOption | VarChar(32) | N | N | N |
| Product | instanceType | VarChar(32) | N | N | N |
| Product | instanceTypeFamily | VarChar(8) | N | N | N |
| Product | licenseModel | VarChar(32) | N | N | N |
| Product | location | VarChar(64) | N | N | N |
| Product | operatingSystem | VarChar(8) | N | N | N |
| Product | region | VarChar(32) | N | N | N |
| Product | tenancy | VarChar(8) | N | N | N |

# API Design
**Sum Of UnblendedCost By UsageAccountId**
* **URL**
[/apiv1/lineitem/:usageaccountid/products/summary/unblendedcost](https://ascendant-chain-296306.uc.r.appspot.com/apiv1/lineitem/147878817734/products/summary/unblendedcost)

* **Method**
GET

* **URL Params**
**Required:**
usageaccountid=[int]

* **Data Params**
None

* **Success Response**
  * **Code:** 200
  * **Content:** {"ProductA": "0.00", "ProductB": "25.36", "ProductC": "0.00"}

* **Error Response**
  * **Code:** 404 NOT FOUND
  * **Content:** 

**Daily Sum Of UsageAmount By UsageAccountId**
* **URL**
[/apiv1/lineitem/:usageaccountid/products/summary/daily/usageamount](https://ascendant-chain-296306.uc.r.appspot.com/apiv1/lineitem/147878817734/products/summary/daily/usageamount)

* **Method**
GET

* **URL Params**
**Required:**
usageaccountid=[int]

* **Data Params**
None

* **Success Response**
  * **Code:** 200
  * **Content:** {"Amazon Elastic Compute Cloud": {"2020/04/01": "32.40", "2020/04/02": "32.36", "2020/04/03": "32.45"}, "AWS Data Transfer": {"2020/04/01": "0.10", "2020/04/02": "0.10", "2020/04/03": "0.10"}}

* **Error Response**
  * **Code:** 404 NOT FOUND
  * **Content:** 


