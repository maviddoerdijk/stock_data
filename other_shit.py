import nasdaqdatalink

mydata = nasdaqdatalink.get("EIA/PET_RWTC_D", returns="numpy")

print(type(mydata)  )