
import twccommon
import time

areaList = wxdata.getUGCInterestList('CCC999', 'county')

twccommon.Log.info("i1DT - Thanks for using the 45 Degrees i1 Encoder.")

Y, M, D, h, m, s, wd, jd, dst = time.localtime(time.time())
dOffset = 0  # Always use offset of 0

keyTime = time.mktime((Y, M, D + dOffset, 5, 0, 0, 0, 0, -1))

numDayparts = 4

times = [
    keyTime,
    keyTime + (12 * 3600),
    keyTime + (24 * 3600),
    keyTime + (36 * 3600)
]


    


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Overcast. Low -9C. Winds W at 10 to 15 km/h.'
    
    b_1_2.skyCondition = 2600
    b_1_2.temp = -9
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_1_2,
        validTime=1763938800,
        numDayparts=4,
        expiration=int(1763938800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_2))
                


for area in areaList:
    forecastTime_2_1 = 1763982000
    b_2_1 = twc.Data()
    
    b_2_1.phrase = 'Cloudy. High -2C. Winds WNW at 10 to 15 km/h.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = -2
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_2_1,
        validTime=1763982000,
        numDayparts=4,
        expiration=int(1763982000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_1))
        


for area in areaList:
    forecastTime_2_2 = 1764025200
    b_2_2 = twc.Data()
    
    b_2_2.phrase = 'Mostly cloudy. Low around -10C. Winds NW at 10 to 15 km/h.'
    
    b_2_2.skyCondition = 2700
    b_2_2.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_2_2,
        validTime=1764025200,
        numDayparts=4,
        expiration=int(1764025200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_2))
                


for area in areaList:
    forecastTime_3_1 = 1764068400
    b_3_1 = twc.Data()
    
    b_3_1.phrase = 'Cloudy skies early will become partly cloudy later in the day. High around -5C. Winds W at 10 to 15 km/h.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = -5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_3_1,
        validTime=1764068400,
        numDayparts=4,
        expiration=int(1764068400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_1))
        


for area in areaList:
    forecastTime_3_2 = 1764111600
    b_3_2 = twc.Data()
    
    b_3_2.phrase = 'Partly cloudy skies during the evening will give way to cloudy skies overnight. Low -14C. Winds light and variable.'
    
    b_3_2.skyCondition = 2700
    b_3_2.temp = -14
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_3_2,
        validTime=1764111600,
        numDayparts=4,
        expiration=int(1764111600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_2))
                


for area in areaList:
    forecastTime_4_1 = 1764154800
    b_4_1 = twc.Data()
    
    b_4_1.phrase = 'Cloudy skies early, then partly cloudy in the afternoon. High -6C. Winds light and variable.'
    
    b_4_1.skyCondition = 9003
    b_4_1.temp = -6
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_4_1,
        validTime=1764154800,
        numDayparts=4,
        expiration=int(1764154800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_1))
        


for area in areaList:
    forecastTime_4_2 = 1764198000
    b_4_2 = twc.Data()
    
    b_4_2.phrase = 'Partly cloudy. Low -14C. Winds light and variable.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = -14
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_4_2,
        validTime=1764198000,
        numDayparts=4,
        expiration=int(1764198000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_2))
                


for area in areaList:
    forecastTime_5_1 = 1764241200
    b_5_1 = twc.Data()
    
    b_5_1.phrase = 'Sunshine and clouds mixed. High -8C. Winds light and variable.'
    
    b_5_1.skyCondition = 3000
    b_5_1.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_5_1,
        validTime=1764241200,
        numDayparts=4,
        expiration=int(1764241200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_1))
        


for area in areaList:
    forecastTime_5_2 = 1764284400
    b_5_2 = twc.Data()
    
    b_5_2.phrase = 'Cloudy. Low -13C. Winds ENE at 10 to 15 km/h.'
    
    b_5_2.skyCondition = 2600
    b_5_2.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_5_2,
        validTime=1764284400,
        numDayparts=4,
        expiration=int(1764284400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_2))
                


for area in areaList:
    forecastTime_6_1 = 1764327600
    b_6_1 = twc.Data()
    
    b_6_1.phrase = 'Cloudy. High -8C. Winds N at 10 to 15 km/h.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_6_1,
        validTime=1764327600,
        numDayparts=4,
        expiration=int(1764327600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_1))
        


for area in areaList:
    forecastTime_6_2 = 1764370800
    b_6_2 = twc.Data()
    
    b_6_2.phrase = 'Considerable cloudiness. Low -16C. Winds light and variable.'
    
    b_6_2.skyCondition = 2700
    b_6_2.temp = -16
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_6_2,
        validTime=1764370800,
        numDayparts=4,
        expiration=int(1764370800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_2))
                


for area in areaList:
    forecastTime_7_1 = 1764414000
    b_7_1 = twc.Data()
    
    b_7_1.phrase = 'Sunshine and clouds mixed. High near -10C. Winds NW at 10 to 15 km/h.'
    
    b_7_1.skyCondition = 3000
    b_7_1.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_7_1,
        validTime=1764414000,
        numDayparts=4,
        expiration=int(1764414000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_1))
        


for area in areaList:
    forecastTime_7_2 = 1764457200
    b_7_2 = twc.Data()
    
    b_7_2.phrase = 'Partly cloudy. Low around -20C. Winds WNW at 10 to 15 km/h.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -20
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_7_2,
        validTime=1764457200,
        numDayparts=4,
        expiration=int(1764457200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_2))
                


for area in areaList:
    forecastTime_8_1 = 1764500400
    b_8_1 = twc.Data()
    
    b_8_1.phrase = 'Mostly sunny skies. High -13C. Winds SW at 10 to 15 km/h.'
    
    b_8_1.skyCondition = 3400
    b_8_1.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_8_1,
        validTime=1764500400,
        numDayparts=4,
        expiration=int(1764500400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_1))
        


for area in areaList:
    forecastTime_8_2 = 1764543600
    b_8_2 = twc.Data()
    
    b_8_2.phrase = 'A few clouds. Low -17C. Winds SSW at 10 to 15 km/h.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = -17
    # Vocal key for those trying to recreate: man nvm bruh whatever AI worked on this code did ts wrong
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_8_2,
        validTime=1764543600,
        numDayparts=4,
        expiration=int(1764543600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_2))
                


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Partly cloudy early followed by cloudy skies overnight. Low -9C. Winds W at 10 to 15 km/h.'
    
    b_1_2.skyCondition = 2700
    b_1_2.temp = -9
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_1_2,
        validTime=1763938800,
        numDayparts=4,
        expiration=int(1763938800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_2))
                


for area in areaList:
    forecastTime_2_1 = 1763982000
    b_2_1 = twc.Data()
    
    b_2_1.phrase = 'Cloudy skies. High -3C. Winds WNW at 10 to 15 km/h.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = -3
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_2_1,
        validTime=1763982000,
        numDayparts=4,
        expiration=int(1763982000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_1))
        


for area in areaList:
    forecastTime_2_2 = 1764025200
    b_2_2 = twc.Data()
    
    b_2_2.phrase = 'Cloudy. Low near -10C. Winds NW at 10 to 15 km/h.'
    
    b_2_2.skyCondition = 2600
    b_2_2.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_2_2,
        validTime=1764025200,
        numDayparts=4,
        expiration=int(1764025200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_2))
                


for area in areaList:
    forecastTime_3_1 = 1764068400
    b_3_1 = twc.Data()
    
    b_3_1.phrase = 'Cloudy. High near -5C. Winds WNW at 10 to 15 km/h.'
    
    b_3_1.skyCondition = 2600
    b_3_1.temp = -5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_3_1,
        validTime=1764068400,
        numDayparts=4,
        expiration=int(1764068400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_1))
        


for area in areaList:
    forecastTime_3_2 = 1764111600
    b_3_2 = twc.Data()
    
    b_3_2.phrase = 'Partly cloudy during the evening followed by cloudy skies overnight. Low -13C. Winds light and variable.'
    
    b_3_2.skyCondition = 2700
    b_3_2.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_3_2,
        validTime=1764111600,
        numDayparts=4,
        expiration=int(1764111600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_2))
                


for area in areaList:
    forecastTime_4_1 = 1764154800
    b_4_1 = twc.Data()
    
    b_4_1.phrase = 'Cloudy skies early, followed by partial clearing. High -6C. Winds light and variable.'
    
    b_4_1.skyCondition = 9003
    b_4_1.temp = -6
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_4_1,
        validTime=1764154800,
        numDayparts=4,
        expiration=int(1764154800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_1))
        


for area in areaList:
    forecastTime_4_2 = 1764198000
    b_4_2 = twc.Data()
    
    b_4_2.phrase = 'Mostly clear skies. Low -13C. Winds light and variable.'
    
    b_4_2.skyCondition = 3300
    b_4_2.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_4_2,
        validTime=1764198000,
        numDayparts=4,
        expiration=int(1764198000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_2))
                


for area in areaList:
    forecastTime_5_1 = 1764241200
    b_5_1 = twc.Data()
    
    b_5_1.phrase = 'Partly cloudy skies. High -8C. Winds light and variable.'
    
    b_5_1.skyCondition = 3000
    b_5_1.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_5_1,
        validTime=1764241200,
        numDayparts=4,
        expiration=int(1764241200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_1))
        


for area in areaList:
    forecastTime_5_2 = 1764284400
    b_5_2 = twc.Data()
    
    b_5_2.phrase = 'Cloudy skies. Low -13C. Winds light and variable.'
    
    b_5_2.skyCondition = 2600
    b_5_2.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_5_2,
        validTime=1764284400,
        numDayparts=4,
        expiration=int(1764284400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_2))
                


for area in areaList:
    forecastTime_6_1 = 1764327600
    b_6_1 = twc.Data()
    
    b_6_1.phrase = 'Cloudy. High -9C. Winds N at 10 to 15 km/h.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = -9
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_6_1,
        validTime=1764327600,
        numDayparts=4,
        expiration=int(1764327600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_1))
        


for area in areaList:
    forecastTime_6_2 = 1764370800
    b_6_2 = twc.Data()
    
    b_6_2.phrase = 'Mostly cloudy. Low -16C. Winds light and variable.'
    
    b_6_2.skyCondition = 2700
    b_6_2.temp = -16
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_6_2,
        validTime=1764370800,
        numDayparts=4,
        expiration=int(1764370800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_2))
                


for area in areaList:
    forecastTime_7_1 = 1764414000
    b_7_1 = twc.Data()
    
    b_7_1.phrase = 'Mostly cloudy skies. High around -10C. Winds NW at 10 to 15 km/h.'
    
    b_7_1.skyCondition = 2800
    b_7_1.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_7_1,
        validTime=1764414000,
        numDayparts=4,
        expiration=int(1764414000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_1))
        


for area in areaList:
    forecastTime_7_2 = 1764457200
    b_7_2 = twc.Data()
    
    b_7_2.phrase = 'A few clouds. Low around -20C. Winds WNW at 10 to 15 km/h.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -20
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_7_2,
        validTime=1764457200,
        numDayparts=4,
        expiration=int(1764457200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_2))
                


for area in areaList:
    forecastTime_8_1 = 1764500400
    b_8_1 = twc.Data()
    
    b_8_1.phrase = 'Sunshine and clouds mixed. High -14C. Winds SW at 15 to 25 km/h.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = -14
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_8_1,
        validTime=1764500400,
        numDayparts=4,
        expiration=int(1764500400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_1))
        


for area in areaList:
    forecastTime_8_2 = 1764543600
    b_8_2 = twc.Data()
    
    b_8_2.phrase = 'A few clouds. Low -18C. Winds SW at 10 to 15 km/h.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = -18
    # Vocal key for those trying to recreate: man nvm bruh whatever AI worked on this code did ts wrong
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_8_2,
        validTime=1764543600,
        numDayparts=4,
        expiration=int(1764543600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_2))
                


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Mostly cloudy. Low near -5C. Winds NNW at 10 to 15 km/h.'
    
    b_1_2.skyCondition = 2700
    b_1_2.temp = -5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_1_2,
        validTime=1763938800,
        numDayparts=4,
        expiration=int(1763938800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_2))
                


for area in areaList:
    forecastTime_2_1 = 1763982000
    b_2_1 = twc.Data()
    
    b_2_1.phrase = 'Cloudy with snow showers developing during the afternoon. High 2C. Winds N at 10 to 15 km/h. Chance of snow 40%.'
    
    b_2_1.skyCondition = 7803
    b_2_1.temp = 2
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_2_1,
        validTime=1763982000,
        numDayparts=4,
        expiration=int(1763982000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_1))
        


for area in areaList:
    forecastTime_2_2 = 1764025200
    b_2_2 = twc.Data()
    
    b_2_2.phrase = 'Cloudy with snow showers mainly during the evening. Low -8C. Winds NNW at 15 to 30 km/h. Chance of snow 40%. Snow accumulations less than 2cm.'
    
    b_2_2.skyCondition = 6800
    b_2_2.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_2_2,
        validTime=1764025200,
        numDayparts=4,
        expiration=int(1764025200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_2))
                


for area in areaList:
    forecastTime_3_1 = 1764068400
    b_3_1 = twc.Data()
    
    b_3_1.phrase = 'Cloudy skies early will become partly cloudy later in the day. High -3C. Winds NW at 15 to 30 km/h.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = -3
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_3_1,
        validTime=1764068400,
        numDayparts=4,
        expiration=int(1764068400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_1))
        


for area in areaList:
    forecastTime_3_2 = 1764111600
    b_3_2 = twc.Data()
    
    b_3_2.phrase = 'A few clouds. Low -12C. Winds WNW at 10 to 15 km/h.'
    
    b_3_2.skyCondition = 2900
    b_3_2.temp = -12
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_3_2,
        validTime=1764111600,
        numDayparts=4,
        expiration=int(1764111600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_2))
                


for area in areaList:
    forecastTime_4_1 = 1764154800
    b_4_1 = twc.Data()
    
    b_4_1.phrase = 'Intervals of clouds and sunshine. High -4C. Winds W at 10 to 15 km/h.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = -4
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_4_1,
        validTime=1764154800,
        numDayparts=4,
        expiration=int(1764154800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_1))
        


for area in areaList:
    forecastTime_4_2 = 1764198000
    b_4_2 = twc.Data()
    
    b_4_2.phrase = 'Generally fair. Low -12C. Winds light and variable.'
    
    b_4_2.skyCondition = 3300
    b_4_2.temp = -12
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_4_2,
        validTime=1764198000,
        numDayparts=4,
        expiration=int(1764198000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_2))
                


for area in areaList:
    forecastTime_5_1 = 1764241200
    b_5_1 = twc.Data()
    
    b_5_1.phrase = 'Partly cloudy. High around -5C. Winds WNW at 10 to 15 km/h.'
    
    b_5_1.skyCondition = 3000
    b_5_1.temp = -5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_5_1,
        validTime=1764241200,
        numDayparts=4,
        expiration=int(1764241200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_1))
        


for area in areaList:
    forecastTime_5_2 = 1764284400
    b_5_2 = twc.Data()
    
    b_5_2.phrase = 'Considerable cloudiness. Low -12C. Winds ESE at 10 to 15 km/h.'
    
    b_5_2.skyCondition = 2700
    b_5_2.temp = -12
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_5_2,
        validTime=1764284400,
        numDayparts=4,
        expiration=int(1764284400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_2))
                


for area in areaList:
    forecastTime_6_1 = 1764327600
    b_6_1 = twc.Data()
    
    b_6_1.phrase = 'Overcast. High -6C. Winds NNE at 10 to 15 km/h.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = -6
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_6_1,
        validTime=1764327600,
        numDayparts=4,
        expiration=int(1764327600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_1))
        


for area in areaList:
    forecastTime_6_2 = 1764370800
    b_6_2 = twc.Data()
    
    b_6_2.phrase = 'Overcast. Low -14C. Winds N at 10 to 15 km/h.'
    
    b_6_2.skyCondition = 2600
    b_6_2.temp = -14
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_6_2,
        validTime=1764370800,
        numDayparts=4,
        expiration=int(1764370800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_2))
                


for area in areaList:
    forecastTime_7_1 = 1764414000
    b_7_1 = twc.Data()
    
    b_7_1.phrase = 'Overcast. High -8C. Winds NW at 10 to 15 km/h.'
    
    b_7_1.skyCondition = 2600
    b_7_1.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_7_1,
        validTime=1764414000,
        numDayparts=4,
        expiration=int(1764414000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_1))
        


for area in areaList:
    forecastTime_7_2 = 1764457200
    b_7_2 = twc.Data()
    
    b_7_2.phrase = 'Mostly cloudy skies. Low -18C. Winds NW at 10 to 15 km/h.'
    
    b_7_2.skyCondition = 2700
    b_7_2.temp = -18
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_7_2,
        validTime=1764457200,
        numDayparts=4,
        expiration=int(1764457200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_2))
                


for area in areaList:
    forecastTime_8_1 = 1764500400
    b_8_1 = twc.Data()
    
    b_8_1.phrase = 'Partly cloudy skies. High -13C. Winds W at 15 to 25 km/h.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_8_1,
        validTime=1764500400,
        numDayparts=4,
        expiration=int(1764500400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_1))
        


for area in areaList:
    forecastTime_8_2 = 1764543600
    b_8_2 = twc.Data()
    
    b_8_2.phrase = 'Partly cloudy. Low -17C. Winds SSW at 15 to 25 km/h.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = -17
    # Vocal key for those trying to recreate: man nvm bruh whatever AI worked on this code did ts wrong
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_8_2,
        validTime=1764543600,
        numDayparts=4,
        expiration=int(1764543600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_2))
                


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Partly cloudy skies during the evening will give way to considerable cloudiness and fog after midnight. Low 3C. Winds light and variable.'
    
    b_1_2.skyCondition = 9300
    b_1_2.temp = 3
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_1_2,
        validTime=1763938800,
        numDayparts=4,
        expiration=int(1763938800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_2))
                


for area in areaList:
    forecastTime_2_1 = 1763982000
    b_2_1 = twc.Data()
    
    b_2_1.phrase = 'Cloudy skies with some morning fog. High around 15C. Winds light and variable.'
    
    b_2_1.skyCondition = 9203
    b_2_1.temp = 15
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_2_1,
        validTime=1763982000,
        numDayparts=4,
        expiration=int(1763982000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_1))
        


for area in areaList:
    forecastTime_2_2 = 1764025200
    b_2_2 = twc.Data()
    
    b_2_2.phrase = 'Showers early, becoming a steady rain late. Low 11C. Winds SSE at 10 to 15 km/h. Chance of rain 90%. Rainfall near 12mm.'
    
    b_2_2.skyCondition = 1200
    b_2_2.temp = 11
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_2_2,
        validTime=1764025200,
        numDayparts=4,
        expiration=int(1764025200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_2))
                


for area in areaList:
    forecastTime_3_1 = 1764068400
    b_3_1 = twc.Data()
    
    b_3_1.phrase = 'Rain diminishing to a few showers in the afternoon. High 16C. Winds SSW at 10 to 15 km/h. Chance of rain 70%.'
    
    b_3_1.skyCondition = 1200
    b_3_1.temp = 16
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_3_1,
        validTime=1764068400,
        numDayparts=4,
        expiration=int(1764068400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_1))
        


for area in areaList:
    forecastTime_3_2 = 1764111600
    b_3_2 = twc.Data()
    
    b_3_2.phrase = 'Cloudy skies. Low 7C. Winds WSW at 15 to 25 km/h.'
    
    b_3_2.skyCondition = 2600
    b_3_2.temp = 7
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_3_2,
        validTime=1764111600,
        numDayparts=4,
        expiration=int(1764111600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_2))
                


for area in areaList:
    forecastTime_4_1 = 1764154800
    b_4_1 = twc.Data()
    
    b_4_1.phrase = 'Sunshine and clouds mixed. High around 10C. Winds W at 15 to 30 km/h.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = 10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_4_1,
        validTime=1764154800,
        numDayparts=4,
        expiration=int(1764154800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_1))
        


for area in areaList:
    forecastTime_4_2 = 1764198000
    b_4_2 = twc.Data()
    
    b_4_2.phrase = 'Mostly cloudy skies early will become partly cloudy late. Low -2C. Winds W at 10 to 15 km/h.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = -2
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_4_2,
        validTime=1764198000,
        numDayparts=4,
        expiration=int(1764198000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_2))
                


for area in areaList:
    forecastTime_5_1 = 1764241200
    b_5_1 = twc.Data()
    
    b_5_1.phrase = 'Abundant sunshine. High around 5C. Winds WNW at 15 to 25 km/h.'
    
    b_5_1.skyCondition = 3200
    b_5_1.temp = 5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_5_1,
        validTime=1764241200,
        numDayparts=4,
        expiration=int(1764241200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_1))
        


for area in areaList:
    forecastTime_5_2 = 1764284400
    b_5_2 = twc.Data()
    
    b_5_2.phrase = 'A mostly clear sky. Low around -5C. Winds WNW at 10 to 15 km/h.'
    
    b_5_2.skyCondition = 3100
    b_5_2.temp = -5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_5_2,
        validTime=1764284400,
        numDayparts=4,
        expiration=int(1764284400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_2))
                


for area in areaList:
    forecastTime_6_1 = 1764327600
    b_6_1 = twc.Data()
    
    b_6_1.phrase = 'Mostly sunny skies. High around 5C. Winds light and variable.'
    
    b_6_1.skyCondition = 3400
    b_6_1.temp = 5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_6_1,
        validTime=1764327600,
        numDayparts=4,
        expiration=int(1764327600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_1))
        


for area in areaList:
    forecastTime_6_2 = 1764370800
    b_6_2 = twc.Data()
    
    b_6_2.phrase = 'Partly cloudy skies during the evening will give way to cloudy skies overnight. Low -2C. Winds light and variable.'
    
    b_6_2.skyCondition = 2900
    b_6_2.temp = -2
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_6_2,
        validTime=1764370800,
        numDayparts=4,
        expiration=int(1764370800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_2))
                


for area in areaList:
    forecastTime_7_1 = 1764414000
    b_7_1 = twc.Data()
    
    b_7_1.phrase = 'Cloudy in the morning, then off and on rain showers during the afternoon hours. High 6C. Winds light and variable. Chance of rain 40%.'
    
    b_7_1.skyCondition = 7103
    b_7_1.temp = 6
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_7_1,
        validTime=1764414000,
        numDayparts=4,
        expiration=int(1764414000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_1))
        


for area in areaList:
    forecastTime_7_2 = 1764457200
    b_7_2 = twc.Data()
    
    b_7_2.phrase = 'Cloudy with showers. Low 3C. Winds light and variable. Chance of rain 60%.'
    
    b_7_2.skyCondition = 1100
    b_7_2.temp = 3
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_7_2,
        validTime=1764457200,
        numDayparts=4,
        expiration=int(1764457200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_2))
                


for area in areaList:
    forecastTime_8_1 = 1764500400
    b_8_1 = twc.Data()
    
    b_8_1.phrase = 'Cloudy with occasional rain showers. High 11C. Winds S at 10 to 15 km/h. Chance of rain 60%.'
    
    b_8_1.skyCondition = 1100
    b_8_1.temp = 11
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_8_1,
        validTime=1764500400,
        numDayparts=4,
        expiration=int(1764500400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_1))
        


for area in areaList:
    forecastTime_8_2 = 1764543600
    b_8_2 = twc.Data()
    
    b_8_2.phrase = 'Overcast with rain showers at times. Low 9C. Winds S at 10 to 15 km/h. Chance of rain 60%.'
    
    b_8_2.skyCondition = 1100
    b_8_2.temp = 9
    # Vocal key for those trying to recreate: man nvm bruh whatever AI worked on this code did ts wrong
    wxdata.setDaypartData(
        loc='72423000',
        type='textFcst',
        data=b_8_2,
        validTime=1764543600,
        numDayparts=4,
        expiration=int(1764543600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_2))
                


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Partly cloudy. Low around -10C. Winds WNW at 10 to 15 km/h.'
    
    b_1_2.skyCondition = 2900
    b_1_2.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_1_2,
        validTime=1763938800,
        numDayparts=4,
        expiration=int(1763938800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_2))
                


for area in areaList:
    forecastTime_2_1 = 1763982000
    b_2_1 = twc.Data()
    
    b_2_1.phrase = 'Cloudy. High -3C. Winds NW at 10 to 15 km/h.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = -3
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_2_1,
        validTime=1763982000,
        numDayparts=4,
        expiration=int(1763982000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_1))
        


for area in areaList:
    forecastTime_2_2 = 1764025200
    b_2_2 = twc.Data()
    
    b_2_2.phrase = 'Cloudy. Low near -10C. Winds NW at 10 to 15 km/h.'
    
    b_2_2.skyCondition = 2600
    b_2_2.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_2_2,
        validTime=1764025200,
        numDayparts=4,
        expiration=int(1764025200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_2))
                


for area in areaList:
    forecastTime_3_1 = 1764068400
    b_3_1 = twc.Data()
    
    b_3_1.phrase = 'Cloudy skies early, followed by partial clearing. High near -5C. Winds WNW at 10 to 15 km/h.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = -5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_3_1,
        validTime=1764068400,
        numDayparts=4,
        expiration=int(1764068400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_1))
        


for area in areaList:
    forecastTime_3_2 = 1764111600
    b_3_2 = twc.Data()
    
    b_3_2.phrase = 'Partly to mostly cloudy. Low near -15C. Winds light and variable.'
    
    b_3_2.skyCondition = 2900
    b_3_2.temp = -15
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_3_2,
        validTime=1764111600,
        numDayparts=4,
        expiration=int(1764111600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_2))
                


for area in areaList:
    forecastTime_4_1 = 1764154800
    b_4_1 = twc.Data()
    
    b_4_1.phrase = 'Cloudy early with partial sunshine expected late. High -7C. Winds light and variable.'
    
    b_4_1.skyCondition = 9003
    b_4_1.temp = -7
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_4_1,
        validTime=1764154800,
        numDayparts=4,
        expiration=int(1764154800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_1))
        


for area in areaList:
    forecastTime_4_2 = 1764198000
    b_4_2 = twc.Data()
    
    b_4_2.phrase = 'A few clouds. Low -14C. Winds light and variable.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = -14
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_4_2,
        validTime=1764198000,
        numDayparts=4,
        expiration=int(1764198000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_2))
                


for area in areaList:
    forecastTime_5_1 = 1764241200
    b_5_1 = twc.Data()
    
    b_5_1.phrase = 'Considerable clouds early. Some decrease in clouds later in the day. High -8C. Winds light and variable.'
    
    b_5_1.skyCondition = 3000
    b_5_1.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_5_1,
        validTime=1764241200,
        numDayparts=4,
        expiration=int(1764241200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_1))
        


for area in areaList:
    forecastTime_5_2 = 1764284400
    b_5_2 = twc.Data()
    
    b_5_2.phrase = 'Cloudy skies. Low -13C. Winds light and variable.'
    
    b_5_2.skyCondition = 2600
    b_5_2.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_5_2,
        validTime=1764284400,
        numDayparts=4,
        expiration=int(1764284400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_2))
                


for area in areaList:
    forecastTime_6_1 = 1764327600
    b_6_1 = twc.Data()
    
    b_6_1.phrase = 'Cloudy. High -9C. Winds light and variable.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = -9
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_6_1,
        validTime=1764327600,
        numDayparts=4,
        expiration=int(1764327600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_1))
        


for area in areaList:
    forecastTime_6_2 = 1764370800
    b_6_2 = twc.Data()
    
    b_6_2.phrase = 'Considerable cloudiness. Low around -15C. Winds light and variable.'
    
    b_6_2.skyCondition = 2700
    b_6_2.temp = -15
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_6_2,
        validTime=1764370800,
        numDayparts=4,
        expiration=int(1764370800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_2))
                


for area in areaList:
    forecastTime_7_1 = 1764414000
    b_7_1 = twc.Data()
    
    b_7_1.phrase = 'Considerable cloudiness. High around -10C. Winds NNW at 10 to 15 km/h.'
    
    b_7_1.skyCondition = 2800
    b_7_1.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_7_1,
        validTime=1764414000,
        numDayparts=4,
        expiration=int(1764414000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_1))
        


for area in areaList:
    forecastTime_7_2 = 1764457200
    b_7_2 = twc.Data()
    
    b_7_2.phrase = 'A few clouds. Low around -20C. Winds NW at 10 to 15 km/h.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -20
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_7_2,
        validTime=1764457200,
        numDayparts=4,
        expiration=int(1764457200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_2))
                


for area in areaList:
    forecastTime_8_1 = 1764500400
    b_8_1 = twc.Data()
    
    b_8_1.phrase = 'Sunshine and clouds mixed. High -13C. Winds SW at 10 to 15 km/h.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_8_1,
        validTime=1764500400,
        numDayparts=4,
        expiration=int(1764500400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_1))
        


for area in areaList:
    forecastTime_8_2 = 1764543600
    b_8_2 = twc.Data()
    
    b_8_2.phrase = 'A few clouds. Low -17C. Winds SW at 10 to 15 km/h.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = -17
    # Vocal key for those trying to recreate: man nvm bruh whatever AI worked on this code did ts wrong
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_8_2,
        validTime=1764543600,
        numDayparts=4,
        expiration=int(1764543600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_2))
                


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'A few passing clouds. Low -8C. Winds W at 10 to 15 km/h.'
    
    b_1_2.skyCondition = 3300
    b_1_2.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_1_2,
        validTime=1763938800,
        numDayparts=4,
        expiration=int(1763938800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_2))
                


for area in areaList:
    forecastTime_2_1 = 1763982000
    b_2_1 = twc.Data()
    
    b_2_1.phrase = 'Cloudy skies. High -3C. Winds WNW at 10 to 15 km/h.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = -3
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_2_1,
        validTime=1763982000,
        numDayparts=4,
        expiration=int(1763982000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_1))
        


for area in areaList:
    forecastTime_2_2 = 1764025200
    b_2_2 = twc.Data()
    
    b_2_2.phrase = 'Cloudy skies. Low -8C. Winds light and variable.'
    
    b_2_2.skyCondition = 2600
    b_2_2.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_2_2,
        validTime=1764025200,
        numDayparts=4,
        expiration=int(1764025200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_2_2))
                


for area in areaList:
    forecastTime_3_1 = 1764068400
    b_3_1 = twc.Data()
    
    b_3_1.phrase = 'Cloudy skies early will become partly cloudy later in the day. High near -5C. Winds WNW at 10 to 15 km/h.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = -5
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_3_1,
        validTime=1764068400,
        numDayparts=4,
        expiration=int(1764068400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_1))
        


for area in areaList:
    forecastTime_3_2 = 1764111600
    b_3_2 = twc.Data()
    
    b_3_2.phrase = 'Mostly cloudy. Low -13C. Winds light and variable.'
    
    b_3_2.skyCondition = 2700
    b_3_2.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_3_2,
        validTime=1764111600,
        numDayparts=4,
        expiration=int(1764111600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_3_2))
                


for area in areaList:
    forecastTime_4_1 = 1764154800
    b_4_1 = twc.Data()
    
    b_4_1.phrase = 'Intervals of clouds and sunshine. High -7C. Winds light and variable.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = -7
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_4_1,
        validTime=1764154800,
        numDayparts=4,
        expiration=int(1764154800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_1))
        


for area in areaList:
    forecastTime_4_2 = 1764198000
    b_4_2 = twc.Data()
    
    b_4_2.phrase = 'Partly cloudy early with increasing clouds overnight. Low -11C. Winds light and variable.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = -11
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_4_2,
        validTime=1764198000,
        numDayparts=4,
        expiration=int(1764198000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_4_2))
                


for area in areaList:
    forecastTime_5_1 = 1764241200
    b_5_1 = twc.Data()
    
    b_5_1.phrase = 'Mostly cloudy skies. High -8C. Winds light and variable.'
    
    b_5_1.skyCondition = 2800
    b_5_1.temp = -8
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_5_1,
        validTime=1764241200,
        numDayparts=4,
        expiration=int(1764241200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_1))
        


for area in areaList:
    forecastTime_5_2 = 1764284400
    b_5_2 = twc.Data()
    
    b_5_2.phrase = 'Overcast. Low -13C. Winds light and variable.'
    
    b_5_2.skyCondition = 2600
    b_5_2.temp = -13
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_5_2,
        validTime=1764284400,
        numDayparts=4,
        expiration=int(1764284400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_5_2))
                


for area in areaList:
    forecastTime_6_1 = 1764327600
    b_6_1 = twc.Data()
    
    b_6_1.phrase = 'Mainly cloudy. High near -10C. Winds NNW at 10 to 15 km/h.'
    
    b_6_1.skyCondition = 2800
    b_6_1.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_6_1,
        validTime=1764327600,
        numDayparts=4,
        expiration=int(1764327600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_1))
        


for area in areaList:
    forecastTime_6_2 = 1764370800
    b_6_2 = twc.Data()
    
    b_6_2.phrase = 'Mostly cloudy skies early, then partly cloudy after midnight. Low -16C. Winds light and variable.'
    
    b_6_2.skyCondition = 2900
    b_6_2.temp = -16
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_6_2,
        validTime=1764370800,
        numDayparts=4,
        expiration=int(1764370800 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_6_2))
                


for area in areaList:
    forecastTime_7_1 = 1764414000
    b_7_1 = twc.Data()
    
    b_7_1.phrase = 'Partly cloudy skies. High around -10C. Winds NW at 10 to 15 km/h.'
    
    b_7_1.skyCondition = 3000
    b_7_1.temp = -10
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_7_1,
        validTime=1764414000,
        numDayparts=4,
        expiration=int(1764414000 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_1))
        


for area in areaList:
    forecastTime_7_2 = 1764457200
    b_7_2 = twc.Data()
    
    b_7_2.phrase = 'A few clouds from time to time. Low near -20C. Winds WNW at 10 to 15 km/h.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -20
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_7_2,
        validTime=1764457200,
        numDayparts=4,
        expiration=int(1764457200 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_7_2))
                


for area in areaList:
    forecastTime_8_1 = 1764500400
    b_8_1 = twc.Data()
    
    b_8_1.phrase = 'Partly cloudy. High near -15C. Winds WSW at 10 to 15 km/h.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = -15
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_8_1,
        validTime=1764500400,
        numDayparts=4,
        expiration=int(1764500400 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_1))
        


for area in areaList:
    forecastTime_8_2 = 1764543600
    b_8_2 = twc.Data()
    
    b_8_2.phrase = 'Partly cloudy. Low -19C. Winds SW at 10 to 15 km/h.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = -19
    # Vocal key for those trying to recreate: man nvm bruh whatever AI worked on this code did ts wrong
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_8_2,
        validTime=1764543600,
        numDayparts=4,
        expiration=int(1764543600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_8_2))
                


