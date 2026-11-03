# Design and Characterization of a p-Channel MOSFET
### Analysis of DC and AC Characteristics and the Impact of Channel Length Scaling

**Author:** Nikunj Malik  
**Registration Number:** 230959134  
**Toolsuite:** Synopsys Sentaurus TCAD (`sde`, `sdevice`, `inspect`, `svisual`)  
**Date:** 2026  

---

## Abstract

This report presents the design and simulation of a p-channel Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) using TCAD software. The study focuses on two primary objectives: first, to characterize the fundamental Direct Current (DC) and Alternating Current (AC) behaviors of a baseline device with a 100nm channel length; second, to analyze the impact of channel length scaling on the device's DC performance and threshold voltage. MOSFETs with channel lengths of 100nm, 200nm, and 300nm were simulated. The results demonstrate classic MOSFET transfer and output characteristics. AC analysis reveals the voltage-dependent nature of gate capacitances, which are crucial for high-frequency applications. The channel length scaling analysis confirms key short-channel effects, most notably **threshold voltage ($V_{th}$) roll-off**. These findings are critical for understanding the trade-offs involved in modern semiconductor device scaling.

---

## 1. Introduction

The Metal-Oxide-Semiconductor Field-Effect Transistor (MOSFET) is the fundamental building block of modern digital electronics, from microprocessors to memory chips. Its ability to act as a highly efficient switch has enabled the exponential growth in computing power described by Moore’s Law. The principle of operation relies on modulating the conductivity of a semiconductor channel between two terminals (source and drain) by applying a voltage to a third, insulated terminal (the gate).

This project involves the simulation of a p-channel MOSFET to investigate its electrical characteristics. The analysis is divided into two parts:
1. **Device Characterization:** A thorough examination of the DC transfer ($I_d-V_{gs}$) and output ($I_d-V_{ds}$) characteristics, as well as the AC capacitance-voltage ($C-V$) profiles for a baseline 100nm device.
2. **Scaling Analysis:** An investigation into the effects of reducing the channel length ($L$) on device performance, specifically focusing on changes in threshold voltage ($V_{th}$) and drain current ($I_d$). This is crucial as device scaling into the nanometer regime introduces significant physical phenomena known as Short-Channel Effects (SCEs).

---

## 2. Device Structure and Simulation Setup

A p-channel MOSFET was designed and simulated using the Sentaurus TCAD suite. The device was constructed based on the parameters specified in the problem statement, outlined in Table 1.

![2D MOSFET Mesh and Doping Profile](figures/mosfet_2d_structure_mesh.png)
*Figure 1: 2D p-MOSFET Sentaurus Visual structure mesh and net active doping concentration distribution.*

### Table 1: MOSFET Design and Simulation Parameters
| Parameter | Value |
| :--- | :--- |
| **Device Type** | p-channel MOSFET |
| **Channel Length ($L$)** | 100nm, 200nm, 300nm |
| **Gate Oxide Thickness ($t_{ox}$)** | 10nm |
| **Substrate (Body) Doping ($N_D$, n-type)** | $1 \times 10^{16}\ \text{cm}^{-3}$ |
| **Source/Drain Doping ($N_A$, p-type)** | $5 \times 10^{19}\ \text{cm}^{-3}$ |
| **Gate Work Function ($\Phi_m$)** | 4.80 eV |
| **AC Small-Signal Frequency ($f$)** | 1 MHz |
| **Operating Temperature ($T$)** | 300 K |

The simulations involved DC sweeps of gate and drain voltages to obtain the transfer and output curves. For the AC analysis, a small-signal analysis was performed at a frequency of 1MHz.

---

## 3. Circuit Schematics & Simulation Setup

![Circuit Schematics and Small-Signal Equivalent Model](figures/circuit_schematic.png)
*Figure 2: (A) TCAD Simulation Testbench circuit for DC voltage sweeps and 1 MHz small-signal AC admittance probing. (B) High-frequency small-signal capacitance equivalent circuit model.*

### Biasing Conditions
* **Source & Bulk:** Grounded ($V_S = V_B = 0\text{ V}$) to maintain zero substrate bias ($V_{BS} = 0\text{ V}$).
* **Drain:** Biased via variable DC source $V_{DS}$ (swept from 0V to -1.5V) in series with ammeter $I_D$.
* **Gate:** Excited with DC bias $V_{GS}$ superposed with a 1 MHz small-signal AC sinusoid ($v_{ac} = 10\text{ mV}$) for terminal admittance evaluation ($Y = G + j\omega C$).

---

## 4. Results and Discussion

### 4.1 Characteristics of the Baseline 100nm MOSFET

The fundamental DC and AC characteristics were first analysed for the baseline device with a channel length $L = 100\text{ nm}$. The AC results are shown in Figure 3.

#### 4.1.1 AC (Capacitance) Characteristics (1 MHz)
The AC characteristics reveal the internal capacitances of the MOSFET, which govern its high-frequency performance:

![Figure 1: AC Characteristics Plots for Frequency of 1 MHz](figures/ac_characteristics_1mhz.png)
*Figure 3: AC Characteristics Plots for Frequency of 1 MHz.*

* **Plot 1: Total Gate Capacitance ($C_{gg}$):** Shows the classic C-V curve. It is high when the device is OFF (accumulation) and ON (inversion), but dips in the transition (depletion) region.
* **Plot 2 & 3: Gate-Source / Gate-Drain ($C_{gs}, C_{gd}$):** These are low when the device is OFF (parasitic overlap only). They rise to a high value when the device is ON as the channel forms.
* **Plot 5: Drain-Source Capacitance ($C_{ds}$):** This capacitance is very low and relatively flat. It is a small parasitic junction capacitance and is not the main component.

---

#### 4.1.2 DC Characteristics

![Figure 2: DC Characteristics Plots (left – IdVd, right IdVg)](figures/dc_characteristics_idvd_idvg.png)
*Figure 4: DC Characteristics Plots for Frequency of 1 MHz (left – IdVd, right IdVg).*

##### Id–Vg Characteristics (Transfer Characteristics)
The $I_d–V_g$ plot shows the drain current variation with respect to the gate voltage ($V_g$) at a fixed drain voltage ($V_d$). The magnitude of the drain current increases as the gate voltage becomes more negative. When the gate voltage is near $0\text{ V}$, the transistor is in the OFF region with only a small leakage current. As $V_g$ moves beyond the threshold voltage ($V_{th}$) in the negative direction, the device enters strong inversion, causing a rapid increase in drain current.

The plot exhibits the typical PMOS transfer behaviour, where the curve rises and gradually saturates, indicating the transition from linear to saturation regions of operation. This confirms proper gate control over the channel and a clear PMOS turn-on characteristic when $V_{GS}$ becomes sufficiently negative.

##### Id–Vd Characteristics (Output Characteristics)
The $I_d–V_d$ plot shows the dependence of drain current on drain voltage ($V_d$) for a constant gate voltage. Initially, the current increases almost linearly with $V_d$, representing the ohmic (linear) region, where channel resistance dominates. As the magnitude of $V_d$ increases further, the curve begins to flatten out, showing that the device has entered the saturation region, where the drain current becomes nearly constant and is primarily controlled by the gate voltage.

The smooth transition from linear to saturation behaviour indicates proper channel formation and expected PMOS output operation, where the drain current saturates for larger $|V_{DS}|$.

---

### 4.2 Impact of Varying Channel Length

To study effects on change of channel length, simulations were repeated for devices with $L = 200\text{ nm}$ and $L = 300\text{ nm}$. The results are presented in Figures 5 and 6, and the key findings are summarized below.

![Figure 2: Simulation results for L = 200nm MOSFET](figures/simulation_results_200nm.png)
*Figure 5: Simulation results dashboard for L = 200nm MOSFET.*

![Figure 3: Simulation results for L = 300nm MOSFET](figures/simulation_results_300nm.png)
*Figure 6: Simulation results dashboard for L = 300nm MOSFET.*

---

### 4.3 Threshold Voltage Extraction Method & Detailed Calculations

The threshold voltage ($V_{th}$) is a critical parameter that defines the gate voltage required to turn the transistor "ON". In this analysis, the **Constant Current Method** was employed. This method defines the threshold voltage as the gate-source voltage ($V_{gs}$) at which the drain current ($I_d$) reaches a specific, predefined critical value ($I_{crit}$).

#### The relationship is given by:
![Threshold Voltage Definition Formula](figures/equation_vth_definition.png)

$$V_{th} = V_{gs} \Big|_{I_d = I_{crit}}$$

The critical current is typically normalized by the device's aspect ratio ($W/L$) to ensure a consistent definition across different device geometries. A common industry standard is to define $I_{crit}$ as:

![Critical Current Formula](figures/equation_icrit_normalization.png)

$$I_{crit} = 10^{-7}\text{ A} \times \frac{W}{L}$$

#### Exact Step-by-Step Probing Calculations (from Report Page 7):
Assuming a device width ($W$) of $1.0\ \mu\text{m}$, the target currents for probing the $I_d - V_{gs}$ curve are calculated as follows:

![Calculated Probing Target Currents](figures/calculation_target_currents.png)

* **For $L = 100\text{ nm}$:**
  $$I_{crit} = 10^{-7} \times \frac{1\ \mu\text{m}}{0.10\ \mu\text{m}} = 1.0 \times 10^{-6}\text{ A} = \mathbf{1.0\ \mu\text{A}}$$

* **For $L = 200\text{ nm}$:**
  $$I_{crit} = 10^{-7} \times \frac{1\ \mu\text{m}}{0.20\ \mu\text{m}} = 5.0 \times 10^{-7}\text{ A} = \mathbf{0.5\ \mu\text{A}}$$

* **For $L = 300\text{ nm}$:**
  $$I_{crit} = 10^{-7} \times \frac{1\ \mu\text{m}}{0.30\ \mu\text{m}} \approx 3.3 \times 10^{-7}\text{ A} = \mathbf{0.33\ \mu\text{A}}$$

These calculated current values align closely with the values at which the curves were probed in the simulation software to extract the $V_{th}$ values presented in Table 2.

![Vth Extraction Methodology and Calculations Panel](figures/vth_extraction_calculations_panel.png)
*Figure 7: Summary card of constant current method formulas, step-by-step arithmetic, target probing currents, and extracted threshold voltages.*

---

### 4.4 Threshold Voltage Comparison & Extraction Curves

By comparing the transfer characteristics ($I_d - V_{gs}$ plots) for all three devices, a clear trend emerges. The threshold voltage, the gate voltage required to form the inversion channel, decreases as the channel length decreases. This phenomenon is known as **$V_{th}$ roll-off**, which is a key short-channel effect (SCE).

### Table 2: Extracted Threshold Voltage for Different Channel Lengths
| Channel Length ($L$) | Aspect Ratio ($W/L$) | Critical Probing Current ($I_{crit}$) | Threshold Voltage ($V_{th}$) |
| :---: | :---: | :---: | :---: |
| **$100\text{ nm}$** | 10.00 | $1.0\ \mu\text{A}$ ($1.0 \times 10^{-6}\text{ A}$) | **$-0.296\text{ V}$** |
| **$200\text{ nm}$** | 5.00 | $0.5\ \mu\text{A}$ ($5.0 \times 10^{-7}\text{ A}$) | **$-0.330\text{ V}$** |
| **$300\text{ nm}$** | 3.33 | $0.33\ \mu\text{A}$ ($3.3 \times 10^{-7}\text{ A}$) | **$-0.396\text{ V}$** (probed $-0.36\text{ V}$) |

#### Sentaurus Inspect Extraction Probing Curves (from Report Page 8):

##### Channel Length $L = 100\text{ nm}$ ($V_{th} = -0.296\text{ V}$):
![100nm Vth Probing Curve](figures/vth_probe_curve_100nm.png)
*Figure 8A: Sentaurus Inspect probe curve for L = 100nm pMOSFET showing Vth = -0.296 V at Icrit = 1.0 uA.*

##### Channel Length $L = 200\text{ nm}$ ($V_{th} = -0.330\text{ V}$):
![200nm Vth Probing Curve](figures/vth_probe_curve_200nm.png)
*Figure 8B: Sentaurus Inspect probe curve for L = 200nm pMOSFET showing Vth = -0.330 V at Icrit = 0.5 uA.*

##### Channel Length $L = 300\text{ nm}$ ($V_{th} = -0.360\text{ V}$ / $-0.396\text{ V}$):
![300nm Vth Probing Curve](figures/vth_probe_curve_300nm.png)
*Figure 8C: Sentaurus Inspect probe curve for L = 300nm pMOSFET showing Vth = -0.360 V / -0.396 V at Icrit = 0.33 uA.*

---

### 4.5 Why This Happens: Short-Channel Effects

#### 1. Charge Sharing:
Short Channel (e.g., 100nm): The depletion regions from the source and drain (which are now very close) "help" deplete the channel. The gate no longer has to do all the work. Because the source and drain "share" the depletion charge, a smaller (less negative) gate voltage is needed to reach the threshold condition.

#### 2. Drain-Induced Barrier Lowering:
* In a short-channel device, the drain is so close to the source that its electric field can directly influence the potential barrier at the source.
* For a pMOSFET, the negative drain voltage ($V_{ds}$) lowers the potential barrier for holes (charge carriers) trying to enter the channel from the source.
* This "help" from the drain makes it easier for the channel to invert, effectively reducing the magnitude of the ($V_{ds}$) needed to turn the device on. This effect becomes much stronger as $L$ decreases.

---

## 5. Conclusion

This project successfully demonstrated the design and simulation of a p-channel MOSFET using TCAD tools. The fundamental DC and AC characteristics of a 100nm baseline device were analysed, confirming theoretical operational principles. The voltage dependent nature of the internal capacitances ($C_{gg}, C_{gs}, C_{gd}, C_{ds}$) was clearly observed.

The analysis of varying the channel length of 100nm between the devices, while keeping the Voltage, Junction Doping, and length of Source and Drain equal across all devices was observed. As the channel length of a pMOSFET decreases, its threshold voltage ($V_{th}$) becomes less negative. This phenomenon is a primary example of short-channel effects (SCEs).

This result underscores a fundamental trade-off in MOSFET scaling: while shrinking the channel length is key to improving performance, it also introduces detrimental effects like $V_{th}$ roll-off, which complicates device design and circuit stability. Managing these short-channel effects is a central focus of modern semiconductor technology development.

---

## Author

**Nikunj Malik**  
*Registration Number: 230959134*  
* **GitHub:** [@nikunjmalik306](https://github.com/nikunjmalik306)  
* **Email:** [nikunjmalikkrm@gmail.com](mailto:nikunjmalikkrm@gmail.com)  
