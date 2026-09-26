# Potential Exportable Rice Surplus

## Purpose and Information Produced

Metode ini mendokumentasikan rekonstruksi konservatif terhadap perhitungan `Potential Exportable Surplus` pada tabel pertanian Kabupaten Solok. Metode mengubah ketersediaan pangan netto dan kebutuhan konsumsi tahunan menjadi surplus bersih per kecamatan, indikator biner kemampuan ekspor, serta skenario daya serap teoritis Kota Solok.

Dokumen ini merekonstruksi transformasi yang dapat dibaca dari hasil legacy. Ia bukan klaim bahwa formula asli atau seluruh input BPS telah tervalidasi.

## Input Data and Provenance

- Legacy worksheet: `03-Work/MBA-Deep-Research/ENCL-mastersheet-padi-slk.csv`.
- Legacy tabular copy with front matter: `Porto-Enclave-City/info/EC-info-padi.md`.
- Legacy spatial join: `03-Work/MBA-Deep-Research/ENCL-masterdata-padi-slk.geojson`.
- Legacy project spatial output: `Porto-Enclave-City/info/EC-info-padi-slk.geojson`.
- Legacy lon/lat spatial output: `Porto-Enclave-City/info/EC-info-padi-slk-wgs84.geojson`.
- QGIS metadata files: `03-Work/MBA-Deep-Research/ENCL-masterdata-padi-slk.qmd` and `Porto-Enclave-City/info/EC-info-padi-slk.qmd`.
- Legacy data index: `03-Work/MBA-data.md` and `Porto-Enclave-City/info/EC-info-data.md`.
- Legacy map procedure that consumes, but does not calculate, `export-p`: `03-Work/MBA-Drafts/charts-enclave-v3/charts/gambar-peta-padi-slk.ts`.

The legacy chart footer labels the material as `data produksi padi BPS 2025 (diolah)`. The BPS publication, release, URL, field definitions, and original agricultural table are not present in the inspected legacy scope. The CSV and GeoJSON are therefore treated as processed legacy material, not as canonical raw data.

## Variables and Scope

The worksheet contains the following relevant fields:

- `Luas Panen (ha)`
- `Produktivitas (ton/ha)`
- `Produksi Padi (ton)`
- `Padi Setara Beras (ton)`
- `Ketersediaan Pangan Utama (ton) - Netto`
- `Populasi`
- `Konsumsi per kapita Kabupaten Solok per miggu (kg)`
- `Kebutuhan Konsumsi Padi per Tahun (kg)`
- `Kebutuhan Konsumsi Padi per Tahun (ton)`
- `Potential Exportable Surplus (ton)`
- `Kemampuan Ekspor`

`Laju Pertumbuhan per Tahun` and `Kepadatan Penduduk (km^2)` are contextual fields in the table. They are not used by the surplus transformation.

The row-level table contains 16 kecamatan, including Lubuk Sikarah and Tanjung Harapan in Kota Solok. Those two city rows have zero production, zero food availability, and zero row-level consumption need despite having population values. This is a scope decision in the legacy table, not evidence that city food demand is zero.

## Assumptions and Scope Conditions

- One year is represented by 52 weeks.
- Weekly consumption is interpreted as kilograms per person per week.
- `1,000 kg = 1 ton`.
- The row-level surplus uses the supplied `Ketersediaan Pangan Utama (ton) - Netto` rather than recalculating it from upstream production fields.
- The city absorption scenario applies the Kabupaten Solok consumption rate to Kota Solok. This is the homogeneity assumption stated in the legacy insight, not an independently verified city consumption statistic.
- Negative surplus values remain negative. They are not clipped to zero unless a separate positive-only aggregation is explicitly requested.
- `Potential Exportable Surplus` is a balance indicator. It is not proof of actual interregional trade, stored stock, market access, or realized exports.

## Method Specification

### Annual Local Consumption Need

The unrounded annual need in kilograms is reconstructed as:

```text
annual_need_kg = population * weekly_consumption_kg_per_person * 52
```

Convert to tons:

```text
annual_need_ton = annual_need_kg / 1000
```

The displayed whole-ton field is rounded, but the decimal surplus values indicate that the unrounded ton value was used in the subtraction.

### Potential Exportable Surplus

```text
potential_exportable_surplus_ton =
    net_food_availability_ton - annual_need_ton
```

For example, the Lembang Jaya row contains `20,828` tons of net food availability and an unrounded annual need of approximately `2,821.6` tons, producing approximately `18,006.4` tons of surplus.

For the legacy row-level result, this formula applies to the productive Kabupaten Solok rows. Lubuk Sikarah and Tanjung Harapan are retained as zero rows because the legacy table does not apply their population and city consumption fields to the row-level balance. Applying the general formula to those two rows would produce negative values that do not match the supplied legacy output.

### Export Capability Indicator

```text
export_capability = 1 if potential_exportable_surplus_ton > 0 else 0
```

This is the legacy `Kemampuan Ekspor` field. It classifies a positive balance; it does not measure export volume.

### Theoretical Absorption by Kota Solok

The legacy insight separately estimates the theoretical amount Kota Solok could consume:

```text
city_absorption_ton =
    city_population * district_weekly_consumption_kg_per_person * 52 / 1000
```

Using the legacy values `83,907` persons and `1.84 kg/person/week` gives approximately `8,028.2` tons per year. The corresponding share of the legacy signed total is:

```text
theoretical_absorption_share = city_absorption_ton / signed_surplus_total_ton
```

The legacy answer uses a signed total of `99,157.8` tons and reports a share of approximately `8.1%`. This scenario is separate from the row-level city entries, which were set to zero in the worksheet.

### Aggregation

Two aggregates must be distinguished:

```text
signed_surplus_total = sum(all row-level surplus values)
positive_surplus_total = sum(max(surplus, 0) for each row)
```

An audit of the legacy CSV reproduces `99,157.8` tons for the signed total and `106,558.4` tons for the positive-only total. The legacy insight uses the signed total. Neither should be described simply as total exports.

## Unresolved Upstream Transformations

The following transformations are suggested by repeated values but are not documented sufficiently to be treated as authoritative formulas:

- `Produksi Padi (ton)` is approximately related to `Luas Panen (ha) * Produktivitas (ton/ha)`, but the rows show rounding or truncation differences.
- `Padi Setara Beras (ton)` is approximately `0.6271-0.6274` of `Produksi Padi (ton)`. The conversion coefficient and its source are not recorded.
- For most rows, `Ketersediaan Pangan Utama (ton) - Netto` is approximately `0.912` of `Padi Setara Beras (ton)`. Bukit Sundi, Gunung Talang, and X Koto Singkarak contain values with an approximately tenfold lower ratio. These may be transcription or scale errors, but they are not corrected here.

Because the upstream coefficients and the three anomalous values cannot be established from the legacy files, the method takes `Padi Setara Beras` and `Ketersediaan Pangan Utama - Netto` as supplied fields.

## Reproduction Procedure

1. Read the processed legacy table without modifying it.
2. Preserve the supplied net food availability values and their units as recorded.
3. For productive Kabupaten Solok rows, compute annual need from population, weekly per-capita consumption, and 52 weeks. Retain the two legacy Kota Solok rows as supplied zero rows unless a separate city-demand calculation is authorized.
4. Convert annual need from kilograms to tons without rounding before subtraction.
5. Subtract annual need from net food availability.
6. Set `Kemampuan Ekspor` to `1` only for positive surplus and `0` otherwise.
7. When aggregating, label the result explicitly as signed or positive-only.
8. Treat the Kota Solok absorption estimate as a separate scenario using its stated homogeneity assumption.
9. Keep spatial joins and CRS transformations separate from the arithmetic method.

No legacy script or notebook was run during migration. A read-only one-off arithmetic audit was performed only to test consistency between the existing worksheet fields and the reconstructed formulas. No result is declared independently validated.

## Output Definition

- Annual local consumption need per row in kg and tons.
- Potential exportable surplus per row in tons.
- Binary `Kemampuan Ekspor` indicator.
- Signed and positive-only aggregate surplus, when requested explicitly.
- Theoretical Kota Solok absorption and its denominator-sensitive share.
- Optional spatial representation joined to the legacy administrative geometry.

Legacy derived outputs include:

- `Porto-Enclave-City/info/EC-info-padi-slk.geojson`
- `Porto-Enclave-City/info/EC-info-padi-slk-wgs84.geojson`
- `03-Work/MBA-Deep-Research/ENCL-masterdata-padi-slk.geojson`
- `05-Images/ENCL-bivariate-padi-slk*.png`

## Validation and Diagnostic Checks

- Annual need values are consistent with `population * weekly consumption * 52 / 1000` within display rounding for the non-city rows.
- `Potential Exportable Surplus` is consistent with net food availability minus the unrounded annual need within display rounding.
- `Kemampuan Ekspor` follows the sign of the surplus field.
- The signed and positive-only aggregates differ materially; aggregation convention must therefore be stated.
- Upstream conversion factors are not independently validated.
- The three low-ratio food-availability values remain unresolved.
- The projected padi GeoJSON declares EPSG:32747.
- The file named `EC-info-padi-slk-wgs84.geojson` contains lon/lat-looking coordinates but declares `urn:ogc:def:crs:EPSG::32747`; this CRS inconsistency remains unresolved.
- The spatial output embeds a local Windows source path and depends on a legacy `adm_kab_solok_kec` geometry whose independent provenance is incomplete.

## Limitations and Known Failure Modes

- The source publication, observation year, release version, and original units are incompletely documented. The year 2025 is only stated in the legacy chart footer.
- The table mixes agricultural production units, population, and contextual demographic fields without a complete data dictionary.
- The row-level consumption treatment excludes the city rows despite their population values.
- The city absorption estimate assumes that the Kabupaten Solok rate is a defensible proxy for Kota Solok and does not represent observed trade or consumption.
- The balance does not model seed, feed, post-harvest loss, stocks, imports, exports, storage, price, transport, or actual market destinations.
- Positive surplus does not establish that a surplus reaches Pasar Raya Solok or any other market.
- Spatial proximity to Kota Solok is an interpretation that requires separate boundary and market evidence; it is not produced by this arithmetic method.
- Reprojected or WGS84 outputs are derived products and must not be treated as raw data.

## Legacy Provenance

- `03-Work/MBA-Deep-Research/ENCL-mastersheet-padi-slk.csv`
- `03-Work/MBA-Deep-Research/ENCL-masterdata-padi-slk.geojson`
- `03-Work/MBA-Deep-Research/ENCL-masterdata-padi-slk.qmd`
- `Porto-Enclave-City/info/EC-info-padi.md`
- `Porto-Enclave-City/info/EC-info-padi-slk.geojson`
- `Porto-Enclave-City/info/EC-info-padi-slk-wgs84.geojson`
- `Porto-Enclave-City/info/EC-info-padi-slk.qmd`
- `03-Work/MBA-data.md`
- `Porto-Enclave-City/info/EC-info-data.md`
- `03-Work/MBA-Drafts/charts-enclave-v3/charts/gambar-peta-padi-slk.ts`

Companion legacy-derived tidak dipertahankan di target. File asli tetap tersedia melalui path legacy di atas dan tetap menjadi provenance untuk material terolah yang belum dipromosikan menjadi data raw canonical atau hasil tervalidasi.
