import os
import shutil
import xbmc
import xbmcgui
from xbmcvfs import translatePath

def clear_cache():
    try:
        # Resolve the cache path
        cache_path = translatePath("special://cache/")
        xbmc.log(f"[Clear Cache] Resolved cache path: {cache_path}", level=xbmc.LOGDEBUG)

        # Verify path existence
        if not os.path.exists(cache_path):
            xbmcgui.Dialog().ok("Error", "Cache path not found. Operation aborted.")
            xbmc.log(f"[Clear Cache] Cache path not found: {cache_path}", level=xbmc.LOGERROR)
            return

        # Confirm action with the user
        dialog = xbmcgui.Dialog()
        if not dialog.yesno(
            "Clear Cache",
            f"This will delete all files in the cache directory:\n\n{cache_path}\n\nDo you want to continue?",
        ):
            xbmcgui.Dialog().ok("Canceled", "No changes were made.")
            return

        # Delete cache contents
        for item in os.listdir(cache_path):
            item_path = os.path.join(cache_path, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                xbmc.log(f"[Clear Cache] Deleted: {item_path}", level=xbmc.LOGDEBUG)
            except Exception as e:
                xbmc.log(f"[Clear Cache] Failed to delete {item_path}: {str(e)}", level=xbmc.LOGERROR)

        xbmcgui.Dialog().ok("Success", "Cache has been cleared successfully.")
        xbmc.log("[Clear Cache] Cache cleared successfully.", level=xbmc.LOGINFO)

    except Exception as e:
        xbmcgui.Dialog().ok("Error", f"An error occurred while clearing the cache: {str(e)}")
        xbmc.log(f"[Clear Cache] Critical Error: {str(e)}", level=xbmc.LOGERROR)

if __name__ == "__main__":
    clear_cache()
