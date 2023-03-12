#Save Settings to Standard Directory
import shutil
import xbmc, xbmcgui,xbmcvfs
src = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/settings.xml')
dst = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Standard/settings.xml')
shutil.copyfile(src, dst)
dialog = xbmcgui.Dialog()
dialog.ok("Task complete", "Standard skin settings saved!")