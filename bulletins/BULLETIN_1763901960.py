# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ807')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ807")
areaList = wxdata.getBulletinInterestList('PKZ807')
group = """"""
txt = """Northwestern Alaska Coastal Waters out 100 NM  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent the average of the highest one- third of the combined wind-wave and swell height.  .TODAY...N winds 20 kt. Seas 4 ft subsiding. Heavy freezing spray. .TONIGHT...NE winds 15 kt. Seas 3 ft. Freezing spray. .MON...E winds 15 kt. Seas 3 ft. Heavy freezing spray. .MON NIGHT...E winds 20 kt. Seas 4 ft. Heavy freezing spray. .TUE...E winds 20 kt. Seas 4 ft. Heavy freezing spray. .TUE NIGHT...E winds 20 kt. Seas 5 ft. Heavy freezing spray. .WED...E winds 25 kt. Seas 5 ft. .THU...E winds 20 kt. Seas 4 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'UPW'
  b.pilExt = '001'
  b.issueTime = 1763901960
  b.dispExpiration = 1763953200
  b.group = group
  b.text = txt
  exp = 1763953200
  wxdata.setBulletin(area, b, exp)
