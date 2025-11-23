# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('CAZ006')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR CAZ006")
areaList = wxdata.getBulletinInterestList('CAZ006')
group = """"""
txt = """* WHAT...A long period northwesterly swell will result in an increased risk for sneaker waves and rip currents. Breaking waves of 13 to 18 feet are expected.  * WHERE...Pacific Coast beaches.  * WHEN...Now through 10 PM Monday night.  * IMPACTS...Sneaker waves can unexpectedly run significantly farther up the beach than normal, including over rocks and jetties. Rip currents are typically more frequent and stronger in the vicinity of jetties, inlets, and piers."""

for area in areaList:
  b = twc.Data()
  b.pil = 'BHS'
  b.pilExt = '001'
  b.issueTime = 1763900040
  b.dispExpiration = 1763938800
  b.group = group
  b.text = txt
  exp = 1763938800
  wxdata.setBulletin(area, b, exp)
