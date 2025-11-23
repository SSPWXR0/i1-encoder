# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ712')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ712")
areaList = wxdata.getBulletinInterestList('PKZ712')
group = """"""
txt = """Coastal Waters Forecast for the Northern Gulf of Alaska Coast up to 100 nm out including Kodiak Island and Cook Inlet.  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent an average of the highest one-third of the combined wind wave and swell height.  .TONIGHT...E wind 25 kt. Seas 9 ft. .SUN...E wind 25 kt. Seas 10 ft. .SUN NIGHT...NE wind 25 kt. Seas 8 ft. .MON AND MON NIGHT...E wind 20 kt. Seas 6 ft. .TUE...E wind 20 kt. Seas 7 ft. .WED THROUGH THU...SE wind 15 kt. Seas 9 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763857980
  b.dispExpiration = 1763902800
  b.group = group
  b.text = txt
  exp = 1763902800
  wxdata.setBulletin(area, b, exp)
