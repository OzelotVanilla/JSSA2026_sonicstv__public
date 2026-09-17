from sonicstv import (
    bake, Sheet, SingleFreqNote as s, RestNote as r,
    nudgeAll, biasAll, coverRandomly
)
from functools import partial

from functions import saveSSTVAudio


"""
Description for the picture:

* around upper 1/3 of the picture (phase 1): sound is dark and unclear
* around middle 1/3 (phase 2): sound starts trembling, offset is negative, and melogy shape become hard to be controlled.
* around lower 1/3 (phase 3): sound becomes clearer and clearer, offset is positive.
"""

f0 = 1500.000000000000
f1 = 1633.874047369416
f2 = 1779.696268444877
f3 = 1938.533030141518
f4 = 2111.545871944413
f5 = 2300.000000000000


sheet = Sheet([
    # line 1 ~ 24 (each line is 3 frame)
    # Melodic, motif A.
    *[s(f, duration_frame=3)
      for f in [
        # 1                                 # 10    # 12
        f2, f3, f2, f4, f3, f2, f5, f4, f3, f4, f3, f2,
        # 13                        # 20            # 24
        f0, f2, f4, f2, f4, f5, f5, f2, f0, f3, f5, f2,
    ]],

    # line 25 ~ 36
    # Using of "rest note": use the original sound of SSTV that with hoarse texture.
    # The using of rest note, is motif B.
    # 25                                      # 27
    r(duration_frame=3), r(duration_frame=3), r(duration_frame=3),
    #                                  # 28    # 30
    *[s(f, duration_frame=3) for f in [f2, f2, f2]],
    # 31                                      # 33
    r(duration_frame=3), r(duration_frame=3), r(duration_frame=3),
    #                                  # 34    # 36
    *[s(f, duration_frame=3) for f in [f5, f5, f5]],

    # line 37 ~ 52
    # A little start of motif B, then fast ascending sound.
    # 37                                      # 39
    r(duration_frame=3), r(duration_frame=3), r(duration_frame=3),
    #                                  # 40    # 42
    *[s(f, duration_frame=3) for f in [f2, f2, f2]],
    *[s(f, duration_frame=1)
        for f in [
            # 43        # 44        # 45        # 46
            f0, f1, f2, f1, f2, f3, f2, f3, f4, f3, f4, f5,
            # 47        # 48
            f0, f2, f4, f1, f3, f5
    ]],
    # After the ascending sound, trying to slow down, and prepare for the next fast-pace mix sound.
    # 49                     # 50                     # 51                     # 52,53,54
    s(f3, duration_frame=3), s(f5, duration_frame=3), s(f3, duration_frame=3), s(f2, duration_frame=9),

    # line 55
    # Motif C1, still using the mix of original sstv sound and designated note.
    # Played in fast-pace to show tense, and prepare for the frequency move.
    # Repeated twice.
    *([
        # 55/71                                       # 56/72
        s(f3, duration_frame=1), r(duration_frame=2), s(f3, duration_frame=1), r(duration_frame=2),
        # 57/73                                       # 58/74
        s(f3, duration_frame=1), r(duration_frame=2), s(f3, duration_frame=1), r(duration_frame=2),
        # 59/75                                       # 60/76
        r(duration_frame=1), s(f0, duration_frame=2), r(duration_frame=1), s(f0, duration_frame=2),
        # 61/77                                       # 62/78
        r(duration_frame=1), s(f0, duration_frame=2), r(duration_frame=1), s(f0, duration_frame=2),

        # 63/79                                       # 64/80
        s(f3, duration_frame=1), r(duration_frame=2), s(f3, duration_frame=1), r(duration_frame=2),
        # 65/81                                       # 66/82
        s(f3, duration_frame=1), r(duration_frame=2), s(f3, duration_frame=1), r(duration_frame=2),
        # 67/83                                           # 68/84
        s(f5, duration_frame=1), s(f3, duration_frame=2), s(f5, duration_frame=1), s(f3, duration_frame=2),
        # 69/85                                           # 70/86
        s(f5, duration_frame=1), s(f3, duration_frame=2), s(f5, duration_frame=1), s(f3, duration_frame=2)
    ] * 2),

    # line 87 ~ 94
    # Use the original sstv sound for 4 lines at twice.
    # The first rest note still have a higher freq, while the second note shows the shift.
    # 87,88,89,90         # 91,92,93,94
    r(duration_frame=12), r(duration_frame=12),

    # line 95 ~ 108 (each line is 3 frame)
    # Motif A modified (A'). Showing a feeling of chaos and trembling.
    *[s(f, duration_frame=3)
      for f in [
        # 95                # 100                   # 106
        f0, f2, f0, f4, f2, f0, f5, f4, f3, f4, f2, f0,
        # 107       # 110                           # 118
        f5, f4, f2, f4, f0, f2, f3, f0, f2, f5, f3, f1,
    ]],

    # Motif B modified (B1), appearance of note and rest, and the freq, are all different.
    # 119,120,121            # 122,123,124        # 125,126,127            # 128,129,130
    s(f5, duration_frame=9), r(duration_frame=9), s(f3, duration_frame=9), r(duration_frame=9),

    # Motif C2 (similar to C1), allowing the bird-alike noice to be mixed with note.
    *([
        # 131/133/135                                 # 132/134/136
        s(f5, duration_frame=1), r(duration_frame=2), s(f4, duration_frame=1), s(f2, duration_frame=1), s(f0, duration_frame=1)
    ] * 3),
    # 137                                         # 138
    s(f5, duration_frame=1), r(duration_frame=2), s(f2, duration_frame=1), s(f4, duration_frame=1), s(f5, duration_frame=1),
    # 139                                         # 140
    s(f3, duration_frame=1), r(duration_frame=2), s(f5, duration_frame=1), s(f3, duration_frame=1), s(f1, duration_frame=1),
    # 141                                         # 142
    s(f3, duration_frame=1), r(duration_frame=2), s(f5, duration_frame=1), s(f3, duration_frame=1), s(f1, duration_frame=1),
    # 143                                             # 143.6~144
    s(f0, duration_frame=1), s(f2, duration_frame=1), s(f4, duration_frame=4),
    # 145                                             # 146
    s(f1, duration_frame=1), s(f3, duration_frame=1), s(f5, duration_frame=4),

    # line 147 ~ 170
    # Motif A unchanged, but in the end of phase 2.
    *[s(f, duration_frame=3)
      for f in [
        # 147       # 150                           # 158
        f2, f3, f2, f4, f3, f2, f5, f4, f3, f4, f3, f2,
        # 159                                       # 170
        f0, f2, f4, f2, f4, f5, f5, f2, f0, f3, f5, f2,
    ]],

    # The base frequency is going to move up.
    # line 171 ~ 172
    *[*[s(f0, duration_frame=1), r(duration_frame=1)] * 3],
    # line 173 ~ 174
    *[*[s(f2, duration_frame=1), r(duration_frame=1)] * 3],
    # line 175 ~ 176
    *[*[s(f3, duration_frame=1), r(duration_frame=1)] * 3],
    # line 177 ~ 178
    *[*[s(f5, duration_frame=1), r(duration_frame=1)] * 3],

    # Dot-like sounding of ascending note, creating tense to resolve.
    # 179
    s(f0, duration_frame=1), r(duration_frame=1), s(f2, duration_frame=1),
    # 180
    r(duration_frame=1), s(f4, duration_frame=1), r(duration_frame=1),
    # 181
    s(f2, duration_frame=1), r(duration_frame=1), s(f4, duration_frame=1),
    # 182
    r(duration_frame=1), s(f5, duration_frame=1), r(duration_frame=1),
    # 183
    s(f1, duration_frame=1), r(duration_frame=1), s(f3, duration_frame=1),
    # 184
    r(duration_frame=1), s(f4, duration_frame=1), r(duration_frame=1),

    # Another motif-B-alike (B2), rest the tense made before,
    #  and be ready to move to phase 3.
    # Variation add to the second part of
    # first part, line 185 ~ 196
    # 185,186,187            # 188,189,190        # 191,192,193            # 194,195,196
    s(f5, duration_frame=9), r(duration_frame=9), s(f2, duration_frame=9), s(f3, duration_frame=9),
    # second part, line 197 ~ 208
    # 197,198,199        # 200,201,202            # 203,204,205            # 206,207,208
    r(duration_frame=9), s(f3, duration_frame=9), s(f2, duration_frame=9), r(duration_frame=9),

    # Motif A again, in the starting of phase 3.
    *[s(f, duration_frame=3)
      for f in [
        # 209                                       # 220
        f2, f3, f2, f4, f3, f2, f5, f4, f3, f4, f3, f2,
        # 221                               # 230   # 232
        f0, f2, f4, f2, f4, f5, f5, f2, f0, f3, f5, f2,
    ]],

    # Another motif-B-alike (B3), mixture of rest and note.
    # 233,234,235        # 236,237,238            # 239,240,241        # 242,243,244
    r(duration_frame=9), s(f1, duration_frame=9), r(duration_frame=9), s(f0, duration_frame=9),

    # This part could be used as the main theme of DeepMaze game itself.
    # line 245 ~ 246
    r(duration_frame=2), s(f4, duration_frame=2), s(f0, duration_frame=2),
    # line 247 ~ 248
    s(f1, duration_frame=2), r(duration_frame=2), s(f1, duration_frame=2),
    # line 249 ~ 250
    r(duration_frame=2), s(f4, duration_frame=2), s(f0, duration_frame=2),
    # line 251 ~ 252
    s(f1, duration_frame=2), r(duration_frame=2), s(f1, duration_frame=2),

    # With a sudden stop produced by triple fast note, the transmission stops.
    # 253,254                # 255                                                       # 256
    s(f0, duration_frame=6), s(f1, duration_frame=3), *[s(f, duration_frame=1) for f in [f4, f1, f0]],
])


bake_result__nudgeAll = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.50)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./experiment/output/sheet__5eqlog800_nudgeAll_50.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__nudgeAll,
        "./experiment/output/sheet__5eqlog800_nudgeAll_50.wav",
        should_overwrite_if_existed=True
    )


bake_result__biasAll = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(biasAll, strength=0.75)
)

if bake_result__biasAll is not None:
    bake_result__biasAll.save(
        "./experiment/output/sheet__5eqlog800_biasAll.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__biasAll,
        "./experiment/output/sheet__5eqlog800_biasAll.wav",
        should_overwrite_if_existed=True
    )


bake_result__coverRandomly = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(coverRandomly, strength=0.25)
)

if bake_result__coverRandomly is not None:
    bake_result__coverRandomly.save(
        "./experiment/output/sheet__5eqlog800_coverRandomly.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__coverRandomly,
        "./experiment/output/sheet__5eqlog800_coverRandomly.wav",
        should_overwrite_if_existed=True
    )
