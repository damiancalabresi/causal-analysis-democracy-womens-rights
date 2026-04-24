# V-Dem - Processed Dataset

**Source:** Varieties of Democracy (V-Dem) Project, version 16
**Original file:** `V-Dem-CY-Core-v16.csv` (country-year, core variables)
**Reference:** Coppedge, Michael et al. (2025). *V-Dem Dataset v16.* Varieties of Democracy (V-Dem) Project.

## Coverage

| | |
|---|---|
| Years | 1789–2025 |
| Countries | 202 unique polities (including historical/defunct states) |
| Observations | 28,092 country-years |

## Notes

- All continuous indices are scaled **0–1** (higher = more democratic / more rights) unless noted.
- `v2xpe_exlgender` is **inverted**: higher values mean greater political exclusion by gender (i.e., worse outcomes for women). Negate before combining with other women's rights measures.
- Historical/defunct states (Soviet Union, Yugoslavia, Czechoslovakia, etc.) have `iso3c = null`.
- `COWcode` has no nulls in this processed file. Entities missing a COW code in the original V-Dem source have been assigned codes as described below.

### COW Code Assignment

Entities without a COW code in the original V-Dem data were assigned codes as follows:

| Entity | COWcode | Rationale |
|--------|---------|-----------|
| Papal States | 327 | Reuses existing Polity5 COW code (same entity) |
| Tuscany | 337 | Reuses existing Polity5 COW code (same entity) |
| Piedmont-Sardinia | 324 | Reuses Polity5 "Sardinia" code (same entity, different name) |
| Hesse-Darmstadt | 275 | Extended from existing V-Dem code (partial years had 275) |
| Zanzibar | 511 | Extended from existing V-Dem code (partial years had 511) |
| Brunswick | 1001 | New code (≥ 1001, no COW collision) |
| Hamburg | 1002 | New code (≥ 1001, no COW collision) |
| Hong Kong | 1004 | New code (≥ 1001, no COW collision) |
| Nassau | 1005 | New code (≥ 1001, no COW collision) |
| Oldenburg | 1006 | New code (≥ 1001, no COW collision) |
| Palestine/British Mandate | 1007 | New code (≥ 1001, no COW collision) |
| Palestine/Gaza | 1008 | New code (≥ 1001, no COW collision) |
| Palestine/West Bank | 1009 | New code (≥ 1001, no COW collision) |
| Saxe-Weimar-Eisenach | 1010 | New code (≥ 1001, no COW collision) |
| Somaliland | 1011 | New code (≥ 1001, no COW collision) |

## Fields

### Identifiers

| Column | Type | Description |
|--------|------|-------------|
| `COWcode` | float | **COW Numeric Country Code.** Correlates of War numeric identifier. Use to merge with Polity5 (`ccode`) and other COW datasets. `null` for non-COW entities. |
| `country_text_id` | str | **V-Dem Country Code.** Three-letter ISO-like code used natively in V-Dem (e.g. `MEX`, `USA`). Not always identical to ISO 3166-1 alpha-3. |
| `iso3c` | str | **ISO 3166-1 alpha-3.** Added during processing via `country_converter`. `null` for historical/defunct states. |
| `country_name` | str | **Country name** as used in V-Dem. |
| `year` | int | **Year coded.** |

### Democracy Indices (Treatment Variables)

All five indices range 0–1 (higher = more democratic).

| Column | Type | Description |
|--------|------|-------------|
| `v2x_polyarchy` | float | **Electoral Democracy Index.** Measures the extent to which the ideal of electoral democracy is achieved. Core components: elected officials, clean elections, freedom of expression, associational autonomy, and universal suffrage. |
| `v2x_libdem` | float | **Liberal Democracy Index.** Combines electoral democracy with protection of individual and minority rights, and constraints on the executive via rule of law and independent judiciary. |
| `v2x_partipdem` | float | **Participatory Democracy Index.** Emphasizes active citizen participation beyond voting: civil society organizations, direct democracy, and subnational elected bodies. |
| `v2x_delibdem` | float | **Deliberative Democracy Index.** Focuses on the quality of public reasoning: whether political decisions are justified through reasoned debate rather than coercion or narrow interests. |
| `v2x_egaldem` | float | **Egalitarian Democracy Index.** Combines electoral democracy with equal distribution of political power across social groups (gender, ethnicity, income). |

### Women's Rights Outcomes

| Column | Type | Description |
|--------|------|-------------|
| `v2x_gender` | float | **Women Political Empowerment Index.** Aggregate of civil liberties (`v2x_gencl`), civil society participation (`v2x_gencs`), and political participation (`v2x_genpp`) for women. Range 0–1. |
| `v2x_gencl` | float | **Women Civil Liberties Index.** Aggregates women's freedom of movement, freedom from forced labour, property rights, and freedom from discrimination. Range 0–1. |
| `v2x_gencs` | float | **Women Civil Society Participation Index.** Extent to which women participate in civil society organizations. Range 0–1. |
| `v2x_genpp` | float | **Women Political Participation Index.** Extent to which women participate in formal political institutions (legislature, executive, judiciary). Range 0–1. |
| `v2xpe_exlgender` | float | **Political Exclusion by Gender Index.** ⚠️ **Inverted scale**: higher = greater exclusion of women from political power. Range 0–1. Negate when combining with other women's rights measures. |
| `v2lgfemleg` | float | **Female Legislators (%).** Share of women among members of the lower (or unicameral) chamber of the legislature. Range 0–100. |

### Component Women's Indicators

Individual survey-based measures (interval scale, typically −5 to +5 in raw form, standardized to a continuous scale in the dataset).

| Column | Type | Description |
|--------|------|-------------|
| `v2cldmovew` | float | **Freedom of Domestic Movement for Women.** Extent to which adult women can move freely throughout the country. |
| `v2clslavef` | float | **Freedom from Forced Labour for Women.** Extent to which women are free from forced labour, including trafficking and debt bondage. |
| `v2clprptyw` | float | **Property Rights for Women.** Extent to which women enjoy the same property rights as men (inheritance, land, assets). |
| `v2cldiscw` | float | **Freedom from Discrimination for Women.** Extent to which women are free from socioeconomic and political discrimination. |
| `v2pepwrgen` | float | **Power Distributed by Gender.** Extent to which political power is distributed equally between men and women. |
| `v2peapsgen` | float | **Political Participation by Gender.** Extent to which women and men have equal access to political participation. |
| `v2peasjgen` | float | **Access to State Jobs by Gender.** Extent to which women and men have equal access to public sector employment. |
| `v2peasbgen` | float | **Access to State Business by Gender.** Extent to which women and men have equal access to state business opportunities and contracts. |
| `v2csgender` | float | **CSO Women's Participation.** Extent to which women participate in civil society organizations relative to men. |
| `v2mefemjrn` | float | **Female Journalists.** Extent to which women are represented among journalists and media professionals. |

### Mechanisms

| Column | Type | Description |
|--------|------|-------------|
| `v2x_cspart` | float | **Civil Society Participation Index.** Extent to which people participate in civil society organizations and whether CSOs are able to operate freely. Range 0–1. |
| `v2x_frassoc_thick` | float | **Freedom of Association (thick).** Combines freedom to organize parties, CSOs, and other associations with the actual realization of this freedom. Range 0–1. |
| `v2x_freexp_altinf` | float | **Freedom of Expression and Alternative Information.** Extent to which the government respects press freedom and citizens' access to alternative information sources. Range 0–1. |
| `v2x_suffr` | float | **Suffrage.** Share of adult population with the legal right to vote (takes into account gender, ethnic, and wealth-based exclusions). Range 0–1. |
| `v2xlg_legcon` | float | **Legislative Constraints on Executive.** Extent to which the legislature formally constrains executive power and exercises oversight in practice. Range 0–1. |
| `v2x_jucon` | float | **Judicial Constraints on Executive.** Extent to which the judiciary independently constrains executive action and enforces rule-of-law norms. Range 0–1. |
| `v2xeg_eqprotec` | float | **Equal Protection Index.** Extent to which laws are applied equally and individuals are equally protected from state and private violence. Range 0–1. |
| `v2xeg_eqaccess` | float | **Equal Access Index.** Extent to which public goods and services are distributed equally across social groups. Range 0–1. |

### Controls

| Column | Type | Description |
|--------|------|-------------|
| `v2x_corr` | float | **Political Corruption Index.** Extent of political corruption across executive, legislative, and judicial branches. Range 0–1 (higher = more corrupt). |
| `v2x_rule` | float | **Rule of Law Index.** Extent to which laws are transparently and equally enforced, and state agents are accountable to the law. Range 0–1. |
| `v2xeg_eqdr` | float | **Equal Distribution of Resources Index.** Extent to which income, land, and other resources are distributed equally across society. Range 0–1. |
