# Sub-Micron p-Channel MOSFET Design, Characterization & Scaling Analysis
### Numerical Simulation of DC/AC Characteristics, Gate Capacitances, and Short-Channel Effects (100nm – 300nm) using Synopsys Sentaurus TCAD

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![TCAD: Synopsys Sentaurus](https://img.shields.io/badge/TCAD-Synopsys%20Sentaurus-red.svg)](https://www.synopsys.com/silicon/tcad.html)
[![Domain: Device Physics](https://img.shields.io/badge/Domain-Semiconductor%20Device%20Physics-orange.svg)](#)
[![Python: Verification](https://img.shields.io/badge/Python-Automation%20%26%20Extraction-green.svg)](scripts/extract_vth.py)

---

## Overview

This project presents a comprehensive 2D numerical simulation and device physics study of a sub-micron p-channel Metal-Oxide-Semiconductor Field-Effect Transistor (**p-MOSFET**) using the industry-standard **Synopsys Sentaurus TCAD** suite. 

The project evaluates:
1. **Full Baseline Device Characterization ($L = 100\text{ nm}$):** Static DC transfer ($I_d-V_{gs}$), output ($I_d-V_{ds}$) characteristics, and 1 MHz small-signal AC gate capacitance curves ($C_{gg}, C_{gs}, C_{gd}, C_{ds}$).
2. **Channel Length Scaling Analysis:** Parametric evaluation across $100\text{ nm}$, $200\text{ nm}$, and $300\text{ nm}$ gate lengths.
3. **Short-Channel Effects (SCE):** Quantitative extraction of threshold voltage roll-off via the **Constant Current Method** ($I_{crit} = 10^{-7} \times \frac{W}{L}$) and analysis of physical degradation mechanisms (Charge Sharing and Drain-Induced Barrier Lowering).

---

## Device Architecture & Parameters

The 2D device structure features an n-type bulk silicon substrate with abrupt, heavily doped p-type source and drain extensions.

<p align="center">
  <img src="docs/figures/mosfet_2d_structure_mesh.png" alt="2D MOSFET Mesh and Doping Profile" width="650"/>
  <br>
  <em>Figure 1: 2D p-MOSFET Sentaurus Visual structure mesh and net doping concentration distribution.</em>
</p>

### Key Simulation Parameters
| Parameter | Symbol | Value | Unit | Description |
| :--- | :---: | :---: | :---: | :--- |
| **Channel Length** | $L$ | 100, 200, 300 | $\text{nm}$ | Evaluated sub-micron gate lengths |
| **Device Width** | $W$ | 1.0 | $\mu\text{m}$ | Normalized device width |
| **Gate Oxide Thickness** | $t_{ox}$ | 10 | $\text{nm}$ | Thermally grown $\text{SiO}_2$ dielectric |
| **Substrate (Body) Doping** | $N_D$ | $1.0 \times 10^{16}$ | $\text{cm}^{-3}$ | Uniform n-type Phosphorus concentration |
| **Source / Drain Doping** | $N_A$ | $5.0 \times 10^{19}$ | $\text{cm}^{-3}$ | Degenerate p-type Boron concentration |
| **Gate Work Function** | $\Phi_m$ | 4.80 | $\text{eV}$ | Tuned mid-gap metal gate electrode |
| **AC Small-Signal Frequency**| $f$ | 1.0 | $\text{MHz}$ | Admittance analysis frequency |
| **Ambient Temperature** | $T$ | 300 | $\text{K}$ | Standard room temperature |

---

## TCAD Physical Models & Simulation Deck

The physical transport and electrostatic phenomena were solved in **Sentaurus Device (`sdevice`)** using coupled non-linear partial differential equations:
* **Carrier Transport:** Drift-Diffusion model coupled self-consistently with Poisson's equation and hole/electron continuity equations.
* **Mobility Modeling:** 
  * *Lombardi Surface Model (`Enormal`):* Accounts for acoustic phonon scattering and surface roughness degradation at the $\text{Si}/\text{SiO}_2$ interface.
  * *High-Field Velocity Saturation:* Models lateral velocity saturation of hole carriers in the pinch-off region.
* **Generation & Recombination:** Doping-dependent Shockley-Read-Hall (SRH) recombination and Auger recombination.
* **Carrier Statistics:** Fermi-Dirac statistics to accurately capture carrier freeze-out and high-density degeneracy in source/drain regions.

---

## Results & Discussion

### 1. High-Frequency AC Capacitance ($1\text{ MHz}$)
The dynamic gate admittance was probed at $1\text{ MHz}$ to extract terminal capacitance components as a function of gate bias $V_{gs}$.

<p align="center">
  <img src="docs/figures/ac_characteristics_1mhz.png" alt="AC Capacitance Curves" width="700"/>
  <br>
  <em>Figure 2: 1 MHz AC capacitance profiles (Total Gate Capacitance Cgg, Gate-Source Cgs, Gate-Drain Cgd, and Drain-Source Cds).</em>
</p>

* **Total Gate Capacitance ($C_{gg}$):** Displays the standard MOS C-V envelope. In **accumulation** ($V_{gs} > 0$), majority carrier electrons accumulate at the interface, yielding high capacitance ($C_{gg} \approx C_{ox}$). In **depletion** (near $0\text{ V}$), depletion charge depth increases in series with the oxide, causing $C_{gg}$ to dip. In strong **inversion** ($V_{gs} \ll V_{th}$), inversion holes populate the channel, pulling $C_{gg}$ back up to the oxide limit.
* **Terminal Coupling ($C_{gs}, C_{gd}$):** In the OFF state, coupling is restricted to parasitic metallurgical gate-to-diffusion overlap capacitance. As the conductive inversion layer bridges the channel, $C_{gs}$ and $C_{gd}$ increase symmetrically.
* **Parasitic Drain-Source Capacitance ($C_{ds}$):** Remains virtually constant and negligible across gate sweep, confirming clean junction isolation.

---

### 2. Static DC Transfer & Output Curves
DC sweeps were performed to map both linear and saturation operating boundaries.

<p align="center">
  <img src="docs/figures/dc_transfer_output_curves.png" alt="DC Transfer and Output Curves" width="750"/>
  <br>
  <em>Figure 3: Output characteristics (left: Id-Vds for varying Vgs) and Transfer characteristics (right: Id-Vgs at fixed Vds).</em>
</p>

* **$I_d-V_{gs}$ (Transfer):** Demonstrates steep subthreshold swing, low off-state leakage current ($I_{off}$), and a transition into quadratic saturation current as the gate potential exceeds the threshold point in the negative direction.
* **$I_d-V_{ds}$ (Output):** Clear transition from linear (ohmic) operation at low $|V_{ds}|$ (where channel inversion resistance dominates) into current saturation at higher $|V_{ds}|$ caused by carrier velocity saturation and channel pinch-off at the drain boundary.

---

### 3. Scaling Comparison & Threshold Voltage Roll-Off

Simulations were repeated for channel lengths $L = 200\text{ nm}$ and $L = 300\text{ nm}$ to study geometric scaling impacts.

<p align="center">
  <img src="docs/figures/simulation_results_200nm.png" alt="200nm Simulation Results" width="450"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/figures/simulation_results_300nm.png" alt="300nm Simulation Results" width="450"/>
  <br>
  <em>Figure 4: Sentaurus Visual multi-variable simulation monitors for L = 200nm (left) and L = 300nm (right).</em>
</p>

#### Threshold Voltage ($V_{th}$) Extraction (Constant Current Method)
To extract $V_{th}$ independent of subthreshold slope variations, the industry-standard **Constant Current Method** was applied:

$$I_{crit} = 10^{-7} \times \frac{W}{L}\ \text{[A]}$$

With $W = 1.0\ \mu\text{m}$:

| Channel Length ($L$) | Aspect Ratio ($W/L$) | Target $I_{crit}$ ($\mu\text{A}$) | Extracted $V_{th}$ ($\text{V}$) | Scaling Behavior |
| :---: | :---: | :---: | :---: | :--- |
| **$300\text{ nm}$** | 3.33 | $0.333\ \mu\text{A}$ | **$-0.396\text{ V}$** | Baseline long-channel control |
| **$200\text{ nm}$** | 5.00 | $0.500\ \mu\text{A}$ | **$-0.330\text{ V}$** | Gradual threshold roll-off |
| **$100\text{ nm}$** | 10.00 | $1.000\ \mu\text{A}$ | **$-0.296\text{ V}$** | Significant Short-Channel Effect ($|\Delta V_{th}| = 100\text{ mV}$) |

<p align="center">
  <img src="docs/figures/threshold_voltage_probes.png" alt="Vth Probing Curves" width="650"/>
  <br>
  <em>Figure 5: Sentaurus Inspect constant-current extraction probes for 100nm (-0.296V), 200nm (-0.330V), and 300nm (-0.396V).</em>
</p>

---

## Physical Mechanisms: Why Short-Channel Effects Occur

1. **Depletion Charge Sharing:** In a long-channel MOSFET, the gate voltage must support all depletion charge beneath the gate oxide to achieve inversion. As channel length reduces to $100\text{ nm}$, the depletion regions from the source and drain metallurgical junctions encroach upon the central channel. These junctions share the responsibility of depleting the channel, requiring a **smaller magnitude gate voltage** to trigger inversion. Consequently, $|V_{th}|$ rolls off from $0.396\text{ V}$ to $0.296\text{ V}$.
2. **Drain-Induced Barrier Lowering (DIBL):** In sub-micron geometries, the drain electrostatic field extends across the channel to lower the source-to-channel potential energy barrier. This accelerates hole carrier injection even at reduced gate potentials, resulting in $V_{th}$ shifts and elevated off-state leakage.

---

## Repository Structure

```text
pmos-tcad-characterization/
├── README.md                          # Comprehensive project documentation
├── LICENSE                            # MIT Open Source License
├── docs/
│   ├── technical_report.md            # In-depth technical report
│   └── figures/                       # High-resolution simulation plots & meshes
│       ├── ac_characteristics_1mhz.png
│       ├── dc_transfer_output_curves.png
│       ├── mosfet_2d_structure_mesh.png
│       ├── simulation_results_200nm.png
│       ├── simulation_results_300nm.png
│       └── threshold_voltage_probes.png
└── scripts/
    ├── sde_pmos.cmd                   # Sentaurus Structure Editor 2D meshing deck
    ├── sdevice_pmos.cmd               # Sentaurus Device DC/AC physics & solve deck
    ├── inspect.cmd                    # Sentaurus Inspect post-processing script
    └── extract_vth.py                 # Standalone Python script for Vth extraction
```

---

## Automated Verification

A standalone Python script is provided to verify and extract the threshold voltage parameters using standard library routines (no external dependencies required):

```bash
python3 scripts/extract_vth.py
```

**Output:**
```text
============================================================================
 Sub-Micron p-MOSFET Vth Extraction Summary (Constant Current Method)
 Formula: I_crit = 10^-7 * (W / L)  [A]
============================================================================
Device / Channel   | I_crit Target    | Extracted Vth  | Status
----------------------------------------------------------------------------
100nm pMOS         |    1.000 uA       |   -0.296 V     | Validated
200nm pMOS         |    0.500 uA       |   -0.330 V     | Validated
300nm pMOS         |    0.333 uA       |   -0.396 V     | Validated
============================================================================
```

---

## Author

**Nikunj Malik**  
- **GitHub:** [@nikunjmalik306](https://github.com/nikunjmalik306)  
- **LinkedIn:** [Nikunj Malik](https://linkedin.com/in/nikunjmalik)  

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
