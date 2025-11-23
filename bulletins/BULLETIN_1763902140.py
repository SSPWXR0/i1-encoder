# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('PKZ644')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR PKZ644")
areaList = wxdata.getBulletinInterestList('PKZ644')
group = """"""
txt = """Southeast Alaska Coastal Waters from Dixon Entrance to Cape Suckling out 100 NM  Wind forecasts reflect the predominant speed and direction expected. Seas forecasts represent the average of the highest one-third of the combined windwave and swell height.  .TODAY...E wind 20 kt. Seas 10 ft. Rain showers early in the morning, then slight chance of thunderstorms. .TONIGHT...E wind 25 kt. Seas 9 ft. Slight chance of thunderstorms in the evening, then rain showers and snow showers late. .MON...E wind 15 kt. Seas 7 ft. Rain showers and slight chance of thunderstorms in the morning. Snow showers. .MON NIGHT...E wind 20 kt. Seas 6 ft. .TUE...E wind 20 kt. Seas 9 ft. .WED...E wind 20 kt. Seas 9 ft. .THU...E wind 25 kt. Seas 8 ft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763902140
  b.dispExpiration = 1763967600
  b.group = group
  b.text = txt
  exp = 1763967600
  wxdata.setBulletin(area, b, exp)
