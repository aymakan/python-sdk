# Aymakan Python SDK
This is the official Aymakan Python SDK. It can be used to integrate with Aymakan APIs. The following features list 
are available in this SDK. For more details about our API requests and responses [click here](https://developer.aymakan.com.sa/docs/1.0).

- Ping API
- Aymakan Cities
- Create shipping
- Create reverse pickup Shipping
- Track shipping
- Track shipping by reference
- Cancel Shipping
- Cancel shipping by reference
- Shipping AWB label
- Bulk shipping AWB labels
- Customer shipping
- ########################
- Pickup requests
- Create pickup request
- Cancel pickup request
- Time slots
- ########################
- Customer Address
- Get Address
- Add Address
- Update address
- Delete address
- ########################
- Web Hooks
- Get Web hooks
- Add Web Hook
- Update Web Hook
- Delete webhook



## Requirements

* Python 3.0 or higher
* requests 2.27.1 or higher
* python-decouple

## Installing using PIP/PIP3
```
pip install aymakan-sdk
```

## Getting Started

Your Aymakan access token are available in your customer dashboard account

Setting configuration while instantiating the Client object

Used for pip based installation
```python
from aymakan-sdk import Client

client = Client()

client.setApiKey('Api-secret-key')
client.setSandBox()
```

## Ping API Method

Below is an example on how to fetch api status through ping API call:

```python
res = client.pingApi();
client.prettyPrint(res)
```

[Ping API Details](https://developer.aymakan.com.sa/docs/1.0/cities)

## Cities Method

Below is an example on how to fetch all cities through GetCities API call:

```python
res = client.getCityList();
client.prettyPrint(res)
```

[Cities API Details](https://developer.aymakan.com.sa/docs/1.0/cities)

## Shipping Methods

### Create Shipping

Creates a new shipment , to find out more details about `request parameters` checkout our  
[Create Shipping API Documentation](https://developer.aymakan.com.sa/docs/1.0/create-shipping)
```python
data = {
    #request parameters
    #...
    #...
}

res = client.createShipment(data)
client.prettyPrint(res)
```
### Create a Reverse Pickup Shipping

Creates a reverse pickup shipment , to find out more details about `request parameters` checkout our  
[Create Reverse Pickup ShippingAPI Documentation](https://developer.aymakan.com.sa/docs/1.0/create-reverse-pickup-shipping)
```python
data = {
    #request parameters
    #...
    #...
}

res = client.createReversePickupShipment(data)
client.prettyPrint(res)
```
### Track Shipping


Below is an example on how to track shipments through TrackShipment API call.
Shipments can be fetched as a single shipment or multiple shipments at the same time .
It is important to note that the tracking numbers should be sent in an array format.


#### Mandatory Parameter

| Parameter    | Type | Mandatory |
|--------------|----------------|----------------|
| Tracking Number  | Array  |  Yes  |


```python
#Track single shipment 
res = client.trackShipment(['AY120266'])

#Track multiple shipments
res = client.trackShipment(['AY669001659', '143862', '143866'])

client.prettyPrint(res)
```

[Track Shipping API Details](https://developer.aymakan.com.sa/docs/1.0/track-shipping)

### Track Shipping Using Reference

Below is an example on how to track shipments by reference number.
Shipments can be fetched by reference number as a single shipment or multiple shipments at the same time .
It is important to note that the reference number numbers should be sent in an array format.

#### Mandatory Parameter

| Parameter    |    Type    | Mandatory|
|--------------|----------------|----------------|
| Reference Number | Array    | Yes |


```python
#Track single shipment by reference number
res = client.shipmentByReference(['200018179'])

#Track Multiple shipment by reference number
res = client.shipmentByReference(['200018179','test-200018179'])

client.prettyPrint(res)
```

[Shipment By Reference API Details](https://developer.aymakan.com.sa/docs/1.0/shipments-by-reference)

### Cancel Shipping


Below is an example of how to Cancel Shipment :


#### Mandatory Parameters

| Parameter    | variable name | Type | Mandatory|
|--------------|---------------|----------------|----------------|
| Tracking Number  | `tracking` | Array | Yes|


```python
res = client.cancelShipment({"tracking": "AY120266"})

echo $response . "\n";
```
[Cancel Shipment API Details](https://developer.aymakan.com.sa/docs/1.0/cancel-shipping)

### Cancel Shipping Using Reference

Below is an example on how to cancel shipments by reference number.
Shipments can be fetched by reference number as a single shipment or multiple shipments at the same time .
It is important to note that the reference number numbers should be sent in an array format.

#### Mandatory Parameter

| Parameter    |    Type    | Mandatory|
|--------------|----------------|----------------|
| Reference Number | Array    | Yes |


```python
#Track single shipment by reference number
res = client.shipmentByReference(['200018179'])

#Track Multiple shipment by reference number
res = client.shipmentByReference(['200018179','test-200018179'])

client.prettyPrint(res)
```

[Shipment By Reference API Details](https://developer.aymakan.com.sa/docs/1.0/shipments-by-reference)
### Shipping AWB label Printing


Below is an example on how to make the Shipping AWB label Printing API call.
This API requires a single tracking number associated with the customer account , and
returns a URL to download the pdf file for all AWB

#### Mandatory Parameters

| Parameter    | variable name |Type| Mandatory
|--------------|---------------|----------------|----------------
| Tracking Code  | `tracking_number` |String| Yes


```python

res = client.getShipmentLabel("AY120266")

client.prettyPrint(res)
```
[Shipping AWB label Printing API Details](https://developer.aymakan.com.sa/docs/1.0/shipping-awb-label)


### Bulk Shipping AWB label Printing

Below is an example on how get Bulk Shipping AWB label .
This API requires an array with tracking numbers associated with the customer account.
If all the tracking numbers are found for that associated account, 
this API returns a URL to download the pdf file for all AWB.

#### Mandatory Parameters

| Parameter     | Type |Mandatory|
|--------------|----------------|----------------|
| Tracking Number  | Array |Yes|


```python
#Get multiple shipment label
res = client.getBulkShipmentLabel(['AY669001659', '143862', '143866', '143892'])

client.prettyPrint(res)
```
[Bulk Shipping AWB label Printing API Details](https://developer.aymakan.com.sa/docs/1.0/bulk-awb-labels)

### Customer Shipping


Below is an example on how to make the Customer Shipping  API call:

```python
res = client.getCustomerShipments();
client.prettyPrint(res)
```
[Customer Shipping  API Details](https://developer.aymakan.com.sa/docs/1.0/customer-shipping)



## Web Hooks

Web Hooks are a convenient way to receive real time updates for your shipments as soon as a status is updated. Web Hooks can be used to update customer internal systems with the latest shipments statuses.


### Get Webhooks

Below is an example on how to get webhooks .


```php
$response = $client->getWebHook();
echo $response . "\n";
```

[Get Webhooks API Details](https://developer.aymakan.com.sa/docs/1.0/web-hooks-get)


### Add Webhook

Below is an example on how to add webhook .


#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| Web Hook URL  | `webhook_url` | Yes

```php

$data = array( "webhook_url" => "https://testings.com" );
 $response = $client->createWebHook($data);
echo $response . "\n";
```

[Add Webhook API Details](https://developer.aymakan.com.sa/docs/1.0/web-hooks-add)


### Update Webhook

Below is an example on how to update Webhook .

#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| Web Hook URL  | `webhook_url` | Yes
| ID  | `id` | Yes


```php

$data = array(
    "id"=> 219 ,
    "webhook_url" => "https://www.testings.com"
);
 $response = $client->updateWebHook($data);
echo $response . "\n";
```

[Update Webhook API Details](https://developer.aymakan.com.sa/docs/1.0/web-hooks-update)



## Addresses 

Manages address associated to customer account.


### Get Address

Fetches ALL addresses associated to customer account.

```php
$response = $client->getAddress();

echo $response . "\n";
```

[Get Address API Details](https://developer.aymakan.com.sa/docs/1.0/customer-address-get)




### Create Address

Below is an example on how to make the create address associated to customer account.

#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| Title  | `title` | Yes
|Name  | `name` | Yes
| Email  | `email` | Yes
| Address | `address` | Yes
| Neighbourhood  | `neighbourhood` | Yes
| Postcode  | `postcode` | Yes
| Phone  | `phone` | Yes
| Description  | `description` | Yes



```php
$data = array(
    "title" => "Mr",
    "name" => "Test",
    "email" => "test@aymakan.com.sa",
    "city" => "Riyadh",
    "address" => 123,
    "neighbourhood" => "Al-Sahafah",
    "postcode" => "11534",
    "phone" => 580000000,
    "description" => "Test User"
);

$response = $client->createAddress($data);
echo $response . "\n";


```

[Create Address API Details](https://developer.aymakan.com.sa/docs/1.0/customer-address-add)





### Update Address

Below is an example on how to update address associated to customer account.


#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| ID  | `id` | Yes
| Title  | `title` | Yes
|Name  | `name` | Yes
| Email  | `email` | Yes
| Address | `address` | Yes
| Neighbourhood  | `neighbourhood` | Yes
| Postcode  | `postcode` | Yes
| Phone  | `phone` | Yes
| Description  | `description` | Yes



```php
$data = array(
    "id" => "3",
    "title" => "Mr",
    "name" => "Test",
    "email" => "test@aymakan.com.sa",
    "city" => "Riyadh",
    "address" => 123,
    "neighbourhood" => "Al-Sahafah",
    "postcode" => "11534",
    "phone" => 580000000,
    "description" => "Test User"
);

$response = $client->createAddress($data);
echo $response . "\n";


```

[Update Address API Details](https://developer.aymakan.com.sa/docs/1.0/customer-address-update)




### Delete Address

Below is an example on how to delete an address associated to customer account.


#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| ID  | `id` | Yes


```php
$data = array(
    "id" => 544,
);

$response = $client->deleteAddress($data);
var_dump($response);

```

[Delete Address API Details](https://developer.aymakan.com.sa/docs/1.0/customer-address-delete)





