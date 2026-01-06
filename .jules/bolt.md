## Critical Learnings

## 2026-01-06 - Font Loading Performance
**Learning:** Large icon libraries like Font Awesome (all.min.css) can significantly block First Contentful Paint.
**Action:** Load non-critical CSS asynchronously using `media="print" onload="this.media='all'"` and provide a `<noscript>` fallback.

## 2026-01-06 - Dark Mode FOUC Prevention
**Learning:** Accessing `document.body` in the `<head>` throws an error because the body element doesn't exist yet.
**Action:** Initialize theme classes on `document.documentElement` in `<head>` or place the body-specific script immediately after the opening `<body>` tag.
