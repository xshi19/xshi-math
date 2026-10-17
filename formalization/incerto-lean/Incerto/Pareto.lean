import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith

/-!
# Elementary Pareto identities

These declarations check the algebra used by the wiki. They do not construct
a probability measure or prove convergence of the improper moment integral.
-/

namespace Incerto

/-- The exponent comparison in the Pareto power-integral criterion.
This equivalence holds for all real moment orders and exponents. -/
theorem moment_exponent_threshold (p alpha : ℝ) :
    p - alpha - 1 < -1 ↔ p < alpha := by
  constructor <;> intro h <;> linarith

/-- The piecewise Pareto Type I survival expression, treated as a real function.
It represents a survival function when `xm > 0` and `alpha > 0`. -/
noncomputable def paretoSurvival (xm alpha x : ℝ) : ℝ :=
  if x < xm then 1 else (xm / x) ^ alpha

/-- Exact scaling when both thresholds are at or above the lower cutoff.
The shape hypothesis retains the Pareto parameter domain, although the
power identity itself holds for every real exponent. -/
theorem pareto_survival_scale (xm alpha x t : ℝ)
    (hxm : 0 < xm) (_halpha : 0 < alpha) (hx : xm ≤ x)
    (ht : 0 < t) (htx : xm ≤ t * x) :
    paretoSurvival xm alpha (t * x) / paretoSurvival xm alpha x = t ^ (-alpha) := by
  have hxpos : 0 < x := lt_of_lt_of_le hxm hx
  have hbase : 0 < xm / x := div_pos hxm hxpos
  unfold paretoSurvival
  rw [if_neg (not_lt.mpr htx), if_neg (not_lt.mpr hx)]
  rw [show xm / (t * x) = (xm / x) / t by
    rw [div_div, mul_comm x t]]
  rw [Real.div_rpow (le_of_lt hbase) (le_of_lt ht)]
  rw [div_right_comm, div_self (ne_of_gt (Real.rpow_pos_of_pos hbase alpha))]
  rw [one_div, Real.rpow_neg (le_of_lt ht)]

end Incerto
