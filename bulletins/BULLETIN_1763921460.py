# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('IDZ006')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR IDZ006")
areaList = wxdata.getBulletinInterestList('IDZ006')
group = """"""
txt = """* WHAT...Snow expected. There is a likelihood of minor to moderate winter weather impacts. Total snow accumulations up to 2 inches in the valleys and 2 to 6 inches in the higher terrain including Lolo and Lost Trail passes. Winds gusting as high as 35 mph.  * WHERE...Highway 93 Sula to Lost Trail Pass, Highway 12 Powell to Lolo Pass, Lolo Pass, and Dixie.  * WHEN...From 11 PM MST /10 PM PST/ this evening to noon MST /11 AM PST/ Monday.  * IMPACTS...For MODERATE winter weather impacts, expect disruptions to normal activities. Hazardous traveling conditions. Use extra caution while driving. Closures and disruptions to infrastructure may occur. The hazardous conditions could impact the Monday morning commute, especially over higher passes."""

for area in areaList:
  b = twc.Data()
  b.pil = 'WWY'
  b.pilExt = '001'
  b.issueTime = 1763921460
  b.dispExpiration = 1764008100
  b.group = group
  b.text = txt
  exp = 1764008100
  wxdata.setBulletin(area, b, exp)
