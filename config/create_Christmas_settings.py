#Save Settings to Christmas Directory
import shutil
import xbmc, xbmcgui,xbmcvfs
src = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/settings.xml')
dst = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Christmas/settings.xml')
shutil.copyfile(src, dst)
dialog = xbmcgui.Dialog()
dialog.ok("Task complete", "Christmas skin settings saved!")