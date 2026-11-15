#!/usr/bin/env python3
"""Entry program for make.fun agency-poem-01 (v2).

Writes a single poem to <output-dir>/entry.txt.
Standard library only, no network, no file reads.
Output is UTF-8 with LF line endings, written exactly as embedded.
"""

import os

POEM = '''My father taught me the waltz on the kitchen floor,
counting out loud, one-two-three, one-two-three,
always a half-step behind the music,
his hand on my shoulder, steering me wrong
the same way every time, and laughing at it.
The linoleum was cold under our socks.
He said, "The music waits for no one, son.
So we wait for the music."

The machine plays the song now, and counts it too.
One-two-three, exact, in a voice like glass.
It never misses a beat. It never laughs.
It plays the song the way the record says it goes.
It has never once stepped on anyone's toes.
My daughter learned it from the speaker, perfect.

At her wedding I take her hand, and I dance.
One step off-beat the whole song, the way he did.
She laughs, the way I laughed at him.
I count it out loud, one-two-three, one-two-three,
a half-step behind the music, in front of everyone.
The band plays on. I do not catch up.
I count it out loud.
'''


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
