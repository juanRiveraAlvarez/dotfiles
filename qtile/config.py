from Keys.Keys import keys, mod, terminal
from Groups.Groups import groups
from Layouts.layouts import layouts, floating_layout
from Widgets.Widgets import extension_defaults, screens, widget_defaults
from Mouse.Mouse import mouse
import Autostart.autostart


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None


