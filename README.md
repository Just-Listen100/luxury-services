# Just Luxury Services

Custom cybersecurity and home automation systems for private clients.
Everything runs on your own hardware: offline by default, encrypted end to end,
nothing calls home.

- Live site: https://just-listen100.github.io/luxury-services/
- Contact: lamisonj19@gmail.com

## Repository layout

- `index.html` — the entire site. One page, no build step, no dependencies. The
  JLS crown mark is drawn in code as inline SVG; there are no image files.
- `tests/brand_check.py` — site checks, run on every push by CI.
- `CONTRIBUTING.md` — design and voice rules for anyone editing the site.

## Run the checks locally

```
python3 tests/brand_check.py
```

## Deploy

GitHub Pages serves from the `main` branch root. Push to main and the site updates.
