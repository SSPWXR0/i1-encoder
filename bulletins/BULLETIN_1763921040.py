# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('ANZ331')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR ANZ331")
areaList = wxdata.getBulletinInterestList('ANZ331')
group = """"""
txt = """* WHAT...Northwest winds 10 to 20 kt with gusts up to 25 kt.  * WHERE...Long Island Sound from Port Jefferson and New Haven east to Orient Point and the Connecticut River, and Peconic and Gardiners Bays.  * WHEN...From 10 PM this evening to 2 PM EST Monday.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763921040
  b.dispExpiration = 1763978400
  b.group = group
  b.text = txt
  exp = 1763978400
  wxdata.setBulletin(area, b, exp)
