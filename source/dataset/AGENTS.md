# AGENTS.md

## Scope

These rules apply to `source/dataset/`. Inherit `source/AGENTS.md` and the root `AGENTS.md`.

Use this folder for externally obtained datasets and their provenance records.

## Storage and Immutability

- Store a raw data file with a companion Markdown Source record when its size is reasonable.
- For large or remote datasets, store the record with the stable location, version, and checksum when available instead of copying the full data.
- Treat raw data as immutable. Never clean, overwrite, normalize, or transform the original in place.
- Document transformations in `calculation`; do not save transformed data as if it were raw Source.

## Naming

Use the semantic pattern `creator_dataset_version.md` for companion records, omitting the version only when none exists. All record, raw-data, and derivative filenames in this folder use lowercase ASCII `snake_case` with a lowercase extension. Preserve raw bytes; when an approved naming normalization renames a raw file, retain its original filename in the companion record's provenance notes or legacy-source path.

## Type-Specific YAML

Add these fields to the required Source core:

```yaml
publisher: null
version: null
release_date: null
license: null
spatial_coverage: null
temporal_coverage: null
unit_of_observation: null
data_format: null
raw_files: []
checksum: null
```

Use `access_basis: raw-data` only when the data itself was accessed. Use `metadata-only` when only documentation or a catalog record was available.

## Dataset Body

Use this body instead of the general Source body:

```markdown
# Dataset Title

## Dataset Description

## Variables or Schema

## Coverage and Unit of Observation

## Collection or Production Method

## Known Limitations

## Raw File Inventory

## Provenance Notes
```

Do not infer undocumented variable meanings, units, coordinate reference systems, missing-value conventions, or collection methods. Record uncertainty explicitly.
