
import twccommon
import time
import twc.dsmarshal as dsm

areaList = wxdata.getUGCInterestList('CCC999', 'county')

twccommon.Log.info("i1DT - Thanks for using the 45 Degrees i1 Encoder.")

if not areaList:
    abortMsg()

Y, M, D, h, m, s, wd, jd, dst = time.localtime(time.time())
if h < 16:
    dOffset = 0
else:
    dOffset = 1
keyTime = time.mktime((Y, M, D + dOffset, 0, 0, 0, 0, 0, -1))

for area in areaList:
    forecastTime_1_71866000 = 1763935200
    b_1_71866000 = twc.Data()
    b_1_71866000.minTemp = 36
    b_1_71866000.maxTemp = 36
    b_1_71866000.windSpeed = 7
    b_1_71866000.windDir = 7
    b_1_71866000.temp = 36
    b_1_71866000.skyCondition = 2800
    b_1_71866000.pop = 2

    key_1_71866000 = ('71866000.' + str(int(forecastTime_1_71866000)))
    wxdata.setData(key_1_71866000, 'hourlyFcst', b_1_71866000, int(forecastTime_1_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_1_71866000)))

for area in areaList:
    forecastTime_2_71866000 = 1763938800
    b_2_71866000 = twc.Data()
    b_2_71866000.minTemp = 34
    b_2_71866000.maxTemp = 34
    b_2_71866000.windSpeed = 7
    b_2_71866000.windDir = 6
    b_2_71866000.temp = 34
    b_2_71866000.skyCondition = 2600
    b_2_71866000.pop = 2

    key_2_71866000 = ('71866000.' + str(int(forecastTime_2_71866000)))
    wxdata.setData(key_2_71866000, 'hourlyFcst', b_2_71866000, int(forecastTime_2_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_2_71866000)))

for area in areaList:
    forecastTime_3_71866000 = 1763942400
    b_3_71866000 = twc.Data()
    b_3_71866000.minTemp = 31
    b_3_71866000.maxTemp = 31
    b_3_71866000.windSpeed = 7
    b_3_71866000.windDir = 6
    b_3_71866000.temp = 31
    b_3_71866000.skyCondition = 2600
    b_3_71866000.pop = 2

    key_3_71866000 = ('71866000.' + str(int(forecastTime_3_71866000)))
    wxdata.setData(key_3_71866000, 'hourlyFcst', b_3_71866000, int(forecastTime_3_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_3_71866000)))

for area in areaList:
    forecastTime_4_71866000 = 1763946000
    b_4_71866000 = twc.Data()
    b_4_71866000.minTemp = 29
    b_4_71866000.maxTemp = 29
    b_4_71866000.windSpeed = 7
    b_4_71866000.windDir = 7
    b_4_71866000.temp = 29
    b_4_71866000.skyCondition = 2600
    b_4_71866000.pop = 2

    key_4_71866000 = ('71866000.' + str(int(forecastTime_4_71866000)))
    wxdata.setData(key_4_71866000, 'hourlyFcst', b_4_71866000, int(forecastTime_4_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_4_71866000)))

for area in areaList:
    forecastTime_5_71866000 = 1763949600
    b_5_71866000 = twc.Data()
    b_5_71866000.minTemp = 28
    b_5_71866000.maxTemp = 28
    b_5_71866000.windSpeed = 7
    b_5_71866000.windDir = 6
    b_5_71866000.temp = 28
    b_5_71866000.skyCondition = 2700
    b_5_71866000.pop = 2

    key_5_71866000 = ('71866000.' + str(int(forecastTime_5_71866000)))
    wxdata.setData(key_5_71866000, 'hourlyFcst', b_5_71866000, int(forecastTime_5_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_5_71866000)))

for area in areaList:
    forecastTime_6_71866000 = 1763953200
    b_6_71866000 = twc.Data()
    b_6_71866000.minTemp = 28
    b_6_71866000.maxTemp = 28
    b_6_71866000.windSpeed = 7
    b_6_71866000.windDir = 6
    b_6_71866000.temp = 28
    b_6_71866000.skyCondition = 2900
    b_6_71866000.pop = 2

    key_6_71866000 = ('71866000.' + str(int(forecastTime_6_71866000)))
    wxdata.setData(key_6_71866000, 'hourlyFcst', b_6_71866000, int(forecastTime_6_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_6_71866000)))

for area in areaList:
    forecastTime_7_71866000 = 1763956800
    b_7_71866000 = twc.Data()
    b_7_71866000.minTemp = 27
    b_7_71866000.maxTemp = 27
    b_7_71866000.windSpeed = 7
    b_7_71866000.windDir = 7
    b_7_71866000.temp = 27
    b_7_71866000.skyCondition = 2900
    b_7_71866000.pop = 5

    key_7_71866000 = ('71866000.' + str(int(forecastTime_7_71866000)))
    wxdata.setData(key_7_71866000, 'hourlyFcst', b_7_71866000, int(forecastTime_7_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_7_71866000)))

for area in areaList:
    forecastTime_8_71866000 = 1763960400
    b_8_71866000 = twc.Data()
    b_8_71866000.minTemp = 25
    b_8_71866000.maxTemp = 25
    b_8_71866000.windSpeed = 7
    b_8_71866000.windDir = 6
    b_8_71866000.temp = 25
    b_8_71866000.skyCondition = 3300
    b_8_71866000.pop = 9

    key_8_71866000 = ('71866000.' + str(int(forecastTime_8_71866000)))
    wxdata.setData(key_8_71866000, 'hourlyFcst', b_8_71866000, int(forecastTime_8_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_8_71866000)))

for area in areaList:
    forecastTime_9_71866000 = 1763964000
    b_9_71866000 = twc.Data()
    b_9_71866000.minTemp = 24
    b_9_71866000.maxTemp = 24
    b_9_71866000.windSpeed = 7
    b_9_71866000.windDir = 6
    b_9_71866000.temp = 24
    b_9_71866000.skyCondition = 2900
    b_9_71866000.pop = 9

    key_9_71866000 = ('71866000.' + str(int(forecastTime_9_71866000)))
    wxdata.setData(key_9_71866000, 'hourlyFcst', b_9_71866000, int(forecastTime_9_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_9_71866000)))

for area in areaList:
    forecastTime_10_71866000 = 1763967600
    b_10_71866000 = twc.Data()
    b_10_71866000.minTemp = 23
    b_10_71866000.maxTemp = 23
    b_10_71866000.windSpeed = 6
    b_10_71866000.windDir = 7
    b_10_71866000.temp = 23
    b_10_71866000.skyCondition = 2900
    b_10_71866000.pop = 9

    key_10_71866000 = ('71866000.' + str(int(forecastTime_10_71866000)))
    wxdata.setData(key_10_71866000, 'hourlyFcst', b_10_71866000, int(forecastTime_10_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_10_71866000)))

for area in areaList:
    forecastTime_11_71866000 = 1763971200
    b_11_71866000 = twc.Data()
    b_11_71866000.minTemp = 22
    b_11_71866000.maxTemp = 22
    b_11_71866000.windSpeed = 7
    b_11_71866000.windDir = 6
    b_11_71866000.temp = 22
    b_11_71866000.skyCondition = 2900
    b_11_71866000.pop = 9

    key_11_71866000 = ('71866000.' + str(int(forecastTime_11_71866000)))
    wxdata.setData(key_11_71866000, 'hourlyFcst', b_11_71866000, int(forecastTime_11_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_11_71866000)))

for area in areaList:
    forecastTime_12_71866000 = 1763974800
    b_12_71866000 = twc.Data()
    b_12_71866000.minTemp = 20
    b_12_71866000.maxTemp = 20
    b_12_71866000.windSpeed = 6
    b_12_71866000.windDir = 6
    b_12_71866000.temp = 20
    b_12_71866000.skyCondition = 2700
    b_12_71866000.pop = 9

    key_12_71866000 = ('71866000.' + str(int(forecastTime_12_71866000)))
    wxdata.setData(key_12_71866000, 'hourlyFcst', b_12_71866000, int(forecastTime_12_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_12_71866000)))

for area in areaList:
    forecastTime_13_71866000 = 1763978400
    b_13_71866000 = twc.Data()
    b_13_71866000.minTemp = 20
    b_13_71866000.maxTemp = 20
    b_13_71866000.windSpeed = 6
    b_13_71866000.windDir = 7
    b_13_71866000.temp = 20
    b_13_71866000.skyCondition = 2600
    b_13_71866000.pop = 9

    key_13_71866000 = ('71866000.' + str(int(forecastTime_13_71866000)))
    wxdata.setData(key_13_71866000, 'hourlyFcst', b_13_71866000, int(forecastTime_13_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_13_71866000)))

for area in areaList:
    forecastTime_14_71866000 = 1763982000
    b_14_71866000 = twc.Data()
    b_14_71866000.minTemp = 19
    b_14_71866000.maxTemp = 19
    b_14_71866000.windSpeed = 4
    b_14_71866000.windDir = 6
    b_14_71866000.temp = 19
    b_14_71866000.skyCondition = 2600
    b_14_71866000.pop = 9

    key_14_71866000 = ('71866000.' + str(int(forecastTime_14_71866000)))
    wxdata.setData(key_14_71866000, 'hourlyFcst', b_14_71866000, int(forecastTime_14_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_14_71866000)))

for area in areaList:
    forecastTime_15_71866000 = 1763985600
    b_15_71866000 = twc.Data()
    b_15_71866000.minTemp = 18
    b_15_71866000.maxTemp = 18
    b_15_71866000.windSpeed = 4
    b_15_71866000.windDir = 6
    b_15_71866000.temp = 18
    b_15_71866000.skyCondition = 2600
    b_15_71866000.pop = 9

    key_15_71866000 = ('71866000.' + str(int(forecastTime_15_71866000)))
    wxdata.setData(key_15_71866000, 'hourlyFcst', b_15_71866000, int(forecastTime_15_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_15_71866000)))

for area in areaList:
    forecastTime_16_71866000 = 1763989200
    b_16_71866000 = twc.Data()
    b_16_71866000.minTemp = 18
    b_16_71866000.maxTemp = 18
    b_16_71866000.windSpeed = 4
    b_16_71866000.windDir = 7
    b_16_71866000.temp = 18
    b_16_71866000.skyCondition = 2600
    b_16_71866000.pop = 9

    key_16_71866000 = ('71866000.' + str(int(forecastTime_16_71866000)))
    wxdata.setData(key_16_71866000, 'hourlyFcst', b_16_71866000, int(forecastTime_16_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_16_71866000)))

for area in areaList:
    forecastTime_17_71866000 = 1763992800
    b_17_71866000 = twc.Data()
    b_17_71866000.minTemp = 17
    b_17_71866000.maxTemp = 17
    b_17_71866000.windSpeed = 5
    b_17_71866000.windDir = 6
    b_17_71866000.temp = 17
    b_17_71866000.skyCondition = 2600
    b_17_71866000.pop = 9

    key_17_71866000 = ('71866000.' + str(int(forecastTime_17_71866000)))
    wxdata.setData(key_17_71866000, 'hourlyFcst', b_17_71866000, int(forecastTime_17_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_17_71866000)))

for area in areaList:
    forecastTime_18_71866000 = 1763996400
    b_18_71866000 = twc.Data()
    b_18_71866000.minTemp = 17
    b_18_71866000.maxTemp = 17
    b_18_71866000.windSpeed = 5
    b_18_71866000.windDir = 6
    b_18_71866000.temp = 17
    b_18_71866000.skyCondition = 2600
    b_18_71866000.pop = 9

    key_18_71866000 = ('71866000.' + str(int(forecastTime_18_71866000)))
    wxdata.setData(key_18_71866000, 'hourlyFcst', b_18_71866000, int(forecastTime_18_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_18_71866000)))

for area in areaList:
    forecastTime_19_71866000 = 1764000000
    b_19_71866000 = twc.Data()
    b_19_71866000.minTemp = 19
    b_19_71866000.maxTemp = 19
    b_19_71866000.windSpeed = 6
    b_19_71866000.windDir = 7
    b_19_71866000.temp = 19
    b_19_71866000.skyCondition = 2600
    b_19_71866000.pop = 8

    key_19_71866000 = ('71866000.' + str(int(forecastTime_19_71866000)))
    wxdata.setData(key_19_71866000, 'hourlyFcst', b_19_71866000, int(forecastTime_19_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_19_71866000)))

for area in areaList:
    forecastTime_20_71866000 = 1764003600
    b_20_71866000 = twc.Data()
    b_20_71866000.minTemp = 22
    b_20_71866000.maxTemp = 22
    b_20_71866000.windSpeed = 6
    b_20_71866000.windDir = 6
    b_20_71866000.temp = 22
    b_20_71866000.skyCondition = 2600
    b_20_71866000.pop = 8

    key_20_71866000 = ('71866000.' + str(int(forecastTime_20_71866000)))
    wxdata.setData(key_20_71866000, 'hourlyFcst', b_20_71866000, int(forecastTime_20_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_20_71866000)))

for area in areaList:
    forecastTime_21_71866000 = 1764007200
    b_21_71866000 = twc.Data()
    b_21_71866000.minTemp = 24
    b_21_71866000.maxTemp = 24
    b_21_71866000.windSpeed = 6
    b_21_71866000.windDir = 6
    b_21_71866000.temp = 24
    b_21_71866000.skyCondition = 2600
    b_21_71866000.pop = 7

    key_21_71866000 = ('71866000.' + str(int(forecastTime_21_71866000)))
    wxdata.setData(key_21_71866000, 'hourlyFcst', b_21_71866000, int(forecastTime_21_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_21_71866000)))

for area in areaList:
    forecastTime_22_71866000 = 1764010800
    b_22_71866000 = twc.Data()
    b_22_71866000.minTemp = 25
    b_22_71866000.maxTemp = 25
    b_22_71866000.windSpeed = 6
    b_22_71866000.windDir = 7
    b_22_71866000.temp = 25
    b_22_71866000.skyCondition = 2600
    b_22_71866000.pop = 6

    key_22_71866000 = ('71866000.' + str(int(forecastTime_22_71866000)))
    wxdata.setData(key_22_71866000, 'hourlyFcst', b_22_71866000, int(forecastTime_22_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_22_71866000)))

for area in areaList:
    forecastTime_23_71866000 = 1764014400
    b_23_71866000 = twc.Data()
    b_23_71866000.minTemp = 27
    b_23_71866000.maxTemp = 27
    b_23_71866000.windSpeed = 7
    b_23_71866000.windDir = 6
    b_23_71866000.temp = 27
    b_23_71866000.skyCondition = 2800
    b_23_71866000.pop = 5

    key_23_71866000 = ('71866000.' + str(int(forecastTime_23_71866000)))
    wxdata.setData(key_23_71866000, 'hourlyFcst', b_23_71866000, int(forecastTime_23_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_23_71866000)))

for area in areaList:
    forecastTime_24_71866000 = 1764018000
    b_24_71866000 = twc.Data()
    b_24_71866000.minTemp = 28
    b_24_71866000.maxTemp = 28
    b_24_71866000.windSpeed = 7
    b_24_71866000.windDir = 6
    b_24_71866000.temp = 28
    b_24_71866000.skyCondition = 2600
    b_24_71866000.pop = 5

    key_24_71866000 = ('71866000.' + str(int(forecastTime_24_71866000)))
    wxdata.setData(key_24_71866000, 'hourlyFcst', b_24_71866000, int(forecastTime_24_71866000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_24_71866000)))

for area in areaList:
    forecastTime_1_71866002 = 1763935200
    b_1_71866002 = twc.Data()
    b_1_71866002.minTemp = 35
    b_1_71866002.maxTemp = 35
    b_1_71866002.windSpeed = 6
    b_1_71866002.windDir = 7
    b_1_71866002.temp = 35
    b_1_71866002.skyCondition = 3000
    b_1_71866002.pop = 2

    key_1_71866002 = ('71866002.' + str(int(forecastTime_1_71866002)))
    wxdata.setData(key_1_71866002, 'hourlyFcst', b_1_71866002, int(forecastTime_1_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_1_71866002)))

for area in areaList:
    forecastTime_2_71866002 = 1763938800
    b_2_71866002 = twc.Data()
    b_2_71866002.minTemp = 33
    b_2_71866002.maxTemp = 33
    b_2_71866002.windSpeed = 6
    b_2_71866002.windDir = 6
    b_2_71866002.temp = 33
    b_2_71866002.skyCondition = 3000
    b_2_71866002.pop = 2

    key_2_71866002 = ('71866002.' + str(int(forecastTime_2_71866002)))
    wxdata.setData(key_2_71866002, 'hourlyFcst', b_2_71866002, int(forecastTime_2_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_2_71866002)))

for area in areaList:
    forecastTime_3_71866002 = 1763942400
    b_3_71866002 = twc.Data()
    b_3_71866002.minTemp = 31
    b_3_71866002.maxTemp = 31
    b_3_71866002.windSpeed = 7
    b_3_71866002.windDir = 6
    b_3_71866002.temp = 31
    b_3_71866002.skyCondition = 2900
    b_3_71866002.pop = 2

    key_3_71866002 = ('71866002.' + str(int(forecastTime_3_71866002)))
    wxdata.setData(key_3_71866002, 'hourlyFcst', b_3_71866002, int(forecastTime_3_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_3_71866002)))

for area in areaList:
    forecastTime_4_71866002 = 1763946000
    b_4_71866002 = twc.Data()
    b_4_71866002.minTemp = 29
    b_4_71866002.maxTemp = 29
    b_4_71866002.windSpeed = 8
    b_4_71866002.windDir = 7
    b_4_71866002.temp = 29
    b_4_71866002.skyCondition = 2900
    b_4_71866002.pop = 2

    key_4_71866002 = ('71866002.' + str(int(forecastTime_4_71866002)))
    wxdata.setData(key_4_71866002, 'hourlyFcst', b_4_71866002, int(forecastTime_4_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_4_71866002)))

for area in areaList:
    forecastTime_5_71866002 = 1763949600
    b_5_71866002 = twc.Data()
    b_5_71866002.minTemp = 27
    b_5_71866002.maxTemp = 27
    b_5_71866002.windSpeed = 8
    b_5_71866002.windDir = 6
    b_5_71866002.temp = 27
    b_5_71866002.skyCondition = 2900
    b_5_71866002.pop = 3

    key_5_71866002 = ('71866002.' + str(int(forecastTime_5_71866002)))
    wxdata.setData(key_5_71866002, 'hourlyFcst', b_5_71866002, int(forecastTime_5_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_5_71866002)))

for area in areaList:
    forecastTime_6_71866002 = 1763953200
    b_6_71866002 = twc.Data()
    b_6_71866002.minTemp = 26
    b_6_71866002.maxTemp = 26
    b_6_71866002.windSpeed = 8
    b_6_71866002.windDir = 6
    b_6_71866002.temp = 26
    b_6_71866002.skyCondition = 2900
    b_6_71866002.pop = 3

    key_6_71866002 = ('71866002.' + str(int(forecastTime_6_71866002)))
    wxdata.setData(key_6_71866002, 'hourlyFcst', b_6_71866002, int(forecastTime_6_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_6_71866002)))

for area in areaList:
    forecastTime_7_71866002 = 1763956800
    b_7_71866002 = twc.Data()
    b_7_71866002.minTemp = 26
    b_7_71866002.maxTemp = 26
    b_7_71866002.windSpeed = 8
    b_7_71866002.windDir = 7
    b_7_71866002.temp = 26
    b_7_71866002.skyCondition = 3300
    b_7_71866002.pop = 6

    key_7_71866002 = ('71866002.' + str(int(forecastTime_7_71866002)))
    wxdata.setData(key_7_71866002, 'hourlyFcst', b_7_71866002, int(forecastTime_7_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_7_71866002)))

for area in areaList:
    forecastTime_8_71866002 = 1763960400
    b_8_71866002 = twc.Data()
    b_8_71866002.minTemp = 25
    b_8_71866002.maxTemp = 25
    b_8_71866002.windSpeed = 7
    b_8_71866002.windDir = 6
    b_8_71866002.temp = 25
    b_8_71866002.skyCondition = 2900
    b_8_71866002.pop = 9

    key_8_71866002 = ('71866002.' + str(int(forecastTime_8_71866002)))
    wxdata.setData(key_8_71866002, 'hourlyFcst', b_8_71866002, int(forecastTime_8_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_8_71866002)))

for area in areaList:
    forecastTime_9_71866002 = 1763964000
    b_9_71866002 = twc.Data()
    b_9_71866002.minTemp = 23
    b_9_71866002.maxTemp = 23
    b_9_71866002.windSpeed = 7
    b_9_71866002.windDir = 6
    b_9_71866002.temp = 23
    b_9_71866002.skyCondition = 2900
    b_9_71866002.pop = 9

    key_9_71866002 = ('71866002.' + str(int(forecastTime_9_71866002)))
    wxdata.setData(key_9_71866002, 'hourlyFcst', b_9_71866002, int(forecastTime_9_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_9_71866002)))

for area in areaList:
    forecastTime_10_71866002 = 1763967600
    b_10_71866002 = twc.Data()
    b_10_71866002.minTemp = 22
    b_10_71866002.maxTemp = 22
    b_10_71866002.windSpeed = 7
    b_10_71866002.windDir = 7
    b_10_71866002.temp = 22
    b_10_71866002.skyCondition = 2900
    b_10_71866002.pop = 9

    key_10_71866002 = ('71866002.' + str(int(forecastTime_10_71866002)))
    wxdata.setData(key_10_71866002, 'hourlyFcst', b_10_71866002, int(forecastTime_10_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_10_71866002)))

for area in areaList:
    forecastTime_11_71866002 = 1763971200
    b_11_71866002 = twc.Data()
    b_11_71866002.minTemp = 21
    b_11_71866002.maxTemp = 21
    b_11_71866002.windSpeed = 7
    b_11_71866002.windDir = 6
    b_11_71866002.temp = 21
    b_11_71866002.skyCondition = 2900
    b_11_71866002.pop = 9

    key_11_71866002 = ('71866002.' + str(int(forecastTime_11_71866002)))
    wxdata.setData(key_11_71866002, 'hourlyFcst', b_11_71866002, int(forecastTime_11_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_11_71866002)))

for area in areaList:
    forecastTime_12_71866002 = 1763974800
    b_12_71866002 = twc.Data()
    b_12_71866002.minTemp = 20
    b_12_71866002.maxTemp = 20
    b_12_71866002.windSpeed = 6
    b_12_71866002.windDir = 6
    b_12_71866002.temp = 20
    b_12_71866002.skyCondition = 2700
    b_12_71866002.pop = 9

    key_12_71866002 = ('71866002.' + str(int(forecastTime_12_71866002)))
    wxdata.setData(key_12_71866002, 'hourlyFcst', b_12_71866002, int(forecastTime_12_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_12_71866002)))

for area in areaList:
    forecastTime_13_71866002 = 1763978400
    b_13_71866002 = twc.Data()
    b_13_71866002.minTemp = 19
    b_13_71866002.maxTemp = 19
    b_13_71866002.windSpeed = 5
    b_13_71866002.windDir = 7
    b_13_71866002.temp = 19
    b_13_71866002.skyCondition = 2700
    b_13_71866002.pop = 9

    key_13_71866002 = ('71866002.' + str(int(forecastTime_13_71866002)))
    wxdata.setData(key_13_71866002, 'hourlyFcst', b_13_71866002, int(forecastTime_13_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_13_71866002)))

for area in areaList:
    forecastTime_14_71866002 = 1763982000
    b_14_71866002 = twc.Data()
    b_14_71866002.minTemp = 19
    b_14_71866002.maxTemp = 19
    b_14_71866002.windSpeed = 4
    b_14_71866002.windDir = 6
    b_14_71866002.temp = 19
    b_14_71866002.skyCondition = 2600
    b_14_71866002.pop = 9

    key_14_71866002 = ('71866002.' + str(int(forecastTime_14_71866002)))
    wxdata.setData(key_14_71866002, 'hourlyFcst', b_14_71866002, int(forecastTime_14_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_14_71866002)))

for area in areaList:
    forecastTime_15_71866002 = 1763985600
    b_15_71866002 = twc.Data()
    b_15_71866002.minTemp = 18
    b_15_71866002.maxTemp = 18
    b_15_71866002.windSpeed = 4
    b_15_71866002.windDir = 6
    b_15_71866002.temp = 18
    b_15_71866002.skyCondition = 2600
    b_15_71866002.pop = 9

    key_15_71866002 = ('71866002.' + str(int(forecastTime_15_71866002)))
    wxdata.setData(key_15_71866002, 'hourlyFcst', b_15_71866002, int(forecastTime_15_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_15_71866002)))

for area in areaList:
    forecastTime_16_71866002 = 1763989200
    b_16_71866002 = twc.Data()
    b_16_71866002.minTemp = 18
    b_16_71866002.maxTemp = 18
    b_16_71866002.windSpeed = 4
    b_16_71866002.windDir = 7
    b_16_71866002.temp = 18
    b_16_71866002.skyCondition = 2600
    b_16_71866002.pop = 9

    key_16_71866002 = ('71866002.' + str(int(forecastTime_16_71866002)))
    wxdata.setData(key_16_71866002, 'hourlyFcst', b_16_71866002, int(forecastTime_16_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_16_71866002)))

for area in areaList:
    forecastTime_17_71866002 = 1763992800
    b_17_71866002 = twc.Data()
    b_17_71866002.minTemp = 17
    b_17_71866002.maxTemp = 17
    b_17_71866002.windSpeed = 5
    b_17_71866002.windDir = 6
    b_17_71866002.temp = 17
    b_17_71866002.skyCondition = 2600
    b_17_71866002.pop = 9

    key_17_71866002 = ('71866002.' + str(int(forecastTime_17_71866002)))
    wxdata.setData(key_17_71866002, 'hourlyFcst', b_17_71866002, int(forecastTime_17_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_17_71866002)))

for area in areaList:
    forecastTime_18_71866002 = 1763996400
    b_18_71866002 = twc.Data()
    b_18_71866002.minTemp = 17
    b_18_71866002.maxTemp = 17
    b_18_71866002.windSpeed = 4
    b_18_71866002.windDir = 6
    b_18_71866002.temp = 17
    b_18_71866002.skyCondition = 2600
    b_18_71866002.pop = 9

    key_18_71866002 = ('71866002.' + str(int(forecastTime_18_71866002)))
    wxdata.setData(key_18_71866002, 'hourlyFcst', b_18_71866002, int(forecastTime_18_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_18_71866002)))

for area in areaList:
    forecastTime_19_71866002 = 1764000000
    b_19_71866002 = twc.Data()
    b_19_71866002.minTemp = 19
    b_19_71866002.maxTemp = 19
    b_19_71866002.windSpeed = 5
    b_19_71866002.windDir = 7
    b_19_71866002.temp = 19
    b_19_71866002.skyCondition = 2600
    b_19_71866002.pop = 8

    key_19_71866002 = ('71866002.' + str(int(forecastTime_19_71866002)))
    wxdata.setData(key_19_71866002, 'hourlyFcst', b_19_71866002, int(forecastTime_19_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_19_71866002)))

for area in areaList:
    forecastTime_20_71866002 = 1764003600
    b_20_71866002 = twc.Data()
    b_20_71866002.minTemp = 22
    b_20_71866002.maxTemp = 22
    b_20_71866002.windSpeed = 4
    b_20_71866002.windDir = 6
    b_20_71866002.temp = 22
    b_20_71866002.skyCondition = 2600
    b_20_71866002.pop = 8

    key_20_71866002 = ('71866002.' + str(int(forecastTime_20_71866002)))
    wxdata.setData(key_20_71866002, 'hourlyFcst', b_20_71866002, int(forecastTime_20_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_20_71866002)))

for area in areaList:
    forecastTime_21_71866002 = 1764007200
    b_21_71866002 = twc.Data()
    b_21_71866002.minTemp = 24
    b_21_71866002.maxTemp = 24
    b_21_71866002.windSpeed = 5
    b_21_71866002.windDir = 6
    b_21_71866002.temp = 24
    b_21_71866002.skyCondition = 2600
    b_21_71866002.pop = 8

    key_21_71866002 = ('71866002.' + str(int(forecastTime_21_71866002)))
    wxdata.setData(key_21_71866002, 'hourlyFcst', b_21_71866002, int(forecastTime_21_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_21_71866002)))

for area in areaList:
    forecastTime_22_71866002 = 1764010800
    b_22_71866002 = twc.Data()
    b_22_71866002.minTemp = 25
    b_22_71866002.maxTemp = 25
    b_22_71866002.windSpeed = 5
    b_22_71866002.windDir = 7
    b_22_71866002.temp = 25
    b_22_71866002.skyCondition = 2600
    b_22_71866002.pop = 7

    key_22_71866002 = ('71866002.' + str(int(forecastTime_22_71866002)))
    wxdata.setData(key_22_71866002, 'hourlyFcst', b_22_71866002, int(forecastTime_22_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_22_71866002)))

for area in areaList:
    forecastTime_23_71866002 = 1764014400
    b_23_71866002 = twc.Data()
    b_23_71866002.minTemp = 26
    b_23_71866002.maxTemp = 26
    b_23_71866002.windSpeed = 6
    b_23_71866002.windDir = 6
    b_23_71866002.temp = 26
    b_23_71866002.skyCondition = 2800
    b_23_71866002.pop = 7

    key_23_71866002 = ('71866002.' + str(int(forecastTime_23_71866002)))
    wxdata.setData(key_23_71866002, 'hourlyFcst', b_23_71866002, int(forecastTime_23_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_23_71866002)))

for area in areaList:
    forecastTime_24_71866002 = 1764018000
    b_24_71866002 = twc.Data()
    b_24_71866002.minTemp = 27
    b_24_71866002.maxTemp = 27
    b_24_71866002.windSpeed = 6
    b_24_71866002.windDir = 6
    b_24_71866002.temp = 27
    b_24_71866002.skyCondition = 2800
    b_24_71866002.pop = 6

    key_24_71866002 = ('71866002.' + str(int(forecastTime_24_71866002)))
    wxdata.setData(key_24_71866002, 'hourlyFcst', b_24_71866002, int(forecastTime_24_71866002 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_24_71866002)))

for area in areaList:
    forecastTime_1_71863000 = 1763935200
    b_1_71863000 = twc.Data()
    b_1_71863000.minTemp = 41
    b_1_71863000.maxTemp = 41
    b_1_71863000.windSpeed = 9
    b_1_71863000.windDir = 7
    b_1_71863000.temp = 41
    b_1_71863000.skyCondition = 2600
    b_1_71863000.pop = 2

    key_1_71863000 = ('71863000.' + str(int(forecastTime_1_71863000)))
    wxdata.setData(key_1_71863000, 'hourlyFcst', b_1_71863000, int(forecastTime_1_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_1_71863000)))

for area in areaList:
    forecastTime_2_71863000 = 1763938800
    b_2_71863000 = twc.Data()
    b_2_71863000.minTemp = 37
    b_2_71863000.maxTemp = 37
    b_2_71863000.windSpeed = 8
    b_2_71863000.windDir = 6
    b_2_71863000.temp = 37
    b_2_71863000.skyCondition = 3000
    b_2_71863000.pop = 2

    key_2_71863000 = ('71863000.' + str(int(forecastTime_2_71863000)))
    wxdata.setData(key_2_71863000, 'hourlyFcst', b_2_71863000, int(forecastTime_2_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_2_71863000)))

for area in areaList:
    forecastTime_3_71863000 = 1763942400
    b_3_71863000 = twc.Data()
    b_3_71863000.minTemp = 34
    b_3_71863000.maxTemp = 34
    b_3_71863000.windSpeed = 8
    b_3_71863000.windDir = 6
    b_3_71863000.temp = 34
    b_3_71863000.skyCondition = 2900
    b_3_71863000.pop = 2

    key_3_71863000 = ('71863000.' + str(int(forecastTime_3_71863000)))
    wxdata.setData(key_3_71863000, 'hourlyFcst', b_3_71863000, int(forecastTime_3_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_3_71863000)))

for area in areaList:
    forecastTime_4_71863000 = 1763946000
    b_4_71863000 = twc.Data()
    b_4_71863000.minTemp = 31
    b_4_71863000.maxTemp = 31
    b_4_71863000.windSpeed = 9
    b_4_71863000.windDir = 7
    b_4_71863000.temp = 31
    b_4_71863000.skyCondition = 2900
    b_4_71863000.pop = 2

    key_4_71863000 = ('71863000.' + str(int(forecastTime_4_71863000)))
    wxdata.setData(key_4_71863000, 'hourlyFcst', b_4_71863000, int(forecastTime_4_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_4_71863000)))

for area in areaList:
    forecastTime_5_71863000 = 1763949600
    b_5_71863000 = twc.Data()
    b_5_71863000.minTemp = 30
    b_5_71863000.maxTemp = 30
    b_5_71863000.windSpeed = 8
    b_5_71863000.windDir = 6
    b_5_71863000.temp = 30
    b_5_71863000.skyCondition = 2700
    b_5_71863000.pop = 2

    key_5_71863000 = ('71863000.' + str(int(forecastTime_5_71863000)))
    wxdata.setData(key_5_71863000, 'hourlyFcst', b_5_71863000, int(forecastTime_5_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_5_71863000)))

for area in areaList:
    forecastTime_6_71863000 = 1763953200
    b_6_71863000 = twc.Data()
    b_6_71863000.minTemp = 29
    b_6_71863000.maxTemp = 29
    b_6_71863000.windSpeed = 8
    b_6_71863000.windDir = 6
    b_6_71863000.temp = 29
    b_6_71863000.skyCondition = 2700
    b_6_71863000.pop = 2

    key_6_71863000 = ('71863000.' + str(int(forecastTime_6_71863000)))
    wxdata.setData(key_6_71863000, 'hourlyFcst', b_6_71863000, int(forecastTime_6_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_6_71863000)))

for area in areaList:
    forecastTime_7_71863000 = 1763956800
    b_7_71863000 = twc.Data()
    b_7_71863000.minTemp = 29
    b_7_71863000.maxTemp = 29
    b_7_71863000.windSpeed = 8
    b_7_71863000.windDir = 7
    b_7_71863000.temp = 29
    b_7_71863000.skyCondition = 2600
    b_7_71863000.pop = 6

    key_7_71863000 = ('71863000.' + str(int(forecastTime_7_71863000)))
    wxdata.setData(key_7_71863000, 'hourlyFcst', b_7_71863000, int(forecastTime_7_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_7_71863000)))

for area in areaList:
    forecastTime_8_71863000 = 1763960400
    b_8_71863000 = twc.Data()
    b_8_71863000.minTemp = 29
    b_8_71863000.maxTemp = 29
    b_8_71863000.windSpeed = 7
    b_8_71863000.windDir = 6
    b_8_71863000.temp = 29
    b_8_71863000.skyCondition = 2600
    b_8_71863000.pop = 8

    key_8_71863000 = ('71863000.' + str(int(forecastTime_8_71863000)))
    wxdata.setData(key_8_71863000, 'hourlyFcst', b_8_71863000, int(forecastTime_8_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_8_71863000)))

for area in areaList:
    forecastTime_9_71863000 = 1763964000
    b_9_71863000 = twc.Data()
    b_9_71863000.minTemp = 29
    b_9_71863000.maxTemp = 29
    b_9_71863000.windSpeed = 7
    b_9_71863000.windDir = 6
    b_9_71863000.temp = 29
    b_9_71863000.skyCondition = 2600
    b_9_71863000.pop = 6

    key_9_71863000 = ('71863000.' + str(int(forecastTime_9_71863000)))
    wxdata.setData(key_9_71863000, 'hourlyFcst', b_9_71863000, int(forecastTime_9_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_9_71863000)))

for area in areaList:
    forecastTime_10_71863000 = 1763967600
    b_10_71863000 = twc.Data()
    b_10_71863000.minTemp = 28
    b_10_71863000.maxTemp = 28
    b_10_71863000.windSpeed = 7
    b_10_71863000.windDir = 7
    b_10_71863000.temp = 28
    b_10_71863000.skyCondition = 2600
    b_10_71863000.pop = 6

    key_10_71863000 = ('71863000.' + str(int(forecastTime_10_71863000)))
    wxdata.setData(key_10_71863000, 'hourlyFcst', b_10_71863000, int(forecastTime_10_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_10_71863000)))

for area in areaList:
    forecastTime_11_71863000 = 1763971200
    b_11_71863000 = twc.Data()
    b_11_71863000.minTemp = 27
    b_11_71863000.maxTemp = 27
    b_11_71863000.windSpeed = 6
    b_11_71863000.windDir = 6
    b_11_71863000.temp = 27
    b_11_71863000.skyCondition = 2600
    b_11_71863000.pop = 6

    key_11_71863000 = ('71863000.' + str(int(forecastTime_11_71863000)))
    wxdata.setData(key_11_71863000, 'hourlyFcst', b_11_71863000, int(forecastTime_11_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_11_71863000)))

for area in areaList:
    forecastTime_12_71863000 = 1763974800
    b_12_71863000 = twc.Data()
    b_12_71863000.minTemp = 27
    b_12_71863000.maxTemp = 27
    b_12_71863000.windSpeed = 6
    b_12_71863000.windDir = 6
    b_12_71863000.temp = 27
    b_12_71863000.skyCondition = 2600
    b_12_71863000.pop = 6

    key_12_71863000 = ('71863000.' + str(int(forecastTime_12_71863000)))
    wxdata.setData(key_12_71863000, 'hourlyFcst', b_12_71863000, int(forecastTime_12_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_12_71863000)))

for area in areaList:
    forecastTime_13_71863000 = 1763978400
    b_13_71863000 = twc.Data()
    b_13_71863000.minTemp = 26
    b_13_71863000.maxTemp = 26
    b_13_71863000.windSpeed = 6
    b_13_71863000.windDir = 7
    b_13_71863000.temp = 26
    b_13_71863000.skyCondition = 2700
    b_13_71863000.pop = 7

    key_13_71863000 = ('71863000.' + str(int(forecastTime_13_71863000)))
    wxdata.setData(key_13_71863000, 'hourlyFcst', b_13_71863000, int(forecastTime_13_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_13_71863000)))

for area in areaList:
    forecastTime_14_71863000 = 1763982000
    b_14_71863000 = twc.Data()
    b_14_71863000.minTemp = 25
    b_14_71863000.maxTemp = 25
    b_14_71863000.windSpeed = 6
    b_14_71863000.windDir = 6
    b_14_71863000.temp = 25
    b_14_71863000.skyCondition = 2600
    b_14_71863000.pop = 7

    key_14_71863000 = ('71863000.' + str(int(forecastTime_14_71863000)))
    wxdata.setData(key_14_71863000, 'hourlyFcst', b_14_71863000, int(forecastTime_14_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_14_71863000)))

for area in areaList:
    forecastTime_15_71863000 = 1763985600
    b_15_71863000 = twc.Data()
    b_15_71863000.minTemp = 25
    b_15_71863000.maxTemp = 25
    b_15_71863000.windSpeed = 5
    b_15_71863000.windDir = 6
    b_15_71863000.temp = 25
    b_15_71863000.skyCondition = 2600
    b_15_71863000.pop = 8

    key_15_71863000 = ('71863000.' + str(int(forecastTime_15_71863000)))
    wxdata.setData(key_15_71863000, 'hourlyFcst', b_15_71863000, int(forecastTime_15_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_15_71863000)))

for area in areaList:
    forecastTime_16_71863000 = 1763989200
    b_16_71863000 = twc.Data()
    b_16_71863000.minTemp = 24
    b_16_71863000.maxTemp = 24
    b_16_71863000.windSpeed = 4
    b_16_71863000.windDir = 7
    b_16_71863000.temp = 24
    b_16_71863000.skyCondition = 2600
    b_16_71863000.pop = 8

    key_16_71863000 = ('71863000.' + str(int(forecastTime_16_71863000)))
    wxdata.setData(key_16_71863000, 'hourlyFcst', b_16_71863000, int(forecastTime_16_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_16_71863000)))

for area in areaList:
    forecastTime_17_71863000 = 1763992800
    b_17_71863000 = twc.Data()
    b_17_71863000.minTemp = 24
    b_17_71863000.maxTemp = 24
    b_17_71863000.windSpeed = 5
    b_17_71863000.windDir = 6
    b_17_71863000.temp = 24
    b_17_71863000.skyCondition = 2600
    b_17_71863000.pop = 8

    key_17_71863000 = ('71863000.' + str(int(forecastTime_17_71863000)))
    wxdata.setData(key_17_71863000, 'hourlyFcst', b_17_71863000, int(forecastTime_17_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_17_71863000)))

for area in areaList:
    forecastTime_18_71863000 = 1763996400
    b_18_71863000 = twc.Data()
    b_18_71863000.minTemp = 25
    b_18_71863000.maxTemp = 25
    b_18_71863000.windSpeed = 3
    b_18_71863000.windDir = 6
    b_18_71863000.temp = 25
    b_18_71863000.skyCondition = 2600
    b_18_71863000.pop = 7

    key_18_71863000 = ('71863000.' + str(int(forecastTime_18_71863000)))
    wxdata.setData(key_18_71863000, 'hourlyFcst', b_18_71863000, int(forecastTime_18_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_18_71863000)))

for area in areaList:
    forecastTime_19_71863000 = 1764000000
    b_19_71863000 = twc.Data()
    b_19_71863000.minTemp = 27
    b_19_71863000.maxTemp = 27
    b_19_71863000.windSpeed = 4
    b_19_71863000.windDir = 7
    b_19_71863000.temp = 27
    b_19_71863000.skyCondition = 2600
    b_19_71863000.pop = 7

    key_19_71863000 = ('71863000.' + str(int(forecastTime_19_71863000)))
    wxdata.setData(key_19_71863000, 'hourlyFcst', b_19_71863000, int(forecastTime_19_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_19_71863000)))

for area in areaList:
    forecastTime_20_71863000 = 1764003600
    b_20_71863000 = twc.Data()
    b_20_71863000.minTemp = 29
    b_20_71863000.maxTemp = 29
    b_20_71863000.windSpeed = 5
    b_20_71863000.windDir = 6
    b_20_71863000.temp = 29
    b_20_71863000.skyCondition = 2600
    b_20_71863000.pop = 5

    key_20_71863000 = ('71863000.' + str(int(forecastTime_20_71863000)))
    wxdata.setData(key_20_71863000, 'hourlyFcst', b_20_71863000, int(forecastTime_20_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_20_71863000)))

for area in areaList:
    forecastTime_21_71863000 = 1764007200
    b_21_71863000 = twc.Data()
    b_21_71863000.minTemp = 31
    b_21_71863000.maxTemp = 31
    b_21_71863000.windSpeed = 4
    b_21_71863000.windDir = 6
    b_21_71863000.temp = 31
    b_21_71863000.skyCondition = 2600
    b_21_71863000.pop = 5

    key_21_71863000 = ('71863000.' + str(int(forecastTime_21_71863000)))
    wxdata.setData(key_21_71863000, 'hourlyFcst', b_21_71863000, int(forecastTime_21_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_21_71863000)))

for area in areaList:
    forecastTime_22_71863000 = 1764010800
    b_22_71863000 = twc.Data()
    b_22_71863000.minTemp = 32
    b_22_71863000.maxTemp = 32
    b_22_71863000.windSpeed = 6
    b_22_71863000.windDir = 7
    b_22_71863000.temp = 32
    b_22_71863000.skyCondition = 2600
    b_22_71863000.pop = 4

    key_22_71863000 = ('71863000.' + str(int(forecastTime_22_71863000)))
    wxdata.setData(key_22_71863000, 'hourlyFcst', b_22_71863000, int(forecastTime_22_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_22_71863000)))

for area in areaList:
    forecastTime_23_71863000 = 1764014400
    b_23_71863000 = twc.Data()
    b_23_71863000.minTemp = 33
    b_23_71863000.maxTemp = 33
    b_23_71863000.windSpeed = 8
    b_23_71863000.windDir = 6
    b_23_71863000.temp = 33
    b_23_71863000.skyCondition = 2600
    b_23_71863000.pop = 2

    key_23_71863000 = ('71863000.' + str(int(forecastTime_23_71863000)))
    wxdata.setData(key_23_71863000, 'hourlyFcst', b_23_71863000, int(forecastTime_23_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_23_71863000)))

for area in areaList:
    forecastTime_24_71863000 = 1764018000
    b_24_71863000 = twc.Data()
    b_24_71863000.minTemp = 34
    b_24_71863000.maxTemp = 34
    b_24_71863000.windSpeed = 8
    b_24_71863000.windDir = 6
    b_24_71863000.temp = 34
    b_24_71863000.skyCondition = 2600
    b_24_71863000.pop = 3

    key_24_71863000 = ('71863000.' + str(int(forecastTime_24_71863000)))
    wxdata.setData(key_24_71863000, 'hourlyFcst', b_24_71863000, int(forecastTime_24_71863000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_24_71863000)))

for area in areaList:
    forecastTime_1_72423000 = 1763938800
    b_1_72423000 = twc.Data()
    b_1_72423000.minTemp = 54
    b_1_72423000.maxTemp = 54
    b_1_72423000.windSpeed = 6
    b_1_72423000.windDir = 7
    b_1_72423000.temp = 54
    b_1_72423000.skyCondition = 3200
    b_1_72423000.pop = 2

    key_1_72423000 = ('72423000.' + str(int(forecastTime_1_72423000)))
    wxdata.setData(key_1_72423000, 'hourlyFcst', b_1_72423000, int(forecastTime_1_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_1_72423000)))

for area in areaList:
    forecastTime_2_72423000 = 1763942400
    b_2_72423000 = twc.Data()
    b_2_72423000.minTemp = 50
    b_2_72423000.maxTemp = 50
    b_2_72423000.windSpeed = 5
    b_2_72423000.windDir = 6
    b_2_72423000.temp = 50
    b_2_72423000.skyCondition = 3100
    b_2_72423000.pop = 2

    key_2_72423000 = ('72423000.' + str(int(forecastTime_2_72423000)))
    wxdata.setData(key_2_72423000, 'hourlyFcst', b_2_72423000, int(forecastTime_2_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_2_72423000)))

for area in areaList:
    forecastTime_3_72423000 = 1763946000
    b_3_72423000 = twc.Data()
    b_3_72423000.minTemp = 48
    b_3_72423000.maxTemp = 48
    b_3_72423000.windSpeed = 4
    b_3_72423000.windDir = 6
    b_3_72423000.temp = 48
    b_3_72423000.skyCondition = 3100
    b_3_72423000.pop = 2

    key_3_72423000 = ('72423000.' + str(int(forecastTime_3_72423000)))
    wxdata.setData(key_3_72423000, 'hourlyFcst', b_3_72423000, int(forecastTime_3_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_3_72423000)))

for area in areaList:
    forecastTime_4_72423000 = 1763949600
    b_4_72423000 = twc.Data()
    b_4_72423000.minTemp = 48
    b_4_72423000.maxTemp = 48
    b_4_72423000.windSpeed = 1
    b_4_72423000.windDir = 7
    b_4_72423000.temp = 48
    b_4_72423000.skyCondition = 3100
    b_4_72423000.pop = 2

    key_4_72423000 = ('72423000.' + str(int(forecastTime_4_72423000)))
    wxdata.setData(key_4_72423000, 'hourlyFcst', b_4_72423000, int(forecastTime_4_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_4_72423000)))

for area in areaList:
    forecastTime_5_72423000 = 1763953200
    b_5_72423000 = twc.Data()
    b_5_72423000.minTemp = 45
    b_5_72423000.maxTemp = 45
    b_5_72423000.windSpeed = 1
    b_5_72423000.windDir = 6
    b_5_72423000.temp = 45
    b_5_72423000.skyCondition = 3100
    b_5_72423000.pop = 4

    key_5_72423000 = ('72423000.' + str(int(forecastTime_5_72423000)))
    wxdata.setData(key_5_72423000, 'hourlyFcst', b_5_72423000, int(forecastTime_5_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_5_72423000)))

for area in areaList:
    forecastTime_6_72423000 = 1763956800
    b_6_72423000 = twc.Data()
    b_6_72423000.minTemp = 44
    b_6_72423000.maxTemp = 44
    b_6_72423000.windSpeed = 0
    b_6_72423000.windDir = 6
    b_6_72423000.temp = 44
    b_6_72423000.skyCondition = 3100
    b_6_72423000.pop = 5

    key_6_72423000 = ('72423000.' + str(int(forecastTime_6_72423000)))
    wxdata.setData(key_6_72423000, 'hourlyFcst', b_6_72423000, int(forecastTime_6_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_6_72423000)))

for area in areaList:
    forecastTime_7_72423000 = 1763960400
    b_7_72423000 = twc.Data()
    b_7_72423000.minTemp = 42
    b_7_72423000.maxTemp = 42
    b_7_72423000.windSpeed = 1
    b_7_72423000.windDir = 7
    b_7_72423000.temp = 42
    b_7_72423000.skyCondition = 3300
    b_7_72423000.pop = 6

    key_7_72423000 = ('72423000.' + str(int(forecastTime_7_72423000)))
    wxdata.setData(key_7_72423000, 'hourlyFcst', b_7_72423000, int(forecastTime_7_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_7_72423000)))

for area in areaList:
    forecastTime_8_72423000 = 1763964000
    b_8_72423000 = twc.Data()
    b_8_72423000.minTemp = 41
    b_8_72423000.maxTemp = 41
    b_8_72423000.windSpeed = 1
    b_8_72423000.windDir = 6
    b_8_72423000.temp = 41
    b_8_72423000.skyCondition = 3300
    b_8_72423000.pop = 7

    key_8_72423000 = ('72423000.' + str(int(forecastTime_8_72423000)))
    wxdata.setData(key_8_72423000, 'hourlyFcst', b_8_72423000, int(forecastTime_8_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_8_72423000)))

for area in areaList:
    forecastTime_9_72423000 = 1763967600
    b_9_72423000 = twc.Data()
    b_9_72423000.minTemp = 40
    b_9_72423000.maxTemp = 40
    b_9_72423000.windSpeed = 1
    b_9_72423000.windDir = 6
    b_9_72423000.temp = 40
    b_9_72423000.skyCondition = 2000
    b_9_72423000.pop = 8

    key_9_72423000 = ('72423000.' + str(int(forecastTime_9_72423000)))
    wxdata.setData(key_9_72423000, 'hourlyFcst', b_9_72423000, int(forecastTime_9_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_9_72423000)))

for area in areaList:
    forecastTime_10_72423000 = 1763971200
    b_10_72423000 = twc.Data()
    b_10_72423000.minTemp = 39
    b_10_72423000.maxTemp = 39
    b_10_72423000.windSpeed = 1
    b_10_72423000.windDir = 7
    b_10_72423000.temp = 39
    b_10_72423000.skyCondition = 2000
    b_10_72423000.pop = 8

    key_10_72423000 = ('72423000.' + str(int(forecastTime_10_72423000)))
    wxdata.setData(key_10_72423000, 'hourlyFcst', b_10_72423000, int(forecastTime_10_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_10_72423000)))

for area in areaList:
    forecastTime_11_72423000 = 1763974800
    b_11_72423000 = twc.Data()
    b_11_72423000.minTemp = 39
    b_11_72423000.maxTemp = 39
    b_11_72423000.windSpeed = 2
    b_11_72423000.windDir = 6
    b_11_72423000.temp = 39
    b_11_72423000.skyCondition = 2000
    b_11_72423000.pop = 8

    key_11_72423000 = ('72423000.' + str(int(forecastTime_11_72423000)))
    wxdata.setData(key_11_72423000, 'hourlyFcst', b_11_72423000, int(forecastTime_11_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_11_72423000)))

for area in areaList:
    forecastTime_12_72423000 = 1763978400
    b_12_72423000 = twc.Data()
    b_12_72423000.minTemp = 39
    b_12_72423000.maxTemp = 39
    b_12_72423000.windSpeed = 2
    b_12_72423000.windDir = 6
    b_12_72423000.temp = 39
    b_12_72423000.skyCondition = 2000
    b_12_72423000.pop = 9

    key_12_72423000 = ('72423000.' + str(int(forecastTime_12_72423000)))
    wxdata.setData(key_12_72423000, 'hourlyFcst', b_12_72423000, int(forecastTime_12_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_12_72423000)))

for area in areaList:
    forecastTime_13_72423000 = 1763982000
    b_13_72423000 = twc.Data()
    b_13_72423000.minTemp = 39
    b_13_72423000.maxTemp = 39
    b_13_72423000.windSpeed = 3
    b_13_72423000.windDir = 7
    b_13_72423000.temp = 39
    b_13_72423000.skyCondition = 2000
    b_13_72423000.pop = 9

    key_13_72423000 = ('72423000.' + str(int(forecastTime_13_72423000)))
    wxdata.setData(key_13_72423000, 'hourlyFcst', b_13_72423000, int(forecastTime_13_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_13_72423000)))

for area in areaList:
    forecastTime_14_72423000 = 1763985600
    b_14_72423000 = twc.Data()
    b_14_72423000.minTemp = 38
    b_14_72423000.maxTemp = 38
    b_14_72423000.windSpeed = 2
    b_14_72423000.windDir = 6
    b_14_72423000.temp = 38
    b_14_72423000.skyCondition = 2000
    b_14_72423000.pop = 9

    key_14_72423000 = ('72423000.' + str(int(forecastTime_14_72423000)))
    wxdata.setData(key_14_72423000, 'hourlyFcst', b_14_72423000, int(forecastTime_14_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_14_72423000)))

for area in areaList:
    forecastTime_15_72423000 = 1763989200
    b_15_72423000 = twc.Data()
    b_15_72423000.minTemp = 38
    b_15_72423000.maxTemp = 38
    b_15_72423000.windSpeed = 3
    b_15_72423000.windDir = 6
    b_15_72423000.temp = 38
    b_15_72423000.skyCondition = 2000
    b_15_72423000.pop = 7

    key_15_72423000 = ('72423000.' + str(int(forecastTime_15_72423000)))
    wxdata.setData(key_15_72423000, 'hourlyFcst', b_15_72423000, int(forecastTime_15_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_15_72423000)))

for area in areaList:
    forecastTime_16_72423000 = 1763992800
    b_16_72423000 = twc.Data()
    b_16_72423000.minTemp = 39
    b_16_72423000.maxTemp = 39
    b_16_72423000.windSpeed = 4
    b_16_72423000.windDir = 7
    b_16_72423000.temp = 39
    b_16_72423000.skyCondition = 2000
    b_16_72423000.pop = 7

    key_16_72423000 = ('72423000.' + str(int(forecastTime_16_72423000)))
    wxdata.setData(key_16_72423000, 'hourlyFcst', b_16_72423000, int(forecastTime_16_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_16_72423000)))

for area in areaList:
    forecastTime_17_72423000 = 1763996400
    b_17_72423000 = twc.Data()
    b_17_72423000.minTemp = 41
    b_17_72423000.maxTemp = 41
    b_17_72423000.windSpeed = 4
    b_17_72423000.windDir = 6
    b_17_72423000.temp = 41
    b_17_72423000.skyCondition = 2000
    b_17_72423000.pop = 7

    key_17_72423000 = ('72423000.' + str(int(forecastTime_17_72423000)))
    wxdata.setData(key_17_72423000, 'hourlyFcst', b_17_72423000, int(forecastTime_17_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_17_72423000)))

for area in areaList:
    forecastTime_18_72423000 = 1764000000
    b_18_72423000 = twc.Data()
    b_18_72423000.minTemp = 45
    b_18_72423000.maxTemp = 45
    b_18_72423000.windSpeed = 4
    b_18_72423000.windDir = 6
    b_18_72423000.temp = 45
    b_18_72423000.skyCondition = 2600
    b_18_72423000.pop = 6

    key_18_72423000 = ('72423000.' + str(int(forecastTime_18_72423000)))
    wxdata.setData(key_18_72423000, 'hourlyFcst', b_18_72423000, int(forecastTime_18_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_18_72423000)))

for area in areaList:
    forecastTime_19_72423000 = 1764003600
    b_19_72423000 = twc.Data()
    b_19_72423000.minTemp = 48
    b_19_72423000.maxTemp = 48
    b_19_72423000.windSpeed = 4
    b_19_72423000.windDir = 7
    b_19_72423000.temp = 48
    b_19_72423000.skyCondition = 2800
    b_19_72423000.pop = 5

    key_19_72423000 = ('72423000.' + str(int(forecastTime_19_72423000)))
    wxdata.setData(key_19_72423000, 'hourlyFcst', b_19_72423000, int(forecastTime_19_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_19_72423000)))

for area in areaList:
    forecastTime_20_72423000 = 1764007200
    b_20_72423000 = twc.Data()
    b_20_72423000.minTemp = 51
    b_20_72423000.maxTemp = 51
    b_20_72423000.windSpeed = 5
    b_20_72423000.windDir = 6
    b_20_72423000.temp = 51
    b_20_72423000.skyCondition = 2600
    b_20_72423000.pop = 5

    key_20_72423000 = ('72423000.' + str(int(forecastTime_20_72423000)))
    wxdata.setData(key_20_72423000, 'hourlyFcst', b_20_72423000, int(forecastTime_20_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_20_72423000)))

for area in areaList:
    forecastTime_21_72423000 = 1764010800
    b_21_72423000 = twc.Data()
    b_21_72423000.minTemp = 54
    b_21_72423000.maxTemp = 54
    b_21_72423000.windSpeed = 5
    b_21_72423000.windDir = 6
    b_21_72423000.temp = 54
    b_21_72423000.skyCondition = 2800
    b_21_72423000.pop = 4

    key_21_72423000 = ('72423000.' + str(int(forecastTime_21_72423000)))
    wxdata.setData(key_21_72423000, 'hourlyFcst', b_21_72423000, int(forecastTime_21_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_21_72423000)))

for area in areaList:
    forecastTime_22_72423000 = 1764014400
    b_22_72423000 = twc.Data()
    b_22_72423000.minTemp = 57
    b_22_72423000.maxTemp = 57
    b_22_72423000.windSpeed = 5
    b_22_72423000.windDir = 7
    b_22_72423000.temp = 57
    b_22_72423000.skyCondition = 2600
    b_22_72423000.pop = 3

    key_22_72423000 = ('72423000.' + str(int(forecastTime_22_72423000)))
    wxdata.setData(key_22_72423000, 'hourlyFcst', b_22_72423000, int(forecastTime_22_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_22_72423000)))

for area in areaList:
    forecastTime_23_72423000 = 1764018000
    b_23_72423000 = twc.Data()
    b_23_72423000.minTemp = 58
    b_23_72423000.maxTemp = 58
    b_23_72423000.windSpeed = 5
    b_23_72423000.windDir = 6
    b_23_72423000.temp = 58
    b_23_72423000.skyCondition = 2800
    b_23_72423000.pop = 4

    key_23_72423000 = ('72423000.' + str(int(forecastTime_23_72423000)))
    wxdata.setData(key_23_72423000, 'hourlyFcst', b_23_72423000, int(forecastTime_23_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_23_72423000)))

for area in areaList:
    forecastTime_24_72423000 = 1764021600
    b_24_72423000 = twc.Data()
    b_24_72423000.minTemp = 58
    b_24_72423000.maxTemp = 58
    b_24_72423000.windSpeed = 4
    b_24_72423000.windDir = 6
    b_24_72423000.temp = 58
    b_24_72423000.skyCondition = 2600
    b_24_72423000.pop = 5

    key_24_72423000 = ('72423000.' + str(int(forecastTime_24_72423000)))
    wxdata.setData(key_24_72423000, 'hourlyFcst', b_24_72423000, int(forecastTime_24_72423000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_24_72423000)))

for area in areaList:
    forecastTime_1_71876000 = 1763935200
    b_1_71876000 = twc.Data()
    b_1_71876000.minTemp = 36
    b_1_71876000.maxTemp = 36
    b_1_71876000.windSpeed = 8
    b_1_71876000.windDir = 7
    b_1_71876000.temp = 36
    b_1_71876000.skyCondition = 3000
    b_1_71876000.pop = 2

    key_1_71876000 = ('71876000.' + str(int(forecastTime_1_71876000)))
    wxdata.setData(key_1_71876000, 'hourlyFcst', b_1_71876000, int(forecastTime_1_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_1_71876000)))

for area in areaList:
    forecastTime_2_71876000 = 1763938800
    b_2_71876000 = twc.Data()
    b_2_71876000.minTemp = 32
    b_2_71876000.maxTemp = 32
    b_2_71876000.windSpeed = 7
    b_2_71876000.windDir = 6
    b_2_71876000.temp = 32
    b_2_71876000.skyCondition = 3000
    b_2_71876000.pop = 2

    key_2_71876000 = ('71876000.' + str(int(forecastTime_2_71876000)))
    wxdata.setData(key_2_71876000, 'hourlyFcst', b_2_71876000, int(forecastTime_2_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_2_71876000)))

for area in areaList:
    forecastTime_3_71876000 = 1763942400
    b_3_71876000 = twc.Data()
    b_3_71876000.minTemp = 31
    b_3_71876000.maxTemp = 31
    b_3_71876000.windSpeed = 8
    b_3_71876000.windDir = 6
    b_3_71876000.temp = 31
    b_3_71876000.skyCondition = 2900
    b_3_71876000.pop = 3

    key_3_71876000 = ('71876000.' + str(int(forecastTime_3_71876000)))
    wxdata.setData(key_3_71876000, 'hourlyFcst', b_3_71876000, int(forecastTime_3_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_3_71876000)))

for area in areaList:
    forecastTime_4_71876000 = 1763946000
    b_4_71876000 = twc.Data()
    b_4_71876000.minTemp = 28
    b_4_71876000.maxTemp = 28
    b_4_71876000.windSpeed = 8
    b_4_71876000.windDir = 7
    b_4_71876000.temp = 28
    b_4_71876000.skyCondition = 2900
    b_4_71876000.pop = 3

    key_4_71876000 = ('71876000.' + str(int(forecastTime_4_71876000)))
    wxdata.setData(key_4_71876000, 'hourlyFcst', b_4_71876000, int(forecastTime_4_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_4_71876000)))

for area in areaList:
    forecastTime_5_71876000 = 1763949600
    b_5_71876000 = twc.Data()
    b_5_71876000.minTemp = 26
    b_5_71876000.maxTemp = 26
    b_5_71876000.windSpeed = 8
    b_5_71876000.windDir = 6
    b_5_71876000.temp = 26
    b_5_71876000.skyCondition = 2900
    b_5_71876000.pop = 3

    key_5_71876000 = ('71876000.' + str(int(forecastTime_5_71876000)))
    wxdata.setData(key_5_71876000, 'hourlyFcst', b_5_71876000, int(forecastTime_5_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_5_71876000)))

for area in areaList:
    forecastTime_6_71876000 = 1763953200
    b_6_71876000 = twc.Data()
    b_6_71876000.minTemp = 24
    b_6_71876000.maxTemp = 24
    b_6_71876000.windSpeed = 7
    b_6_71876000.windDir = 6
    b_6_71876000.temp = 24
    b_6_71876000.skyCondition = 3300
    b_6_71876000.pop = 3

    key_6_71876000 = ('71876000.' + str(int(forecastTime_6_71876000)))
    wxdata.setData(key_6_71876000, 'hourlyFcst', b_6_71876000, int(forecastTime_6_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_6_71876000)))

for area in areaList:
    forecastTime_7_71876000 = 1763956800
    b_7_71876000 = twc.Data()
    b_7_71876000.minTemp = 24
    b_7_71876000.maxTemp = 24
    b_7_71876000.windSpeed = 6
    b_7_71876000.windDir = 7
    b_7_71876000.temp = 24
    b_7_71876000.skyCondition = 3100
    b_7_71876000.pop = 6

    key_7_71876000 = ('71876000.' + str(int(forecastTime_7_71876000)))
    wxdata.setData(key_7_71876000, 'hourlyFcst', b_7_71876000, int(forecastTime_7_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_7_71876000)))

for area in areaList:
    forecastTime_8_71876000 = 1763960400
    b_8_71876000 = twc.Data()
    b_8_71876000.minTemp = 23
    b_8_71876000.maxTemp = 23
    b_8_71876000.windSpeed = 6
    b_8_71876000.windDir = 6
    b_8_71876000.temp = 23
    b_8_71876000.skyCondition = 3100
    b_8_71876000.pop = 9

    key_8_71876000 = ('71876000.' + str(int(forecastTime_8_71876000)))
    wxdata.setData(key_8_71876000, 'hourlyFcst', b_8_71876000, int(forecastTime_8_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_8_71876000)))

for area in areaList:
    forecastTime_9_71876000 = 1763964000
    b_9_71876000 = twc.Data()
    b_9_71876000.minTemp = 22
    b_9_71876000.maxTemp = 22
    b_9_71876000.windSpeed = 5
    b_9_71876000.windDir = 6
    b_9_71876000.temp = 22
    b_9_71876000.skyCondition = 3100
    b_9_71876000.pop = 9

    key_9_71876000 = ('71876000.' + str(int(forecastTime_9_71876000)))
    wxdata.setData(key_9_71876000, 'hourlyFcst', b_9_71876000, int(forecastTime_9_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_9_71876000)))

for area in areaList:
    forecastTime_10_71876000 = 1763967600
    b_10_71876000 = twc.Data()
    b_10_71876000.minTemp = 20
    b_10_71876000.maxTemp = 20
    b_10_71876000.windSpeed = 6
    b_10_71876000.windDir = 7
    b_10_71876000.temp = 20
    b_10_71876000.skyCondition = 3100
    b_10_71876000.pop = 9

    key_10_71876000 = ('71876000.' + str(int(forecastTime_10_71876000)))
    wxdata.setData(key_10_71876000, 'hourlyFcst', b_10_71876000, int(forecastTime_10_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_10_71876000)))

for area in areaList:
    forecastTime_11_71876000 = 1763971200
    b_11_71876000 = twc.Data()
    b_11_71876000.minTemp = 18
    b_11_71876000.maxTemp = 18
    b_11_71876000.windSpeed = 5
    b_11_71876000.windDir = 6
    b_11_71876000.temp = 18
    b_11_71876000.skyCondition = 2900
    b_11_71876000.pop = 9

    key_11_71876000 = ('71876000.' + str(int(forecastTime_11_71876000)))
    wxdata.setData(key_11_71876000, 'hourlyFcst', b_11_71876000, int(forecastTime_11_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_11_71876000)))

for area in areaList:
    forecastTime_12_71876000 = 1763974800
    b_12_71876000 = twc.Data()
    b_12_71876000.minTemp = 18
    b_12_71876000.maxTemp = 18
    b_12_71876000.windSpeed = 5
    b_12_71876000.windDir = 6
    b_12_71876000.temp = 18
    b_12_71876000.skyCondition = 2900
    b_12_71876000.pop = 9

    key_12_71876000 = ('71876000.' + str(int(forecastTime_12_71876000)))
    wxdata.setData(key_12_71876000, 'hourlyFcst', b_12_71876000, int(forecastTime_12_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_12_71876000)))

for area in areaList:
    forecastTime_13_71876000 = 1763978400
    b_13_71876000 = twc.Data()
    b_13_71876000.minTemp = 17
    b_13_71876000.maxTemp = 17
    b_13_71876000.windSpeed = 4
    b_13_71876000.windDir = 7
    b_13_71876000.temp = 17
    b_13_71876000.skyCondition = 2700
    b_13_71876000.pop = 9

    key_13_71876000 = ('71876000.' + str(int(forecastTime_13_71876000)))
    wxdata.setData(key_13_71876000, 'hourlyFcst', b_13_71876000, int(forecastTime_13_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_13_71876000)))

for area in areaList:
    forecastTime_14_71876000 = 1763982000
    b_14_71876000 = twc.Data()
    b_14_71876000.minTemp = 17
    b_14_71876000.maxTemp = 17
    b_14_71876000.windSpeed = 4
    b_14_71876000.windDir = 6
    b_14_71876000.temp = 17
    b_14_71876000.skyCondition = 2700
    b_14_71876000.pop = 9

    key_14_71876000 = ('71876000.' + str(int(forecastTime_14_71876000)))
    wxdata.setData(key_14_71876000, 'hourlyFcst', b_14_71876000, int(forecastTime_14_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_14_71876000)))

for area in areaList:
    forecastTime_15_71876000 = 1763985600
    b_15_71876000 = twc.Data()
    b_15_71876000.minTemp = 17
    b_15_71876000.maxTemp = 17
    b_15_71876000.windSpeed = 4
    b_15_71876000.windDir = 6
    b_15_71876000.temp = 17
    b_15_71876000.skyCondition = 2700
    b_15_71876000.pop = 9

    key_15_71876000 = ('71876000.' + str(int(forecastTime_15_71876000)))
    wxdata.setData(key_15_71876000, 'hourlyFcst', b_15_71876000, int(forecastTime_15_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_15_71876000)))

for area in areaList:
    forecastTime_16_71876000 = 1763989200
    b_16_71876000 = twc.Data()
    b_16_71876000.minTemp = 16
    b_16_71876000.maxTemp = 16
    b_16_71876000.windSpeed = 3
    b_16_71876000.windDir = 7
    b_16_71876000.temp = 16
    b_16_71876000.skyCondition = 2600
    b_16_71876000.pop = 9

    key_16_71876000 = ('71876000.' + str(int(forecastTime_16_71876000)))
    wxdata.setData(key_16_71876000, 'hourlyFcst', b_16_71876000, int(forecastTime_16_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_16_71876000)))

for area in areaList:
    forecastTime_17_71876000 = 1763992800
    b_17_71876000 = twc.Data()
    b_17_71876000.minTemp = 15
    b_17_71876000.maxTemp = 15
    b_17_71876000.windSpeed = 4
    b_17_71876000.windDir = 6
    b_17_71876000.temp = 15
    b_17_71876000.skyCondition = 2600
    b_17_71876000.pop = 9

    key_17_71876000 = ('71876000.' + str(int(forecastTime_17_71876000)))
    wxdata.setData(key_17_71876000, 'hourlyFcst', b_17_71876000, int(forecastTime_17_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_17_71876000)))

for area in areaList:
    forecastTime_18_71876000 = 1763996400
    b_18_71876000 = twc.Data()
    b_18_71876000.minTemp = 15
    b_18_71876000.maxTemp = 15
    b_18_71876000.windSpeed = 3
    b_18_71876000.windDir = 6
    b_18_71876000.temp = 15
    b_18_71876000.skyCondition = 2600
    b_18_71876000.pop = 9

    key_18_71876000 = ('71876000.' + str(int(forecastTime_18_71876000)))
    wxdata.setData(key_18_71876000, 'hourlyFcst', b_18_71876000, int(forecastTime_18_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_18_71876000)))

for area in areaList:
    forecastTime_19_71876000 = 1764000000
    b_19_71876000 = twc.Data()
    b_19_71876000.minTemp = 18
    b_19_71876000.maxTemp = 18
    b_19_71876000.windSpeed = 3
    b_19_71876000.windDir = 7
    b_19_71876000.temp = 18
    b_19_71876000.skyCondition = 2600
    b_19_71876000.pop = 8

    key_19_71876000 = ('71876000.' + str(int(forecastTime_19_71876000)))
    wxdata.setData(key_19_71876000, 'hourlyFcst', b_19_71876000, int(forecastTime_19_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_19_71876000)))

for area in areaList:
    forecastTime_20_71876000 = 1764003600
    b_20_71876000 = twc.Data()
    b_20_71876000.minTemp = 21
    b_20_71876000.maxTemp = 21
    b_20_71876000.windSpeed = 5
    b_20_71876000.windDir = 6
    b_20_71876000.temp = 21
    b_20_71876000.skyCondition = 2600
    b_20_71876000.pop = 8

    key_20_71876000 = ('71876000.' + str(int(forecastTime_20_71876000)))
    wxdata.setData(key_20_71876000, 'hourlyFcst', b_20_71876000, int(forecastTime_20_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_20_71876000)))

for area in areaList:
    forecastTime_21_71876000 = 1764007200
    b_21_71876000 = twc.Data()
    b_21_71876000.minTemp = 23
    b_21_71876000.maxTemp = 23
    b_21_71876000.windSpeed = 6
    b_21_71876000.windDir = 6
    b_21_71876000.temp = 23
    b_21_71876000.skyCondition = 2800
    b_21_71876000.pop = 6

    key_21_71876000 = ('71876000.' + str(int(forecastTime_21_71876000)))
    wxdata.setData(key_21_71876000, 'hourlyFcst', b_21_71876000, int(forecastTime_21_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_21_71876000)))

for area in areaList:
    forecastTime_22_71876000 = 1764010800
    b_22_71876000 = twc.Data()
    b_22_71876000.minTemp = 24
    b_22_71876000.maxTemp = 24
    b_22_71876000.windSpeed = 6
    b_22_71876000.windDir = 7
    b_22_71876000.temp = 24
    b_22_71876000.skyCondition = 2800
    b_22_71876000.pop = 6

    key_22_71876000 = ('71876000.' + str(int(forecastTime_22_71876000)))
    wxdata.setData(key_22_71876000, 'hourlyFcst', b_22_71876000, int(forecastTime_22_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_22_71876000)))

for area in areaList:
    forecastTime_23_71876000 = 1764014400
    b_23_71876000 = twc.Data()
    b_23_71876000.minTemp = 25
    b_23_71876000.maxTemp = 25
    b_23_71876000.windSpeed = 8
    b_23_71876000.windDir = 6
    b_23_71876000.temp = 25
    b_23_71876000.skyCondition = 2800
    b_23_71876000.pop = 5

    key_23_71876000 = ('71876000.' + str(int(forecastTime_23_71876000)))
    wxdata.setData(key_23_71876000, 'hourlyFcst', b_23_71876000, int(forecastTime_23_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_23_71876000)))

for area in areaList:
    forecastTime_24_71876000 = 1764018000
    b_24_71876000 = twc.Data()
    b_24_71876000.minTemp = 25
    b_24_71876000.maxTemp = 25
    b_24_71876000.windSpeed = 8
    b_24_71876000.windDir = 6
    b_24_71876000.temp = 25
    b_24_71876000.skyCondition = 2800
    b_24_71876000.pop = 5

    key_24_71876000 = ('71876000.' + str(int(forecastTime_24_71876000)))
    wxdata.setData(key_24_71876000, 'hourlyFcst', b_24_71876000, int(forecastTime_24_71876000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_24_71876000)))

for area in areaList:
    forecastTime_1_71869000 = 1763935200
    b_1_71869000 = twc.Data()
    b_1_71869000.minTemp = 33
    b_1_71869000.maxTemp = 33
    b_1_71869000.windSpeed = 6
    b_1_71869000.windDir = 7
    b_1_71869000.temp = 33
    b_1_71869000.skyCondition = 3000
    b_1_71869000.pop = 2

    key_1_71869000 = ('71869000.' + str(int(forecastTime_1_71869000)))
    wxdata.setData(key_1_71869000, 'hourlyFcst', b_1_71869000, int(forecastTime_1_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_1_71869000)))

for area in areaList:
    forecastTime_2_71869000 = 1763938800
    b_2_71869000 = twc.Data()
    b_2_71869000.minTemp = 31
    b_2_71869000.maxTemp = 31
    b_2_71869000.windSpeed = 7
    b_2_71869000.windDir = 6
    b_2_71869000.temp = 31
    b_2_71869000.skyCondition = 2900
    b_2_71869000.pop = 2

    key_2_71869000 = ('71869000.' + str(int(forecastTime_2_71869000)))
    wxdata.setData(key_2_71869000, 'hourlyFcst', b_2_71869000, int(forecastTime_2_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_2_71869000)))

for area in areaList:
    forecastTime_3_71869000 = 1763942400
    b_3_71869000 = twc.Data()
    b_3_71869000.minTemp = 30
    b_3_71869000.maxTemp = 30
    b_3_71869000.windSpeed = 6
    b_3_71869000.windDir = 6
    b_3_71869000.temp = 30
    b_3_71869000.skyCondition = 3300
    b_3_71869000.pop = 2

    key_3_71869000 = ('71869000.' + str(int(forecastTime_3_71869000)))
    wxdata.setData(key_3_71869000, 'hourlyFcst', b_3_71869000, int(forecastTime_3_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_3_71869000)))

for area in areaList:
    forecastTime_4_71869000 = 1763946000
    b_4_71869000 = twc.Data()
    b_4_71869000.minTemp = 28
    b_4_71869000.maxTemp = 28
    b_4_71869000.windSpeed = 7
    b_4_71869000.windDir = 7
    b_4_71869000.temp = 28
    b_4_71869000.skyCondition = 3100
    b_4_71869000.pop = 3

    key_4_71869000 = ('71869000.' + str(int(forecastTime_4_71869000)))
    wxdata.setData(key_4_71869000, 'hourlyFcst', b_4_71869000, int(forecastTime_4_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_4_71869000)))

for area in areaList:
    forecastTime_5_71869000 = 1763949600
    b_5_71869000 = twc.Data()
    b_5_71869000.minTemp = 26
    b_5_71869000.maxTemp = 26
    b_5_71869000.windSpeed = 7
    b_5_71869000.windDir = 6
    b_5_71869000.temp = 26
    b_5_71869000.skyCondition = 3100
    b_5_71869000.pop = 3

    key_5_71869000 = ('71869000.' + str(int(forecastTime_5_71869000)))
    wxdata.setData(key_5_71869000, 'hourlyFcst', b_5_71869000, int(forecastTime_5_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_5_71869000)))

for area in areaList:
    forecastTime_6_71869000 = 1763953200
    b_6_71869000 = twc.Data()
    b_6_71869000.minTemp = 25
    b_6_71869000.maxTemp = 25
    b_6_71869000.windSpeed = 6
    b_6_71869000.windDir = 6
    b_6_71869000.temp = 25
    b_6_71869000.skyCondition = 3100
    b_6_71869000.pop = 3

    key_6_71869000 = ('71869000.' + str(int(forecastTime_6_71869000)))
    wxdata.setData(key_6_71869000, 'hourlyFcst', b_6_71869000, int(forecastTime_6_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_6_71869000)))

for area in areaList:
    forecastTime_7_71869000 = 1763956800
    b_7_71869000 = twc.Data()
    b_7_71869000.minTemp = 24
    b_7_71869000.maxTemp = 24
    b_7_71869000.windSpeed = 6
    b_7_71869000.windDir = 7
    b_7_71869000.temp = 24
    b_7_71869000.skyCondition = 3300
    b_7_71869000.pop = 6

    key_7_71869000 = ('71869000.' + str(int(forecastTime_7_71869000)))
    wxdata.setData(key_7_71869000, 'hourlyFcst', b_7_71869000, int(forecastTime_7_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_7_71869000)))

for area in areaList:
    forecastTime_8_71869000 = 1763960400
    b_8_71869000 = twc.Data()
    b_8_71869000.minTemp = 23
    b_8_71869000.maxTemp = 23
    b_8_71869000.windSpeed = 6
    b_8_71869000.windDir = 6
    b_8_71869000.temp = 23
    b_8_71869000.skyCondition = 3100
    b_8_71869000.pop = 9

    key_8_71869000 = ('71869000.' + str(int(forecastTime_8_71869000)))
    wxdata.setData(key_8_71869000, 'hourlyFcst', b_8_71869000, int(forecastTime_8_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_8_71869000)))

for area in areaList:
    forecastTime_9_71869000 = 1763964000
    b_9_71869000 = twc.Data()
    b_9_71869000.minTemp = 22
    b_9_71869000.maxTemp = 22
    b_9_71869000.windSpeed = 6
    b_9_71869000.windDir = 6
    b_9_71869000.temp = 22
    b_9_71869000.skyCondition = 2900
    b_9_71869000.pop = 9

    key_9_71869000 = ('71869000.' + str(int(forecastTime_9_71869000)))
    wxdata.setData(key_9_71869000, 'hourlyFcst', b_9_71869000, int(forecastTime_9_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_9_71869000)))

for area in areaList:
    forecastTime_10_71869000 = 1763967600
    b_10_71869000 = twc.Data()
    b_10_71869000.minTemp = 21
    b_10_71869000.maxTemp = 21
    b_10_71869000.windSpeed = 5
    b_10_71869000.windDir = 7
    b_10_71869000.temp = 21
    b_10_71869000.skyCondition = 2900
    b_10_71869000.pop = 9

    key_10_71869000 = ('71869000.' + str(int(forecastTime_10_71869000)))
    wxdata.setData(key_10_71869000, 'hourlyFcst', b_10_71869000, int(forecastTime_10_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_10_71869000)))

for area in areaList:
    forecastTime_11_71869000 = 1763971200
    b_11_71869000 = twc.Data()
    b_11_71869000.minTemp = 21
    b_11_71869000.maxTemp = 21
    b_11_71869000.windSpeed = 5
    b_11_71869000.windDir = 6
    b_11_71869000.temp = 21
    b_11_71869000.skyCondition = 2900
    b_11_71869000.pop = 9

    key_11_71869000 = ('71869000.' + str(int(forecastTime_11_71869000)))
    wxdata.setData(key_11_71869000, 'hourlyFcst', b_11_71869000, int(forecastTime_11_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_11_71869000)))

for area in areaList:
    forecastTime_12_71869000 = 1763974800
    b_12_71869000 = twc.Data()
    b_12_71869000.minTemp = 20
    b_12_71869000.maxTemp = 20
    b_12_71869000.windSpeed = 5
    b_12_71869000.windDir = 6
    b_12_71869000.temp = 20
    b_12_71869000.skyCondition = 2900
    b_12_71869000.pop = 9

    key_12_71869000 = ('71869000.' + str(int(forecastTime_12_71869000)))
    wxdata.setData(key_12_71869000, 'hourlyFcst', b_12_71869000, int(forecastTime_12_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_12_71869000)))

for area in areaList:
    forecastTime_13_71869000 = 1763978400
    b_13_71869000 = twc.Data()
    b_13_71869000.minTemp = 19
    b_13_71869000.maxTemp = 19
    b_13_71869000.windSpeed = 5
    b_13_71869000.windDir = 7
    b_13_71869000.temp = 19
    b_13_71869000.skyCondition = 2900
    b_13_71869000.pop = 9

    key_13_71869000 = ('71869000.' + str(int(forecastTime_13_71869000)))
    wxdata.setData(key_13_71869000, 'hourlyFcst', b_13_71869000, int(forecastTime_13_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_13_71869000)))

for area in areaList:
    forecastTime_14_71869000 = 1763982000
    b_14_71869000 = twc.Data()
    b_14_71869000.minTemp = 19
    b_14_71869000.maxTemp = 19
    b_14_71869000.windSpeed = 5
    b_14_71869000.windDir = 6
    b_14_71869000.temp = 19
    b_14_71869000.skyCondition = 2900
    b_14_71869000.pop = 9

    key_14_71869000 = ('71869000.' + str(int(forecastTime_14_71869000)))
    wxdata.setData(key_14_71869000, 'hourlyFcst', b_14_71869000, int(forecastTime_14_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_14_71869000)))

for area in areaList:
    forecastTime_15_71869000 = 1763985600
    b_15_71869000 = twc.Data()
    b_15_71869000.minTemp = 19
    b_15_71869000.maxTemp = 19
    b_15_71869000.windSpeed = 4
    b_15_71869000.windDir = 6
    b_15_71869000.temp = 19
    b_15_71869000.skyCondition = 2700
    b_15_71869000.pop = 9

    key_15_71869000 = ('71869000.' + str(int(forecastTime_15_71869000)))
    wxdata.setData(key_15_71869000, 'hourlyFcst', b_15_71869000, int(forecastTime_15_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_15_71869000)))

for area in areaList:
    forecastTime_16_71869000 = 1763989200
    b_16_71869000 = twc.Data()
    b_16_71869000.minTemp = 19
    b_16_71869000.maxTemp = 19
    b_16_71869000.windSpeed = 4
    b_16_71869000.windDir = 7
    b_16_71869000.temp = 19
    b_16_71869000.skyCondition = 2700
    b_16_71869000.pop = 9

    key_16_71869000 = ('71869000.' + str(int(forecastTime_16_71869000)))
    wxdata.setData(key_16_71869000, 'hourlyFcst', b_16_71869000, int(forecastTime_16_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_16_71869000)))

for area in areaList:
    forecastTime_17_71869000 = 1763992800
    b_17_71869000 = twc.Data()
    b_17_71869000.minTemp = 18
    b_17_71869000.maxTemp = 18
    b_17_71869000.windSpeed = 4
    b_17_71869000.windDir = 6
    b_17_71869000.temp = 18
    b_17_71869000.skyCondition = 2600
    b_17_71869000.pop = 9

    key_17_71869000 = ('71869000.' + str(int(forecastTime_17_71869000)))
    wxdata.setData(key_17_71869000, 'hourlyFcst', b_17_71869000, int(forecastTime_17_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_17_71869000)))

for area in areaList:
    forecastTime_18_71869000 = 1763996400
    b_18_71869000 = twc.Data()
    b_18_71869000.minTemp = 17
    b_18_71869000.maxTemp = 17
    b_18_71869000.windSpeed = 4
    b_18_71869000.windDir = 6
    b_18_71869000.temp = 17
    b_18_71869000.skyCondition = 2800
    b_18_71869000.pop = 9

    key_18_71869000 = ('71869000.' + str(int(forecastTime_18_71869000)))
    wxdata.setData(key_18_71869000, 'hourlyFcst', b_18_71869000, int(forecastTime_18_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_18_71869000)))

for area in areaList:
    forecastTime_19_71869000 = 1764000000
    b_19_71869000 = twc.Data()
    b_19_71869000.minTemp = 20
    b_19_71869000.maxTemp = 20
    b_19_71869000.windSpeed = 5
    b_19_71869000.windDir = 7
    b_19_71869000.temp = 20
    b_19_71869000.skyCondition = 2800
    b_19_71869000.pop = 8

    key_19_71869000 = ('71869000.' + str(int(forecastTime_19_71869000)))
    wxdata.setData(key_19_71869000, 'hourlyFcst', b_19_71869000, int(forecastTime_19_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_19_71869000)))

for area in areaList:
    forecastTime_20_71869000 = 1764003600
    b_20_71869000 = twc.Data()
    b_20_71869000.minTemp = 22
    b_20_71869000.maxTemp = 22
    b_20_71869000.windSpeed = 5
    b_20_71869000.windDir = 6
    b_20_71869000.temp = 22
    b_20_71869000.skyCondition = 2600
    b_20_71869000.pop = 7

    key_20_71869000 = ('71869000.' + str(int(forecastTime_20_71869000)))
    wxdata.setData(key_20_71869000, 'hourlyFcst', b_20_71869000, int(forecastTime_20_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_20_71869000)))

for area in areaList:
    forecastTime_21_71869000 = 1764007200
    b_21_71869000 = twc.Data()
    b_21_71869000.minTemp = 24
    b_21_71869000.maxTemp = 24
    b_21_71869000.windSpeed = 6
    b_21_71869000.windDir = 6
    b_21_71869000.temp = 24
    b_21_71869000.skyCondition = 2800
    b_21_71869000.pop = 7

    key_21_71869000 = ('71869000.' + str(int(forecastTime_21_71869000)))
    wxdata.setData(key_21_71869000, 'hourlyFcst', b_21_71869000, int(forecastTime_21_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_21_71869000)))

for area in areaList:
    forecastTime_22_71869000 = 1764010800
    b_22_71869000 = twc.Data()
    b_22_71869000.minTemp = 25
    b_22_71869000.maxTemp = 25
    b_22_71869000.windSpeed = 6
    b_22_71869000.windDir = 7
    b_22_71869000.temp = 25
    b_22_71869000.skyCondition = 2800
    b_22_71869000.pop = 6

    key_22_71869000 = ('71869000.' + str(int(forecastTime_22_71869000)))
    wxdata.setData(key_22_71869000, 'hourlyFcst', b_22_71869000, int(forecastTime_22_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_22_71869000)))

for area in areaList:
    forecastTime_23_71869000 = 1764014400
    b_23_71869000 = twc.Data()
    b_23_71869000.minTemp = 26
    b_23_71869000.maxTemp = 26
    b_23_71869000.windSpeed = 6
    b_23_71869000.windDir = 6
    b_23_71869000.temp = 26
    b_23_71869000.skyCondition = 2800
    b_23_71869000.pop = 6

    key_23_71869000 = ('71869000.' + str(int(forecastTime_23_71869000)))
    wxdata.setData(key_23_71869000, 'hourlyFcst', b_23_71869000, int(forecastTime_23_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_23_71869000)))

for area in areaList:
    forecastTime_24_71869000 = 1764018000
    b_24_71869000 = twc.Data()
    b_24_71869000.minTemp = 26
    b_24_71869000.maxTemp = 26
    b_24_71869000.windSpeed = 6
    b_24_71869000.windDir = 6
    b_24_71869000.temp = 26
    b_24_71869000.skyCondition = 2800
    b_24_71869000.pop = 6

    key_24_71869000 = ('71869000.' + str(int(forecastTime_24_71869000)))
    wxdata.setData(key_24_71869000, 'hourlyFcst', b_24_71869000, int(forecastTime_24_71869000 + 3600))
    twccommon.Log.info("i1DG - Hourly forecast set for " + area + " at " + time.strftime('%Y-%m-%d %H:%M', time.localtime(forecastTime_24_71869000)))

