import shutil,xbmcvfs
src = xbmcvfs.translatePath('special://home/addons/skin.aeonmq8.nexus.mod/xml/Pointer.batman.xml')
dst = xbmcvfs.translatePath('special://home/addons/skin.aeonmq8.nexus.mod/xml/Pointer.xml')
shutil.copyfile(src, dst)
xbmc.sleep(700)
xbmc.executebuiltin('ReloadSkin()')