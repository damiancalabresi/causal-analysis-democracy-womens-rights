# Datasets

Raw source datasets used in this project. Processed/cleaned versions are in `../processed-datasets/`.

---

## Political Regime Characteristics and Transitions, 1800–2018

**Source:** Polity5 Project, Center for Systemic Peace
**Reference:** Marshall, Monty G. (2020). *POLITY5: Political Regime Characteristics and Transitions, 1800–2018. Dataset Users' Manual.* Center for Systemic Peace.

### Files

| File | Description |
|------|-------------|
| [p5v2018.xls](polity/p5v2018.xls) | Main dataset (country-year panel) |
| [p5manualv2018.pdf](polity/p5manualv2018.pdf) | Dataset users' manual |

### Coverage

| | |
|---|---|
| Years | 1776–2018 |
| Countries | 195 unique polities (including historical/defunct states) |
| Observations | ~17,500 country-years |

### Key Variables

| Variable | Range | Description |
|----------|-------|-------------|
| `polity2` | −10 to +10 | **Revised Combined Polity Score.** Primary democracy/autocracy index. Regimes: full democracy (+6 to +10), anocracy (−5 to +5), autocracy (−10 to −6). |
| `democ` | 0–10 | Institutionalized Democracy index |
| `autoc` | 0–10 | Institutionalized Autocracy index |
| `exrec` | 1–8 | Executive Recruitment Concept (how the chief executive comes to power) |
| `exconst` | 1–7 | Executive Constraints Concept (limits on executive authority) |
| `polcomp` | 1–10 | Political Competition Concept (regulation and competitiveness of participation) |
| `regtrans` | — | Regime Transition Category (populated only in transition years) |

Special authority codes `−66` (interruption), `−77` (interregnum), `−88` (transition) replace numeric scores when normal coding is not applicable. `polity2` converts these to usable values and should be preferred for quantitative analysis.

---

## V-Dem Dataset

**Source:** Varieties of Democracy (V-Dem) Project, version 16
**Reference:** Coppedge, Michael et al. (2025). *V-Dem Dataset v16.* Varieties of Democracy (V-Dem) Project.

The world's most comprehensive and detailed democracy ratings.

### Files

| File | Description |
|------|-------------|
| [V-Dem-CY-Core-v16.csv](v-dem/V-Dem-CY-Core-v16.csv) | Country-Year core variables |
| [codebook.pdf](v-dem/codebook.pdf) | Full variable codebook |
| [whats_new.pdf](v-dem/whats_new.pdf) | Changes since previous version |
| [cautionary_notes.pdf](v-dem/cautionary_notes.pdf) | Notes on appropriate use |
| [suggested_citation.pdf](v-dem/suggested_citation.pdf) | Citation guidance |

### Coverage

| | |
|---|---|
| Years | 1789–2025 |
| Countries | 202 unique polities (including historical/defunct states) |
| Observations | ~28,000 country-years |

### Key Variables

All continuous indices are scaled **0–1** (higher = more democratic / more rights) unless noted.

**Democracy Indices (Treatment Variables)**

| Variable | Description |
|----------|-------------|
| `v2x_polyarchy` | Electoral Democracy Index |
| `v2x_libdem` | Liberal Democracy Index |
| `v2x_partipdem` | Participatory Democracy Index |
| `v2x_delibdem` | Deliberative Democracy Index |
| `v2x_egaldem` | Egalitarian Democracy Index |

**Women's Rights Outcomes**

| Variable | Description |
|----------|-------------|
| `v2x_gender` | Women Political Empowerment Index (aggregate) |
| `v2x_gencl` | Women Civil Liberties Index |
| `v2x_gencs` | Women Civil Society Participation Index |
| `v2x_genpp` | Women Political Participation Index |
| `v2xpe_exlgender` | Political Exclusion by Gender (⚠️ inverted: higher = worse) |
| `v2lgfemleg` | Female Legislators (%, range 0–100) |

---

## Women, Business and the Law 1.0 Data for 1971–2024

**Source:** World Bank, Women, Business and the Law project
**Reference:** World Bank (2024). *Women, Business and the Law 1.0 Historical Panel Data.* DOI: https://doi.org/10.57966/gtdw-yp27

Tracks laws and regulations affecting women's economic opportunities across 190+ economies since 1971. Scores are based on binary indicators (legal provisions present or absent) across eight thematic areas.

### Files

| File | Description |
|------|-------------|
| [WBL2024-1-0-Historical-Panel-Data.xlsx](wbl/WBL2024-1-0-Historical-Panel-Data.xlsx) | Main historical panel dataset |

### Coverage

| | |
|---|---|
| Years | 1971–2024 |
| Countries | 190 economies |
| Observations | ~9,120 country-years (processed subset through 2018) |

### Key Variables

| Variable | Range | Description |
|----------|-------|-------------|
| `wbl_index` | 0–100 | **Overall WBL Index.** Average of the eight area scores below. |
| `mobility` | 0–100 | Freedom of movement (passport, travel, residence) |
| `workplace` | 0–100 | Workplace protections (job access, discrimination, harassment) |
| `pay` | 0–100 | Equal pay provisions |
| `marriage` | 0–100 | Marriage and family laws (divorce, domestic violence) |
| `parenthood` | 0–100 | Maternity/paternity leave and pregnancy protections |
| `entrepreneurship` | 0–100 | Access to credit, contracts, business registration |
| `assets` | 0–100 | Property and inheritance rights |
| `pension` | 0–100 | Pension and retirement parity |

Each area score is derived from binary (True/False) legal indicators. See individual indicator columns (e.g., `law_equal_pay`, `paid_maternity_leave_14weeks`) for the underlying provisions.

---

## Religious Composition by Country, 2010–2050

**Source:** Pew Research Center, Global Religious Futures Project
**Reference:** Pew Research Center (2012). *Global Religious Diversity.* Pew Research Center.

Estimates of religious composition for 230 countries and territories, based on censuses, surveys, and demographic modeling. Used in this project as a control variable (religious fractionalization).

### Files

| File | Description |
|------|-------------|
| [Religious_Composition_by_Country_2010-2050.xlsx](pew-research-center/Religious_Composition_by_Country_2010-2050.xlsx) | Full Pew dataset with projections to 2050 |
| [religious-diversity-index.csv](pew-research-center/religious-diversity-index.csv) | Simplified CSV (2010 snapshot): RDI + share per religion |
| [religious-diversity-index-extended.csv](pew-research-center/religious-diversity-index-extended.csv) | Extended CSV with dominant religion and majority flags |

### Coverage

| | |
|---|---|
| Reference year | 2010 (with projections to 2050 in the Excel file) |
| Countries | 230 countries and territories |

### Key Variables (Extended CSV)

| Variable | Description |
|----------|-------------|
| `rdi` | **Religious Diversity Index.** Herfindahl-based fractionalization index (0 = perfectly homogeneous, 10 = maximum diversity) |
| `christian`, `muslim`, `unaffiliated`, `hindu`, `buddhist`, `folk`, `other`, `jewish` | Population share of each religious group (0–1) |
| `dominant_religion` | Largest religious group in the country |
| `maj_christian`, `maj_muslim`, … | Binary flag: 1 if that religion comprises a majority (>50%) |

Because this dataset covers only a single point in time (2010), it is used as a time-invariant control in panel regressions.
