JSSA 2026 `sonicstv` Public Mirrored Repository
========

Step to Reproduce
--------

1. Install Python package `sonicstv`, which is the API mentioned in the paper.
   1. Go to [`sonicstv` repository](https://github.com/OzelotVanilla/sonicstv) and clone it to local.
   2. Install it following the instruction in `sonicstv` repository.
      Currently, it is done by running a script `utils/install_local_editable.py`.
      Always refer to the [`sonicstv` repository](https://github.com/OzelotVanilla/sonicstv)
       for the accurate way of installation.
2. Navigate to this repository's `experiment` folder.
3. `probe_sound__7eqlog800.py` will generate probed image and sound (検証用の対数的等間隔音列),
    while `sheet_5eqlog800.py` generate image and sound with designed sound contour (旋律輪郭).