# Contributing to the Just Luxury Services site

## The product

Just Luxury Services builds custom security and automation software for private
clients. The site is the brand: quiet, precise, no hype.

## Voice rules

- Short sentences. Plain words. No superlatives, no invented claims, no fake
  testimonials, no prices without the owner's approval.
- The company name is exactly "Just Luxury Services". Never shorten it to
  "Luxury Services"; the checks fail the build if the name appears shortened.
- The product is software. Never describe physical estate installation work.

## Design rules

- Typography and color only: no photographs, no illustrations, no images of
  houses or properties.
- The JLS crown mark is the only brand mark. It is drawn as inline SVG code in
  the page (navigation, hero, footer, favicon), never shipped as an image file.
- Dark background, gold accent. Headings in a serif face, body in a sans face.
- One page, no build step, no external dependencies.
- The contact button is a mailto link owned by the principal. Do not point it
  anywhere else without the owner's instruction.

## Checks

Run `python3 tests/brand_check.py` before pushing. CI runs it on every push.
