## 2024-05-22 - Script Execution Context Matters
**Learning:** `document.body` is null in `<head>`. Always ensure DOM elements exist before querying them. This caused the dark mode initialization to fail silently, resulting in FOUC or broken theme state.
**Action:** Move DOM-dependent initialization scripts to the start of `<body>` or use `DOMContentLoaded`. For critical visual state (like theme), inline script at start of body is preferred to avoid FOUC.
