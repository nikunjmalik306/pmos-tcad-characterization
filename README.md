# Sub-Micron p-Channel MOSFET Design, Characterization & Scaling Analysis
### Numerical TCAD Simulation of DC/AC Characteristics, Gate Capacitances, and Short-Channel Effects (100nm – 300nm) using Synopsys Sentaurus

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![TCAD: Synopsys Sentaurus](https://img.shields.io/badge/TCAD-Synopsys%20Sentaurus-red.svg)](https://www.synopsys.com/silicon/tcad.html)
[![Domain: Device Physics](https://img.shields.io/badge/Domain-Semiconductor%20Device%20Physics-orange.svg)](#)
[![Python: Verification](https://img.shields.io/badge/Python-Automation%20%26%20Extraction-green.svg)](scripts/extract_vth.py)
[![Author: Nikunj Malik](https://img.shields.io/badge/Author-Nikunj%20Malik-blueviolet.svg)](#author)

---

## Executive Summary & Objectives

This project presents a comprehensive 2D numerical device simulation and semiconductor physics investigation of a sub-micron p-channel Metal-Oxide-Semiconductor Field-Effect Transistor (**p-MOSFET**) using the industry-standard **Synopsys Sentaurus TCAD** suite (`sde`, `sdevice`, `inspect`, and `svisual`).

The study focuses on two primary objectives:
1. **Device Characterization (Baseline $L = 100\text{ nm}$):**
   * **DC Operation:** Mapping transfer characteristics ($I_d-V_{gs}$) and output characteristics ($I_d-V_{ds}$) to examine subthreshold behavior, linear ohmic conduction, and saturation.
   * **AC Small-Signal Behavior (1 MHz):** Extracting voltage-dependent gate admittance and terminal capacitances ($C_{gg}, C_{gs}, C_{gd}, C_{ds}$) across accumulation, depletion, and strong inversion regimes.
2. **Channel Length Scaling & Short-Channel Effects (SCEs):**
   * Evaluating geometric scaling across $100\text{ nm}$, $200\text{ nm}$, and $300\text{ nm}$ channel lengths while keeping gate oxide thickness ($t_{ox} = 10\text{ nm}$), substrate doping, and source/drain doping uniform.
   * Quantifying **Threshold Voltage ($V_{th}$) Roll-Off** using the standardized **Constant Current Method** ($I_{crit} = 10^{-7} \times \frac{W}{L}$).
   * Analyzing underlying physical degradation mechanisms: **Depletion Charge Sharing** and **Drain-Induced Barrier Lowering (DIBL)**.

---

## Device Architecture & Specifications

The 2D device structure features an n-type bulk silicon substrate with heavily doped p-type source and drain extension regions, separated by a thermally grown silicon dioxide ($\text{SiO}_2$) gate insulator.

<p align="center">
  <img src="docs/figures/mosfet_2d_structure_mesh.png" alt="2D MOSFET Mesh and Doping Profile" width="700"/>
  <br>
  <em>Figure 1: 2D p-MOSFET Sentaurus Visual structure mesh and net active doping concentration distribution ($N_D = 10^{16}\ \text{cm}^{-3}$ n-substrate, $N_A = 5 \times 10^{19}\ \text{cm}^{-3}$ p+ source/drain).</em>
</p>

### Table 1: MOSFET Design & Simulation Parameters
| Parameter | Symbol | Value | Unit | Description / Physical Role |
| :--- | :---: | :---: | :---: | :--- |
| **Device Type** | -- | p-channel MOSFET | -- | Inversion-mode hole carrier transistor |
| **Channel Length** | $L$ | **100, 200, 300** | $\text{nm}$ | Evaluated sub-micron gate lengths |
| **Device Width** | $W$ | 1.0 | $\mu\text{m}$ | Normalized device width for current scaling |
| **Gate Oxide Thickness** | $t_{ox}$ | 10 | $\text{nm}$ | Thermally grown $\text{SiO}_2$ dielectric insulator |
| **Substrate (Body) Doping** | $N_D$ | $1.0 \times 10^{16}$ | $\text{cm}^{-3}$ | Uniform n-type Phosphorus concentration |
| **Source / Drain Doping** | $N_A$ | $5.0 \times 10^{19}$ | $\text{cm}^{-3}$ | Degenerate p-type Boron concentration |
| **Gate Work Function** | $\Phi_m$ | 4.80 | $\text{eV}$ | Tuned mid-gap metal gate electrode |
| **AC Small-Signal Frequency**| $f$ | 1.0 | $\text{MHz}$ | Small-signal admittance analysis frequency ($\omega = 2\pi \times 10^6\ \text{rad/s}$) |
| **Small-Signal Amplitude** | $v_{ac}$ | 10 | $\text{mV}$ | AC perturbation voltage |
| **Ambient Temperature** | $T$ | 300 | $\text{K}$ | Standard room temperature operating condition |

---

## Circuit Schematics & Simulation Setup

To simulate both static DC characteristics and high-frequency dynamic AC admittance, the device was connected in a dedicated TCAD simulation circuit testbench.

<p align="center">
  <img src="docs/figures/circuit_schematic.png" alt="p-MOSFET Characterization and Capacitance Circuits" width="880"/>
  <br>
  <em>Figure 2: (A) TCAD Simulation Testbench circuit for DC voltage sweeps and 1 MHz small-signal AC admittance probing. (B) High-frequency small-signal capacitance equivalent circuit model showing terminal capacitances ($C_{gs}, C_{gd}, C_{ds}, C_{gb}, C_{db}, C_{sb}$).</em>
</p>

### Circuit Configurations & Terminal Connectivity

#### 1. DC & AC Simulation Testbench Circuit (Figure 2A)
* **Source (S) Terminal:** Tied to reference ground ($V_S = 0.0\text{ V}$).
* **Substrate / Bulk (B) Terminal:** Tied directly to the source terminal ($V_B = V_S = 0.0\text{ V}$) ensuring zero substrate body bias ($V_{BS} = 0\text{ V}$) to prevent extraneous body effect shifts.
* **Drain (D) Terminal:** Connected to a variable DC voltage supply ($V_{DS}$) through an ammeter ($I_D$) to measure channel current. Swept from $0.0\text{ V}$ down to $-1.5\text{ V}$.
* **Gate (G) Terminal:** Connected to a compound excitation network consisting of a variable DC gate bias ($V_{GS}$, swept from $0.0\text{ V}$ down to $-1.5\text{ V}$) superposed with a small-signal AC voltage source ($v_{ac} = 10\text{ mV}$ sinusoidal at $f = 1\text{ MHz}$).

#### 2. High-Frequency Small-Signal Capacitance Equivalent Circuit (Figure 2B)
In Sentaurus Device, small-signal AC analysis solves the linearized complex admittance matrix $Y(\omega) = G(\omega) + j\omega C(\omega)$:
* **Gate-to-Source Capacitance ($C_{gs}$):** Composed of gate-to-source metallurgical overlap capacitance ($C_{ov}$) plus the forward portion of the channel inversion charge.
* **Gate-to-Drain Capacitance ($C_{gd}$):** Composed of gate-to-drain overlap capacitance plus the drain-end channel inversion charge.
* **Gate-to-Bulk Capacitance ($C_{gb}$):** Dominates in the accumulation regime where majority electrons accumulate at the $\text{Si}/\text{SiO}_2$ interface.
* **Drain-to-Source Capacitance ($C_{ds}$):** Small parasitic capacitance between source and drain diffusions.
* **Total Gate Capacitance ($C_{gg}$):**
  $$C_{gg} = C_{gs} + C_{gd} + C_{gb} = \frac{\partial Q_{gate}}{\partial V_{gs}}$$

```
                      +-------------------+
                      |      Gate (G)     |
                      +---+-----------+---+
                          |           |
                        [Cgs]       [Cgd]
                          |           |
      +-------------------+           +-------------------+
      |   Source (S)      |<---[Cds]-->|     Drain (D)     |
      +---+---------------+           +---+---------------+
          |       |                       |       |
        [Csb]    GND                    [Cdb]  (Ammeter)
          |                               |       |
      +---+-------------------------------+--+  [Vds]
      |              Body / Bulk (B)          |   |
      +---------------------------------------+  GND
```

---

## TCAD Numerical Physics Models

The physical transport and electrostatic phenomena were solved self-consistently in **Sentaurus Device (`sdevice`)** by coupling non-linear partial differential equations:
* **Carrier Transport:** Drift-Diffusion transport coupled self-consistently with Poisson's equation and hole/electron continuity equations.
* **Inversion-Layer Mobility Modeling:**
  * *Lombardi Surface Model (`Enormal`):* Incorporates acoustic surface phonon scattering and surface roughness degradation at the $\text{Si}/\text{SiO}_2$ boundary.
  * *High-Field Velocity Saturation:* Solves carrier velocity saturation under high tangential electric fields at the drain end.
* **Generation & Recombination:** Doping-dependent Shockley-Read-Hall (SRH) recombination combined with Auger recombination.
* **Carrier Statistics:** Fermi-Dirac statistics for accurate modeling of degenerate carrier populations in the source/drain diffusions.

---

## Results & Discussion

### 1. High-Frequency AC Gate Capacitance Characteristics (1 MHz)

Dynamic admittance analysis was performed at $1\text{ MHz}$ to extract terminal capacitances as a function of gate bias $V_{gs}$ for the baseline $100\text{ nm}$ p-MOSFET.

<p align="center">
  <img src="docs/figures/ac_characteristics_1mhz.png" alt="AC Capacitance Curves at 1 MHz" width="750"/>
  <br>
  <em>Figure 3: 1 MHz AC capacitance profiles for 100nm p-MOSFET: Plot 1: Total Gate Capacitance (Cgg), Plot 2 & 3: Gate-Source (Cgs) and Gate-Drain (Cgd), Plot 5: Drain-Source Capacitance (Cds).</em>
</p>

#### Operational Regimes:
1. **Accumulation Region ($V_{gs} > 0\text{ V}$):** Positive gate voltage attracts majority carrier electrons to the silicon surface. The total gate capacitance $C_{gg}$ is high and approaches the oxide capacitance $C_{ox} = \frac{\epsilon_{ox}}{t_{ox}}$.
2. **Depletion Region ($V_{gs} \approx 0\text{ V}$ to $-0.3\text{ V}$):** As $V_{gs}$ becomes slightly negative, majority carriers are repelled, creating an insulating space-charge depletion layer of depth $W_{dep}$. The depletion capacitance acts in series with $C_{ox}$, resulting in the characteristic **capacitance dip**:
   $$C_{gg} = \frac{C_{ox} C_{dep}}{C_{ox} + C_{dep}} < C_{ox}$$
3. **Strong Inversion Region ($V_{gs} < V_{th}$):** When $V_{gs}$ exceeds the threshold voltage negatively, mobile minority holes form a continuous conductive channel beneath the oxide. $C_{gg}$ rises back up to the oxide limit.
4. **Terminal Partitions ($C_{gs}, C_{gd}, C_{ds}$):**
   * In the OFF state, $C_{gs}$ and $C_{gd}$ remain small, limited strictly to parasitic metallurgical overlap capacitance.
   * Once the inversion layer forms, $C_{gs}$ and $C_{gd}$ rise symmetrically to equal fractions of the inversion channel capacitance.
   * The drain-source capacitance $C_{ds}$ remains very small and flat across the entire voltage sweep, confirming excellent junction isolation.

---

### 2. Static DC Transfer ($I_d-V_{gs}$) & Output ($I_d-V_{ds}$) Characteristics

DC sweeps were performed to map linear and saturation operating boundaries.

<p align="center">
  <img src="docs/figures/dc_transfer_output_curves.png" alt="DC Transfer and Output Curves" width="750"/>
  <br>
  <em>Figure 4: Sentaurus Visual DC characteristic curves for 100nm p-MOSFET: (Left) Output characteristics Id-Vds; (Right) Transfer characteristics Id-Vgs.</em>
</p>

* **Transfer Characteristics ($I_d-V_{gs}$ at fixed $V_{ds}$):**
  * When $V_{gs} \approx 0\text{ V}$, the device is OFF with negligible subthreshold leakage current.
  * As $V_{gs}$ crosses the threshold voltage ($V_{th} = -0.296\text{ V}$) in the negative direction, the channel enters strong inversion, driving a steep increase in drain current that transitions smoothly into quadratic saturation.
* **Output Characteristics ($I_d-V_{ds}$ at constant $V_{gs}$):**
  * **Linear (Ohmic) Region:** At low $|V_{ds}|$, current increases linearly with drain voltage where channel resistance dominates:
    $$I_d \approx \mu_p C_{ox} \frac{W}{L} \left[(V_{gs} - V_{th})V_{ds} - \frac{V_{ds}^2}{2}\right]$$
  * **Saturation Region:** As $|V_{ds}|$ increases beyond $|V_{gs} - V_{th}|$, the channel pinches off at the drain end, and carrier velocity saturation causes $I_d$ to flatten into a constant current plateau.

---

### 3. Channel Length Scaling Analysis ($100\text{ nm}$, $200\text{ nm}$, $300\text{ nm}$)

Simulations were repeated under identical doping and oxide conditions for channel lengths $L = 200\text{ nm}$ and $L = 300\text{ nm}$.

<p align="center">
  <img src="docs/figures/simulation_results_200nm.png" alt="200nm Simulation Results" width="440"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/figures/simulation_results_300nm.png" alt="300nm Simulation Results" width="440"/>
  <br>
  <em>Figure 5: Sentaurus Visual multi-panel simulation dashboards for L = 200nm (left) and L = 300nm (right), displaying 2D mesh, Id-Vd, Id-Vg, and high-frequency capacitance curves.</em>
</p>

---

## Threshold Voltage ($V_{th}$) Extraction & Short-Channel Effects

### Constant Current Method
To extract the threshold voltage objectively and eliminate ambiguities from transconductance variations, the industry-standard **Constant Current Method** was utilized:

$$I_{crit} = 10^{-7} \times \frac{W}{L}\quad \text{[Amperes]}$$

$$V_{th} = V_{gs} \Big|_{I_d = I_{crit}}$$

With a standardized device width $W = 1.0\ \mu\text{m}$:
* **For $L = 100\text{ nm}$:** $I_{crit} = 10^{-7} \times \frac{1.0\ \mu\text{m}}{0.10\ \mu\text{m}} = 1.0 \times 10^{-6}\text{ A} = \mathbf{1.00\ \mu\text{A}}$
* **For $L = 200\text{ nm}$:** $I_{crit} = 10^{-7} \times \frac{1.0\ \mu\text{m}}{0.20\ \mu\text{m}} = 5.0 \times 10^{-7}\text{ A} = \mathbf{0.50\ \mu\text{A}}$
* **For $L = 300\text{ nm}$:** $I_{crit} = 10^{-7} \times \frac{1.0\ \mu\text{m}}{0.30\ \mu\text{m}} \approx 3.3 \times 10^{-7}\text{ A} = \mathbf{0.33\ \mu\text{A}}$

<p align="center">
  <img src="docs/figures/threshold_voltage_probes.png" alt="Sentaurus Inspect Threshold Voltage Extraction Probes" width="700"/>
  <br>
  <em>Figure 6: Sentaurus Inspect threshold voltage extraction curves probed at target critical currents: L = 100nm (Vth = -0.296V), L = 200nm (Vth = -0.330V), and L = 300nm (Vth = -0.396V / -0.36V).</em>
</p>

### Table 2: Extracted Threshold Voltage Comparison
| Channel Length ($L$) | Aspect Ratio ($W/L$) | Target $I_{crit}$ ($\mu\text{A}$) | Extracted $V_{th}$ ($\text{V}$) | Magnitude $|V_{th}|$ | Scaling Impact |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$300\text{ nm}$** | 3.33 | $0.333\ \mu\text{A}$ | **$-0.396\text{ V}$** | $0.396\text{ V}$ | Long-channel reference baseline |
| **$200\text{ nm}$** | 5.00 | $0.500\ \mu\text{A}$ | **$-0.330\text{ V}$** | $0.330\text{ V}$ | Moderate threshold shift |
| **$100\text{ nm}$** | 10.00 | $1.000\ \mu\text{A}$ | **$-0.296\text{ V}$** | $0.296\text{ V}$ | Pronounced $V_{th}$ Roll-Off ($|\Delta V_{th}| = 100\text{ mV}$) |

---

## Physical Mechanisms Driving Short-Channel Effects (SCE)

As channel length scales from $300\text{ nm}$ to $100\text{ nm}$, the magnitude of $V_{th}$ rolls off by **$100\text{ mV}$** ($V_{th}$ becomes less negative). Two dominant physical mechanisms explain this behavior:

### 1. Depletion Charge Sharing
In a long-channel MOSFET, the gate voltage must electrostatically support all bulk depletion charge beneath the gate oxide before an inversion layer can form:
$$Q_{dep} \propto W \cdot L \cdot \sqrt{2 \epsilon_{si} q N_D \psi_s}$$
In short-channel devices ($L = 100\text{ nm}$), the depletion boundaries of the reverse-biased source and drain p-n junctions encroach substantially into the channel region. These metallurgical junctions "share" the burden of depleting the channel, reducing the total net depletion charge that must be terminated by the gate electrode. Consequently, a **smaller magnitude gate voltage** is sufficient to trigger inversion, causing $|V_{th}|$ to roll off.

### 2. Drain-Induced Barrier Lowering (DIBL)
In sub-micron planar devices, the physical proximity of the drain terminal permits its electric field lines to penetrate deep into the channel region, pulling down the source-to-channel potential barrier for holes. As a result:
* Holes are injected into the channel at lower gate magnitudes $|V_{gs}|$.
* The effective threshold voltage decreases as $|V_{ds}|$ increases, causing elevated off-state subthreshold leakage.

---

## Automated Python Verification

A standalone verification script using standard Python libraries validates the constant-current threshold voltage extraction:

```bash
python3 scripts/extract_vth.py
```

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

## Repository Structure

```text
pmos-tcad-characterization/
├── README.md                          # Comprehensive project documentation
├── LICENSE                            # MIT Open Source License
├── docs/
│   ├── technical_report.md            # Complete formal technical report
│   └── figures/                       # High-resolution simulation plots & circuits
│       ├── circuit_schematic.png      # DC/AC testbench & small-signal equivalent circuits
│       ├── mosfet_2d_structure_mesh.png # 2D mesh & net doping concentration
│       ├── ac_characteristics_1mhz.png# 1 MHz AC capacitance profiles (Cgg, Cgs, Cgd, Cds)
│       ├── dc_transfer_output_curves.png # Static Id-Vgs and Id-Vds characteristics
│       ├── simulation_results_200nm.png # Sentaurus Visual dashboard (L = 200nm)
│       ├── simulation_results_300nm.png # Sentaurus Visual dashboard (L = 300nm)
│       └── threshold_voltage_probes.png # Inspect constant current extraction probes
└── scripts/
    ├── sde_pmos.cmd                   # Sentaurus Structure Editor 2D meshing deck
    ├── sdevice_pmos.cmd               # Sentaurus Device DC/AC physics solve deck
    ├── inspect.cmd                    # Sentaurus Inspect post-processing script
    ├── extract_vth.py                 # Standalone Python verification script
    └── generate_circuit_diagram.py    # Generator for high-resolution circuit schematic
```

---

## Author

**Nikunj Malik**  
*Registration Number: 230959134*  
* **GitHub:** [@nikunjmalik306](https://github.com/nikunjmalik306)  
* **Email:** [nikunjmalikkrm@gmail.com](mailto:nikunjmalikkrm@gmail.com)  

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
