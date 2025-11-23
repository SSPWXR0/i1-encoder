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
txt = """Offshore Waters Forecast for the Bering Sea  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent an average of the highest one-third of the combined wind wave and swell height.  .TODAY...E wind 35 to 50 kt diminishing to 30 to 40 kt in the afternoon. Seas 12 to 20 ft. .TONIGHT...E wind 30 to 40 kt. Seas 13 to 19 ft. Rain. .MON...NE wind 20 to 35 kt. Seas 12 to 19 ft. Rain showers. .MON NIGHT...E wind 15 to 30 kt. Seas 9 to 17 ft. .TUE...NE wind up to 20 kt. Seas 7 to 12 ft. .WED THROUGH THU...N wind up to 20 kt. Seas 4 to 9 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SRW'
  b.pilExt = '001'
  b.issueTime = 1763900820
  b.dispExpiration = 1763952300
  b.group = group
  b.text = txt
  exp = 1763952300
  wxdata.setBulletin(area, b, exp)
