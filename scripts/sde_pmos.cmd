; ====================================================================
; Synopsys Sentaurus Structure Editor (SDE) Deck: Sub-Micron p-MOSFET
; Author: Nikunj Malik
; Parameters:
;   Channel Lengths: L = 100nm, 200nm, 300nm
;   Gate Oxide Thickness: tox = 10nm
;   Substrate Doping (n-type): NA = 1.0e16 cm^-3
;   Source/Drain Doping (p-type): ND = 5.0e19 cm^-3
; ====================================================================

(sde:clear)

; --- 1. Coordinate Definitions (Baseline L = 100nm) ---
(define Lgate 0.10)       ; Channel length in micrometers (100nm)
(define Tox   0.010)      ; Gate oxide thickness in micrometers (10nm)
(define Xsub  1.0)        ; Substrate depth (1.0 um)
(define Ysemi 0.5)        ; Half-device lateral span

; --- 2. Geometry Creation: Silicon Substrate ---
(sdegeo:create-rectangle 
    (position (- 0 Ysemi) 0.0 0.0) 
    (position Ysemi Xsub 0.0) 
    "Silicon" "SubstrateRegion")

; --- 3. Geometry Creation: Gate Oxide ---
(sdegeo:create-rectangle 
    (position (- 0 (/ Lgate 2.0)) (- 0 Tox) 0.0) 
    (position (/ Lgate 2.0) 0.0 0.0) 
    "SiO2" "OxideRegion")

; --- 4. Contact Definitions ---
(sdegeo:define-contact-set "gate" 4 (color:rgb 1 0 0) "##")
(sdegeo:set-current-contact-set "gate")
(sdegeo:define-2d-contact 
    (find-edge-id (position 0.0 (- 0 Tox) 0.0)) "gate")

(sdegeo:define-contact-set "source" 4 (color:rgb 0 1 0) "##")
(sdegeo:define-2d-contact 
    (find-edge-id (position (- 0 (* 0.75 Ysemi)) 0.0 0.0)) "source")

(sdegeo:define-contact-set "drain" 4 (color:rgb 0 0 1) "##")
(sdegeo:define-2d-contact 
    (find-edge-id (position (* 0.75 Ysemi) 0.0 0.0)) "drain")

(sdegeo:define-contact-set "substrate" 4 (color:rgb 0.5 0.5 0.5) "##")
(sdegeo:define-2d-contact 
    (find-edge-id (position 0.0 Xsub 0.0)) "substrate")

; --- 5. Doping Profiles ---
; Uniform Substrate Doping (n-type, 1e16 cm^-3)
(sdedr:define-constant-profile "SubstrateDopingDef" "PhosphorusActiveConcentration" 1.0e16)
(sdedr:define-constant-profile-placement "SubstratePlacement" "SubstrateDopingDef" "SubstrateRegion")

; Source/Drain Implantation Doping (p-type, 5e19 cm^-3)
(sdedr:define-gaussian-profile "SD_DopingDef" "BoronActiveConcentration" "PeakPos" 0.0 "PeakVal" 5.0e19 "ValueAtDepth" 1.0e16 "Depth" 0.05 "Factor" 0.8)
(sdedr:define-element-placement "SourcePlacement" "SD_DopingDef" (position (- 0 Ysemi) 0.0 0.0))
(sdedr:define-element-placement "DrainPlacement" "SD_DopingDef" (position Ysemi 0.0 0.0))

; --- 6. Meshing Definitions & Refinements ---
(sdedr:define-refinement-size "Ref_Global" 0.05 0.05 0.0 0.01 0.01 0.0)
(sdedr:define-refinement-placement "GlobalMesh" "Ref_Global" "SubstrateRegion")

(sdedr:define-refinement-size "Ref_Channel" 0.005 0.002 0.0 0.001 0.001 0.0)
(sdedr:define-refinement-window "Win_Channel" "Rectangle" (position (- 0 (/ Lgate 2.0)) 0.0 0.0) (position (/ Lgate 2.0) 0.03 0.0))
(sdedr:define-refinement-placement "ChannelMesh" "Ref_Channel" "Win_Channel")

; --- 7. Save Model & Build Mesh ---
(sdesave:save-model "pmos_100nm")
(sde:build-mesh "snmesh" "" "pmos_100nm")
