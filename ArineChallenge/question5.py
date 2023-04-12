
from typing import Optional
from datetime import datetime

def get_latest_med_ndc(data_obj: dict) -> Optional[str]:
    latest_fill_date = None
    latest_ndc9 = None
    
    if "medications" in data_obj:
        for med in data_obj["medications"]:
            if "fills" in med:
                for fill in med["fills"]:
                    if "fillDate" in fill:
                        fill_date = datetime.strptime(fill["fillDate"], "%Y-%m-%d")
                        if latest_fill_date is None or fill_date > latest_fill_date:
                            latest_fill_date = fill_date
                            latest_ndc9 = med["ndc9"]
                            
    return latest_ndc9


data_obj = {
"etlUpdated": "2012-12-21T23:58:00",
"id": "123",
"medications": [
{
"ndc9": "39017-0147",
"brandName": "AMLODIPINE BESYLATE",
"dosageStrength": "5",
"dosageUnit": "mg",
"doseForm": "tablet",
"drugGroup": [
"ccb",
"antihtn"
],
"route": "oral",
"quantity": "90",
"daysSupply": "90",
"fills": [
{
"fillDate": "2012-02-18",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-05-16",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-08-06",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-11-01",
"daysSupply": "90",
"quantity": "90"
}
],
"display": "AMLODIPINE BESYLATE 5 MG",

"unitsPerDay": "1",
"dosePerDay": "5"
},
{
"ndc9": "60505-2671",
"brandName": "ATORVASTATIN CALCIUM",
"genericName": "ATORVASTATIN CALCIUM",
"dosageStrength": "80",
"dosageUnit": "mg",
"doseForm": "tablet, film coated",
"drugGroup": [
"statin",
"azoleddi",
"antilipid",
"cms_statin",
"cms_spc_statin"
],
"route": "oral",
"quantity": "90",
"daysSupply": "90",
"fills": [
{
"fillDate": "2012-04-10",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-07-09",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-10-09",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-01-03",
"daysSupply": "90",
"quantity": "90"
},
{

"fillDate": "2012-04-01",
"daysSupply": "90",
"quantity": "90"
}
],
"unitsPerDay": "1",
"dosePerDay": "80"
},
{
"ndc9": "68382-0136",
"brandName": "LOSARTAN POTASSIUM",
"genericName": "LOSARTAN POTASSIUM",
"dosageStrength": "50",
"dosageUnit": "mg",
"doseForm": "tablet, film coated",
"drugGroup": [
"arb",
"antihtn",
"cms_rasa"
],
"route": "oral",
"quantity": "90",
"daysSupply": "90",
"fills": [
{
"fillDate": "2012-02-25",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-05-25",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-07-14",
"daysSupply": "90",
"quantity": "90"
},
{
"fillDate": "2012-10-15",
"daysSupply": "90",

"quantity": "90"
}
],
"unitsPerDay": "1",
"dosePerDay": "50"
},
{
"ndc9": "00378-0018",
"brandName": "METOPROLOL TARTRATE",
"genericName": "METOPROLOL TARTRATE",
"dosageStrength": "25",
"dosageUnit": "mg",
"doseForm": "tablet, film coated",
"drugGroup": [
"antihtn",
"betablocker"
],
"route": "oral",
"quantity": "180",
"daysSupply": "90",
"fills": [
{
"fillDate": "2012-02-06",
"daysSupply": "90",
"quantity": "180"
},
{
"fillDate": "2012-05-16",
"daysSupply": "90",
"quantity": "180"
},
{
"fillDate": "2012-08-13",
"daysSupply": "90",
"quantity": "180"
},
{
"fillDate": "2012-11-12",
"daysSupply": "90",
"quantity": "180"
},
{

"fillDate": "2012-02-16",
"daysSupply": "90",
"quantity": "180"
}
],
"unitsPerDay": "2",
"dosePerDay": "50"
}
],
"resourceType": "cmr"
}

print(get_latest_med_ndc(data_obj))