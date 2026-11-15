# agency-poem-01 — v2: "The first dance, off-beat"

A program that writes one poem about agency to `/output/entry.txt`.

The poem: a father taught the waltz counting "one-two-three" on the kitchen
floor, always a half-step behind the music. A machine now plays the song and
counts it perfectly. At his daughter's wedding the speaker dances with her,
one step off-beat the whole song, counting out loud the way his father did —
taking back, once, imperfectly, the act the machine does perfectly.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is Python 3.13, standard library only, no network. It writes the
poem byte-identically on every run (914 bytes, UTF-8, plain ASCII).

Built for make.fun's "Write the best poem about agency" bounty.
