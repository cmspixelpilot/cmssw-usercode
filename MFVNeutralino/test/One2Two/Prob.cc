#include "Prob.h"
#include <cmath>
#include "Math/QuantFuncMathCore.h"

namespace jmt {
  interval clopper_pearson_binom(const double n_on, const double n_tot,
                                 const double alpha, const bool equal_tailed) {
    const double alpha_min = equal_tailed ? alpha/2 : alpha;

    interval i;
    i.success = !(n_on == 0 && n_tot == 0);
    i.value = n_on / n_tot;
    i.lower = 0;
    i.upper = 1;

    if (n_on > 0)         i.lower = ROOT::Math::beta_quantile  (alpha_min, n_on,     n_tot - n_on + 1);
    if (n_tot - n_on > 0) i.upper = ROOT::Math::beta_quantile_c(alpha_min, n_on + 1, n_tot - n_on);

    return i;
  }

  interval clopper_pearson_poisson_means_ratio(const double x, const double y,
                                               const double alpha, const bool equal_tailed) {
    const interval i_binom = clopper_pearson_binom(x, x+y, alpha, equal_tailed);
    const double rl = i_binom.lower;
    const double rh = i_binom.upper;
    interval i;
    i.success = i_binom.success && y != 0 && fabs(rh - 1) > 1e-9;
    i.value = i.success ? x/y : 0;
    i.lower = rl/(1-rl);
    i.upper = i.success ? rh/(1-rh) : 0;
    return i;
  }
}