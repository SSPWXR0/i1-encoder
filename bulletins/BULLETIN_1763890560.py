# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('ORZ021')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR ORZ021")
areaList = wxdata.getBulletinInterestList('ORZ021')
group = """"""
txt = """* WHAT...Increased risk of sneaker waves expected.  * WHERE...Beaches of Douglas, Coos and Curry counties.  * WHEN...Through this evening.  * IMPACTS...Sneaker waves can run up significantly farther on beaches than normal, including over rocks and jetties. These waves can suddenly knock people off of their feet and sweep them into the ocean. The waves can also move logs or other objects which could crush or trap anyone caught underneath.  * ADDITIONAL DETAILS...While sneaker waves can occur at any time, the greatest risk is on an incoming tide. Please be aware of the tides if venturing out onto the beaches today.  * View the hazard area in detail at https://www.wrh.noaa.gov/map/?wfo=mfr"""

for area in areaList:
  b = twc.Data()
  b.pil = 'BHS'
  b.pilExt = '001'
  b.issueTime = 1763890560
  b.dispExpiration = 1763964000
  b.group = group
  b.text = txt
  exp = 1763964000
  wxdata.setBulletin(area, b, exp)
