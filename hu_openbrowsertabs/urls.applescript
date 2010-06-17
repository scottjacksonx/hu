set urls to ""
tell application "Safari"
  set window_list to windows
  repeat with w in window_list
    try
      set tab_list to tabs of w
      repeat with t in tab_list
        set urls to urls & "<tab " & "title=\"" & name of t & "\" url=\"" & URL of t & "\" />\n"
      end repeat
    on error
      -- not all windows have tabs
    end try
  end repeat
get urls
end tell