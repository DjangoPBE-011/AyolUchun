# core/jazzmin_conf.py

JAZZMIN_SETTINGS = {
    "site_title": "Ayol Uchun Admin",
    "site_header": "Ayol Uchun",
    "site_brand": "AyolUchun",
    "welcome_sign": "Ayol Uchun boshqaruv paneliga xush kelibsiz",
    "copyright": "Ayol Uchun",

    "show_sidebar": True,
    "navigation_expanded": False,

    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    "order_with_respect_to": [
        "accounts",
        "accounts.CustomUser",
        "accounts.Interest",
        "accounts.UserInterest",
        "accounts.PromoCode",
        "courses",
        "courses.Category",
        "courses.Course",
        "courses.Module",
        "courses.Video",
        "courses.Comment",
        "courses.Sertificate",
        "auth",
        "token_blacklist",
    ],

    "icons": {
        "accounts": "fas fa-user-shield",
        "accounts.CustomUser": "fas fa-user",
        "accounts.Interest": "fas fa-heart",
        "accounts.UserInterest": "fas fa-hand-holding-heart",
        "accounts.PromoCode": "fas fa-tags",

        "courses": "fas fa-chalkboard-teacher",
        "courses.Category": "fas fa-layer-group",
        "courses.Course": "fas fa-graduation-cap",
        "courses.Module": "fas fa-book-open",
        "courses.Video": "fas fa-play-circle",
        "courses.Comment": "fas fa-comments",
        "courses.Sertificate": "fas fa-certificate",

        "auth": "fas fa-users-cog",
        "auth.Group": "fas fa-users",

        "token_blacklist": "fas fa-key",
        "token_blacklist.BlacklistedToken": "fas fa-ban",
        "token_blacklist.OutstandingToken": "fas fa-clock",
    },

    "language_chooser": True,
    "usermenu_links": [],
}