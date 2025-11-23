# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ761')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ761")
areaList = wxdata.getBulletinInterestList('PKZ761')
group = """"""
txt = """Coastal Waters Forecast for Southwest Alaska+Bristol Bay+The Alaska Peninsula Waters and the Aleutian Islands up to 100 nm out.  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent an average of the highest one-third of the combined wind wave and swell height.  .TODAY...NE wind 15 kt. Seas 4 ft. Freezing spray. .TONIGHT...E wind 10 kt increasing to 15 kt after midnight. Seas 3 ft. .MON...E wind 25 kt. Seas 4 ft. .MON NIGHT...E wind 35 kt. Seas 7 ft. .TUE...E wind 30 kt. Seas 5 ft. .WED THROUGH THU...E wind 25 kt. Seas 5 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763901360
  b.dispExpiration = 1763949600
  b.group = group
  b.text = txt
  exp = 1763949600
  wxdata.setBulletin(area, b, exp)
