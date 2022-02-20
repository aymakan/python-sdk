# Aymakan Python SDK
This is the official Aymakan Python SDK. It can be used to integrate with Aymakan APIs. The following features list 
are available in this SDK. For more details about our API requests and responses [click here](https://developer.aymakan.com.sa/docs/1.0).

- ### [General Methods](#general-methods-1)
  - [Ping API](#ping-api-method)
  - [Aymakan Cities](#cities-method)
- ### [Shipping Methods](#shipping-methods-1)
  - [Create shipping](#create-shipping)
  - [Create reverse pickup Shipping](#create-a-reverse-pickup-shipping)
  - [Track shipping](#track-shipping)
  - [Track shipping by reference](#track-shipping-using-reference)
  - [Cancel Shipping](#cancel-shipping)
  - [Cancel shipping by reference](#cancel-shipping-using-reference)
  - [Shipping AWB label](#shipping-awb-label-printing)
  - [Bulk shipping AWB labels](#bulk-shipping-awb-label-printing)
  - [Customer shipping](#customer-shipping)
- ### [Pickup Requests Methods](#pickup-requests-methods)
  - [Get pickup requests](#get-pickup-requests)
  - [Create pickup request](#create-pickup-request)
  - [Cancel pickup request](#cancel-pickup-request)
  - [Time slots](#time-slots)
- ### [Customer Addresses Methods](#customer-addresses-methods)
  - [Get Address](#get-address)
  - [Add Address](#create-address)
  - [Update address](#update-address)
  - [Delete address](#delete-address)
- ### [WebHooks Methods](#web-hooks)
  - [Get Web hooks](#get-webhooks)
  - [Add Web Hook](#add-webhook)
  - [Update Web Hook](#update-webhook)
  - [Delete webhook](#delete-webhook)

------------------------------
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

# Basic usage:
res = client.getCityList()

print(res.url)         # <-- for response URL
print(res.status_code) # <-- for response status code
print(res.json())      # <-- for response data in JSON format

# or just use this method to print indented/pretty JSON
client.prettyPrint(res)
```

## General Methods
### Ping API Method

Below is an example on how to fetch api status through ping API call:

```python
res = client.pingApi();
client.prettyPrint(res)
```

[Ping API Details](https://developer.aymakan.com.sa/docs/1.0/cities)

### Cities Method

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
    # request parameters
    # ...
    # ...
}

res = client.createShipment(data)
client.prettyPrint(res)
```
### Create a Reverse Pickup Shipping

Creates a reverse pickup shipment , to find out more details about `request parameters` checkout our  
[Create Reverse Pickup ShippingAPI Documentation](https://developer.aymakan.com.sa/docs/1.0/create-reverse-pickup-shipping)
```python
data = {
    # request parameters
    # ...
    # ...
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
# Track single shipment 
res = client.trackShipment(['AY120266'])

# Track multiple shipments
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
# Track single shipment by reference number
res = client.shipmentByReference(['200018179'])

# Track Multiple shipment by reference number
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
client.prettyPrint(res)
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
# Track single shipment by reference number
res = client.shipmentByReference(['200018179'])

# Track Multiple shipment by reference number
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
# Get multiple shipment label
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

## Pickup Requests Methods
### Get Pickup Requests
This API fetches all current customer pickup requests.

```python
res = client.pickupRequest()
client.prettyPrint(res)
```
### Create pickup request
Below is an example on how to create a pickup request.

```python
data = {
    "pickup_date": "2022-12-02",
    "time_slot": "afternoon",
    "contact_name": "example",
    "contact_phone": "059999999",
    "address": "example address",
    "shipments": 2
}

res = client.createPickupRequest(data)
client.prettyPrint(res)
```

### Cancel pickup request
Below is an example on how to cancel a pickup request.

```python
data = {
    "pickup_request": 4021
}

res = client.cancelPickupRequest(data)
client.prettyPrint(res)
```

### Time slots
Below is an example on how to fetch all time slots available to current customer.

```python
res = client.timeSlots("2022-12-02")
client.prettyPrint(res)
```
## Customer Addresses Methods 

Manages address associated to customer account.


### Get Address

Fetches ALL addresses associated to customer account.

```python
res = client.getAddress()
client.prettyPrint(res)
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



```python
data = {
    "title": "Mr",
    "name": "example",
    "email": "example@example.com",
    "city": "Riyadh",
    "address": 123,
    "neighbourhood": "Al-Sahafah",
    "postcode": "11534",
    "phone": 0599999999,
    "description": "create address example"
}

res = client.createAddress(data)
client.prettyPrint(res)
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



```python
data = {
    "id": "3",
    "title": "Mr",
    "name": "example",
    "email": "example@example.com",
    "city": "Riyadh",
    "address": 123,
    "neighbourhood": "Al-Sahafah",
    "postcode": "11534",
    "phone": 0599999999,
    "description": "create address example"
}

res = client.updateAddress(data)
client.prettyPrint(res)
```

[Update Address API Details](https://developer.aymakan.com.sa/docs/1.0/customer-address-update)




### Delete Address

Below is an example on how to delete an address associated to customer account.


#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| ID  | `id` | Yes


```python
data = {
    "id": 544
}

$response = client.deleteAddress(data)
client.prettyPrint(res)
```

[Delete Address API Details](https://developer.aymakan.com.sa/docs/1.0/customer-address-delete)


## Web Hooks

Web Hooks are a convenient way to receive real time updates for your shipments as soon as a status is updated. Web Hooks can be used to update customer internal systems with the latest shipments statuses.


### Get Webhooks

Below is an example on how to get webhooks .


```python
res = client.getWebHook()
client.prettyPrint(res)
```

[Get Webhooks API Details](https://developer.aymakan.com.sa/docs/1.0/web-hooks-get)


### Add Webhook

Below is an example on how to add webhook .


#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| Web Hook URL  | `webhook_url` | Yes

```python
data = {
    "webhook_url": "https://testings.com"
}

res = client.createWebHook(data)
client.prettyPrint(res)
```

[Add Webhook API Details](https://developer.aymakan.com.sa/docs/1.0/web-hooks-add)


### Update Webhook

Below is an example on how to update Webhook .

#### Mandatory Parameters

| Parameter    | variable name | Mandatory
|--------------|---------------|----------------
| ID  | `id` | Yes
| Web Hook URL  | `webhook_url` | Yes


```python
data = {
    "id": 219,
    "webhook_url": "https://www.testings.com"
}

res = client.updateWebHook(data)
client.prettyPrint(res)
```

[Update Webhook API Details](https://developer.aymakan.com.sa/docs/1.0/web-hooks-update)


### Delete Webhook

Below is an example on how to delete webhooks .


```python
res = client.deleteWebHook()
client.prettyPrint(res)
```

[Delete Webhooks API Details](https://developer.aymakan.com.sa/docs/1.0/web-hooks-delete)