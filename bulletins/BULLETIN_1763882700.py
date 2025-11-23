# ALERT
import time
import twccommon

areaList = wxdata.getBulletinInterestList('MTZ301')
if ('KABR' == 'KWNS'):
   abortMsg()
if (not areaList):
    abortMsg()

twccommon.Log.info("i1DT - SET BULLETIN FOR MTZ301")
areaList = wxdata.getBulletinInterestList('MTZ301')
group = """"""
txt = """* WHAT...Snow expected. Total snow accumulations of between 5 and 10 inches at Marias Pass, with up to 18 inches over the higher peaks of Glacier National Park. Winds gusting up to 60 mph.  * WHERE...East Glacier Park Region Zone.  * WHEN...From 11 PM Sunday to 11 PM MST Monday.  * IMPACTS...Tire chains may be required for some vehicles if traveling through mountain passes.  * ADDITIONAL DETAILS...The heaviest period of snow will fall from late Monday morning through early Monday evening. Areas of blowing snow will be possible, most notably during the afternoon hours on Monday."""

for area in areaList:
  b = twc.Data()
  b.pil = 'WWY'
  b.pilExt = '001'
  b.issueTime = 1763882700
  b.dispExpiration = 1763942400
  b.group = group
  b.text = txt
  exp = 1763942400
  wxdata.setBulletin(area, b, exp)
