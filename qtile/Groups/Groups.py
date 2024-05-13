from libqtile.lazy import lazy
from libqtile.config import Group, Key
from Keys.Keys import keys, mod

__groups = { 1:Group(" 󰣇 "),2:Group("  "),3:Group(" 󰈙 "),4:Group("  "),5:Group("  "),6:Group("  "),7:Group("  "),8:Group("  "),9:Group("  ")}


groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
