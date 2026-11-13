# arnoobland.github.io

The website of Arnoob Land, a calm nature game for children: the home page, the privacy policy and app-ads.txt, in the game's eight languages.

- English is the original, at the top: `index.html` and `privacy-policy.html`.
- Arabic, Chinese (Simplified), French, German, Japanese, Russian and Spanish each have a folder (`ar/`, `zh/`, `fr/`, `de/`, `ja/`, `ru/`, `es/`) with both pages, and screenshots from the game in that language in `images/<code>/`. These translations were made with the help of AI; each translated privacy policy says the English version applies if they differ.
- **Don't edit the `.html` files by hand.** The words are in `_build/texts.py` (English) and `_build/text_<code>.py`; after changing them run `python3 _build/pages.py`. GitHub Pages doesn't publish folders that start with `_`.
