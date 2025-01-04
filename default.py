import os
import shutil
import xbmc
import xbmcgui
from xbmcvfs import translatePath

def clear_cache():
    try:
        # Resolve the cache path
        cache_path = translatePath("special://cache/")
        xbmc.log(f"Resolved cache path: {cache_path}", level=xbmc.LOGDEBUG)

        # Verify path existence
        if not os.path.exists(cache_path):
            xbmcgui.Dialog().ok("Error", f"Cache path not found: {cache_path}")
            return

        # Confirm action with the user
        dialog = xbmcgui.Dialog()
        if dialog.yesno(
            "Clear Cache",
            f"This will erase all data in:\n{cache_path}\nDo you want to continue?",
        ):
            # Delete cache contents
            for item in os.listdir(cache_path):
                item_path = os.path.join(cache_path, item)
                xbmc.log(f"Attempting to delete: {item_path}", level=xbmc.LOGDEBUG)
                try:
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                except Exception as e:
                    xbmc.log(f"Failed to delete {item_path}: {str(e)}", level=xbmc.LOGERROR)

            xbmcgui.Dialog().ok("Success", "Cache has been cleared.")
        else:
            xbmcgui.Dialog().ok("Canceled", "No changes were made.")
    except Exception as e:
        xbmcgui.Dialog().ok("Error", f"An error occurred: {str(e)}")
        xbmc.log(f"Critical Error: {str(e)}", level=xbmc.LOGERROR)

if __name__ == "__main__":
    clear_cache()
