# AGENTS.md

## Scope

These rules apply to `source/official-document/`. Inherit `source/AGENTS.md` and the root `AGENTS.md`.

Use this folder for government documents, regulations, statutory plans, agency reports, official statistics publications, and other institutionally issued documents.

## Naming

Use `Institution - Year - Short Title.md`. Include the document number in the filename only when it is needed to distinguish or identify the document.

## Type-Specific YAML

Add these fields to the required Source core:

```yaml
institution: null
jurisdiction: null
publication_date: null
document_number: null
```

## Processing

- Identify the issuing institution, jurisdiction, legal or administrative function, geographic scope, period, and document version when available.
- Distinguish normative provisions, institutional claims, policy targets, reported implementation, and observed outcomes.
- Official status establishes provenance, not empirical truth. Surface methodological or political limitations when relevant.
- Preserve article, clause, page, table, map, or appendix locators for important claims.
