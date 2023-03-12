#Save Settings to Independence Day Directory
import shutil,xbmcvfs
src = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/settings.xml')
dst = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Independence/settings.xml')
shutil.copyfile(src, dst)