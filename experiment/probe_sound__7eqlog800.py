from sonicstv import (
    bake, Sheet, SingleFreqNote as s,
    nudgeAll, biasAll, coverRandomly
)
from functools import partial

from functions import saveSSTVAudio


f0 = 1500.0000000000000
f1 = 1594.4495051048468
f2 = 1694.8461495527272
f3 = 1801.5644029221340
f4 = 1915.0023137691367
f5 = 2035.5829943092242
f6 = 2163.7561985841230
f7 = 2300.0000000000000


# Notice: Probe sound is generated based on "3 frame for one sound".
sheet = Sheet([
    # line 1
    s(f, duration_frame=3)
    for f in [
        f0, f1, f2, f3, f4, f5, f6, f7
    ] * 40
])


bake_result__nudgeAll = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.25)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./experiment/output/probe__7eqlog800_nudgeAll_25.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__nudgeAll,
        "./experiment/output/probe__7eqlog800_nudgeAll_25.wav",
        should_overwrite_if_existed=True
    )


bake_result__nudgeAll = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.50)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./experiment/output/probe__7eqlog800_nudgeAll_50.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__nudgeAll,
        "./experiment/output/probe__7eqlog800_nudgeAll_50.wav",
        should_overwrite_if_existed=True
    )


bake_result__nudgeAll = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(nudgeAll, strength=0.75)
)

if bake_result__nudgeAll is not None:
    bake_result__nudgeAll.save(
        "./experiment/output/probe__7eqlog800_nudgeAll_75.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__nudgeAll,
        "./experiment/output/probe__7eqlog800_nudgeAll_75.wav",
        should_overwrite_if_existed=True
    )


bake_result__biasAll = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(biasAll, strength=0.75)
)

if bake_result__biasAll is not None:
    bake_result__biasAll.save(
        "./experiment/output/probe__7eqlog800_biasAll.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__biasAll,
        "./experiment/output/probe__7eqlog800_biasAll.wav",
        should_overwrite_if_existed=True
    )


bake_result__coverRandomly = bake(
    "./experiment/tunnel.png",
    sheet,
    line_process_algo=partial(coverRandomly, strength=0.25)
)

if bake_result__coverRandomly is not None:
    bake_result__coverRandomly.save(
        "./experiment/output/probe__7eqlog800_coverRandomly.png",
        should_overwrite_if_existed=True
    )
    saveSSTVAudio(
        bake_result__coverRandomly,
        "./experiment/output/probe__7eqlog800_coverRandomly.wav",
        should_overwrite_if_existed=True
    )
