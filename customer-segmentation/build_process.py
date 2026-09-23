"""Build the requested HTML overview of agent roles, durations, and review scores."""

from __future__ import annotations

from html import escape
from pathlib import Path


OUT = Path(__file__).parent / "output" / "full" / "process_overview.html"
DIMENSIONS = ["Accuracy", "Clarity", "Decision value", "Visual quality", "Usability and completeness"]
REVIEWS = {
    1: {
        "Methods reviewer": {"report": [4, 4, 4, 3, 3], "explorer": [4, 4, 4, 4, 4], "seconds": 64},
        "Marketing reviewer": {"report": [4, 4, 4, 3, 4], "explorer": [4, 4, 3, 4, 3], "seconds": 84},
        "Visual reviewer": {"report": [4.5, 4.5, 4, 3.5, 4], "explorer": [4.5, 4.5, 4, 4, 3.5], "seconds": 84},
    },
    2: {
        "Methods reviewer": {"report": [5, 4, 5, 3, 4], "explorer": [5, 4, 4, 4, 4], "seconds": 29},
        "Marketing reviewer": {"report": [4, 4, 4, 4, 4], "explorer": [4, 4, 4, 4, 4], "seconds": 35},
        "Visual reviewer": {"report": [4.5, 4.5, 4.5, 4, 4.5], "explorer": [4.5, 4.5, 4.5, 4.5, 4.5], "seconds": 70},
    },
    3: {
        "Methods reviewer": {"report": [5, 4, 5, 4, 4], "explorer": [5, 4, 4, 4, 4], "seconds": 37},
        "Marketing reviewer": {"report": [4, 4, 4, 4, 4], "explorer": [4, 4, 4, 4, 4], "seconds": 40},
        "Visual reviewer": {"report": [4.5, 4.5, 4.5, 4.5, 4.5], "explorer": [4.5, 4.5, 4.5, 4.5, 4.5], "seconds": 43},
    },
}
INITIAL = {"Methods reviewer": 89, "Marketing reviewer": 53}


def mean_score(round_number: int, artifact: str) -> float:
    values = [score for review in REVIEWS[round_number].values() for score in review[artifact]]
    return sum(values) / len(values)


def chart() -> str:
    y_ticks = [3.5, 4.0, 4.5, 5.0]
    tick_lines = "".join(
        f'<line x1="46" x2="632" y1="{235 - (tick - 3.5) * 120:.1f}" y2="{235 - (tick - 3.5) * 120:.1f}" stroke="#d9e2e3"/>'
        f'<text x="34" y="{239 - (tick - 3.5) * 120:.1f}" text-anchor="end" fill="#58707b" font-size="12">{tick:.1f}</text>'
        for tick in y_ticks
    )
    series = []
    for artifact, color, label in [("report", "#167d8d", "DOCX report"), ("explorer", "#ce7130", "HTML explorer")]:
        scores = [mean_score(round_number, artifact) for round_number in REVIEWS]
        points = [(90 + (index * 235), 235 - (score - 3.5) * 120) for index, score in enumerate(scores)]
        path = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        label_offset = 22 if artifact == "report" else -13
        circles = "".join(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{color}" stroke="white" stroke-width="2"/>'
            f'<text x="{x:.1f}" y="{y + label_offset:.1f}" text-anchor="middle" fill="{color}" font-size="13" font-weight="700">{score:.2f}</text>'
            for (x, y), score in zip(points, scores)
        )
        series.append(f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="3"/>{circles}')
    labels = "".join(f'<text x="{90 + index * 235}" y="267" text-anchor="middle" fill="#173040" font-size="13">Pass {index + 1}</text>' for index in range(3))
    return (
        '<svg viewBox="0 0 680 292" role="img" aria-label="Mean reviewer score rises for the report from 3.83 to 4.30 and for the explorer from 3.90 to 4.23, then plateaus">'
        + tick_lines + "".join(series) + labels + "</svg>"
    )


def build() -> None:
    timing_rows = [
        ("Initial skeptical audit", "Methods reviewer", INITIAL["Methods reviewer"], "Statistical construction, joins, denominators"),
        ("Initial skeptical audit", "Marketing reviewer", INITIAL["Marketing reviewer"], "Offer logic, campaign exposure, causal claims"),
    ]
    for round_number, reviewers in REVIEWS.items():
        for role, review in reviewers.items():
            timing_rows.append((f"Scored pass {round_number}", role, review["seconds"], "Report and explorer scoring with findings and fixes"))
    timing_html = "".join(
        f"<tr><td>{escape(task)}</td><td>{escape(role)}</td><td>{seconds // 60}m {seconds % 60:02d}s</td><td>{escape(purpose)}</td></tr>"
        for task, role, seconds, purpose in timing_rows
    )
    score_rows = "".join(
        f"<tr><td>Pass {round_number}</td><td>{mean_score(round_number, 'report'):.2f}</td>"
        f"<td>{mean_score(round_number, 'explorer'):.2f}</td>"
        f"<td>{mean_score(round_number, 'report') - mean_score(round_number - 1, 'report'):+.2f}</td>"
        f"<td>{mean_score(round_number, 'explorer') - mean_score(round_number - 1, 'explorer'):+.2f}</td></tr>"
        if round_number > 1 else
        f"<tr><td>Pass 1</td><td>{mean_score(1, 'report'):.2f}</td><td>{mean_score(1, 'explorer'):.2f}</td><td>Baseline</td><td>Baseline</td></tr>"
        for round_number in REVIEWS
    )
    detail_rows = "".join(
        f"<tr><td>{round_number}</td><td>{escape(role)}</td><td>{sum(review['report']) / 5:.2f}</td><td>{sum(review['explorer']) / 5:.2f}</td></tr>"
        for round_number, reviewers in REVIEWS.items()
        for role, review in reviewers.items()
    )
    dimension_rows = "".join(
        f"<tr><td>{round_number}</td><td>{escape(role)}</td><td>{'DOCX report' if artifact == 'report' else 'HTML explorer'}</td>"
        + "".join(f"<td>{score:g}</td>" for score in review[artifact])
        + f"<td>{sum(review[artifact]) / 5:.2f}</td></tr>"
        for round_number, reviewers in REVIEWS.items()
        for role, review in reviewers.items()
        for artifact in ["report", "explorer"]
    )
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Segmentation process overview</title>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#f5f8f7;color:#173040;font:16px/1.55 system-ui,Arial,sans-serif}}header{{background:#123a48;color:white;padding:42px max(22px,calc((100vw - 1100px)/2));border-bottom:6px solid #57bdc1}}header p{{max-width:770px;color:#d9e9e9}}h1{{font-size:clamp(30px,4vw,46px);margin:4px 0}}h2{{margin:0 0 13px;font-size:25px}}h3{{font-size:18px;margin:0 0 8px}}main{{max-width:1100px;margin:auto;padding:28px 22px 70px}}section{{margin:30px 0}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:13px}}.card{{background:white;border:1px solid #d9e2e3;border-radius:10px;padding:20px;box-shadow:0 4px 14px #15323d0a}}.card strong{{font-size:28px;display:block}}.card small,.muted{{color:#58707b}}.chart{{background:white;border:1px solid #d9e2e3;border-radius:10px;padding:12px 20px}}svg{{width:100%;height:auto;display:block}}.legend{{display:flex;gap:25px;font-size:14px;padding-left:38px}}.key{{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px}}table{{border-collapse:collapse;width:100%;font-size:14px;background:white}}th,td{{padding:9px 11px;border-bottom:1px solid #d9e2e3;text-align:left}}th{{background:#eaf1f1}}td:nth-child(3),td:nth-child(4),td:nth-child(5){{font-variant-numeric:tabular-nums}}.scroll{{overflow-x:auto;border:1px solid #d9e2e3;border-radius:9px}}.scroll table{{min-width:620px}}ol{{padding-left:23px}}li{{margin:7px 0}}footer{{color:#58707b;font-size:13px;border-top:1px solid #d9e2e3;padding-top:16px}}@media(max-width:700px){{.grid{{grid-template-columns:1fr}}}}
</style></head><body><header><div style="text-transform:uppercase;letter-spacing:.14em;font-size:12px;color:#a9d8d9">Agent work and review</div><h1>How the segmentation example was built</h1><p>The primary agent analyzed the simulated retail data and built the report and explorer. Independent agents challenged the first version and scored three successive versions of both deliverables.</p></header><main>
<div class="grid"><div class="card"><strong>2</strong><small>Skeptical reviews before scoring</small></div><div class="card"><strong>3</strong><small>Scored passes with three reviewers each</small></div><div class="card"><strong>0.10 / 0.00</strong><small>Final score gain: report / explorer</small></div></div>
<section><h2>Work sequence</h2><ol><li>The primary agent audited eight parquet files, profiled 2,467 nonfuel-shopping households, compared two through eight clusters, checked sensitivity, and built the first DOCX and standalone explorer.</li><li>A methods skeptic checked joins, denominators, model features, and stability. A marketing skeptic checked campaign records, offer examples, and causal language. The primary agent verified findings and revised the outputs.</li><li>Three independent reviewers scored each artifact on {", ".join(DIMENSIONS[:-1]).lower()}, and {DIMENSIONS[-1].lower()}. The primary agent fixed substantiated findings after each pass.</li></ol></section>
<section><h2>Score trajectory</h2><p class="muted">Each point is the mean of all 15 dimension scores, three reviewers times five dimensions. Scores run from 1 to 5.</p><div class="chart">{chart()}<div class="legend"><span><i class="key" style="background:#167d8d"></i>DOCX report</span><span><i class="key" style="background:#ce7130"></i>HTML explorer</span></div></div><div class="scroll" style="margin-top:14px"><table><thead><tr><th>Review</th><th>Report mean</th><th>Explorer mean</th><th>Report gain</th><th>Explorer gain</th></tr></thead><tbody>{score_rows}</tbody></table></div><p class="muted">The third pass improved the report by 0.10 and left the explorer unchanged. Both gains were below the prespecified 0.25-point continuation threshold, and reviewers reported no material open issue. The loop stopped after three passes.</p></section>
<section><h2>What changed during review</h2><div class="grid"><div class="card"><h3>Methods and counts</h3><p>Corrected the combined meat-share median, reported sparse-history and fuel sensitivity, and verified category evidence against purchase lines.</p></div><div class="card"><h3>Marketing interpretation</h3><p>Checked campaign assignment and redemption joins, replaced generic offers with category-supported examples, and specified a randomized test with margin as the primary outcome.</p></div><div class="card"><h3>Reader experience</h3><p>Kept paired offers on one page, enlarged figure text, added activity quantiles, and fixed the campaign table and controls at narrow browser widths.</p></div></div></section>
<section><h2>Agent time</h2><p class="muted">Elapsed times are measured from dispatch to completion for each subagent task. Agents ran concurrently, so these times do not add to project wall time. The primary agent's analysis and build time was not separately instrumented.</p><div class="scroll"><table><thead><tr><th>Task</th><th>Agent role</th><th>Elapsed</th><th>Assignment</th></tr></thead><tbody>{timing_html}</tbody></table></div></section>
<section><h2>Reviewer scores</h2><div class="scroll"><table><thead><tr><th>Pass</th><th>Reviewer</th><th>Report mean</th><th>Explorer mean</th></tr></thead><tbody>{detail_rows}</tbody></table></div><details style="margin-top:14px"><summary>Show all dimension scores</summary><div class="scroll" style="margin-top:10px"><table><thead><tr><th>Pass</th><th>Reviewer</th><th>Artifact</th><th>Accuracy</th><th>Clarity</th><th>Decision value</th><th>Visual quality</th><th>Usability and completeness</th><th>Mean</th></tr></thead><tbody>{dimension_rows}</tbody></table></div></details><p class="muted">Scores shown here are recomputed from the dimension ratings. A reviewer misstated one arithmetic mean in a message; the table uses the ratings themselves.</p></section>
<footer>Review completed 22 September 2026, America/Chicago. The findings and scores describe this educational proof of concept. They do not validate the simulated data for commercial decisions.</footer></main></body></html>'''
    OUT.write_text(html, encoding="utf-8")
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
