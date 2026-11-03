; ====================================================================
; Synopsys Sentaurus Device (sdevice) Command Deck: Sub-Micron p-MOSFET
; Author: Nikunj Malik
; Objectives:
;   1. DC Transfer (Id-Vgs) & Output (Id-Vds) Characterization
;   2. AC Small-Signal Admittance Analysis (1 MHz) for Cgg, Cgs, Cgd, Cds
;   3. Short-Channel Effect (SCE) & Vth Roll-off Evaluation
; ====================================================================

Device "pMOSFET" {
  Electrode {
    { Name="source"    Voltage=0.0 }
    { Name="drain"     Voltage=0.0 }
    { Name="gate"      Voltage=0.0 Workfunction=4.8 }
    { Name="substrate" Voltage=0.0 }
  }

  File {
    Grid    = "pmos_100nm_msh.tdr"
    Plot    = "pmos_100nm_des.tdr"
    Current = "pmos_100nm_des.plt"
  }

  Physics {
    Hydrodynamic(CarrierTemperature)
    EffectiveIntrinsicDensity(OldSlotboom)
    Mobility(
      DopingDep
      HighFieldSaturation
      Enormal(Lombardi)
    )
    Recombination(
      SRH(DopingDep)
      Auger
    )
    Fermi
  }

  Plot {
    eDensity hDensity
    TotalCurrent/Vector
    eCurrent/Vector hCurrent/Vector
    ElectricField/Vector
    Potential
    SpaceCharge
    Doping
  }
}

Math {
  Extrapolate
  Iterations=25
  Notdamped=50
  Method=ILS
  Number_of_Threads=4
}

Solve {
  # --- Initial Equilibrium Solution ---
  Poisson
  Coupled { Poisson Electron Hole }

  # --- 1. DC Output Characteristics (Id vs Vds sweep at constant Vgs) ---
  Quasistationary (
    InitialStep=0.01 Increment=1.3 MaxStep=0.05 MinStep=1e-5
    Goal { Name="gate" Voltage=-1.2 }
  ) { Coupled { Poisson Electron Hole } }

  NewCurrentPrefix="Id_Vds_"
  Quasistationary (
    InitialStep=0.01 Increment=1.3 MaxStep=0.05 MinStep=1e-5
    Goal { Name="drain" Voltage=-1.5 }
  ) { Coupled { Poisson Electron Hole } }

  # --- 2. DC Transfer & AC Small-Signal Sweep (Id vs Vgs at 1 MHz) ---
  # Reset voltages to baseline
  Quasistationary (
    Goal { Name="gate" Voltage=0.0 }
  ) { Coupled { Poisson Electron Hole } }

  Quasistationary (
    Goal { Name="drain" Voltage=-0.05 }  # Linear regime for Vth extraction
  ) { Coupled { Poisson Electron Hole } }

  NewCurrentPrefix="Id_Vgs_AC_"
  Quasistationary (
    InitialStep=0.005 Increment=1.2 MaxStep=0.02 MinStep=1e-6
    Goal { Name="gate" Voltage=-1.5 }
  ) { 
    ACCoupled (
      StartFrequency=1e6 EndFrequency=1e6 NumberOfPoints=1
      Node(gate source drain substrate)
      Exclude(gate source drain substrate)
    ) { Poisson Electron Hole } 
  }
}
