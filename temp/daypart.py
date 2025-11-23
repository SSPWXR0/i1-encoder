
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
    forecastTime_1_1 = 1763895600
    b_1_1 = twc.Data()
    
    b_1_1.phrase = 'A mix of clouds and sun. High 39F. Winds WNW at 5 to 10 mph.'
    
    b_1_1.skyCondition = 3000
    b_1_1.temp = 39
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866000',
        type='textFcst',
        data=b_1_1,
        validTime=1763895600,
        numDayparts=4,
        expiration=int(1763895600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_1))
        


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Partly cloudy skies this evening will become overcast overnight. Low 16F. Winds W at 5 to 10 mph.'
    
    b_1_2.skyCondition = 2700
    b_1_2.temp = 16
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
    
    b_2_1.phrase = 'Cloudy skies. High 28F. Winds WNW at 5 to 10 mph.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = 28
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
    
    b_2_2.phrase = 'Considerable cloudiness. Low 14F. Winds NW at 5 to 10 mph.'
    
    b_2_2.skyCondition = 2700
    b_2_2.temp = 14
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
    
    b_3_1.phrase = 'Cloudy skies early, then partly cloudy in the afternoon. High 22F. Winds WNW at 5 to 10 mph.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = 22
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
    
    b_3_2.phrase = 'Partly cloudy early with increasing clouds overnight. Low 8F. Winds light and variable.'
    
    b_3_2.skyCondition = 2900
    b_3_2.temp = 8
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
    
    b_4_1.phrase = 'Sunshine and clouds mixed. High around 20F. Winds light and variable.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = 20
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
    
    b_4_2.phrase = 'A few clouds. Low 7F. Winds light and variable.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = 7
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
    
    b_5_1.phrase = 'Partly to mostly cloudy. High 18F. Winds light and variable.'
    
    b_5_1.skyCondition = 3000
    b_5_1.temp = 18
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
    
    b_5_2.phrase = 'Cloudy. Low 8F. Winds ENE at 5 to 10 mph.'
    
    b_5_2.skyCondition = 2600
    b_5_2.temp = 8
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
    
    b_6_1.phrase = 'Cloudy. High 18F. Winds NNE at 5 to 10 mph.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = 18
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
    
    b_6_2.phrase = 'Considerable cloudiness. Low 4F. Winds NNW at 5 to 10 mph.'
    
    b_6_2.skyCondition = 2700
    b_6_2.temp = 4
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
    
    b_7_1.phrase = 'Partly cloudy skies. High 14F. Winds NW at 5 to 10 mph.'
    
    b_7_1.skyCondition = 3000
    b_7_1.temp = 14
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
    
    b_7_2.phrase = 'Partly cloudy. Low around -5F. Winds WNW at 5 to 10 mph.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -5
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
    
    b_8_1.phrase = 'Sunshine and clouds mixed. High 8F. Winds SW at 10 to 15 mph.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = 8
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
    
    b_8_2.phrase = 'Partly cloudy skies. Low 1F. Winds SSW at 10 to 15 mph.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = 1
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
    forecastTime_1_1 = 1763895600
    b_1_1 = twc.Data()
    
    b_1_1.phrase = 'Sun and clouds mixed. High 38F. Winds W at 5 to 10 mph.'
    
    b_1_1.skyCondition = 3000
    b_1_1.temp = 38
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71866002',
        type='textFcst',
        data=b_1_1,
        validTime=1763895600,
        numDayparts=4,
        expiration=int(1763895600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_1))
        


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Partly cloudy early followed by cloudy skies overnight. Low 16F. Winds W at 5 to 10 mph.'
    
    b_1_2.skyCondition = 2700
    b_1_2.temp = 16
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
    
    b_2_1.phrase = 'Cloudy skies. High 28F. Winds WNW at 5 to 10 mph.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = 28
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
    
    b_2_2.phrase = 'Cloudy. Low around 15F. Winds NW at 5 to 10 mph.'
    
    b_2_2.skyCondition = 2600
    b_2_2.temp = 15
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
    
    b_3_1.phrase = 'Cloudy early with partial sunshine expected late. High 23F. Winds WNW at 5 to 10 mph.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = 23
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
    
    b_3_2.phrase = 'Partly cloudy skies during the evening will give way to cloudy skies overnight. Low 8F. Winds light and variable.'
    
    b_3_2.skyCondition = 2900
    b_3_2.temp = 8
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
    
    b_4_1.phrase = 'Mostly cloudy skies early, then partly cloudy in the afternoon. High around 20F. Winds light and variable.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = 20
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
    
    b_4_2.phrase = 'Mainly clear skies. Low 8F. Winds light and variable.'
    
    b_4_2.skyCondition = 3300
    b_4_2.temp = 8
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
    
    b_5_1.phrase = 'Mostly cloudy skies early, then partly cloudy in the afternoon. High 17F. Winds light and variable.'
    
    b_5_1.skyCondition = 3000
    b_5_1.temp = 17
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
    
    b_5_2.phrase = 'Mainly cloudy. Low 8F. Winds light and variable.'
    
    b_5_2.skyCondition = 2700
    b_5_2.temp = 8
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
    
    b_6_1.phrase = 'Overcast. High 16F. Winds N at 5 to 10 mph.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = 16
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
    
    b_6_2.phrase = 'Mainly cloudy. Low 4F. Winds light and variable.'
    
    b_6_2.skyCondition = 2700
    b_6_2.temp = 4
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
    
    b_7_1.phrase = 'Mostly cloudy. High 14F. Winds NW at 5 to 10 mph.'
    
    b_7_1.skyCondition = 2800
    b_7_1.temp = 14
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
    
    b_7_2.phrase = 'A few clouds from time to time. Low -4F. Winds WNW at 5 to 10 mph.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -4
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
    
    b_8_1.phrase = 'Partly cloudy skies. High 7F. Winds SW at 10 to 15 mph.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = 7
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
    
    b_8_2.phrase = 'Partly cloudy skies. Low around 0F. Winds SW at 10 to 15 mph.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = 0
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
    forecastTime_1_1 = 1763895600
    b_1_1 = twc.Data()
    
    b_1_1.phrase = 'Cloudy skies. High 43F. Winds NW at 5 to 10 mph.'
    
    b_1_1.skyCondition = 2600
    b_1_1.temp = 43
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71863000',
        type='textFcst',
        data=b_1_1,
        validTime=1763895600,
        numDayparts=4,
        expiration=int(1763895600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_1))
        


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Cloudy. Low 23F. Winds NNW at 5 to 10 mph.'
    
    b_1_2.skyCondition = 2600
    b_1_2.temp = 23
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
    
    b_2_1.phrase = 'Cloudy. High near 35F. Winds N at 5 to 10 mph.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = 35
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
    
    b_2_2.phrase = 'A few snow showers scattered about the area in the evening, otherwise a good deal of clouds. Low 18F. Winds NNW at 10 to 20 mph. Chance of snow 30%.'
    
    b_2_2.skyCondition = 6800
    b_2_2.temp = 18
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
    
    b_3_1.phrase = 'Cloudy skies early will become partly cloudy later in the day. High 27F. Winds NW at 10 to 20 mph.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = 27
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
    
    b_3_2.phrase = 'A few clouds. Low 11F. Winds WNW at 5 to 10 mph.'
    
    b_3_2.skyCondition = 2900
    b_3_2.temp = 11
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
    
    b_4_1.phrase = 'Intervals of clouds and sunshine. High 24F. Winds WNW at 5 to 10 mph.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = 24
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
    
    b_4_2.phrase = 'Mainly clear skies. Low around 10F. Winds light and variable.'
    
    b_4_2.skyCondition = 3300
    b_4_2.temp = 10
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
    
    b_5_1.phrase = 'Partly cloudy. High 23F. Winds WNW at 5 to 10 mph.'
    
    b_5_1.skyCondition = 3000
    b_5_1.temp = 23
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
    
    b_5_2.phrase = 'Mostly cloudy skies. Low around 10F. Winds ESE at 5 to 10 mph.'
    
    b_5_2.skyCondition = 2700
    b_5_2.temp = 10
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
    
    b_6_1.phrase = 'Overcast. High 21F. Winds NE at 5 to 10 mph.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = 21
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
    
    b_6_2.phrase = 'Cloudy skies. Low 7F. Winds N at 5 to 10 mph.'
    
    b_6_2.skyCondition = 2600
    b_6_2.temp = 7
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
    
    b_7_1.phrase = 'Cloudy. High 18F. Winds NW at 10 to 15 mph.'
    
    b_7_1.skyCondition = 2600
    b_7_1.temp = 18
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
    
    b_7_2.phrase = 'Considerable cloudiness. Low -1F. Winds NW at 5 to 10 mph.'
    
    b_7_2.skyCondition = 2700
    b_7_2.temp = -1
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
    
    b_8_1.phrase = 'Intervals of clouds and sunshine. High around 10F. Winds WSW at 10 to 15 mph.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = 10
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
    
    b_8_2.phrase = 'A few clouds from time to time. Low 2F. Winds SSW at 10 to 15 mph.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = 2
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
    
    b_1_2.phrase = 'Mostly clear this evening, then becoming foggy and damp after midnight. Low 37F. Winds NE at 5 to 10 mph.'
    
    b_1_2.skyCondition = 9300
    b_1_2.temp = 37
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
    
    b_2_1.phrase = 'Cloudy skies with some morning fog. High 61F. Winds light and variable.'
    
    b_2_1.skyCondition = 9203
    b_2_1.temp = 61
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
    
    b_2_2.phrase = 'Rain likely. Low 53F. Winds SSE at 5 to 10 mph. Chance of rain 90%. Rainfall around a half an inch.'
    
    b_2_2.skyCondition = 1200
    b_2_2.temp = 53
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
    
    b_3_1.phrase = 'Considerable cloudiness with occasional rain showers. High around 60F. Winds SSW at 5 to 10 mph. Chance of rain 70%.'
    
    b_3_1.skyCondition = 1100
    b_3_1.temp = 60
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
    
    b_3_2.phrase = 'Cloudy skies. Low around 45F. Winds WSW at 10 to 15 mph.'
    
    b_3_2.skyCondition = 2600
    b_3_2.temp = 45
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
    
    b_4_1.phrase = 'Sunshine and clouds mixed. High 49F. Winds W at 10 to 20 mph.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = 49
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
    
    b_4_2.phrase = 'A few clouds. Low 29F. Winds W at 5 to 10 mph.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = 29
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
    
    b_5_1.phrase = 'Mainly sunny. High near 40F. Winds WNW at 10 to 15 mph.'
    
    b_5_1.skyCondition = 3200
    b_5_1.temp = 40
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
    
    b_5_2.phrase = 'A mostly clear sky. Low 23F. Winds WNW at 5 to 10 mph.'
    
    b_5_2.skyCondition = 3100
    b_5_2.temp = 23
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
    
    b_6_1.phrase = 'Except for a few afternoon clouds, mainly sunny. High 41F. Winds light and variable.'
    
    b_6_1.skyCondition = 3400
    b_6_1.temp = 41
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
    
    b_6_2.phrase = 'Partly cloudy early with increasing clouds overnight. Low 28F. Winds light and variable.'
    
    b_6_2.skyCondition = 2900
    b_6_2.temp = 28
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
    
    b_7_1.phrase = 'Cloudy early with showers for the afternoon hours. High 44F. Winds SE at 5 to 10 mph. Chance of rain 40%.'
    
    b_7_1.skyCondition = 7103
    b_7_1.temp = 44
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
    
    b_7_2.phrase = 'Cloudy with showers. Low 38F. Winds light and variable. Chance of rain 60%.'
    
    b_7_2.skyCondition = 1100
    b_7_2.temp = 38
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
    
    b_8_1.phrase = 'Considerable cloudiness with occasional rain showers. High 52F. Winds S at 5 to 10 mph. Chance of rain 60%.'
    
    b_8_1.skyCondition = 1100
    b_8_1.temp = 52
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
    
    b_8_2.phrase = 'Overcast with rain showers at times. Low 48F. Winds S at 5 to 10 mph. Chance of rain 60%.'
    
    b_8_2.skyCondition = 1100
    b_8_2.temp = 48
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
    forecastTime_1_1 = 1763895600
    b_1_1 = twc.Data()
    
    b_1_1.phrase = 'Sun and clouds mixed. High 39F. Winds WNW at 5 to 10 mph.'
    
    b_1_1.skyCondition = 3000
    b_1_1.temp = 39
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71876000',
        type='textFcst',
        data=b_1_1,
        validTime=1763895600,
        numDayparts=4,
        expiration=int(1763895600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_1))
        


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Some clouds. Low 14F. Winds NW at 5 to 10 mph.'
    
    b_1_2.skyCondition = 2900
    b_1_2.temp = 14
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
    
    b_2_1.phrase = 'Overcast. High 26F. Winds NW at 5 to 10 mph.'
    
    b_2_1.skyCondition = 2600
    b_2_1.temp = 26
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
    
    b_2_2.phrase = 'Mostly cloudy. Low 13F. Winds NW at 5 to 10 mph.'
    
    b_2_2.skyCondition = 2700
    b_2_2.temp = 13
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
    
    b_3_1.phrase = 'Cloudy early with partial sunshine expected late. High 22F. Winds WNW at 5 to 10 mph.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = 22
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
    
    b_3_2.phrase = 'Partly cloudy skies during the evening will give way to cloudy skies overnight. Low near 5F. Winds light and variable.'
    
    b_3_2.skyCondition = 2900
    b_3_2.temp = 5
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
    
    b_4_1.phrase = 'Intervals of clouds and sunshine. High 18F. Winds light and variable.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = 18
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
    
    b_4_2.phrase = 'A few clouds from time to time. Low 6F. Winds light and variable.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = 6
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
    
    b_5_1.phrase = 'Mostly cloudy. High 16F. Winds light and variable.'
    
    b_5_1.skyCondition = 2800
    b_5_1.temp = 16
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
    
    b_5_2.phrase = 'Cloudy. Low 8F. Winds light and variable.'
    
    b_5_2.skyCondition = 2600
    b_5_2.temp = 8
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
    
    b_6_1.phrase = 'Cloudy. High 16F. Winds light and variable.'
    
    b_6_1.skyCondition = 2600
    b_6_1.temp = 16
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
    
    b_6_2.phrase = 'Partly to mostly cloudy. Low 4F. Winds light and variable.'
    
    b_6_2.skyCondition = 2900
    b_6_2.temp = 4
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
    
    b_7_1.phrase = 'Considerable cloudiness. High 13F. Winds NNW at 5 to 10 mph.'
    
    b_7_1.skyCondition = 2800
    b_7_1.temp = 13
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
    
    b_7_2.phrase = 'A few clouds from time to time. Low near -5F. Winds NW at 5 to 10 mph.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -5
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
    
    b_8_1.phrase = 'Sunshine and clouds mixed. High 8F. Winds SW at 5 to 10 mph.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = 8
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
    
    b_8_2.phrase = 'Partly cloudy. Low 1F. Winds WSW at 5 to 10 mph.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = 1
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
    forecastTime_1_1 = 1763895600
    b_1_1 = twc.Data()
    
    b_1_1.phrase = 'Sun and clouds mixed. High 36F. Winds W at 5 to 10 mph.'
    
    b_1_1.skyCondition = 3000
    b_1_1.temp = 36
    # Vocal key for those trying to recreate: D2:DA02:X3000300022:S300021:TL77:W06R02
    wxdata.setDaypartData(
        loc='71869000',
        type='textFcst',
        data=b_1_1,
        validTime=1763895600,
        numDayparts=4,
        expiration=int(1763895600 + 43200)
    )
    twccommon.Log.info("i1DG - Daypart forecast set for " + area + " at " + str(forecastTime_1_1))
        


for area in areaList:
    forecastTime_1_2 = 1763938800
    b_1_2 = twc.Data()
    
    b_1_2.phrase = 'Clear to partly cloudy. Low 17F. Winds W at 5 to 10 mph.'
    
    b_1_2.skyCondition = 3300
    b_1_2.temp = 17
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
    
    b_2_1.phrase = 'Mostly cloudy. High 27F. Winds WNW at 5 to 10 mph.'
    
    b_2_1.skyCondition = 2800
    b_2_1.temp = 27
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
    
    b_2_2.phrase = 'Overcast. Low 18F. Winds light and variable.'
    
    b_2_2.skyCondition = 2600
    b_2_2.temp = 18
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
    
    b_3_1.phrase = 'Cloudy early with partial sunshine expected late. High 23F. Winds WNW at 5 to 10 mph.'
    
    b_3_1.skyCondition = 9003
    b_3_1.temp = 23
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
    
    b_3_2.phrase = 'Mainly cloudy. Low near 10F. Winds light and variable.'
    
    b_3_2.skyCondition = 2700
    b_3_2.temp = 10
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
    
    b_4_1.phrase = 'Partly cloudy. High near 20F. Winds light and variable.'
    
    b_4_1.skyCondition = 3000
    b_4_1.temp = 20
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
    
    b_4_2.phrase = 'Partly to mostly cloudy. Low 12F. Winds light and variable.'
    
    b_4_2.skyCondition = 2900
    b_4_2.temp = 12
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
    
    b_5_1.phrase = 'Mainly cloudy. High 17F. Winds light and variable.'
    
    b_5_1.skyCondition = 2800
    b_5_1.temp = 17
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
    
    b_5_2.phrase = 'Cloudy. Low 9F. Winds light and variable.'
    
    b_5_2.skyCondition = 2600
    b_5_2.temp = 9
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
    
    b_6_1.phrase = 'Mostly cloudy skies. High near 15F. Winds NNW at 5 to 10 mph.'
    
    b_6_1.skyCondition = 2800
    b_6_1.temp = 15
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
    
    b_6_2.phrase = 'Partly to mostly cloudy. Low 3F. Winds light and variable.'
    
    b_6_2.skyCondition = 2900
    b_6_2.temp = 3
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
    
    b_7_1.phrase = 'Intervals of clouds and sunshine. High 13F. Winds NW at 5 to 10 mph.'
    
    b_7_1.skyCondition = 3000
    b_7_1.temp = 13
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
    
    b_7_2.phrase = 'A few clouds. Low -4F. Winds WNW at 5 to 10 mph.'
    
    b_7_2.skyCondition = 2900
    b_7_2.temp = -4
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
    
    b_8_1.phrase = 'Partly cloudy. High 6F. Winds WSW at 10 to 15 mph.'
    
    b_8_1.skyCondition = 3000
    b_8_1.temp = 6
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
    
    b_8_2.phrase = 'Partly cloudy skies. Low -2F. Winds WSW at 5 to 10 mph.'
    
    b_8_2.skyCondition = 2900
    b_8_2.temp = -2
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
                


