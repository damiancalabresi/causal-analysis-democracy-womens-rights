"""
Causal DAG: Democracy, Civil Society & Women's Rights → Women's Legal Rights (WBL)

Sources:
  - Behr et al. (2024) World Bank Policy Research Working Paper 10788
  - Panel FE regression results (05_fixed_effects_regression.ipynb)
  - Granger causality results (04-granger-causality.ipynb)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(22, 11))
ax.set_xlim(0, 22)
ax.set_ylim(3.6, 15.2)
ax.axis("off")
ax.set_facecolor("white")
fig.patch.set_facecolor("white")

# ── Colour palette ─────────────────────────────────────────────────────────────
C_CONF  = "#7F8C8D"
C_INPUT = "#2471A3"
C_CIVIL = "#1A8A6E"
C_WOMEN = "#8E44AD"
C_MED   = "#D35400"
C_REST  = "#E74C3C"
C_ECON  = "#27AE60"
C_PROV  = "#E67E22"
C_INT   = "#922B21"
C_WBL   = "#2C3E50"

# ── Helpers ────────────────────────────────────────────────────────────────────
def node(ax, x, y, label, color, w=2.8, h=0.62, fs=9, tc="white"):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle="round,pad=0.08", facecolor=color, edgecolor="white",
        linewidth=1.5, alpha=0.93, zorder=3))
    ax.text(x, y, label, ha="center", va="center", fontsize=fs,
            color=tc, fontweight="bold", zorder=4, multialignment="center")

def arr(ax, x1, y1, x2, y2, color="#444", lw=1.8, ls="-", alpha=0.75,
        rad=0.0, label=None):
    from matplotlib.patches import FancyArrowPatch
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),
        arrowstyle="-|>", color=color, linewidth=lw, linestyle=ls,
        connectionstyle=f"arc3,rad={rad}", alpha=alpha, zorder=2,
        mutation_scale=13))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx, my, label, ha="center", va="center", fontsize=7.2,
                color=color, zorder=5,
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.0))

# ══════════════════════════════════════════════════════════════════════════════
# NODES
# ══════════════════════════════════════════════════════════════════════════════

# Col 1 - Confounders (x=1.9)
node(ax, 1.9, 12.5, "GDP per capita",   C_CONF, w=2.6, fs=8.5)
node(ax, 1.9, 10.8, "Fertility Rate",   C_CONF, w=2.6, fs=8.5)
node(ax, 1.9,  8.8, "Religion\n(Islam ↓ WBL)", C_CONF, w=2.6, h=0.72, fs=8.2)

# Col 2 - Political / Institutional Drivers (x=5.8)
node(ax, 5.8, 13.5, "Democracy\n(Polity2 / V-Dem)", C_INPUT, w=3.1, h=0.80, fs=9)
node(ax, 5.8, 11.0, "Civil Society\n(v2x_cspart)",  C_CIVIL, w=3.1, h=0.75, fs=9)
node(ax, 5.8,  8.1, "Women's Rights\nGroups\n(v2csgender)", C_WOMEN, w=3.1, h=0.95, fs=8.5)
# Interaction
node(ax, 5.8,  9.6, "Demo × CSO\nComplementarity",  C_INT,   w=3.0, h=0.72, fs=8.5)

# Col 3 - Mediators (x=10.5)
node(ax, 10.5, 13.5, "Female Legislators\n(v2lgfemleg)",          C_MED, w=3.0, h=0.75, fs=8.5)
node(ax, 10.5, 11.3, "Women Political\nEmpowerment\n(v2x_gender)", C_MED, w=3.0, h=0.95, fs=8.5)
node(ax, 10.5,  8.8, "Women Civil Society\n(v2x_gencs)",           C_MED, w=3.0, h=0.75, fs=8.5)

# Col 4 - WBL Outcomes (x=16.2)
node(ax, 16.2, 13.6, "Mobility",      C_REST, w=2.4, fs=9)
node(ax, 16.2, 12.4, "Assets",        C_REST, w=2.4, fs=9)
node(ax, 16.2, 11.2, "Marriage",      C_REST, w=2.4, fs=9)
node(ax, 16.2,  9.6, "Workplace",     C_ECON, w=2.4, fs=9)
node(ax, 16.2,  8.4, "Pay",           C_ECON, w=2.4, fs=9)
node(ax, 16.2,  7.2, "Entrepren.",    C_ECON, w=2.4, fs=9)
node(ax, 16.2,  5.5, "Parenthood",    C_PROV, w=2.4, fs=9)
node(ax, 16.2,  4.3, "Pension",       C_PROV, w=2.4, fs=9)

# Col 5 - WBL Index (x=20.3)
node(ax, 20.3, 9.0, "WBL\nIndex", C_WBL, w=2.3, h=0.8, fs=10)

# ══════════════════════════════════════════════════════════════════════════════
# ARROWS
# ══════════════════════════════════════════════════════════════════════════════

# ── Confounders → WBL (dashed grey, faint) ────────────────────────────────────
for yo in [13.6, 12.4, 11.2, 9.6, 8.4, 7.2]:
    arr(ax, 3.22, 12.5, 15.0, yo, color=C_CONF, lw=0.7, ls="--", alpha=0.25)
arr(ax, 3.22, 10.8, 15.0, 5.5, color=C_CONF, lw=1.0, ls="--", alpha=0.4,
    label="parental altruism")
arr(ax, 3.22,  8.8, 15.0, 11.2, color=C_CONF, lw=1.0, ls="--", alpha=0.4)
arr(ax, 3.22,  8.8, 15.0, 13.6, color=C_CONF, lw=1.0, ls="--", alpha=0.35)

# ── Democracy → Civil Society ──────────────────────────────────────────────────
arr(ax, 5.8, 13.1, 5.8, 11.38, color=C_INPUT, lw=2.2, alpha=0.85)

# ── Democracy + CSO → Interaction ─────────────────────────────────────────────
arr(ax, 5.8, 13.1, 5.8, 9.96, color=C_INPUT, lw=1.4, ls="--", alpha=0.6)
arr(ax, 5.8, 10.63, 5.8, 9.96, color=C_CIVIL, lw=1.4, ls="--", alpha=0.6)

# ── Democracy → Mediators ─────────────────────────────────────────────────────
arr(ax, 7.36, 13.5, 9.0,  13.5, color=C_INPUT, lw=2.2, alpha=0.85)        # → Female Leg
arr(ax, 7.36, 13.3, 9.0,  11.6, color=C_INPUT, lw=1.6, alpha=0.7, rad=0.12) # → WPE
arr(ax, 7.36, 13.1, 9.0,   9.1, color=C_INPUT, lw=1.2, alpha=0.5, rad=0.18) # → WCS

# ── Civil Society → Mediators ─────────────────────────────────────────────────
arr(ax, 7.36, 11.0, 9.0, 11.3, color=C_CIVIL, lw=2.0, alpha=0.85)         # → WPE
arr(ax, 7.36, 10.8, 9.0,  8.8, color=C_CIVIL, lw=1.6, alpha=0.75, rad=0.08) # → WCS

# ── Women's Rights Groups → Mediators ─────────────────────────────────────────
arr(ax, 7.36, 8.1, 9.0, 8.8, color=C_WOMEN, lw=2.0, alpha=0.85)           # → WCS
arr(ax, 7.36, 8.4, 9.0, 11.1, color=C_WOMEN, lw=1.6, alpha=0.7, rad=-0.12) # → WPE

# ── Interaction → WBL (amplified, dotted) ─────────────────────────────────────
for yo in [12.4, 11.2, 9.6, 8.4, 7.2]:
    arr(ax, 7.3, 9.6, 15.0, yo, color=C_INT, lw=0.9, ls=":", alpha=0.45, rad=0.03)

# ── Democracy → WBL (direct) ──────────────────────────────────────────────────
# Economic (strong, solid)
arr(ax, 7.36, 13.7, 15.0, 9.6,  color=C_INPUT, lw=2.4, alpha=0.80, rad=0.04)
# , label="strong (paper + FE)")
arr(ax, 7.36, 13.6, 15.0, 8.4,  color=C_INPUT, lw=2.4, alpha=0.80, rad=0.06)
arr(ax, 7.36, 13.5, 15.0, 7.2,  color=C_INPUT, lw=2.4, alpha=0.80, rad=0.08)
# Restrictions (moderate)
arr(ax, 7.36, 13.8, 15.0, 12.4, color=C_INPUT, lw=1.6, alpha=0.70, rad=-0.04)
arr(ax, 7.36, 13.9, 15.0, 11.2, color=C_INPUT, lw=1.6, alpha=0.70, rad=-0.06)
# Enabling (weak/n.s., dashed)
arr(ax, 7.36, 13.2, 15.0, 5.5,  color=C_INPUT, lw=0.8, alpha=0.35, ls="--", rad=0.1)
arr(ax, 7.36, 13.1, 15.0, 4.3,  color=C_INPUT, lw=0.8, alpha=0.35, ls="--", rad=0.12)

# ── Civil Society → WBL (direct) ──────────────────────────────────────────────
arr(ax, 7.36, 11.2, 15.0, 9.6,  color=C_CIVIL, lw=2.1, alpha=0.80, rad=-0.04)  # Workplace
arr(ax, 7.36, 11.1, 15.0, 8.4,  color=C_CIVIL, lw=2.1, alpha=0.80, rad=-0.02)  # Pay
arr(ax, 7.36, 11.0, 15.0, 7.2,  color=C_CIVIL, lw=2.1, alpha=0.80)             # Entrepren.
# Borderline at lag 4 (p≈0.05), dashed
arr(ax, 7.36, 11.3, 15.0, 12.4, color=C_CIVIL, lw=1.0, alpha=0.50, ls="--", rad=0.04)
# n.s.: Mobility, Marriage, Parenthood, Pension - omitted

# ── Women's Rights Groups → WBL (direct) ──────────────────────────────────────
# Restrictions (strongest)
arr(ax, 7.36, 8.5, 15.0, 13.6, color=C_WOMEN, lw=2.3, alpha=0.85, rad=-0.2)
# , label="strongest:\nremove restrictions")
arr(ax, 7.36, 8.3, 15.0, 12.4, color=C_WOMEN, lw=2.1, alpha=0.80, rad=-0.12)
arr(ax, 7.36, 8.1, 15.0, 11.2, color=C_WOMEN, lw=2.1, alpha=0.80, rad=-0.06)
# Economic
arr(ax, 7.36, 7.8, 15.0, 9.6,  color=C_WOMEN, lw=1.9, alpha=0.75)
arr(ax, 7.36, 7.7, 15.0, 8.4,  color=C_WOMEN, lw=1.9, alpha=0.75)
arr(ax, 7.36, 7.6, 15.0, 7.2,  color=C_WOMEN, lw=1.9, alpha=0.75)
# Enabling (moderate)
arr(ax, 7.36, 7.4, 15.0, 5.5,  color=C_WOMEN, lw=1.5, alpha=0.65, rad=0.05)
# , label="moderate:\nenabling prov.")

# ── Female Legislators → WBL ─────────────────────────────────────────────────
arr(ax, 12.0, 13.5, 15.0, 13.6, color=C_MED, lw=2.6, alpha=0.90)           # Mobility ★★★
arr(ax, 12.0, 13.3, 15.0, 12.4, color=C_MED, lw=2.6, alpha=0.90)           # Assets ★★★
arr(ax, 12.0, 13.2, 15.0, 11.2, color=C_MED, lw=2.4, alpha=0.87, rad=0.05) # Marriage ★★★
arr(ax, 12.0, 13.4, 15.0,  9.6, color=C_MED, lw=2.4, alpha=0.87, rad=0.10) # Workplace ★★★
arr(ax, 12.0, 13.6, 15.0,  5.5, color=C_MED, lw=2.2, alpha=0.85, rad=0.15) # Parenthood ★★

# ── Women Political Empowerment → WBL ────────────────────────────────────────
arr(ax, 12.0, 11.3, 15.0, 11.2, color=C_MED, lw=2.0, alpha=0.80)           # Marriage
arr(ax, 12.0, 11.1, 15.0,  9.6, color=C_MED, lw=2.0, alpha=0.80)           # Workplace
arr(ax, 12.0, 11.0, 15.0,  8.4, color=C_MED, lw=2.0, alpha=0.80)           # Pay
arr(ax, 12.0, 11.4, 15.0, 12.4, color=C_MED, lw=1.8, alpha=0.75, rad=-0.05)# Assets

# ── Women Civil Society → WBL (FE confirmed) ──────────────────────────────────
arr(ax, 12.0, 8.9, 15.0, 13.6, color=C_MED, lw=1.8, alpha=0.78, rad=-0.18) # Mobility ★★
arr(ax, 12.0, 8.8, 15.0, 12.4, color=C_MED, lw=2.2, alpha=0.85, rad=-0.12)
# , label="FE confirmed")                                                     # Assets ★★★
arr(ax, 12.0, 8.75, 15.0, 11.2, color=C_MED, lw=2.1, alpha=0.83, rad=-0.08) # Marriage ★★★
arr(ax, 12.0, 8.7, 15.0,  9.6, color=C_MED, lw=2.2, alpha=0.85, rad=-0.04)  # Workplace ★★★
arr(ax, 12.0, 8.65, 15.0, 8.4, color=C_MED, lw=1.9, alpha=0.80)             # Pay

# ── WBL → Democracy FEEDBACK ─────────────────────────────────────────────────
arr(ax, 15.0, 8.3, 7.36, 11.3, color="#C0392B", lw=1.6, ls="--", alpha=0.65,
    rad=-0.35, label="feedback: Pay/\nEntrepreneur.→Demo")
arr(ax, 15.0, 7.1, 7.36, 11.1, color="#C0392B", lw=1.4, ls="--", alpha=0.55, rad=-0.4)

# ── WBL sub-indices → WBL Index ───────────────────────────────────────────────
for yo in [13.6, 12.4, 11.2, 9.6, 8.4, 7.2, 5.5, 4.3]:
    arr(ax, 17.4, yo, 19.15, 9.0, color=C_WBL, lw=0.9, alpha=0.30)

# ══════════════════════════════════════════════════════════════════════════════
# LABELS & ANNOTATIONS
# ══════════════════════════════════════════════════════════════════════════════

def col_header(ax, x, y, text, color):
    ax.text(x, y, text, ha="center", va="center", fontsize=8.5, color="white",
            fontweight="bold", zorder=6,
            bbox=dict(facecolor=color, edgecolor="none",
                      boxstyle="round,pad=0.35", alpha=0.88))

col_header(ax,  1.9, 14.5, "CONFOUNDERS /\nMODERATORS",  C_CONF)
col_header(ax,  5.8, 14.7, "POLITICAL &\nINSTITUTIONAL\nDRIVERS", C_INPUT)
col_header(ax, 10.5, 14.7, "MEDIATORS\n(representation)", C_MED)
col_header(ax, 16.2, 14.7, "WBL SUB-INDICES",  C_WBL)

# Outcome group labels
ax.text(18.0, 12.5, "← Removing\n   restrictions\n   (Mobility, Assets,\n   Marriage)",
        fontsize=8, color=C_REST, va="center", fontweight="bold")
ax.text(18.0,  7.4, "← Economic\n   rights\n   (Workplace, Pay,\n   Entrepren.)",
        fontsize=8, color=C_ECON, va="center", fontweight="bold")
ax.text(18.0,  4.9, "← Enabling\n   provisions\n   (Parenthood, Pension)",
        fontsize=8, color=C_PROV, va="center", fontweight="bold")

# Key insight box
# insight = (
#     "Structural findings (Behr et al. 2024  +  Panel FE & Granger results):\n"
#     "  • Democracy + Civil Society → strongest at removing legal restrictions (top-down channel)\n"
#     "  • Women's Rights Groups → uniquely effective for enabling provisions (Parenthood, etc.)\n"
#     "  • CSO effect is only robust inside democracies → complementarity (Demo × CSO interaction)\n"
#     "  • Female Legislators = strongest FE predictor: Marriage (β=0.38), Mobility, Assets, Workplace\n"
#     "  • Women Civil Society (v2x_gencs) → Assets★★★, Marriage★★★, Workplace★★★, Mobility★★, Pay\n"
#     "  • Civil Society (v2x_cspart) → Workplace/Pay/Entrepren. only; Mobility n.s. (FE p=0.45–0.53)\n"
#     "  • Pay & Entrepreneurship show bidirectional feedback loop with democracy\n"
#     "  • Islam → consistently lower WBL; Muslim democracies show negative Democracy → Mobility effect"
# )
# ax.text(0.01, 0.01, insight, transform=ax.transAxes, fontsize=8.2,
#         va="bottom", ha="left",
#         bbox=dict(facecolor="white", edgecolor="#AAAAAA",
#                   boxstyle="round,pad=0.5", alpha=0.93))

# ── Legend ─────────────────────────────────────────────────────────────────────
# handles = [
#     mpatches.Patch(color=C_INPUT, label="Democracy / Political institutions"),
#     mpatches.Patch(color=C_CIVIL, label="Civil Society (v2x_cspart)"),
#     mpatches.Patch(color=C_WOMEN, label="Women's Rights Groups (v2csgender)"),
#     mpatches.Patch(color=C_MED,   label="Mediators: representation"),
#     mpatches.Patch(color=C_INT,   label="Interaction: Demo × CSO"),
#     mpatches.Patch(color=C_REST,  label="WBL: Removing restrictions"),
#     mpatches.Patch(color=C_ECON,  label="WBL: Economic rights"),
#     mpatches.Patch(color=C_PROV,  label="WBL: Enabling provisions"),
#     mpatches.Patch(color=C_CONF,  label="Confounders / Moderators"),
#     plt.Line2D([0],[0], color="#444", lw=2.5,                label="Strong causal path"),
#     plt.Line2D([0],[0], color="#444", lw=1.0, ls="--",       label="Weak / n.s. / confounder"),
#     plt.Line2D([0],[0], color="#C0392B", lw=1.6, ls="--",    label="Feedback loop"),
#     plt.Line2D([0],[0], color=C_INT, lw=1.0, ls=":",         label="Complementarity (amplified)"),
# ]
# ax.legend(handles=handles, loc="lower right", fontsize=8, ncol=2,
#           framealpha=0.93, edgecolor="#AAAAAA",
#           bbox_to_anchor=(1.0, 0.0))

# ax.set_title(
#     "Causal DAG: Democracy, Civil Society & Women's Empowerment → Women's Legal Rights (WBL)\n"
#     "Based on: Behr et al. (2024) World Bank WP10788  ·  Panel FE regression  ·  Granger causality",
#     fontsize=12, fontweight="bold", pad=10
# )

plt.tight_layout()
plt.savefig("images/causal_dag.pdf", dpi=150, bbox_inches="tight", facecolor="white")
plt.savefig("images/causal_dag.png", dpi=150, bbox_inches="tight", facecolor="white")
print("Saved images/causal_dag.pdf and images/causal_dag.png")
