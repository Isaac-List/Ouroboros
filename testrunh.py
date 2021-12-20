import xmltodict
import json
import requests
 

def getOCLC(isbn: str):
    url = "http://classify.oclc.org/classify2/Classify?summary=true&isbn=" + isbn
    xml_content= requests.get(url)
    
    #change xml format to ordered json
    my_ordered_dict=xmltodict.parse(xml_content.content)
    json_data= json.dumps(my_ordered_dict)

    code = json.loads(json_data)["classify"]["response"]["@code"]

    if code == "4":
        owi = json.loads(json_data)["classify"]["works"]["work"][0]["@owi"]
        url = "http://classify.oclc.org/classify2/Classify?summary=true&owi=" + owi
        xml_content= requests.get(url)
        my_ordered_dict=xmltodict.parse(xml_content.content)
        json_data= json.dumps(my_ordered_dict)
        code = json.loads(json_data)["classify"]["response"]["@code"]

        if code == "4":
            wi = json.loads(json_data)["classify"]["works"]["work"][0]["@wi"]
            url = "http://classify.oclc.org/classify2/Classify?summary=true&wi=" + wi
            xml_content = requests.get(url)
            data_ordered_dict = xmltodict.parse(xml_content.content)
            json_data = json.dumps(data_ordered_dict)
    
    return json.loads(json_data)

isbn: str = "9780385543781"
book = getOCLC(isbn)
print(book["classify"])
print(book["classify"]["work"]["@author"])
print(book["classify"]["work"]["@title"].title())
print(book["classify"]["recommendations"]["ddc"]["mostPopular"]["@sfa"])
print(book["classify"]["recommendations"]["lcc"]["mostPopular"]["@sfa"])
