#Create Backup Direcotry
import xbmcvfs
import xbmc, xbmcgui
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Standard')
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/New_Years_Day')
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Valentines_Day')
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Independence_Day')
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Halloween')
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Thanksgiving')
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Christmas')
xbmcvfs.mkdir('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Batman')
dialog = xbmcgui.Dialog()
dialog.ok("Task complete", "Skin settings folders created!")
