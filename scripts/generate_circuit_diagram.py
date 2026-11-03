#!/usr/bin/env python3
"""
Generate high-resolution circuit schematic diagram for pMOS characterization:
1. DC Sweep & 1 MHz AC Admittance Simulation Testbench Circuit
2. High-Frequency Small-Signal Capacitance Equivalent Circuit Model
"""

from PIL import Image, ImageDraw, ImageFont
import math

def create_schematic():
    W, H = 1800, 920
    img = Image.new("RGB", (W, H), color="#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Fonts
    font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 28)
    font_section = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 20)
    font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 16)
    font_regular = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 15)
    font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
    font_sym = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)

    # Palette
    c_border = "#D0D7DE"
    c_panel_bg = "#F6F8FA"
    c_navy = "#0969DA"
    c_dark = "#1F2328"
    c_gray = "#656D76"
    c_blue = "#0969DA"
    c_green = "#1A7F37"
    c_red = "#CF222E"
    c_purple = "#8250DF"
    c_wire = "#24292F"

    # Background subtle border & banner
    draw.rounded_rectangle([20, 20, W - 20, H - 20], radius=16, outline=c_border, width=2)
    draw.rounded_rectangle([22, 22, W - 22, 85], radius=14, fill="#F0F6FC")
    draw.text((45, 38), "p-Channel MOSFET Characterization & Admittance Simulation Circuits", fill="#0969DA", font=font_title)

    # Helper: draw ground
    def draw_ground(x, y):
        draw.line([(x, y), (x, y + 16)], fill=c_wire, width=3)
        draw.line([(x - 18, y + 16), (x + 18, y + 16)], fill=c_wire, width=3)
        draw.line([(x - 12, y + 22), (x + 12, y + 22)], fill=c_wire, width=3)
        draw.line([(x - 6, y + 28), (x + 6, y + 28)], fill=c_wire, width=3)

    # Helper: draw capacitor
    def draw_capacitor(x1, y1, x2, y2, label="", is_vertical=True):
        if is_vertical:
            # Vertical capacitor between (x1, y1) and (x2, y2) with x1=x2
            cx = x1
            cy = (y1 + y2) // 2
            draw.line([(cx, y1), (cx, cy - 8)], fill=c_wire, width=2)
            draw.line([(cx - 16, cy - 8), (cx + 16, cy - 8)], fill=c_wire, width=3)
            draw.line([(cx - 16, cy + 8), (cx + 16, cy + 8)], fill=c_wire, width=3)
            draw.line([(cx, cy + 8), (cx, y2)], fill=c_wire, width=2)
            if label:
                draw.text((cx + 22, cy - 10), label, fill=c_dark, font=font_bold)
        else:
            # Horizontal capacitor between (x1, y1) and (x2, y2) with y1=y2
            cx = (x1 + x2) // 2
            cy = y1
            draw.line([(x1, cy), (cx - 8, cy)], fill=c_wire, width=2)
            draw.line([(cx - 8, cy - 16), (cx - 8, cy + 16)], fill=c_wire, width=3)
            draw.line([(cx + 8, cy - 16), (cx + 8, cy + 16)], fill=c_wire, width=3)
            draw.line([(cx + 8, cy), (x2, cy)], fill=c_wire, width=2)
            if label:
                draw.text((cx - 18, cy - 36), label, fill=c_dark, font=font_bold)

    # Helper: draw DC Voltage Source circle
    def draw_vsource(cx, cy, r, label="", val=""):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#FFFFFF", outline=c_navy, width=3)
        draw.text((cx - 6, cy - r + 8), "+", fill=c_red, font=font_bold)
        draw.text((cx - 5, cy + r - 22), "-", fill=c_navy, font=font_bold)
        if label:
            draw.text((cx + r + 12, cy - 18), label, fill=c_dark, font=font_bold)
        if val:
            draw.text((cx + r + 12, cy + 4), val, fill=c_gray, font=font_regular)

    # Helper: draw AC Voltage Source circle
    def draw_acsource(cx, cy, r, label="", val=""):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#FFFFFF", outline=c_purple, width=3)
        # Sine wave inside
        pts = []
        for i in range(-16, 17):
            sx = cx + i
            sy = cy - int(10 * math.sin(i * math.pi / 16))
            pts.append((sx, sy))
        draw.line(pts, fill=c_purple, width=2)
        if label:
            draw.text((cx + r + 12, cy - 18), label, fill=c_dark, font=font_bold)
        if val:
            draw.text((cx + r + 12, cy + 4), val, fill=c_gray, font=font_regular)

    # Helper: draw ammeter circle
    def draw_ammeter(cx, cy, r, label="A"):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#FFFFFF", outline=c_green, width=3)
        draw.text((cx - 7, cy - 11), label, fill=c_green, font=font_bold)

    # -------------------------------------------------------------------------
    # PANEL 1: TCAD Simulation Testbench Circuit
    # -------------------------------------------------------------------------
    p1_left, p1_top, p1_right, p1_bot = 40, 105, 880, 890
    draw.rounded_rectangle([p1_left, p1_top, p1_right, p1_bot], radius=12, fill="#FAFAFA", outline=c_border, width=2)
    draw.text((p1_left + 20, p1_top + 18), "(A) TCAD Simulation Testbench (DC & AC Small-Signal)", fill=c_dark, font=font_section)
    draw.text((p1_left + 20, p1_top + 45), "Sentaurus Device (sdevice) Terminal Biasing & Admittance Characterization", fill=c_gray, font=font_regular)

    # PMOS Device Center
    tx, ty = 430, 310

    # Gate electrode plate
    draw.line([(tx - 40, ty - 50), (tx - 40, ty + 50)], fill=c_wire, width=5)
    # Gate lead with bubble for PMOS
    draw.line([(tx - 110, ty), (tx - 55, ty)], fill=c_wire, width=3)
    draw.ellipse([tx - 55, ty - 7, tx - 41, ty + 7], fill="#FFFFFF", outline=c_wire, width=3)
    draw.text((tx - 95, ty - 28), "Gate (G)", fill=c_navy, font=font_bold)

    # Oxide gap (spacing between plate and channel)
    # Channel segments
    draw.line([(tx - 26, ty - 50), (tx - 26, ty - 20)], fill=c_navy, width=5) # Source channel
    draw.line([(tx - 26, ty - 12), (tx - 26, ty + 12)], fill=c_navy, width=5) # Bulk/Body channel
    draw.line([(tx - 26, ty + 20), (tx - 26, ty + 50)], fill=c_navy, width=5) # Drain channel

    # Source terminal (top)
    draw.line([(tx - 26, ty - 35), (tx + 30, ty - 35)], fill=c_wire, width=3)
    draw.line([(tx + 30, ty - 35), (tx + 30, ty - 120)], fill=c_wire, width=3)
    draw.text((tx + 40, ty - 110), "Source (S)", fill=c_dark, font=font_bold)
    draw.text((tx + 40, ty - 90), "p+ Region (0V Ref)", fill=c_gray, font=font_small)

    # Bulk / Substrate terminal (middle) with arrow pointing OUT (n-type bulk)
    draw.line([(tx - 26, ty), (tx + 30, ty)], fill=c_wire, width=3)
    # Arrowhead on bulk
    draw.polygon([(tx - 20, ty - 7), (tx - 6, ty), (tx - 20, ty + 7)], fill=c_wire)
    draw.line([(tx + 30, ty), (tx + 30, ty - 35)], fill=c_wire, width=3) # Bulk tied to source
    draw.text((tx + 40, ty - 8), "Bulk (B)", fill=c_dark, font=font_bold)
    draw.text((tx + 40, ty + 10), "n-Substrate (Tied to S)", fill=c_gray, font=font_small)

    # Connect Source & Bulk to GND
    draw.line([(tx + 30, ty - 120), (tx - 20, ty - 120)], fill=c_wire, width=3)
    draw_ground(tx - 20, ty - 120)

    # Drain terminal (bottom)
    draw.line([(tx - 26, ty + 35), (tx + 30, ty + 35)], fill=c_wire, width=3)
    draw.line([(tx + 30, ty + 35), (tx + 30, ty + 80)], fill=c_wire, width=3)
    draw.text((tx + 40, ty + 50), "Drain (D)", fill=c_dark, font=font_bold)
    draw.text((tx + 40, ty + 70), "p+ Region", fill=c_gray, font=font_small)

    # Drain Ammeter
    draw_ammeter(tx + 30, ty + 105, 22, "Id")
    draw.line([(tx + 30, ty + 127), (tx + 30, ty + 160)], fill=c_wire, width=3)

    # Drain Voltage Source VDS
    draw_vsource(tx + 30, ty + 200, 32, "Vds Supply", "DC Drain Sweep (0 to -1.5V)")
    draw.line([(tx + 30, ty + 232), (tx + 30, ty + 265)], fill=c_wire, width=3)
    draw_ground(tx + 30, ty + 265)

    # Gate Network: AC + DC Sources in Series
    gx = tx - 210
    draw.line([(tx - 110, ty), (gx, ty)], fill=c_wire, width=3)
    draw.line([(gx, ty), (gx, ty + 30)], fill=c_wire, width=3)

    # AC small signal source
    draw_acsource(gx, ty + 65, 30, "vac (Small Signal)", "10 mV, f = 1 MHz")
    draw.line([(gx, ty + 95), (gx, ty + 130)], fill=c_wire, width=3)

    # DC gate sweep source Vgs
    draw_vsource(gx, ty + 170, 32, "Vgs Supply", "DC Gate Bias (0 to -1.5V)")
    draw.line([(gx, ty + 202), (gx, ty + 240)], fill=c_wire, width=3)
    draw_ground(gx, ty + 240)

    # Simulation Parameter Specs Box inside Panel 1
    box1_t = 635
    draw.rounded_rectangle([p1_left + 20, box1_t, p1_right - 20, p1_bot - 18], radius=8, fill="#FFFFFF", outline="#E1E4E8", width=1)
    draw.text((p1_left + 35, box1_t + 12), "TCAD Simulation Conditions & Setup:", fill=c_dark, font=font_bold)
    specs = [
        "• Channel Lengths: L = 100 nm (baseline), 200 nm, 300 nm  |  Device Width: W = 1.0 um",
        "• Oxide: tox = 10 nm SiO2  |  Substrate Doping: ND = 1.0 x 10^16 cm^-3 (n-type bulk)",
        "• Source/Drain Doping: NA = 5.0 x 10^19 cm^-3 (p-type degenerate)",
        "• DC Analysis: Sweeps Vgs (-1.5V to 0V) for transfer Id-Vgs and Vds (-1.5V to 0V) for output Id-Vds",
        "• AC Analysis: Small-signal admittance Y = G + jωC probed at gate at 1 MHz (ω = 2π x 10^6 rad/s)"
    ]
    for idx, s in enumerate(specs):
        draw.text((p1_left + 35, box1_t + 38 + idx * 23), s, fill="#333333", font=font_small)

    # -------------------------------------------------------------------------
    # PANEL 2: High-Frequency Small-Signal Capacitance Equivalent Circuit
    # -------------------------------------------------------------------------
    p2_left, p2_top, p2_right, p2_bot = 920, 105, W - 40, 890
    draw.rounded_rectangle([p2_left, p2_top, p2_right, p2_bot], radius=12, fill="#FAFAFA", outline=c_border, width=2)
    draw.text((p2_left + 20, p2_top + 18), "(B) Small-Signal AC Capacitance Equivalent Circuit Model", fill=c_dark, font=font_section)
    draw.text((p2_left + 20, p2_top + 45), "Terminal Capacitance Network governing High-Frequency (1 MHz) Admittance", fill=c_gray, font=font_regular)

    # Nodes in Panel 2:
    # Gate Node (Top Left)
    node_g = (p2_left + 160, p2_top + 180)
    # Drain Node (Top Right)
    node_d = (p2_right - 160, p2_top + 180)
    # Source Node (Bottom Left)
    node_s = (p2_left + 160, p2_top + 450)
    # Body Node (Bottom Right)
    node_b = (p2_right - 160, p2_top + 450)

    # Horizontal Cgd between Gate and Drain
    draw_capacitor(node_g[0], node_g[1], node_d[0], node_d[1], "Cgd (Gate-Drain)", is_vertical=False)

    # Vertical Cgs between Gate and Source
    draw_capacitor(node_g[0], node_g[1], node_s[0], node_s[1], "Cgs (Gate-Source)", is_vertical=True)

    # Vertical Cdb between Drain and Body
    draw_capacitor(node_d[0], node_d[1], node_b[0], node_b[1], "Cdb (Drain-Bulk)", is_vertical=True)

    # Horizontal Csb between Source and Body
    draw_capacitor(node_s[0], node_s[1], node_b[0], node_b[1], "Csb (Source-Bulk)", is_vertical=False)

    # Diagonal Cds between Drain and Source
    # Draw via offset box to keep clean
    cds_mid_x = (node_s[0] + node_d[0]) // 2
    cds_mid_y = (node_g[1] + node_s[1]) // 2
    draw.line([(node_d[0], node_d[1] + 25), (cds_mid_x + 50, cds_mid_y - 25)], fill="#666666", width=2)
    draw.line([(cds_mid_x + 50, cds_mid_y - 25), (cds_mid_x + 15, cds_mid_y - 25)], fill="#666666", width=2)
    # Cds symbol
    draw.line([(cds_mid_x + 15, cds_mid_y - 37), (cds_mid_x + 15, cds_mid_y - 13)], fill="#666666", width=3)
    draw.line([(cds_mid_x - 5, cds_mid_y - 37), (cds_mid_x - 5, cds_mid_y - 13)], fill="#666666", width=3)
    draw.line([(cds_mid_x - 5, cds_mid_y - 25), (cds_mid_x - 50, cds_mid_y - 25)], fill="#666666", width=2)
    draw.line([(cds_mid_x - 50, cds_mid_y - 25), (node_s[0] + 25, node_s[1] - 15)], fill="#666666", width=2)
    draw.text((cds_mid_x - 30, cds_mid_y - 60), "Cds (Drain-Source)", fill=c_red, font=font_bold)

    # Cgb diagonal Gate to Body
    draw.line([(node_g[0] + 25, node_g[1] + 20), (cds_mid_x - 50, cds_mid_y + 35)], fill="#666666", width=2)
    draw.line([(cds_mid_x - 50, cds_mid_y + 35), (cds_mid_x - 10, cds_mid_y + 35)], fill="#666666", width=2)
    draw.line([(cds_mid_x - 10, cds_mid_y + 23), (cds_mid_x - 10, cds_mid_y + 47)], fill="#666666", width=3)
    draw.line([(cds_mid_x + 10, cds_mid_y + 23), (cds_mid_x + 10, cds_mid_y + 47)], fill="#666666", width=3)
    draw.line([(cds_mid_x + 10, cds_mid_y + 35), (cds_mid_x + 50, cds_mid_y + 35)], fill="#666666", width=2)
    draw.line([(cds_mid_x + 50, cds_mid_y + 35), (node_b[0] - 25, node_b[1] - 20)], fill="#666666", width=2)
    draw.text((cds_mid_x - 30, cds_mid_y + 55), "Cgb (Gate-Bulk)", fill=c_purple, font=font_bold)

    # Terminals circle markers & labels
    nodes = [
        (node_g, "Gate (G)", c_navy, (-75, -35)),
        (node_d, "Drain (D)", c_red, (15, -35)),
        (node_s, "Source (S)", c_green, (-85, 12)),
        (node_b, "Body (B)", c_purple, (15, 12)),
    ]
    for pt, lbl, col, offset in nodes:
        draw.ellipse([pt[0] - 8, pt[1] - 8, pt[0] + 8, pt[1] + 8], fill=col, outline="#FFFFFF", width=2)
        draw.text((pt[0] + offset[0], pt[1] + offset[1]), lbl, fill=col, font=font_bold)

    # Math & Extraction Equations Box
    box2_t = 560
    draw.rounded_rectangle([p2_left + 20, box2_t, p2_right - 20, p2_bot - 18], radius=8, fill="#FFFFFF", outline="#E1E4E8", width=1)
    draw.text((p2_left + 35, box2_t + 12), "Physical Equations & Admittance Extraction Relations:", fill=c_dark, font=font_bold)

    eqs = [
        "1. Total Gate Capacitance (Cgg):",
        "   Cgg = Cgs + Cgd + Cgb = dQgate / dVgs",
        "   • Accumulation (Vgs > 0): Majority electron accumulation -> Cgg ≈ Cox",
        "   • Depletion (Vgs ~ 0): Bulk depletion region widens in series with Cox -> Cgg reaches minimum dip",
        "   • Strong Inversion (Vgs < Vth): Hole inversion channel bridges S/D -> Cgs & Cgd surge, Cgg -> Cox",
        "",
        "2. Threshold Voltage Extraction (Constant Current Method):",
        "   Icrit = 10^-7 x (W / L) [A]   |   Vth = Vgs at which Id = Icrit",
        "   • L = 100 nm (W/L = 10)  =>  Icrit = 1.00 uA  =>  Vth = -0.296 V",
        "   • L = 200 nm (W/L = 5.0) =>  Icrit = 0.50 uA  =>  Vth = -0.330 V",
        "   • L = 300 nm (W/L = 3.3) =>  Icrit = 0.33 uA  =>  Vth = -0.396 V  (Vth Roll-off |ΔVth| = 100 mV)"
    ]
    cur_y = box2_t + 36
    for line in eqs:
        if line.startswith("1.") or line.startswith("2."):
            draw.text((p2_left + 35, cur_y), line, fill=c_navy, font=font_bold)
            cur_y += 21
        elif line.startswith("   •"):
            draw.text((p2_left + 45, cur_y), line, fill=c_dark, font=font_small)
            cur_y += 20
        elif line.strip() == "":
            cur_y += 6
        else:
            draw.text((p2_left + 45, cur_y), line, fill="#444444", font=font_regular)
            cur_y += 21

    output_path = "/Users/nikunj/Desktop/PROJECTS/pmos-tcad-characterization/docs/figures/circuit_schematic.png"
    img.save(output_path, "PNG", dpi=(300, 300))
    print(f"Saved circuit schematic to: {output_path}")

if __name__ == "__main__":
    create_schematic()
