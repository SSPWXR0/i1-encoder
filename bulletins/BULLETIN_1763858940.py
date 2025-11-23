# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ853')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ853")
areaList = wxdata.getBulletinInterestList('PKZ853')
group = """"""
txt = """Northwestern Alaska Coastal Waters out 100 NM  Wind forecasts reflect the predominant speed and direction expected. Sea forecasts represent the average of the highest one- third of the combined wind-wave and swell height.  .TONIGHT...N winds 25 kt. Seas 7 ft. Heavy freezing spray. .SUN...N winds 20 kt. Seas 5 ft. Heavy freezing spray. .SUN NIGHT...E winds 20 kt. Seas 4 ft. Heavy freezing spray. .MON...E winds 20 kt. Seas 5 ft. Heavy freezing spray. .MON NIGHT...E winds 25 kt. Seas 6 ft. Heavy freezing spray. .TUE...E winds 25 kt. Seas 7 ft. Heavy freezing spray. .TUE NIGHT...E winds 25 kt. Seas 7 ft. Heavy freezing spray. .WED...E winds 25 kt. Seas 9 ft. .THU...E winds 20 kt. Seas 7 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'UPW'
  b.pilExt = '001'
  b.issueTime = 1763858940
  b.dispExpiration = 1763910000
  b.group = group
  b.text = txt
  exp = 1763910000
  wxdata.setBulletin(area, b, exp)
