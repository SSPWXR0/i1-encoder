# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('ANZ232')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR ANZ232")
areaList = wxdata.getBulletinInterestList('ANZ232')
group = """"""
txt = """* WHAT...Northwest winds 10 to 20 kt with gusts up to 25 kt and seas 2 to 3 feet expected.  * WHERE...In Massachusetts coastal waters, Nantucket Sound, Vineyard Sound and Buzzards Bay. In Rhode Island coastal waters, Rhode Island Sound and Block Island Sound.  * WHEN...From midnight tonight to 1 PM EST Monday.  * IMPACTS...Conditions will be hazardous to small craft."""

for area in areaList:
  b = twc.Data()
  b.pil = 'SCY'
  b.pilExt = '001'
  b.issueTime = 1763919300
  b.dispExpiration = 1763985600
  b.group = group
  b.text = txt
  exp = 1763985600
  wxdata.setBulletin(area, b, exp)
