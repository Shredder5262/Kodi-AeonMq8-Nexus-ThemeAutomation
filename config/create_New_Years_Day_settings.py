#Save Settings to New Year's Day Directory
import shutil
import xbmc, xbmcgui,xbmcvfs
src = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/settings.xml')
dst = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/New_Years_Day/settings.xml')
shutil.copyfile(src, dst)
dialog = xbmcgui.Dialog()
dialog.ok("Task complete", "New Year's Day skin settings saved!")