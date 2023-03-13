#REST API Service Validator

import re
from os import system
import pip._vendor.requests

statusCodeDictionary = {
    200: "API statuscode: 200, OK. The request was succesful.",
    400: "API statuscode: 400, Bad Request.",
    401: "API statuscode: 401, Unauthorized.",
    403: "API statuscode: 403, Forbidden.",
    404: "API statuscode: 404, Not Found."
}

def validateURL():
    global websiteURL
    websiteURL = input("Please enter the full REST API web address you wish to check: \n")
    #Validate URL via regex
    httpsInAddress = re.match("^https:\/\/[0-9a-zA-Z]+(\.+[a-zA-Z])", websiteURL)
    httpInAddress = re.match("^http:\/\/[0-9a-zA-Z]+(\.+[a-zA-Z])", websiteURL)
    if httpsInAddress:
        print("This URL is valid.")
        curlURL()
        checkAnotherAddress()
        return
    if httpInAddress:
       checkInput = input("This service may be unsecure. Do you wish to proceed? y/n \n")
       if checkInput == "y":
           curlURL()
           checkAnotherAddress()
           return
    else:
        print("This URL is invalid.")
        checkAnotherAddress()
        return

def curlURL():
    curlResult = system("curl -I {}".format(websiteURL))
    #Validate curl result
    if curlResult == 0:
        print("This API service is online.")
        getAPIStatus()
    else:
        print("This API service is offline or the URL provided was incorrect.")
        return

def getAPIStatus():
    APIrequest = pip._vendor.requests.get(websiteURL)
    APIstatusCode = APIrequest.status_code
    if APIstatusCode in statusCodeDictionary:
        print(statusCodeDictionary.get(APIstatusCode))
        return

def checkAnotherAddress():
    askToCheckAgain = input("Would you like to check another service? y/n: \n")
    if askToCheckAgain == "y":
        validateURL()
    else:
        return

validateURL()
