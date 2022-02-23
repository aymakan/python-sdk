import unittest
import random

import datetime as dt

from src import Client


class ClientTestCase(unittest.TestCase):
    c = Client()

    def setUp(self):
        self.c.setSandBox()
        self.c.setApiKey(config('prd_api_key'))

    def test_pingApi(self):
        res = self.c.pingApi()
        json = res.json()
        self.assertTrue(json['status'])
        self.assertEqual(res.status_code, 200)

    def test_getCityList(self):
        res = self.c.getCityList()
        json = res.json()
        self.assertTrue(json["success"])
        self.assertEqual(res.status_code, 200)

    ##################################################################

    # Track Shipment Test Cases:
    def test_trackShipment_single_shipment(self):
        res = self.c.getCustomerShipments()
        json = res.json()
        tracking = json["data"]["data"][0]["tracking_number"]

        res = self.c.trackShipment(tracking)
        json = res.json()
        self.assertTrue(json["success"])
        self.assertEqual(res.status_code, 200)

    def test_trackShipment_multiple_shipments(self):
        tracking = []
        res = self.c.getCustomerShipments()
        json = res.json()
        tracking.append(json["data"]["data"][0]["tracking_number"])
        tracking.append(json["data"]["data"][1]["tracking_number"])

        res = self.c.trackShipment(tracking)
        json = res.json()
        self.assertTrue(json["success"])
        self.assertEqual(res.status_code, 200)

    def test_trackShipment_failed(self):
        tracking = 'AY3627722661615111'
        res = self.c.trackShipment(tracking)
        json = res.json()
        self.assertTrue(json["error"])
        self.assertEqual(res.status_code, 422)

    ##################################################################

    # Track Shipment by reference Test Cases:
    def test_shipmentByReference_single_reference(self):
        reference = '21367475'
        res = self.c.shipmentByReference(reference)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_shipmentByReference_multiple_references(self):
        reference = ['21367475', '23644487', '23643271']
        res = self.c.shipmentByReference(reference)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_shipmentByReference_failed(self):
        reference = '10292565'
        res = self.c.shipmentByReference(reference)
        json = res.json()
        self.assertTrue(json['error'])
        self.assertEqual(res.status_code, 422)

    ##################################################################

    def test_getShipmentLabel(self):
        data = {
            "requested_by": "Test get shipment label",
            "delivery_name": "delivery",
            "declared_value": "1",
            "delivery_city": "Riyadh",
            "delivery_address": "Riyadh",
            "delivery_neighbourhood": "Riyadh",
            "delivery_country": "SA",
            "delivery_phone": "0599999999",
            "collection_name": "abdullah",
            "collection_email": "test@test.com",
            "collection_city": "Riyadh",
            "collection_address": "Riyadh",
            "collection_country": "SA",
            "collection_phone": "0599999999",
            "pieces": 1
        }

        res = self.c.createShipment(data)
        json = res.json()
        tracking = json['data']['shipping']['tracking_number']

        res = self.c.getShipmentLabel(tracking)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        data = {
            "tracking": tracking
        }

        self.c.cancelShipment(data)

    def test_getBulkShipmentLabel(self):
        tracking = []
        data = {
            "requested_by": "Test get bulk shipment label",
            "delivery_name": "delivery",
            "declared_value": "1",
            "delivery_city": "Riyadh",
            "delivery_address": "Riyadh",
            "delivery_neighbourhood": "Riyadh",
            "delivery_country": "SA",
            "delivery_phone": "0599999999",
            "collection_name": "abdullah",
            "collection_email": "test@test.com",
            "collection_city": "Riyadh",
            "collection_address": "Riyadh",
            "collection_country": "SA",
            "collection_phone": "0599999999",
            "pieces": 1
        }

        res = self.c.createShipment(data)
        json = res.json()
        tracking.append(json['data']['shipping']['tracking_number'])

        data = {
            "requested_by": "Test get bulk shipment label",
            "delivery_name": "delivery",
            "declared_value": "1",
            "delivery_city": "Riyadh",
            "delivery_address": "Riyadh",
            "delivery_neighbourhood": "Riyadh",
            "delivery_country": "SA",
            "delivery_phone": "0599999999",
            "collection_name": "abdullah",
            "collection_email": "test@test.com",
            "collection_city": "Riyadh",
            "collection_address": "Riyadh",
            "collection_country": "SA",
            "collection_phone": "0599999999",
            "pieces": 1
        }

        res = self.c.createShipment(data)
        json = res.json()
        tracking.append(json['data']['shipping']['tracking_number'])

        res = self.c.getBulkShipmentLabel(tracking)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        data = {
            "tracking": tracking[0]
        }

        self.c.cancelShipment(data)

        data = {
            "tracking": tracking[1]
        }

        self.c.cancelShipment(data)

    def test_getCustomerShipments(self):
        res = self.c.getCustomerShipments()
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_createShipment(self):
        data = {
            "requested_by": "Test create shipment",
            "delivery_name": "delivery",
            "declared_value": "1",
            "delivery_city": "Riyadh",
            "delivery_address": "Riyadh",
            "delivery_neighbourhood": "Riyadh",
            "delivery_country": "SA",
            "delivery_phone": "0599999999",
            "collection_name": "abdullah",
            "collection_email": "test@test.com",
            "collection_city": "Riyadh",
            "collection_address": "Riyadh",
            "collection_country": "SA",
            "collection_phone": "0599999999",
            "pieces": 1
        }

        res = self.c.createShipment(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        tracking = json['data']['shipping']['tracking_number']

        data = {'tracking': tracking}

        res = self.c.cancelShipment(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_createReversePickupShipment(self):
        data = {
            "requested_by": "Test create reverse pickup shipment",
            "declared_value": 1,
            "declared_value_currency": "SAR",
            "reference": "",
            "is_cod": 1,
            "cod_amount": 12,
            "currency": "SAR",
            "delivery_name": "Test By Abdullah",
            "delivery_email": "test@test.com",
            "delivery_city": "Riyadh",
            "delivery_address": "Riyadh",
            "delivery_neighbourhood": "Al Sahafa",
            "delivery_postcode": 11543,
            "delivery_country": "SA",
            "delivery_phone": "0599999999",
            "delivery_description": "",
            "collection_name": "Ahmed",
            "collection_email": "Ahmed@email.com",
            "collection_city": "Riyadh",
            "collection_address": "Al Sahafa",
            "collection_neighbourhood": "Riyadh",
            "collection_postcode": 11543,
            "collection_country": "SA",
            "collection_phone": 540000000,
            "collection_description": "",
            "weight": 38,
            "pieces": 1,
            "items_count": 1,
            "products": [
                {
                    "sku": 1212,
                    "qty": 1,
                    "price": 20.1
                }
            ]

        }
        res = self.c.createReversePickupShipment(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_cancelShipment(self):
        data = {
            "requested_by": "Test cancel shipment",
            "delivery_name": "delivery",
            "declared_value": "1",
            "delivery_city": "Riyadh",
            "delivery_address": "Riyadh",
            "delivery_neighbourhood": "Riyadh",
            "delivery_country": "SA",
            "delivery_phone": "0599999999",
            "collection_name": "abdullah",
            "collection_email": "test@test.com",
            "collection_city": "Riyadh",
            "collection_address": "Riyadh",
            "collection_country": "SA",
            "collection_phone": "0599999999",
            "pieces": 1
        }

        res = self.c.createShipment(data)
        json = res.json()

        tracking = json['data']['shipping']['tracking_number']

        data = {
            "tracking": tracking
        }

        res = self.c.cancelShipment(data)
        json = res.json()

        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_cancelShipmentByReference(self):
        data = {
            "reference": 200018179
        }
        res = self.c.cancelShipmentByReference(data)
        json = res.json()
        print(json)

        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_getWebHook(self):
        data = {"webhook_url": "https://testings.com"}
        self.c.createWebHook(data)

        res = self.c.getWebHook()
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        self.c.deleteWebHook()

    def test_createWebHook(self):
        data = {"webhook_url": "https://testings.com"}
        res = self.c.createWebHook(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        self.c.deleteWebHook()

    def test_updateWebHook(self):
        data = {"webhook_url": "https://testings.com"}
        res = self.c.createWebHook(data)
        json = res.json()
        webhook_id = json['data']['webhook']['id']

        data = {
            "id": webhook_id,
            "webhook_url": "https://test-webhook-url.com"
        }

        res = self.c.updateWebHook(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        self.c.deleteWebHook()

    def test_deleteWebhook(self):
        data = {"webhook_url": "https://testings.com"}
        self.c.createWebHook(data)

        res = self.c.deleteWebHook()
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_getAddress(self):
        res = self.c.getAddress()
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_createAddress(self):
        data = {
            'title': 'Mr',
            'name': 'Test create Address',
            'email': 'test@test.com',
            'city': 'Riyadh',
            'address': '123',
            'neighbourhood': 'Al-Dhubbat',
            'postcode': '11534',
            'phone': '580000000',
            'description': 'Test User'
        }

        res = self.c.createAddress(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        address_id = json['data']['address']['id']
        self.c.deleteAddress(data={"id": address_id})

    def test_updateAddress(self):
        data = {
            'title': 'Mr',
            'name': 'Test create Address',
            'email': 'test@test.com',
            'city': 'Riyadh',
            'address': '123',
            'neighbourhood': 'Al-Dhubbat',
            'postcode': '11534',
            'phone': '580000000',
            'description': 'Test User'
        }
        res = self.c.createAddress(data)
        json = res.json()
        address_id = json['data']['address']['id']

        data = {
            "id": address_id,
            "title": "Mr",
            "name": "Test update Address",
            "email": "test2@test2.com",
            "city": "Riyadh",
            "address": "Saudi Arabia Makkah{Mecca} Jeddah Al Muntazahat شارع العام طريق الحرزات 03088",
            "neighbourhood": "Al Wizarat",
            "postcode": "75760",
            "phone": "+966598998110",
            "description": "Home address",
        }

        res = self.c.updateAddress(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        data = {"id": address_id}
        self.c.deleteAddress(data)

    def test_deleteAddress(self):
        data = {
            'title': 'Abdullah',
            'name': 'Main Address',
            'email': 'a.alqattan@aymakan.com.sa',
            'city': 'Riyadh',
            'address': '123',
            'neighbourhood': 'Al-Dhubbat',
            'postcode': '11534',
            'phone': '580000000',
            'description': 'Test User'
        }

        res = self.c.createAddress(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

        address_id = json['data']['address']['id']
        data = {"id": address_id}
        res = self.c.deleteAddress(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_pickupRequest(self):
        res = self.c.pickupRequest()
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_createPickupRequest(self):
        data = {
            "pickup_date": "2023-12-02",
            "time_slot": "morning",
            "contact_name": "Test-999",
            "contact_phone": "Test-999",
            "address": "Test-999",
            "shipments": '3'
        }

        res = self.c.createPickupRequest(data)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_cancelPickupRequest(self):
        today = dt.date.today()
        date = today + dt.timedelta(days=7)
        date = str(date)

        res = self.c.timeSlots(date)
        json = res.json()

        slots = json['data']['slots']
        time_slot = random.choice(list(slots))

        data = {
            "pickup_date": date,
            "time_slot": time_slot,
            "contact_name": "Test cancel pickup request",
            "contact_phone": "0599999999",
            "address": "Test address",
            "shipments": 3
        }
        res = self.c.createPickupRequest(data)
        json = res.json()

        pickup_request_id = json['data']['id']

        data = {
            "pickup_request_id": pickup_request_id
        }

        res = self.c.cancelPickupRequest(data)
        json = res.json()

        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)

    def test_timeSlots(self):
        today = dt.date.today()
        date = today + dt.timedelta(days=7)
        date = str(date)
        res = self.c.timeSlots(date)
        json = res.json()
        self.assertTrue(json['success'])
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
