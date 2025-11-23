# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ413')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ413")
areaList = wxdata.getBulletinInterestList('PKZ413')
group = """"""
txt = """Offshore Waters Forecast for the Bering Sea  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent an average of the highest one-third of the combined wind wave and swell height.  .TODAY...SE wind 10 to 25 kt increasing to 20 to 35 kt in the afternoon. Seas 6 to 10 ft. .TONIGHT...E wind 30 to 45 kt. Seas 9 to 17 ft. Rain. .SUN...E wind 30 to 45 kt. Seas 12 to 20 ft. Rain. .SUN NIGHT...NE wind 40 kt. Seas 13 to 18 ft. .MON THROUGH WED...NE wind 20 to 35 kt. Seas 9 to 17 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'GLW'
  b.pilExt = '001'
  b.issueTime = 1763814900
  b.dispExpiration = 1763864100
  b.group = group
  b.text = txt
  exp = 1763864100
  wxdata.setBulletin(area, b, exp)
