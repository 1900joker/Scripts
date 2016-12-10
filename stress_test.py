import requests

for i in range(10):
    id = '{0:03}'.format(i)
    r=requests.post('http://staging.treebohotels.com/hmssync/rest/v1/reservations',

                  data={
                      "reservations": [
                          {
                              "ID": "1013"+str(id),
                              "GID": "G 101282",
                              "HOTELID": "24627",
                              "EMAIL": "arvind.k.jaishwal@gmail.com",
                              "FNAME": "Arvind",
                              "LNAME": "Jaiswal",
                              "PHONE": "9510022471",
                              "COUNTRY": "",
                              "NATIONALITY": "India",
                              "GEMAIL": "",
                              "GFNAME": "MakeMyTrip",
                              "GLNAME": "-",
                              "GPHONE": "1111111111",
                              "GCOUNTRY": "",
                              "GNATIONALITY": "",
                              "CHECKIN": "2016-10-12",
                              "CHECKOUT": "2016-10-13",
                              "CREATION": "2016-10-12 00:21:40",
                              "ADULT": "2",
                              "CHILDREN": "0",
                              "RESSTATUS": "CHECKOUT",
                              "MSGSTATUS": "Modify",
                              "SOURCE": "MakeMyTrip",
                              "OWNERCODE": "AGENT24717",
                              "MARKETCODE": "TA",
                              "STAYSOURCE": "OTA (prepaid)",
                              "GSTAYSOURCE": "OTA (prepaid)",
                              "MODIFYDATE": "2016-10-13 09:30:07",
                              "CANCELDATE": "0000-00-00 00:00:00",
                              "STAYDETAIL": [
                                  {
                                      "FROMDATE": "2016-10-12",
                                      "TODATE": "2016-10-13",
                                      "ROOMTYPECODE": "Acacia",
                                      "ROOMNAME": " 308",
                                      "RATECODE": "RP001",
                                      "PRICEBEFORETAX": "2269.069989",
                                      "TAX": "317.669798"
                                  }
                              ],
                              "GUESTDETAIL": [
                                  {
                                      "GUESTID": "P232",
                                      "FIRSTNAME": "Arvind",
                                      "LASTNAME": "Jaiswal",
                                      "FROMDATE": "2016-10-12",
                                      "TODATE": "2016-10-13",
                                      "EMAIL": "arvind.k.jaishwal@gmail.com",
                                      "PHONE": "9510022471",
                                      "COUNTRY": "",
                                      "NATIONALITY": "India",
                                      "DOB": "0000-00-00",
                                      "GENDER": "M"
                                  },
                                  {
                                      "GUESTID": "P239",
                                      "FIRSTNAME": "Sisodia",
                                      "LASTNAME": "Ranjana",
                                      "FROMDATE": "2016-10-12",
                                      "TODATE": "2016-10-13",
                                      "EMAIL": "arvind.k.jaishwal@gmail.com",
                                      "PHONE": "9510022471",
                                      "COUNTRY": "",
                                      "NATIONALITY": "India",
                                      "DOB": "0000-00-00",
                                      "GENDER": "F"
                                  }
                              ],
                              "TOTALPRICEBEFORETAX": 2269.069989,
                              "TOTALTAX": 317.669798,
                              "PAIDAMOUNT": "0",
                              "GROUPPAIDAMOUNT": "2586.73978",
                              "COMMENT": "",
                              "GROUPCOMMENT": " ",
                              "WRID": "NH7101434618355",
                              "ADDONAMOUNT": "0.000000",
                              "ADDONTAXES": "0.000000",
                              "OTHERCHARGES": "0.000000",
                              "OTHERCHARGESTAX": "0.000000",
                              "GRPOTHERCHARGES": "0.000000",
                              "GRPOTHERCHARGETAX": "0.000000",
                              "EARLYCHECKINCHARGES": "0.000000",
                              "EARLYCHECKOUTCHARGES": "0.000000",
                              "LATECHECKOUTCHARGES": "0.000000",
                              "TAXEXEMPT": "0.000000",
                              "DISCOUNTS(%)": "0.000000",
                              "NOSHOWCHARGES": "0.000000",
                              "CANCELCHARGES": 0,
                              "BALANCE": 7.0000000960135e-6,
                              "GROUPBALANCE": 0,
                              "EXTRABEDS": "0",
                              "MESSAGES": "",
                              "TASKS": ""
                          }
                      ]
                  }
    )
    print(r.content)