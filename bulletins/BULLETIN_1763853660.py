# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ755')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ755")
areaList = wxdata.getBulletinInterestList('PKZ755')
group = """"""
txt = """Coastal Waters Forecast for Southwest Alaska+Bristol Bay+The Alaska Peninsula Waters and the Aleutian Islands up to 100 nm out.  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent an average of the highest one-third of the combined wind wave and swell height.  .TONIGHT...NW wind 20 kt. Seas 8 ft. .SUN...E wind 15 kt becoming SE 30 kt in the afternoon. Seas 5 ft. .SUN NIGHT...E wind 35 kt. Seas 8 ft building to 13 ft after midnight. Rain. .MON...E wind 35 kt. Seas 14 ft. .MON NIGHT...SE wind 20 kt. Seas 14 ft. .TUE...SE wind 20 kt. Seas 12 ft. .WED...SE wind 15 kt. Seas 10 ft. .THU...SE wind 20 kt. Seas 12 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'GLW'
  b.pilExt = '001'
  b.issueTime = 1763853660
  b.dispExpiration = 1763900100
  b.group = group
  b.text = txt
  exp = 1763900100
  wxdata.setBulletin(area, b, exp)
