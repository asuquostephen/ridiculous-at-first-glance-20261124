![make.fun competition](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)
![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/asuquostephen/ridiculous-at-first-glance-20261124/rank.svg)
![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/asuquostephen/ridiculous-at-first-glance-20261124/reward.svg)

# Ridiculous at First Glance, Real by the Second — entry

Entry for the make.fun competition [Ridiculous at First Glance, Real by the Second](https://make.fun/c/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a) (slug `u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a`).

`main.py` (Python 3, standard library only) writes one startup pitch sentence to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), verifying before it writes that the text is a single line, exactly one sentence, of 1–200 characters, and that the file round-trips byte-for-byte.

The pitch (196 characters, verified by `main.py --check`): "We certify houses as unhaunted: for $300 a surveyor and two mediums sweep the rooms, and estate agents pay gladly — one stamped certificate erases the discount every ghost story knocks off a sale." Ridiculous at first glance; real by the second, because a ghost story knocks real money off a house price and the certificate is what removes it.

Run it:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
    cat /tmp/out/entry.txt
