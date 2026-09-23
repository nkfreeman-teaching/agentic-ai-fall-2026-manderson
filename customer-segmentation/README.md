# Customer segmentation proof of concept

This example groups households by nonfuel shopping behavior in the simulated Complete Journey data. It supports a classroom discussion of segmentation and coupon-test design. The source files are in `data/` and remain unchanged.

Run from this directory:

```bash
pixi run python analyze.py --sample
pixi run python analyze.py
pixi run python build_outputs.py
pixi run python build_process.py
```

The full run writes `output/full/results.json`, `output/full/household_segments.parquet`, `output/full/customer_segmentation_report.docx`, and `output/full/segment_explorer.html`. The explorer opens directly in a browser without a server. The `process_overview.html` file records the requested agent review and score trajectory.

The [dataset publisher](https://cunningjames.github.io/completejourney_py/user-guide/datasets/) describes this release as simulated and intended for education. Coupon proposals are hypotheses for a randomized test. They are not estimates of commercial impact.
