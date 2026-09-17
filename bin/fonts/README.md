# Vendored fonts

Used only by `bin/build_og_images.py` to render the share preview cards. They
are not served to browsers, and the CI build never reads them: the cards are
generated here and committed.

- `Inter-{Regular,SemiBold,Bold}.ttf` from [rsms/inter](https://github.com/rsms/inter)
  v4.0. SIL Open Font License 1.1, see `Inter-LICENSE.txt`.
- `NanumBarunGothic-{Regular,Bold}-subset.ttf` from Naver's Nanum Barun Gothic,
  SIL Open Font License 1.1. Subset with fontTools to the Hangul that appears on
  the cards, which is why they are ~18 KB rather than ~4 MB. Inter carries no
  Hangul, so the card renderer draws Korean runs with these.
