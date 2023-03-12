#Change the Skin to Estuary so we can load the new MQ 8 settings
import xbmc, xbmcgui,xbmcvfs
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin","value":"skin.estuary"}}')
xbmc.sleep(200)
xbmc.executebuiltin('SendClick(11)')

#Copy the Standard settings
import shutil
src = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/Chicago_Bears/settings.xml')
dst = xbmcvfs.translatePath('special://home/userdata/addon_data/skin.aeonmq8.nexus.mod/settings.xml')
shutil.copyfile(src, dst)
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"lookandfeel.skin","value":"skin.aeonmq8.nexus.mod"}}')
xbmc.sleep(200)
xbmc.executebuiltin('SendClick(11)')
#dialog = xbmcgui.Dialog()
#dialog.ok("Skin settings update", "Standard skin settings loaded")