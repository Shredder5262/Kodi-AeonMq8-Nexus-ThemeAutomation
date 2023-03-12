#Save Settings to Thanksgiving Directory
import shutil,xbmcvfs
src = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/settings.xml')
dst = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Thanksgiving/settings.xml')
shutil.copyfile(src, dst)