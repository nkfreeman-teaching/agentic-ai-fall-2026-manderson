# Customer segmentation proof of concept

This example groups households by nonfuel shopping behavior in the simulated Complete Journey data. It supports a classroom discussion of segmentation and coupon-test design. The source files are in `data/` and remain unchanged.

Students do not need to run this example. Its finished outputs are already in `output/full/`, and `output/full/process_overview.html` opens in a web browser to show how the agent and its reviewers built them. To rerun it, install Pixi as described in the getting-started guides, then run these commands from this directory:

```bash
pixi run python analyze.py --sample
pixi run python analyze.py
pixi run python build_outputs.py
pixi run python build_process.py
```

The full run writes `output/full/results.json`, `output/full/household_segments.parquet`, `output/full/customer_segmentation_report.docx`, and `output/full/segment_explorer.html`. The explorer opens directly in a browser without a server. The `output/full/process_overview.html` file records the requested agent review and score trajectory.

The [dataset publisher](https://cunningjames.github.io/completejourney_py/user-guide/datasets/) describes this release as simulated and intended for education. Coupon proposals are hypotheses for a randomized test. They are not estimates of commercial impact.
