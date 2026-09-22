# Agentic AI workshops

This repository holds material for a series of workshops on agentic artificial intelligence (AI), i.e., systems in which a language model plans and carries out multistep tasks using tools such as a code interpreter or a file system. The material pairs a slide deck on the core concepts with two worked examples, one research-oriented and one applied, that we conduct live during the workshops.

## Repository layout

| Folder | Contents |
|---|---|
| `slides/` | The workshop deck (`agentic-ai.html`), with a PDF export (`agentic-ai.pdf`). |
| `reddit/` | A research-oriented example built on a proprietary Reddit dataset. |
| `customer-segmentation/` | A customer segmentation analysis built on the Complete Journey retail dataset. |

## Data

### Complete Journey (customer segmentation)

The customer segmentation example uses the Complete Journey dataset, which contains household-level grocery transactions, demographics, and marketing campaign records from a retailer. We obtained the data from the [completejourney_py](https://github.com/cunningjames/completejourney_py) package, and the repository includes the following eight parquet files in `customer-segmentation/data/`:

- `campaigns.parquet`
- `campaign_descriptions.parquet`
- `coupons.parquet`
- `coupon_redemptions.parquet`
- `demographics.parquet`
- `products.parquet`
- `promotions.parquet`
- `transactions.parquet`

### Reddit (research example)

The Reddit example uses a proprietary dataset that is not tracked in this repository (the `.gitignore` excludes everything in `reddit/data/` except a placeholder file). To run the example, download [`user_daily_post_counts.parquet`](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing) (approximately 756 MB) from Google Drive and place it in `reddit/data/`.
