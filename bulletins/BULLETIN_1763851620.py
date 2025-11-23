# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('AKZ832')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR AKZ832")
areaList = wxdata.getBulletinInterestList('AKZ832')
group = """"""
txt = """Snow showers continue across much the central and eastern Interior. While most of the snowfall over the past 24 hours has been mainly light with accumulations of 2 to 3 inches, a few additional quick bursts of snow will remain possible through the rest of the day Saturday. In general an additional 1 to 2 inches of snowfall will be possible through tonight.  The overall band of snowfall will slowly shift east and southeast tonight through early Sunday. While a few additional light snow showers will be possible prior to noon Sunday, any additional snow accumulations for Sunday will be negligible.  Colder and drier conditions will begin to filter in Sunday with below normal conditions expected for much of next week."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SPS'
  b.pilExt = '001'
  b.issueTime = 1763851620
  b.dispExpiration = 1763931600
  b.group = group
  b.text = txt
  exp = 1763931600
  wxdata.setBulletin(area, b, exp)
