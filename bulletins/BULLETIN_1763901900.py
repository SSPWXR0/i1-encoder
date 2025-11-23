# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ711')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ711")
areaList = wxdata.getBulletinInterestList('PKZ711')
group = """"""
txt = """Coastal Waters Forecast for the Northern Gulf of Alaska Coast up to 100 nm out including Kodiak Island and Cook Inlet.  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent an average of the highest one-third of the combined wind wave and swell height.  .TODAY...NE wind 20 kt. Seas 8 ft. .TONIGHT...NE wind 15 kt. Seas 6 ft. .MON...E wind 15 kt. Seas 5 ft. .MON NIGHT...NE wind 15 kt. Seas 5 ft. .TUE THROUGH THU...SE wind 20 kt. Seas 6 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763901900
  b.dispExpiration = 1763946900
  b.group = group
  b.text = txt
  exp = 1763946900
  wxdata.setBulletin(area, b, exp)
