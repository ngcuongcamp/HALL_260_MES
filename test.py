import pywinauto
from pywinauto import Application, Desktop


# top_windows = Desktop(backend="uia").windows()
# for w in top_windows:
#     print(w.window_text())


# try:
#     export = pywinauto.findwindows.find_windows(
#         best_match="Hall 260    ver:1.0.0.47     Login:V3092552"
#     )
#     if export:
#         app = Application(backend="uia").connect(handle=export[0])
#         dialog = app.window(title="Hall 260    ver:1.0.0.47     Login:V3092552")

#         txtpackqty_element = dialog.child_window(
#             auto_id="MainWindow.centralwidget.groupBox_2.txtpackqty"
#         )
#         dialog.print_control_identifiers()
#     #   print(txtpackqty_element.rectangle().left)
# except Exception as e:
#     print("error:", e)


def get_name_mes_app():
    try:
        top_windows = Desktop(backend="uia").windows()
        is_found = False
        for w in top_windows:
            if (
                "login:" in w.window_text().lower()
                and "ver:" in w.window_text().lower()
            ):
                MES_APP_NAME = w.window_text()
                is_found = True

                break

        if is_found:
            export = pywinauto.findwindows.find_windows(best_match=MES_APP_NAME)
            if export:
                app = Application(backend="uia").connect(handle=export[0])
                dialog = app.window(title=MES_APP_NAME)
                print(dialog.print_control_identifiers())
                txtSN_element = dialog.child_window(
                    # auto_id="MainWindow.centralwidget.groupBox_2.txtpackqty"
                    auto_id="MainWindow.centralwidget.groupBox_2.ruleresult"
                )
                MES_SN_INPUT_POSITION = txtSN_element.rectangle()
                # print(MES_SN_INPUT_POSITION)

        if not is_found:
            print("Can't connect with MES APP")
    except Exception as E:
        print(E)


get_name_mes_app()
