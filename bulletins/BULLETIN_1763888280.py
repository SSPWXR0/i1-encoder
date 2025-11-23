# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('LHZ422')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR LHZ422")
areaList = wxdata.getBulletinInterestList('LHZ422')
group = """"""
txt = """* WHAT...Expect sustained winds up to 20 knots from the west with gusts up to 30 knots. The largest significant waves will be 3 feet with a potential maximum wave height of 5 feet.  * WHERE...Inner Saginaw Bay SW of Point Au Gres to Bay Port MI, Harbor Beach to Port Sanilac MI and Port Sanilac to Port Huron MI.  * WHEN...The maximum winds are expected around 12 PM EST Sunday with the largest waves expected around 2 PM EST Sunday.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763888280
  b.dispExpiration = 1763931600
  b.group = group
  b.text = txt
  exp = 1763931600
  wxdata.setBulletin(area, b, exp)
