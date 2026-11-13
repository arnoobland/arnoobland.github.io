"""The website's words in every language (see pages.py).

English is the original; the other languages were translated from it with
the help of AI, using the same words as the game's own translations.
"""

# The order of the language links: as in the game's picker.
LANGS = ["ar", "zh", "en", "fr", "de", "ja", "ru", "es"]

T = {}

# ---------------------------------------------------------------- English

T["en"] = {
    "name": "English",
    "langlabel": "Languages",
    "desc": "Arnoob Land: a calm nature game for children. Help a little bunny make a garden home again, befriend 80 animals through the seasons, run a little farm, and save up for the golden crown.",
    "og": "A calm nature game for children: befriend animals through the seasons, run a little farm, and learn to count and save.",
    "logoalt": "The Arnoob Land bunny wearing a golden crown",
    "tagline": "A calm nature game for children",
    "banneralt": "A crowned bunny in a spring garden with flowers, a duck pond and the title Arnoob Land",
    "intro": "A quiet garden needs your help. A little bunny wants to make it a home again, one seed at a time. Plant flowers, build a pond, set out treats and watch who comes to visit. Every season brings new animal friends: bees and ducks in spring, turtles and hummingbirds in summer, foxes and badgers in autumn, snowy owls and otters in winter.",
    "features": [
        ("Calm and gentle:", "no timers, no score to lose, nothing to fail."),
        ("Only nature sounds:", "wind, water, rain, birds and animal calls. No music."),
        ("Four seasons and 80 animals", "to befriend, with golden animals and rare moments to discover."),
        ("Watch the moon:", "night after night it changes from new moon to full moon and back, and owls love full-moon nights."),
        ("Take photos", "of your animal friends for your album: every photo earns a coin."),
        ("Learn to care for friends:", "notice what each animal needs and build it a home (a pond, a log pile, a berry bush...) so new friends come sooner, grant their wishes, help two friends play together, give a friend a flower, and watch friendships grow."),
        ("Run a little farm:", "feed the hens, keep bees and a goat, pick apples, berries and flowers, and sell them at your busy market stall to the friends who come to buy. Things you bought sell back for half their price, but not the pond, plants, seeds or trees."),
        ("Be a garden helper:", "pull weeds, rake leaves and clear snow for the compost heap, which brings an extra harvest and a faster farm, and water the flowers and fruit trees. Every job done raises your Garden helper level."),
        ("Bake and fill orders:", "turn eggs, milk, honey, apples and berries into cakes, pies, tarts and jam that sell for more, and add up the bill when a friend brings a little order."),
        ("Count as you play:", "every egg collected or sold, and every coin earned or spent, shows as a simple sum, like 3 + 2 = 5."),
        ("Learn to save:", "put coins in your savings jar, watch it grow a little each day, and save up for the golden crown."),
        ("Build the golden crown piece by piece:", "saving fills it with gold, and friends bring its three gems."),
        ("A calm game in every season:", "fishing (the fish swim free again), gathering fireflies (they fly free), the autumn harvest of nuts and apples, and building a snow fort."),
        ("Hide-and-seek with friends:", "from your fifth friend, friends hide around the garden and play together, and once you have found them all, golden friends visit more often."),
        ("Eight languages:", "English, Arabic, Chinese (Simplified), French, German, Japanese, Russian and Spanish. The game starts in your phone's language (English for any other), and the globe on the title screen changes it. The game was written in English; the other seven languages were translated with the help of AI."),
        ("A long, gentle journey:", "play the whole year over many days, or a shorter game in one season. Your garden is saved as you go."),
        ("A dream garden, if you like:", "save for a swing, a little bridge, a fountain, a treehouse and more. Your friends use them, and four secret friends may come to see them."),
    ],
    "shotstitle": "In the garden",
    "shotalts": [
        "The garden: the market stall with friends coming to buy, the hen house, the beehive and the goat",
        "Your goods: eggs, honey, apples and more, with a sum like 2 + 2 = 4",
        "The oven: honey cakes, apple pies, berry tarts and berry and apple jam, each worth more than what goes in",
        "The savings jar, saving up for the golden crown",
    ],
    "parentstitle": "For parents",
    "parents": "No accounts, no chat and no purchases. Videos play only when the player chooses to watch one, for a small in-game gift: a basket of goods to sell, a few coins, a surprise for the garden, seeds or treats.",
    "privacy": "Privacy Policy",
    "ainote": "",
    "policy": {
        "title": "Arnoob Land - Privacy Policy",
        "h1": "Privacy Policy – Arnoob Land",
        "note": "",
        "seemore": "For more information, see",
        "googlepolicy": "Google's Privacy Policy",
        "googlelink": "Google Privacy Policy",
        "contact": ["Developer:", "App:", "Package:", "Email:"],
        "sections": [
            ("1. Introduction",
             "Arnoob Land is a calm nature game for children, in which a little bunny befriends animals through the seasons, developed by Mohamed Abdelrahman. This policy explains how information is handled when you use the app.",
             "The game is intended for users of all ages, including children."),
            ("2. Information We Collect",
             "Arnoob Land does not require users to create an account or provide their name, email address, phone number, or other personal information directly. The game has no chat and no in-app purchases.",
             "Your garden and game progress are saved only on your device. They are never sent to us, and they are deleted when the app is uninstalled, or with Reset on the game's title screen.",
             "The app uses Google Mobile Ads SDK (AdMob) to display optional rewarded video advertisements. Through this service, information may be collected and shared automatically, including:",
             ["IP address, which may be used to estimate approximate location.",
              "App interactions, such as app launches, taps, and video ad views.",
              "Diagnostic information about app and SDK performance.",
              "Device or other identifiers used for advertising and measurement."],
             "The app does not request precise GPS location."),
            ("3. Advertising",
             "Arnoob Land uses Google AdMob to provide rewarded video ads. Ads play only when the player taps a button to watch one, to receive an in-game reward. There are no other ads.",
             "The app configures ad requests for child-directed treatment and sets the maximum ad content rating to G.",
             "Google may process information to provide advertisements, measure ad performance, analyze interactions, and help prevent fraud and maintain security.",
             "@more"),
            ("4. Children's Privacy",
             "Arnoob Land is designed for users of all ages, including children under 13.",
             "The app does not require children to create accounts or submit personal information directly. Advertising requests are configured for child-directed treatment.",
             "Parents or guardians can contact the developer with privacy-related questions or concerns."),
            ("5. Data Sharing",
             "The app does not sell users' personal information. Information collected through Google AdMob may be shared with Google for advertising, measurement, analytics, fraud prevention, and security purposes."),
            ("6. Data Security and Retention",
             "Data transmitted through Google Mobile Ads SDK is protected using encryption in transit. Google handles information collected through AdMob according to its own data retention and privacy policies."),
            ("7. Privacy Requests",
             "Users, parents, and guardians may contact the developer with questions or privacy-related requests. Data processed directly by Google AdMob may be subject to Google's own data management procedures."),
            ("8. Third-Party Services",
             "The app uses Google Mobile Ads SDK (AdMob) as its third-party advertising service.",
             "@google"),
            ("9. Changes to This Policy",
             "This policy may be updated when necessary. Updates will be published on this page with a revised effective date."),
            ("10. Contact Us", "@contact"),
        ],
    },
}

# ---------------------------------------------------------- translations

from text_ar import AR  # noqa: E402
from text_de import DE  # noqa: E402
from text_es import ES  # noqa: E402
from text_fr import FR  # noqa: E402
from text_ja import JA  # noqa: E402
from text_ru import RU  # noqa: E402
from text_zh import ZH  # noqa: E402

T.update({"ar": AR, "zh": ZH, "fr": FR, "de": DE, "ja": JA, "ru": RU, "es": ES})
for _code in ("zh", "ja"):
    T[_code]["policy"]["end"] = "。"


def _eastern(v):
    """Arabic pages show Arabic digits, as the game does."""
    if isinstance(v, str):
        return v.translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
    if isinstance(v, list):
        return [_eastern(x) for x in v]
    if isinstance(v, tuple):
        return tuple(_eastern(x) for x in v)
    if isinstance(v, dict):
        return {k: _eastern(x) for k, x in v.items()}
    return v


T["ar"] = _eastern(T["ar"])
