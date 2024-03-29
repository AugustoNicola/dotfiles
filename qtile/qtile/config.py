# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copyright (c) 2021 Augusto Nicola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
import random
from datetime import datetime, timezone
import locale

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.widget import base
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy as lazy_cmd
from libqtile.utils import guess_terminal

locale.setlocale(locale.LC_TIME, "es_AR.utf8")

#* colors used throughout the layout
palette_colors = {
    "primary": [
        '#8A3B99',
        '#9F4AB0',
        '#A661B3',
        '#B58BBD',
        '#C59FCB',
        '#9130A5'
    ],
    "secondary": [
        '#74D092',
        '#41975E'
    ],
    "background": "#252525"
}

#? special keys
mod = "mod4"
alt = "mod1"

#? programs used
spawns = {
    "terminal": "alacritty",
    "web_browser": "firefox",
    "file_explorer": "xdg-open .",
    "github": "github-desktop",
    "music_player": "spotify",
    "spotify_cli": "bash /home/lambda/.config/qtile/spotify.sh",
    "ide": "code -n",
    "text_editor": "subl -n",
    "discord": "discord",
    "open_logs": "code /home/lambda/Logs/",
    "screenshot": "scrot '%F_%H:%M:%S.png' -q 100 -zp -e 'mv $f ~/Pictures/Screenshots/'",
    "screenshot_and_edit": "scrot '%F_%H:%M.png' -zp -e 'mv $f ~/Pictures/Screenshots/ && gimp ~/Pictures/Screenshots/$f'",
    "notes": "obsidian"
}

# ============================================================================
# ===========================    KEYBINDINGS     =============================
# ============================================================================
keys = [
    # ========== Move focus between windows ==========
    Key([mod], "Left", lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(),
        desc="Move window focus to next window"),

    # ========== Move windows in a group ==========
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Move window up"),

    # ========== Grow/shrink windows ==========
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    
    # ========== Window interactions ==========
    Key([mod], "w", lazy.window.kill(),
        desc="Kill focused window"),

    # ========== Move between groups ==========
    Key([mod], "Tab", lazy.screen.next_group(),
        desc="Go to next group"),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group(),
        desc="Go to next group"),

    # ========== Move between layouts ==========
    Key([mod], "space", lazy.next_layout(),
        desc="Toggle between layouts"),

    # ========== Spawns ==========
    Key([mod], "r", lazy.spawn("rofi -show run"),
        desc="Spawn rofi to run applications"),
    Key([mod], "x", lazy.spawncmd(),
        desc="Run a command using a prompt widget"),

    Key([mod], "t", lazy.spawn(spawns["terminal"]),
        desc="Launch default terminal"),
    Key([mod], "e", lazy.spawn(spawns["web_browser"]),
        desc="Launch default web browser"),
    Key([mod], "f", lazy.spawn(spawns["file_explorer"]),
        desc="Launch default file explorer"),
    Key([mod], "m", lazy.spawn(spawns["music_player"]),
        desc="Launch default music player"),
    Key([mod], "n", lazy.spawn(spawns["notes"]),
        desc="Launch note-taking app"),
    Key([mod], "c", lazy.spawn(spawns["ide"]),
        desc="Launch default IDE"),
    Key([mod], "s", lazy.spawn(spawns["text_editor"]),
        desc="Launch default text editor"),
    Key([mod], "d", lazy.spawn(spawns["discord"]),
        desc="Launch discord"),
    Key([mod], "l", lazy.spawn(spawns["open_logs"]),
        desc="Open Log Folder in VSCode"),
    Key([], "Print", lazy.spawn(spawns["screenshot"]),
        desc="Take a screenshot of the current view, mouse included"),
    Key([mod], "Print", lazy.spawn(spawns["screenshot_and_edit"]),
        desc="Take a screenshot of the current view, mouse included, and then open it in GIMP"),

    # ========== Spotify controls ==========
    Key([], "XF86AudioPlay", lazy.spawn(spawns["spotify_cli"] + " play"),
        desc="Play/pause spotify"),
    Key([], "XF86AudioPrev", lazy.spawn(spawns["spotify_cli"] + " prev"),
        desc="Rewind spotify"),
    Key([], "XF86AudioNext", lazy.spawn(spawns["spotify_cli"] + " next"),
        desc="Foward spotify"),

    # ========== Qtile interactions ==========
    Key([mod, "control"], "r", lazy.restart(),
        desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
]

# ============================================================================
# ===============================   GROUPS   =================================
# ============================================================================
if __name__ in ["config", "__main__"]:

	#? the strings used in the label attribute are unicode glyphs from the FontAwesome 5 font as well as the FiraCode Nerd Font
	#! the fonts are required for the icons to load 
    group_props = [
    #   ("name", {"arg": "val"}),
        ("HOME", {'label':'ﬦ'}),
        ("WEB", {'label':'', 'matches': [Match(wm_class=["Firefox"])]}),
        ("DEV", {'label':'', 'matches': [Match(wm_class=["Code", "Sublime_text"])]}),
        ("TER", {'label':'', 'matches': [Match(wm_class=["Alacritty"])]}),
        ("MUS", {'label':'', 'spawn': 'spotify'}),
        ("DIS", {'label':'', 'spawn': 'discord'}),
        ("CFG", {'label':'', 'matches': [Match(wm_class=["Pavucontrol"])]})
    ]
    groups = [Group(name, init=True, persist=True, **kwargs) for name, kwargs in group_props]

    for i, (name, kwargs) in enumerate(group_props, 1):
        keys.extend([
            # Switch to group
            Key([mod], str(i), lazy.group[name].toscreen(),
                desc="Switch to group {}".format(name)),

            # Move window to group
            Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(name)),
        ])

# ============================================================================
# =============================      LAYOUTS     =============================
# ============================================================================
layouts = [
    layout.Max(name = "fullscreen"),
    layout.Columns(
        name = "columns",
        border_focus = palette_colors["secondary"][0],
        border_width = 3,
        border_on_single = True,
        grow_amount = 10,
        fair = False,
        num_columns = 2,
        margin = 3
    )
    # layout.MonadTall(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
],
    border_focus = palette_colors["primary"][3],
    border_width = 3,
)
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
		start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
		start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# ============================================================================
# ========================    MOUSE CALLBACKS     ============================
# ============================================================================
def open_wifi_settings():
    qtile.cmd_spawn('nm-connection-editor')
    if qtile.current_group.name != "CFG": #* if we are already on the group, calling the method would revert to the last used group
        qtile.groups_map["CFG"].cmd_toscreen() #? see libqtile/core/manager.py -> method cmd_togroup()

def open_audio_settings():
    qtile.cmd_spawn('pavucontrol')
    if qtile.current_group.name != "CFG":
        qtile.groups_map["CFG"].cmd_toscreen()
        
def open_calendar():
    qtile.cmd_spawn("gnome-calendar")

def open_clock():
    qtile.cmd_spawn("gnome-clocks")

# ============================================================================
# ============================    WIDGETS     ================================
# ============================================================================
class TrayIcon(base._TextBox):
    
    defaults = [
        ("text", "X", "Actual icon that is displayed"),
        ("font", "JetBrains Mono Bold", "Font of the icon"),
        ("fontsize", 13.5, "Size of the icon"),
        ("background_color", "#000000", "Color of the widget's background"),
        ("foreground_color", "#FFFFFF", "Color of the widget's text")
    ]
    
    def __init__(self, text, font, fontsize, background_color, foreground_color, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, background=background_color, foreground=foreground_color, text=text, font=font, fontsize=fontsize, width=width, **config)
        self.add_defaults(TrayIcon.defaults)
    
    def mouse_enter(self, x, y):
        self.foreground = "#CACACA"
        self.draw()
    
    def mouse_leave(self, x, y):
        self.foreground = self.foreground_color
        self.draw()

class CustomCalendar(base.InLoopPollText):
    
    defaults = [
        ("update_interval", 1., "How many seconds between updates"),
        ("background_color", "#000000", "Color of the widget's background"),
        ("foreground_color", "#FFFFFF", "Color of the widget's text")
    ]
    
    def __init__(self, background_color, foreground_color, **config):
        base.InLoopPollText.__init__(self, background=background_color, foreground=foreground_color, **config)
        self.add_defaults(CustomCalendar.defaults)
        self.background_color = background_color
        self.foreground_color = foreground_color
    
    def tick(self):
        self.update(self.poll())
    
    def poll(self):
        # locale is set at the start of the config file in order to display the weekday in spanish
        return datetime.now().strftime("%Y/%m/%d %A").title()
        
    def mouse_enter(self, x, y):
        self.foreground = "#CACACA"
        self.draw()
    
    def mouse_leave(self, x, y):
        self.foreground = self.foreground_color
        self.draw()

class CustomClock(base.InLoopPollText):
    
    defaults = [
        ("update_interval", 1., "How many seconds between updates"),
        ("background_color", "#000000", "Color of the widget's background"),
        ("foreground_color", "#FFFFFF", "Color of the widget's text")
    ]
    
    def __init__(self, background_color, foreground_color, **config):
        base.InLoopPollText.__init__(self, background=background_color, foreground=foreground_color, **config)
        self.add_defaults(CustomCalendar.defaults)
        self.background_color = background_color
        self.foreground_color = foreground_color
    
    def tick(self):
        self.update(self.poll())
    
    def poll(self):
        # 12-hour padding doesn't seem to work with the spanish locale
        return datetime.now().strftime("%X")
        
    def mouse_enter(self, x, y):
        self.foreground = "#CACACA"
        self.draw()
    
    def mouse_leave(self, x, y):
        self.foreground = self.foreground_color
        self.draw()

# ============================================================================
# ============================    SCREENS     ================================
# ============================================================================
groupbox_defaults = dict(
    background = palette_colors["background"],
    
    highlight_method = 'block',
    
    active = '#FFFFFF',
    inactive = '#9b9b9b',
    urgent_alert_method = 'block',
    
    spacing = 5,
    padding = 12,
    margin_y = 2.5,
    rounded = False,
    use_mouse_wheel = False
)

primary_groupbox = dict(
    this_current_screen_border = palette_colors["primary"][5],
    this_screen_border = palette_colors["primary"][5],
    other_current_screen_border = palette_colors["secondary"][1],
    other_screen_border = palette_colors["secondary"][1]
)
secondary_groupbox = dict(
    this_current_screen_border = palette_colors["secondary"][1],
    this_screen_border = palette_colors["secondary"][1],
    other_current_screen_border = palette_colors["primary"][5],
    other_screen_border = palette_colors["primary"][5]
)

widget_defaults = dict(
    font='JetBrains Mono Bold',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# * Wallpaper random selection
n=0
random.seed();
for root, dirs, files in os.walk('/home/lambda/dotfiles/wallpapers/'):
    for name in files:
        n += 1
        if random.uniform(0, n) < 1:
            wallpaper=os.path.join(root, name)

screens = [
    Screen(
        bottom=bar.Bar(
            [
                # Group Bar(s)
                widget.GroupBox(
                    visible_groups = ["HOME"],
                    font = "FiraCode Nerd Font", #? using the font is vital for loading the icon
                    fontsize = 26,
                    **primary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["WEB"],
                    font = "Font Awesome 5 Free",
                    fontsize = 20,
                    **primary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["DEV", "TER"],
                    font = "Font Awesome 5 Free",
                    fontsize = 17,
                    **primary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["DIS", "MUS"],
                    font = "Font Awesome 5 Free",
                    fontsize = 20,
                    **primary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["CFG"],
                    font = "Font Awesome 5 Free",
                    fontsize = 18,
                    **primary_groupbox,
                    **groupbox_defaults
                ),
                # Command-running prompt
                widget.Prompt(
                    background = palette_colors["background"],
                    prompt = 'Run: ',
                    name = 'prompt'
                ),
                # Dynamic spacing
                widget.Spacer(background = palette_colors["background"]),
                # Window name
                widget.WindowName(
                    background = palette_colors["background"],
                    width = bar.CALCULATED,
                    max_chars = 100,
                    foreground = palette_colors["secondary"][0]
                ),
                # Dynamic spacing
                widget.Spacer(background = palette_colors["background"]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background = palette_colors["background"],
                    foreground = palette_colors["primary"][3]
                ),
                # Systray
                widget.Systray(
                    background = palette_colors["primary"][3],
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][3]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background = palette_colors["primary"][3],
                    foreground = palette_colors["primary"][2]
                ),
                # Internet Icon
                TrayIcon(
                    background_color = palette_colors["primary"][2],
                    foreground_color = "#FFFFFF",
                    text='',
                    font="Font Awesome 5 Free",
                    fontsize = 14.5,
                    mouse_callbacks = {'Button1': open_wifi_settings}
                ),
                # Spacing between Icons
                widget.Sep(linewidth = 0, padding = 5, background = palette_colors["primary"][2]),
                # Audio Icon
                TrayIcon(
                    background_color = palette_colors["primary"][2],
                    foreground_color = "#FFFFFF",
                    text='',
                    font="Font Awesome 5 Free",
                    fontsize = 14.5,
                    mouse_callbacks = {'Button1': open_audio_settings}
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][2]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background=palette_colors["primary"][2],
                    foreground=palette_colors["primary"][1]
                ),
                # Calendar Icon 
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 14,
                    background = palette_colors["primary"][1]
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 3, background=palette_colors["primary"][1]),
                # Date Widget
                CustomCalendar(background_color=palette_colors["primary"][1], foreground_color="#FFFFFF", mouse_callbacks = {'Button1': open_calendar}),
                #widget.Clock(
                #    format=f'%Y/%m/%d {weekDay}', #! embrace ISO 8601
                #    background=palette_colors["primary"][1],
                #),
                # Spacing
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][1]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background=palette_colors["primary"][1],
                    foreground=palette_colors["primary"][0]
                ),
                # Clock Icon
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 14,
                    background = palette_colors["primary"][0]
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 3, background=palette_colors["primary"][0]),
                # Time Widget
                CustomClock(background_color=palette_colors["primary"][0], foreground_color="#FFFFFF", mouse_callbacks = {'Button1': open_clock}),
                #widget.Clock(
                #    format='%H:%M',
                #    background=palette_colors["primary"][0],
                #),
                # Right border spacing
                widget.Sep(linewidth = 0, padding = 10, background = palette_colors["primary"][0])
            ],
            32,
        ),
        wallpaper=wallpaper,
        wallpaper_mode="fill"
    ),
    Screen(
        bottom=bar.Bar(
            [
                # Group Bar(s)
                widget.GroupBox(
                    visible_groups = ["HOME"],
                    font = "FiraCode Nerd Font", #? using the font is vital for loading the icon
                    fontsize = 26,
                    **secondary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["WEB"],
                    font = "Font Awesome 5 Free",
                    fontsize = 20,
                    **secondary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["DEV", "TER"],
                    font = "Font Awesome 5 Free",
                    fontsize = 17,
                    **secondary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["DIS", "MUS"],
                    font = "Font Awesome 5 Free",
                    fontsize = 20,
                    **secondary_groupbox,
                    **groupbox_defaults
                ),
                widget.GroupBox(
                    visible_groups = ["CFG"],
                    font = "Font Awesome 5 Free",
                    fontsize = 18,
                    **secondary_groupbox,
                    **groupbox_defaults
                ),
                # Command-running prompt
                widget.Prompt(
                    background = palette_colors["background"],
                    prompt = 'Run: ',
                    name = 'prompt'
                ),
                # Dynamic spacing
                widget.Spacer(background = palette_colors["background"]),
                # Window name
                widget.WindowName(
                    background = palette_colors["background"],
                    width = bar.CALCULATED,
                    max_chars = 100,
                    foreground = palette_colors["secondary"][0]
                ),
                # Dynamic spacing
                widget.Spacer(background = palette_colors["background"]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background = palette_colors["background"],
                    foreground = palette_colors["primary"][3]
                ),
                # Systray
                widget.Systray(
                    background = palette_colors["primary"][3],
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][3]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background = palette_colors["primary"][3],
                    foreground = palette_colors["primary"][2]
                ),
                # Internet Icon
                TrayIcon(
                    background_color = palette_colors["primary"][2],
                    foreground_color = "#FFFFFF",
                    text='',
                    font="Font Awesome 5 Free",
                    fontsize = 14.5,
                    mouse_callbacks = {'Button1': open_wifi_settings}
                ),
                # Spacing between Icons
                widget.Sep(linewidth = 0, padding = 5, background = palette_colors["primary"][2]),
                # Audio Icon
                TrayIcon(
                    background_color = palette_colors["primary"][2],
                    foreground_color = "#FFFFFF",
                    text='',
                    font="Font Awesome 5 Free",
                    fontsize = 14.5,
                    mouse_callbacks = {'Button1': open_audio_settings}
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][2]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background=palette_colors["primary"][2],
                    foreground=palette_colors["primary"][1]
                ),
                # Calendar Icon 
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 14,
                    background = palette_colors["primary"][1]
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 3, background=palette_colors["primary"][1]),
                # Date Widget
                CustomCalendar(background_color=palette_colors["primary"][1], foreground_color="#FFFFFF", mouse_callbacks = {'Button1': open_calendar}),
                #widget.Clock(
                #    format=f'%Y/%m/%d {weekDay}', #! embrace ISO 8601
                #    background=palette_colors["primary"][1],
                #),
                # Spacing
                widget.Sep(linewidth = 0, padding = 5, background=palette_colors["primary"][1]),
                # Powerline Arrow
                widget.TextBox(font='Font Awesome 5 Free', text='', padding=0, fontsize=64,
                    background=palette_colors["primary"][1],
                    foreground=palette_colors["primary"][0]
                ),
                # Clock Icon
                widget.TextBox(
                    font = 'Font Awesome 5 Free',
                    text = '',
                    fontsize = 14,
                    background = palette_colors["primary"][0]
                ),
                # Spacing
                widget.Sep(linewidth = 0, padding = 3, background=palette_colors["primary"][0]),
                # Time Widget
                CustomClock(background_color=palette_colors["primary"][0], foreground_color="#FFFFFF", mouse_callbacks = {'Button1': open_clock}),
                #widget.Clock(
                #    format='%H:%M',
                #    background=palette_colors["primary"][0],
                #),
                # Right border spacing
                widget.Sep(linewidth = 0, padding = 10, background = palette_colors["primary"][0])
            ],
            32,
        ),
        wallpaper=wallpaper,
        wallpaper_mode="fill"
    )
]

# ============================================================================
# =============================    SCRIPTS    ================================
# ============================================================================
@hook.subscribe.startup_once
def startup_once():
    script = os.path.expanduser('~/.config/qtile/startup_once.sh')
    subprocess.call([script])

@hook.subscribe.startup
def startup():
    script = os.path.expanduser('~/.config/qtile/startup.sh')
    subprocess.Popen([script])

# ============================================================================
# =============================    CONFIGS    ================================
# ============================================================================
auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_app_rules = []  # type: List
dgroups_key_binder = None
focus_on_window_activation = "smart"
follow_mouse_focus = False
main = None  # WARNING: this is deprecated and will be removed soon
wmname = "qtile" #! window manager name, e.g. used in neofetch // if having trouble with java, change to "LG3D"
