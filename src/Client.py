import requests
from decouple import config


class Client:
    __url = config('prd_url')
    __api_key = config('prd_api_key')
    __testing = False

    def __init__(self, url=None, api_key=None, testing=None):
        if url:
            self.__url = url
        if api_key:
            self.__api_key = api_key
        if testing:
            self.__testing = testing

    def setApiKey(self, token):
        self.__api_key = token

    def getToken(self):
        return self.__api_key

    def setSandBox(self):
        self.__testing = True
        self.__url = config('dev_url')
        self.__api_key = config('dev_api_key')

    def unsetSandBox(self):
        self.__testing = False
        self.__url = config('prd_url')
        self.__api_key = config('prd_api_key')

    def isSandBox(self):
        return self.__testing

    def callAPI(self, method, url=None, data=False):

        headers = {
            'Accept': 'application/json',
            'Authorization': self.__api_key
        }

        ssl_verify = True
        timeout = 100

        try:
            if method == 'GET':
                r = requests.get(url, headers=headers, verify=ssl_verify, timeout=timeout)
            elif method == 'POST':
                r = requests.post(url, json=data, headers=headers, verify=ssl_verify, timeout=timeout)
            elif method == 'PUT':
                r = requests.put(url, json=data, headers=headers, verify=ssl_verify, timeout=timeout)
            else:
                r = requests.delete(url, json=data, headers=headers, verify=ssl_verify, timeout=timeout)

            return r

        except Exception as e:
            print(e)

    def pingApi(self):
        return self.callAPI('GET', self.__url + '/ping')

    def getCityList(self):
        return self.callAPI('GET', self.__url + '/cities')

    def trackShipment(self, tracking):
        if isinstance(tracking, list):
            tracking = ",".join(tracking)
        return self.callAPI('GET', self.__url + '/shipping/track/' + tracking)

    def shipmentByReference(self, reference):
        if isinstance(reference, list):
            reference = ",".join(reference)
        return self.callAPI('GET', self.__url + '/shipping/by_reference/' + reference)

    def getShipmentLabel(self, tracking):
        return self.callAPI('GET', self.__url + '/shipping/awb/tracking/' + tracking)

    def getBulkShipmentLabel(self, tracking):
        if isinstance(tracking, list):
            tracking = ",".join(tracking)
        return self.callAPI('GET', self.__url + '/shipping/bulk_awb/trackings/' + tracking)

    def getCustomerShipments(self):
        return self.callAPI('GET', self.__url + '/customer/shipments')

    def createShipment(self, data):
        return self.callAPI('POST', self.__url + '/shipping/create', data)

    def createReversePickupShipment(self, data):
        return self.callAPI('POST', self.__url + '/shipping/create/reverse_pickup', data)

    def cancelShipment(self, data):
        return self.callAPI('POST', self.__url + '/shipping/cancel', data)

    def cancelShipmentByReference(self, data):
        return self.callAPI('POST', self.__url + '/shipping/cancel_by_reference', data)

    def getWebHook(self):
        return self.callAPI('GET', self.__url + '/webhooks/list')

    def createWebHook(self, data):
        return self.callAPI('POST', self.__url + '/webhooks/create', data)

    def updateWebHook(self, data):
        return self.callAPI('PUT', self.__url + '/webhooks/update', data)

    def deleteWebHook(self):
        return self.callAPI('DELETE', self.__url + '/webhooks/delete')

    def getAddress(self):
        return self.callAPI('GET', self.__url + '/address/list')

    def createAddress(self, data):
        return self.callAPI('POST', self.__url + '/address/create', data)

    def updateAddress(self, data):
        return self.callAPI('PUT', self.__url + '/address/update', data)

    def deleteAddress(self, data):
        return self.callAPI('DELETE', self.__url + '/address/delete', data)

    def pickupRequest(self):
        return self.callAPI('GET', self.__url + '/pickup_request/list')

    def createPickupRequest(self, data):
        return self.callAPI('POST', self.__url + '/pickup_request/create', data)

    def cancelPickupRequest(self, data):
        return self.callAPI('POST', self.__url + '/pickup_request/cancel', data)

    def timeSlots(self, data):
        return self.callAPI('GET', self.__url + '/time_slots/' + data)
