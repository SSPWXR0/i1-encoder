# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ663')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ663")
areaList = wxdata.getBulletinInterestList('PKZ663')
group = """"""
txt = """Southeast Alaska Coastal Waters from Dixon Entrance to Cape Suckling out 100 NM  Wind forecasts reflect the predominant speed and direction expected. Seas forecasts represent the average of the highest one-third of the combined windwave and swell height.  .TONIGHT...S wind 15 kt. Seas 12 ft. W swell. .SUN...S wind 20 kt. Seas 9 ft. W swell. .SUN NIGHT...S wind 15 kt. Seas 7 ft. W swell. .MON...S wind 10 kt. Seas 6 ft. .MON NIGHT...SE wind 25 kt. Seas 8 ft. Rain. .TUE...E wind 30 kt. Seas 11 ft. .WED...E wind 20 kt. Seas 10 ft. .THU...E wind 25 kt. Seas 7 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763857560
  b.dispExpiration = 1763922600
  b.group = group
  b.text = txt
  exp = 1763922600
  wxdata.setBulletin(area, b, exp)
