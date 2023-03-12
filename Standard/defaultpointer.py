import shutil
src = xbmc.translatePath('special://home/addons/skin.aeonmq8.nexus.mod/xml/Pointer.default.xml')
dst = xbmc.translatePath('special://home/addons/skin.aeonmq8.nexus.mod/xml/Pointer.xml')
shutil.copyfile(src, dst)
xbmc.sleep(700)
xbmc.executebuiltin('ReloadSkin()')