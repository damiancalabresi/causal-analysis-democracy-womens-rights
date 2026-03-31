# References

## Empowering Change: Assessing the Role of Democracy, Civil Society, and Women’s Rights Groups in Advancing Legal Gender Equality

**Authors:** Daniela M. Behr, Caroline Perrin, Marie Hyland, Tea Trumbic
**Publisher:** World Bank, Policy Research Working Paper 10788
**Date:** June 2024

Files:
- [PDF](world_bank_empowering_change.pdf)
- [Text version](world_bank_empowering_change.txt)

Links:
- https://openknowledge.worldbank.org/entities/publication/08c77ac3-6120-4c3e-81fe-fd6ffdf52f5a

Reproducibility package: https://reproducibility.worldbank.org/catalog/147

### Summary

This paper investigates the role of a country’s political economy, civil society organizations (CSOs), and women’s rights groups in driving legal gender equality, using the World Bank’s Women, Business and the Law (WBL) time-series data across 190 economies and five decades (1970–2022). The authors estimate fixed-effects panel regressions with the WBL aggregate index and its eight sub-indicators (Mobility, Workplace, Pay, Marriage, Parenthood, Entrepreneurship, Assets, Pension) as dependent variables, lagging all explanatory variables by three years to reduce reverse causality. Democracy is measured with Polity V’s `polity2` score; civil society activity with V-Dem’s `v2x_cspart` index; and women’s rights group engagement with V-Dem’s `v2csgender` variable.

The main findings are: (1) higher levels of democracy are positively associated with legal gender equality, particularly in Workplace, Pay, Entrepreneurship, and Assets, but show no significant relationship with Mobility, Parenthood, or Pension; (2) a more active civil society is similarly correlated with higher gender equality across most sub-indicators, with the same pattern of stronger effects on economic participation rights and weaker effects on personal and social provisions; (3) active women’s rights groups specifically show the strongest association with legal gender equality of all three drivers, with the notable exception of Parenthood and Pension; and (4) an active civil society is most effective in fully democratic states, suggesting that bottom-up (civil society) and top-down (democratic institutions) channels are complementary rather than substitutes. Across all three drivers, effects are stronger for removing legal restrictions on women than for enacting enabling provisions such as maternity leave. Robustness checks including religion fixed effects (Islam is associated with lower gender equality) and alternative democracy measures confirm the main results.

The authors explicitly note that their analysis cannot establish causal relationships — the regressions identify correlations, not causal effects — which is a key motivation for the causal analysis in this project.

### Analysis

The  paper  shows that both democracy and civil society play a more prominent role in removing legal restrictions that are placed on  women  than  they  do  in  ensuring  rights  to  enabling  provisions, such as the right to maternity leave, and that women’s rights groups seem to be particularly important in this area.

democracy & civil_society_organizations -> less legal restrictions -> not more legal provisions

women's rights groups -> more legal provisions

civil_society_organizations, democracy -> positive interaction effect

legal restrictions -> prohibitions on a woman’s ability  to  travel  or  to  become  head  of  the  household
legal provisions -> equal pay or parental leave

confounders:
- gpd_per_capita
- fertility

