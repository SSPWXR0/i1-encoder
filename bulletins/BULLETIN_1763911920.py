# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('TXZ054')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR TXZ054")
areaList = wxdata.getBulletinInterestList('TXZ054')
group = """"""
txt = """* WHAT...Flooding caused by excessive rainfall is possible.  * WHERE...A portion of west central Texas, including the following counties, Brown, Callahan, Coke, Coleman, Concho, Irion, Jones, Nolan, Runnels, Shackelford, Sterling, Taylor and Tom Green.  * WHEN...From 6 PM CST this evening through Monday morning.  * IMPACTS...Excessive runoff may result in flooding of rivers, creeks, streams, and other low-lying and flood-prone locations. Flooding may occur in poor drainage and urban areas. Low-water crossings may be flooded.  * ADDITIONAL DETAILS... - Showers and thunderstorms will increase in coverage from the Concho Valley, to portions of the Big Country and into the Heartland this evening and into the morning hours Monday. A corridor of heavy rain will develop with totals of 2 to 4 inches expected, and localized higher amounts possible. This will result in flooding, especially in low lying and urban areas. - http://www.weather.gov/safety/flood"""

for area in areaList:
  b = twc.Data()
  b.pil = 'FAA'
  b.pilExt = '001'
  b.issueTime = 1763911920
  b.dispExpiration = 1763992800
  b.group = group
  b.text = txt
  exp = 1763992800
  wxdata.setBulletin(area, b, exp)
