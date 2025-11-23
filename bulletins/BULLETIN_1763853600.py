# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ412')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ412")
areaList = wxdata.getBulletinInterestList('PKZ412')
group = """"""
txt = """Offshore Waters Forecast for the Bering Sea  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent an average of the highest one-third of the combined wind wave and swell height.  .TONIGHT...E wind 20 to 35 kt. Seas 6 to 11 ft. .SUN...E wind 20 to 35 kt. Seas 8 to 13 ft. .SUN NIGHT...E wind 25 to 35 kt. Seas 9 to 16 ft. .MON...NE wind 35 kt. Seas 11 to 15 ft. .MON NIGHT...NE wind 20 to 30 kt. Seas 10 to 16 ft. .TUE THROUGH THU...NE wind 15 to 30 kt. Seas 8 to 13 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'GLW'
  b.pilExt = '001'
  b.issueTime = 1763853600
  b.dispExpiration = 1763907300
  b.group = group
  b.text = txt
  exp = 1763907300
  wxdata.setBulletin(area, b, exp)
