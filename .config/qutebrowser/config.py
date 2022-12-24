
config.load_autoconfig(True)

c.completion.shrink=True

c.auto_save.session=True

c.content.autoplay = False

c.tabs.show = 'always'

c.backend = 'webengine'


c.url.default_page = 'https://www.google.com/'
c.url.start_pages = 'https://www.google.com/'

config.bind("L", "tab-next")
config.bind("H", "tab-prev")

config.bind("<shift+right>", "tab-next")
config.bind("<shift+left>", "tab-prev")

config.bind("<ctrl+right>","tab-move +")
config.bind("<ctrl+left>","tab-move -")

config.bind("J","back")
config.bind("K","forward")
config.bind("<ctrl+u>", "back")
config.bind("<ctrl+z>", "forward")
config.bind("<u>", "back")
config.bind("<z>", "forward")
config.bind("<shift+u>","undo")
config.bind("m","search-prev")
config.bind("<shift+n>","tab-clone")




c.url.searchengines = {
    'DEFAULT':  'https://google.com/search?hl=en&q={}'
    }

config.bind("0", "set-cmd-text :open -t ")
config.bind("<ctrl+f>","set-cmd-text /")
config.bind("<ctrl+a>","mode-enter caret ;; selection-toggle ;; move-to-end-of-document")

config.bind("g","set-cmd-text :tab-select ")



config.bind("<ctrl+v>","unbinded")

# Spellcheck
config.set('spellcheck.languages', ["en-US" ])


#status bar
c.statusbar.widgets=["url","scroll","progress"]

c.statusbar.padding["top"]=1

c.colors.statusbar.normal.bg="#434343"

c.colors.statusbar.normal.fg="white"

#c.colors.statusbar.normal.url.fg="red"

c.fonts.statusbar="monospace"


#hints 

c.hints.border='1px solid skyblue'

c.colors.hints.bg='#383560'

c.colors.hints.match.fg='#FF9C9C'

c.colors.hints.fg='Azure'

c.fonts.hints='bold 13px default_family'

c.hints.padding={"bottom": 3, "left": 5, "right": 5, "top": 3}


#Adblock


c.content.blocking.adblock.lists = [ \
        "https://easylist.to/easylist/easylist.txt", \
        "https://easylist.to/easylist/easyprivacy.txt", \
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt", \
        "https://easylist.to/easylist/fanboy-annoyance.txt", \
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt", \
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt" \
        ]

c.content.blocking.enabled = True
c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']
c.content.blocking.method = 'both'



# theme

c.colors.tabs.even.bg="#434343"

c.colors.tabs.even.fg="white"

c.colors.tabs.odd.bg="#434343"

c.colors.tabs.odd.fg="white"



#right clicked 

c.colors.contextmenu.menu.bg="#474747"

c.colors.contextmenu.menu.fg="Snow"

c.colors.contextmenu.selected.bg="#636363"


#tabs

c.colors.tabs.selected.even.bg="skyblue"

c.colors.tabs.selected.even.fg="black"

c.colors.tabs.selected.odd.bg="skyblue"

c.colors.tabs.selected.odd.fg="black"

c.tabs.max_width = 150

# darkmode
c.colors.webpage.bg = "#434343"

#completion
c.completion.show="always"
c.colors.completion.fg=["white","white","white"]
c.colors.completion.match.fg="#ff9999"
c.colors.completion.item.selected.match.fg="#ff9999"



c.colors.completion.even.bg="#1a1a1a"
c.colors.completion.odd.bg="#1a1a1a"

c.colors.completion.item.selected.bg="#262626"
c.colors.completion.item.selected.fg="white"

c.colors.completion.item.selected.border.top="transparent"
c.colors.completion.item.selected.border.bottom="transparent"


c.tabs.padding["top"] = 6
c.tabs.padding["bottom"] = 6
