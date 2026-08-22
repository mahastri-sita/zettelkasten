# AGENTS.md

## Scope

These rules apply to `source/` and all descendants. Inherit the root `AGENTS.md`.

`source` stores external evidence: what a source states, reports, observes, or provides. It is classified by source type, never by research subject. Do not create additional subject folders.

AI may create and maintain Source records autonomously when doing so supports an active research task.

## Source Boundaries

- Keep source content distinct from personal Argument and Synthesis Product.
- One bibliographic or documentary item normally maps to one Markdown record.
- Put the AI-processed digest and available faithful text or excerpts in the same record, separated clearly.
- Never alter quotations or faithful source text to match an interpretation.
- Label paraphrase and AI inference. Do not write either as a quotation.
- Attach page, section, table, figure, chapter, timestamp, or record locators to important claims when available.
- If only metadata, an abstract, a snippet, or excerpts were accessed, do not imply that the full source was read.
- Use `null` for unavailable metadata. Never infer bibliographic facts without evidence.

## Required Core Template

Every Source Markdown record must begin with this YAML core, extended by its source-type instruction:

```yaml
---
source_type: null
title: ""
creators: []
year: null
identifier: null
url: null
date_accessed: null
access_basis: null
---
```

Set `source_type` to exactly one of `journal`, `book`, `official-document`, `article`, `working-paper`, or `dataset`. Set `access_basis` to exactly one of `full-text`, `excerpt`, `abstract`, `metadata-only`, or `raw-data`. Use an ISO date (`YYYY-MM-DD`) for `date_accessed` when applicable. `access_basis` must describe what was actually available to the agent.

Except where a leaf instruction provides a dataset-specific adaptation, use this body:

```markdown
# Source Title

## AI-Processed Digest

### Core Claims or Contents

### Evidence and Method

### Scope and Limitations

## Faithful Source Text or Excerpts

## Provenance Notes
```

Do not add empty prose to satisfy a heading. State `Not available` or briefly explain why a section does not apply.

## Digest Standards

- Report the source's position before evaluating it.
- Preserve scope conditions, units of analysis, geography, period, and methodological limits.
- Separate findings reported by the source from interpretations made during processing.
- Do not turn relevance to a current project into a universal claim.
- Keep the digest concise relative to the available source text.

## Naming

Use the light naming pattern defined by the applicable source-type folder. Prefer stable, human-readable names. Do not use Zettelkasten IDs or timestamps as the primary filename.
