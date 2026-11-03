# ====================================================================
# Synopsys Sentaurus Inspect Command File: Post-Processing & Extraction
# Author: Nikunj Malik
# ====================================================================

# Load AC admittance and capacitance results
proj_load pmos_100nm_des.plt plt_100nm

# Plot Cgg (Total Gate Capacitance) vs Vgs
cv_create Cgg "plt_100nm gate TotalCapacitance" "plt_100nm gate InnerVoltage"
cv_create Cgs "plt_100nm gate source Capacitance" "plt_100nm gate InnerVoltage"
cv_create Cgd "plt_100nm gate drain Capacitance"  "plt_100nm gate InnerVoltage"

# Export formatted CSV data for external analysis
gr_export "ac_capacitances_100nm.csv" {Cgg Cgs Cgd} -format csv
