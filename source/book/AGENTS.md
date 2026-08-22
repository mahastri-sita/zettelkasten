# AGENTS.md

## Scope

These rules apply to `source/book/`. Inherit `source/AGENTS.md` and the root `AGENTS.md`.

Use this folder for authored books, edited books, and accessed book chapters.

## Naming

Use `Author - Year - Short Title.md`. For an edited volume without a primary author, use the first editor followed by `ed` or `eds`.

## Type-Specific YAML

Add these fields to the required Source core:

```yaml
editors: []
publisher: null
edition: null
isbn: null
chapter_or_pages_covered: null
```

## Processing

- State whether access covered the full book, selected chapters, or excerpts, and set `access_basis` accordingly.
- Preserve chapter and page locators for substantive claims.
- Distinguish the position of a chapter author from the position of the volume editors.
- Do not generalize a chapter-level argument to the entire book unless the full-book evidence supports it.
