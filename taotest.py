from pywinauto.application import Application
import pywinauto
from pywinauto import Desktop


# try:
#     export = pywinauto.findwindows.find_windows(
#         best_match="Hall 260    ver:1.0.0.47     Login:V3092552"
#     )
#     if export:
#         app = Application(backend="uia").connect(handle=export[0])
#         dialog = app.window(title="Hall 260    ver:1.0.0.47     Login:V3092552")
#         dialog.print_control_identifiers()
# except Exception as e:
#     print("error:", e)


# top_windows = Desktop(backend="uia").windows()
# for w in top_windows:
#     print(w.window_text())


export = pywinauto.findwindows.find_windows(
    best_match="Hall 260    ver:1.0.0.47     Login:V3092552"
)
if export:
    app = Application(backend="uia").connect(handle=export[0])
    dialog = app.window(title="Hall 260    ver:1.0.0.47     Login:V3092552")
    input = dialog.child_window(
        auto_id="MainWindow.centralwidget.groupBox_2.ruleresult"
    )
    txt = input.wrapper_object().window_text()
    print(txt)
