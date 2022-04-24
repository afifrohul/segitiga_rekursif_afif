import tkinter as tk
import math

def segitiga(cnv, lvl, curlvl, panjang, titikA):
  Ax=titikA[0]
  Ay=titikA[1]
  # cnv.create_text(Ax, Ay, text='A')
  # =====================================================Level 1=======================================================
  cnv.create_oval(500, ycenter, 500+5, ycenter+5)
  Bx = math.cos( math.radians(60) ) * panjang
  By = math.sin( math.radians(60) ) * panjang
  # cnv.create_text(Ax + Bx, Ay + By, text='B')
  Cx = math.cos( math.radians(120) ) * panjang
  Cy = math.sin( math.radians(120) ) * panjang
  # cnv.create_text(Ax + Cx, Ay + Cy, text='C')
  # =======================================================LLevel 2===================================================
  AB1x = math.cos( math.radians(60) ) * (panjang /3)
  AB1y = math.sin( math.radians(60) ) * (panjang /3)
  # cnv.create_text(Ax + AB1x, Ay + AB1y, text='AB1')
  AB2x = math.cos( math.radians(60) ) * (panjang * 2/3)
  AB2y = math.sin( math.radians(60) ) * (panjang * 2/3)
  # cnv.create_text(Ax + AB2x, Ay + AB2y, text='AB2')

  BC1x = math.cos( math.radians(0) ) * (panjang /3)
  BC1y = math.sin( math.radians(0) ) * (panjang /3)
  # cnv.create_text(Ax + Cx + BC1x, Ay + Cy + BC1y, text='BC1')
  BC2x = math.cos( math.radians(0) ) * (panjang * 2/3)
  BC2y = math.sin( math.radians(0) ) * (panjang * 2/3)
  # cnv.create_text(Ax + Cx + BC2x, Ay + Cy + BC2y, text='BC2')

  CA1x = math.cos( math.radians(120) ) * (panjang /3)
  CA1y = math.sin( math.radians(120) ) * (panjang /3)
  # cnv.create_text(Ax + CA1x, Ay + CA1y, text='CA1')
  CA2x = math.cos( math.radians(120) ) * (panjang * 2/3)
  CA2y = math.sin( math.radians(120) ) * (panjang * 2/3)
  # cnv.create_text(Ax + CA2x, Ay + CA2y, text='CA2')

  Dx = math.cos( math.radians(0) ) * panjang/3
  Dy = math.sin( math.radians(0) ) * panjang/3
  Ex = math.cos( math.radians(-60) ) * panjang/3
  Ey = math.sin( math.radians(-60) ) * panjang/3
  Fx = math.cos( math.radians(180) ) * panjang/3
  Fy = math.sin( math.radians(180) ) * panjang/3
  Gx = math.cos( math.radians(-120) ) * panjang/3
  Gy = math.sin( math.radians(-120) ) * panjang/3

  
  Hx = math.cos( math.radians(60) ) * panjang/3
  Hy = math.sin( math.radians(60) ) * panjang/3

  Ix = math.cos( math.radians(120) ) * panjang/3
  Iy = math.sin( math.radians(120) ) * panjang/3
  # =========================================================Level 3===============================================
  AB3x = math.cos( math.radians(0) ) * (panjang /9)
  AB3y = math.sin( math.radians(0) ) * (panjang /9)
  # cnv.create_text(Ax + AB1x + AB3x, Ay + AB1y + AB3y, text='AB3')

  AB4x = math.cos( math.radians(0) ) * (panjang * 2/9)
  AB4y = math.sin( math.radians(0) ) * (panjang * 2/9)
  # cnv.create_text(Ax + AB1x + AB4x, Ay + AB1y + AB4y, text='AB4')

  Jx = math.cos( math.radians(-60) ) * panjang/9
  Jy = math.sin( math.radians(-60) ) * panjang/9

  Kx = math.cos( math.radians(-120) ) * panjang/9
  Ky = math.sin( math.radians(-120) ) * panjang/9
  AB5x = math.cos( math.radians(-60) ) * (panjang /9)
  AB5y = math.sin( math.radians(-60) ) * (panjang /9)
  # cnv.create_text(Ax + AB2x + AB5x, Ay + AB2y + AB5y, text='AB5')

  AB6x = math.cos( math.radians(-60) ) * (panjang * 2/9)
  AB6y = math.sin( math.radians(-60) ) * (panjang * 2/9)
  # cnv.create_text(Ax + AB2x + AB6x, Ay + AB2y + AB6y, text='AB6')

  Lx = math.cos( math.radians(0) ) * panjang/9
  Ly = math.sin( math.radians(0) ) * panjang/9

  Mx = math.cos( math.radians(60) ) * panjang/9
  My = math.sin( math.radians(60) ) * panjang/9
  # --------------------------------------------BC----------------------------------------------------
  BC3x = math.cos( math.radians(60) ) * (panjang /9)
  BC3y = math.sin( math.radians(60) ) * (panjang /9)
  # cnv.create_text(Ax + Cx + BC1x + BC3x, Ay + Cy + BC1y + BC3y, text='BC3')

  BC4x = math.cos( math.radians(60) ) * (panjang * 2/9)
  BC4y = math.sin( math.radians(60) ) * (panjang * 2/9)
  # cnv.create_text(Ax + Cx + BC1x + BC4x, Ay + Cy + BC1y + BC4y, text='BC4')


  Nx = math.cos( math.radians(120) ) * panjang/9
  Ny = math.sin( math.radians(120) ) * panjang/9

  Ox = math.cos( math.radians(180) ) * panjang/9
  Oy = math.sin( math.radians(180) ) * panjang/9
  BC5x = math.cos( math.radians(120) ) * (panjang /9)
  BC5y = math.sin( math.radians(120) ) * (panjang /9)
  # cnv.create_text(Ax + Cx + BC2x + BC5x, Ay + Cy + BC2y + BC5y, text='BC5')

  BC6x = math.cos( math.radians(120) ) * (panjang * 2/9)
  BC6y = math.sin( math.radians(120) ) * (panjang * 2/9)
  # cnv.create_text(Ax + Cx + BC2x + BC6x, Ay + Cy + BC2y + BC6y, text='BC6')

  Px = math.cos( math.radians(60) ) * panjang/9
  Py = math.sin( math.radians(60) ) * panjang/9

  Qx = math.cos( math.radians(0) ) * panjang/9
  Qy = math.sin( math.radians(0) ) * panjang/9
  # -----------------------------------------------AC-------------------------------------------------
  CA3x = math.cos( math.radians(180) ) * (panjang /9)
  CA3y = math.sin( math.radians(180) ) * (panjang /9)
  # cnv.create_text(Ax + CA1x + CA3x, Ay + CA1y + CA3y, text='CA3')
  CA4x = math.cos( math.radians(180) ) * (panjang * 2/9)
  CA4y = math.sin( math.radians(180) ) * (panjang * 2/9)
  # cnv.create_text(Ax + CA1x + CA4x, Ay + CA1y + CA4y, text='CA4')

  Rx = math.cos( math.radians(-120) ) * panjang/9
  Ry = math.sin( math.radians(-120) ) * panjang/9

  Sx = math.cos( math.radians(-60) ) * panjang/9
  Sy = math.sin( math.radians(-60) ) * panjang/9

  CA5x = math.cos( math.radians(180+60) ) * (panjang /9)
  CA5y = math.sin( math.radians(180+60) ) * (panjang /9)
  # cnv.create_text(Ax + CA2x + CA5x, Ay + CA2y + CA5y, text='CA5')
  CA6x = math.cos( math.radians(180+60) ) * (panjang * 2/9)
  CA6y = math.sin( math.radians(180+60) ) * (panjang * 2/9)
  # cnv.create_text(Ax + CA2x + CA6x, Ay + CA2y + CA6y, text='CA6')

  Tx = math.cos( math.radians(180) ) * panjang/9
  Ty = math.sin( math.radians(180) ) * panjang/9

  Ux = math.cos( math.radians(120) ) * panjang/9
  Uy = math.sin( math.radians(120) ) * panjang/9
  # ==============================================LEVEL 4==========================================================
  # ----------------------------------------------------2 SEGI3 Kanan Atas------------------------------------------
  AB7x = math.cos( math.radians(-60) ) * (panjang /27)
  AB7y = math.sin( math.radians(-60) ) * (panjang /27)
  # cnv.create_text(Ax + AB1x + AB3x + AB7x, Ay + AB1y + AB3y + AB7y, text='AB7')

  AB8x = math.cos( math.radians(-60) ) * (panjang * 2/27)
  AB8y = math.sin( math.radians(-60) ) * (panjang * 2/27)
  # cnv.create_text(Ax + AB1x + AB3x + AB8x, Ay + AB1y + AB3y + AB8y, text='AB8')

  Vx = math.cos( math.radians(-120) ) * panjang/27
  Vy = math.sin( math.radians(-120) ) * panjang/27
  
  Wx = math.cos( math.radians(180) ) * panjang/27
  Wy = math.sin( math.radians(180) ) * panjang/27


  AB9x = math.cos( math.radians(-120) ) * (panjang /27)
  AB9y = math.sin( math.radians(-120) ) * (panjang /27)
  # cnv.create_text(Ax + AB1x + AB4x + AB9x, Ay + AB1y + AB4y + AB9y, text='AB9')

  AB10x = math.cos( math.radians(-120) ) * (panjang * 2/27)
  AB10y = math.sin( math.radians(-120) ) * (panjang * 2/27)
  # cnv.create_text(Ax + AB1x + AB4x + AB10x, Ay + AB1y + AB4y + AB10y, text='AB10')

  Xx = math.cos( math.radians(-60) ) * panjang/27
  Xy = math.sin( math.radians(-60) ) * panjang/27
  
  Yx = math.cos( math.radians(0) ) * panjang/27
  Yy = math.sin( math.radians(0) ) * panjang/27

  # ----------------------------------------------------2 SEGI3 Kanan Bawah------------------------------------------
  AB11x = math.cos( math.radians(0) ) * (panjang /27)
  AB11y = math.sin( math.radians(0) ) * (panjang /27)
  # cnv.create_text(Ax + AB2x + AB5x + AB11x, Ay + AB2y + AB5y + AB11y, text='AB11')

  AB12x = math.cos( math.radians(0) ) * (panjang * 2/27)
  AB12y = math.sin( math.radians(0) ) * (panjang * 2/27)
  # cnv.create_text(Ax + AB2x + AB5x + AB12x, Ay + AB2y + AB5y + AB12y, text='AB12')

  Vvx = math.cos( math.radians(60) ) * panjang/27
  Vvy = math.sin( math.radians(60) ) * panjang/27
  
  Wwx = math.cos( math.radians(120) ) * panjang/27
  Wwy = math.sin( math.radians(120) ) * panjang/27


  AB13x = math.cos( math.radians(60) ) * (panjang /27)
  AB13y = math.sin( math.radians(60) ) * (panjang /27)
  # cnv.create_text(Ax + AB2x + AB6x + AB13x, Ay + AB2y + AB6y + AB13y, text='AB13')

  AB14x = math.cos( math.radians(60) ) * (panjang * 2/27)
  AB14y = math.sin( math.radians(60) ) * (panjang * 2/27)
  # cnv.create_text(Ax + AB2x + AB6x + AB14x, Ay + AB2y + AB6y + AB14y, text='AB14')

  Zx = math.cos( math.radians(0) ) * panjang/27
  Zy = math.sin( math.radians(0) ) * panjang/27
  
  AAx = math.cos( math.radians(-60) ) * panjang/27
  AAy = math.sin( math.radians(-60) ) * panjang/27
  
  # ------------------------------------ 2 SEGI3 Bawah Kiri---------------------------------------
  BC7x = math.cos( math.radians(120) ) * (panjang /27)
  BC7y = math.sin( math.radians(120) ) * (panjang /27)
  # cnv.create_text(Ax + Cx + BC1x + BC3x + BC7x, Ay + Cy + BC1y + BC3y + BC7y, text='BC7')

  BC8x = math.cos( math.radians(120) ) * (panjang * 2/27)
  BC8y = math.sin( math.radians(120) ) * (panjang * 2/27)
  # cnv.create_text(Ax + Cx + BC1x + BC3x + BC8x, Ay + Cy + BC1y + BC3y + BC8y, text='BC8')


  ABx = math.cos( math.radians(180) ) * panjang/27
  ABy = math.sin( math.radians(180) ) * panjang/27
  
  ACx = math.cos( math.radians(-120) ) * panjang/27
  ACy = math.sin( math.radians(-120) ) * panjang/27

  BC9x = math.cos( math.radians(180) ) * (panjang /27)
  BC9y = math.sin( math.radians(180) ) * (panjang /27)
  # cnv.create_text(Ax + Cx + BC1x + BC4x + BC9x, Ay + Cy + BC1y + BC4y + BC9y, text='BC9')

  BC10x = math.cos( math.radians(180) ) * (panjang * 2/27)
  BC10y = math.sin( math.radians(180) ) * (panjang * 2/27)
  # cnv.create_text(Ax + Cx + BC1x + BC4x + BC10x, Ay + Cy + BC1y + BC4y + BC10y, text='BC10')


  ADx = math.cos( math.radians(120) ) * panjang/27
  ADy = math.sin( math.radians(120) ) * panjang/27
  
  AEx = math.cos( math.radians(60) ) * panjang/27
  AEy = math.sin( math.radians(60) ) * panjang/27

  # ------------------------------------ 2 SEGI3 Bawah Kanan---------------------------------------
  BC11x = math.cos( math.radians(60) ) * (panjang /27)
  BC11y = math.sin( math.radians(60) ) * (panjang /27)
  # cnv.create_text(Ax + Cx + BC2x + BC5x + BC11x, Ay + Cy + BC2y + BC5y + BC11y, text='BC11')

  BC12x = math.cos( math.radians(60) ) * (panjang * 2/27)
  BC12y = math.sin( math.radians(60) ) * (panjang * 2/27)
  # cnv.create_text(Ax + Cx + BC2x + BC5x + BC12x, Ay + Cy + BC2y + BC5y + BC12y, text='BC12')

  AFx = math.cos( math.radians(0) ) * panjang/27
  AFy = math.sin( math.radians(0) ) * panjang/27
  
  AGx = math.cos( math.radians(-60) ) * panjang/27
  AGy = math.sin( math.radians(-60) ) * panjang/27


  BC13x = math.cos( math.radians(0) ) * (panjang /27)
  BC13y = math.sin( math.radians(0) ) * (panjang /27)
  # cnv.create_text(Ax + Cx + BC2x + BC6x + BC13x, Ay + Cy + BC2y + BC6y + BC13y, text='BC13')

  BC14x = math.cos( math.radians(0) ) * (panjang * 2/27)
  BC14y = math.sin( math.radians(0) ) * (panjang * 2/27)
  # cnv.create_text(Ax + Cx + BC2x + BC6x + BC14x, Ay + Cy + BC2y + BC6y + BC14y, text='BC14')

  AHx = math.cos( math.radians(60) ) * panjang/27
  AHy = math.sin( math.radians(60) ) * panjang/27
  
  AIx = math.cos( math.radians(120) ) * panjang/27
  AIy = math.sin( math.radians(120) ) * panjang/27

  # ---------------------------------------------2 SEGI3 Kiri Atas----------------------------------------
  CA7x = math.cos( math.radians(-120) ) * (panjang /27)
  CA7y = math.sin( math.radians(-120) ) * (panjang /27)
  # cnv.create_text(Ax + CA1x + CA3x + CA7x, Ay + CA1y + CA3y + CA7y, text='CA7')
  CA8x = math.cos( math.radians(-120) ) * (panjang * 2/27)
  CA8y = math.sin( math.radians(-120) ) * (panjang * 2/27)
  # cnv.create_text(Ax + CA1x + CA3x + CA8x, Ay + CA1y + CA3y + CA8y, text='CA8')

  AJx = math.cos( math.radians(-60) ) * panjang/27
  AJy = math.sin( math.radians(-60) ) * panjang/27
  
  AKx = math.cos( math.radians(0) ) * panjang/27
  AKy = math.sin( math.radians(0) ) * panjang/27

  CA9x = math.cos( math.radians(-60) ) * (panjang /27)
  CA9y = math.sin( math.radians(-60) ) * (panjang /27)
  # cnv.create_text(Ax + CA1x + CA4x + CA9x, Ay + CA1y + CA4y + CA9y, text='CA9')
  CA10x = math.cos( math.radians(-60) ) * (panjang * 2/27)
  CA10y = math.sin( math.radians(-60) ) * (panjang * 2/27)
  # cnv.create_text(Ax + CA1x + CA4x + CA10x, Ay + CA1y + CA4y + CA10y, text='CA10')

  ALx = math.cos( math.radians(-120) ) * panjang/27
  ALy = math.sin( math.radians(-120) ) * panjang/27
  
  AMx = math.cos( math.radians(180) ) * panjang/27
  AMy = math.sin( math.radians(180) ) * panjang/27

  # ------------------------------------------2 SEGI3 Kiri Bawah------------------------------------------------
  CA11x = math.cos( math.radians(180) ) * (panjang /27)
  CA11y = math.sin( math.radians(180) ) * (panjang /27)
  # cnv.create_text(Ax + CA2x + CA5x + CA11x, Ay + CA2y + CA5y + CA11y, text='CA11')
  CA12x = math.cos( math.radians(180) ) * (panjang * 2/27)
  CA12y = math.sin( math.radians(180) ) * (panjang * 2/27)
  # cnv.create_text(Ax + CA2x + CA5x + CA12x, Ay + CA2y + CA5y + CA12y, text='CA12')

  ANx = math.cos( math.radians(120) ) * panjang/27
  ANy = math.sin( math.radians(120) ) * panjang/27
  
  AOx = math.cos( math.radians(60) ) * panjang/27
  AOy = math.sin( math.radians(60) ) * panjang/27

  CA13x = math.cos( math.radians(120) ) * (panjang /27)
  CA13y = math.sin( math.radians(120) ) * (panjang /27)
  # cnv.create_text(Ax + CA2x + CA6x + CA13x, Ay + CA2y + CA6y + CA13y, text='CA13')
  CA14x = math.cos( math.radians(120) ) * (panjang * 2/27)
  CA14y = math.sin( math.radians(120) ) * (panjang * 2/27)
  # cnv.create_text(Ax + CA2x + CA6x + CA14x, Ay + CA2y + CA6y + CA14y, text='CA14')

  APx = math.cos( math.radians(180) ) * panjang/27
  APy = math.sin( math.radians(180) ) * panjang/27
  
  AQx = math.cos( math.radians(-120) ) * panjang/27
  AQy = math.sin( math.radians(-120) ) * panjang/27

  # ============================================5555555555555=====================================================
  # ----------------------------------------- PADA SEGI3 LVL 4 (1)(1)------------------------------------------------
  AB15x = math.cos( math.radians(-120) ) * (panjang /81)
  AB15y = math.sin( math.radians(-120) ) * (panjang /81)
  # cnv.create_text(Ax + AB1x + AB3x + AB7x + AB15x, Ay + AB1y + AB3y + AB7y + AB15y, text='AB15')

  AB16x = math.cos( math.radians(-120) ) * (panjang * 2/81)
  AB16y = math.sin( math.radians(-120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB1x + AB3x + AB7x + AB16x, Ay + AB1y + AB3y + AB7y + AB16y, text='AB16')

  ARx = math.cos( math.radians(180) ) * panjang/81
  ARy = math.sin( math.radians(180) ) * panjang/81

  ASx = math.cos( math.radians(120) ) * panjang/81
  ASy = math.sin( math.radians(120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (1)(2)------------------------------------------------
  AB17x = math.cos( math.radians(180) ) * (panjang /81)
  AB17y = math.sin( math.radians(180) ) * (panjang /81)
  # cnv.create_text(Ax + AB1x + AB3x + AB8x + AB17x, Ay + AB1y + AB3y + AB8y + AB17y, text='AB17')

  AB18x = math.cos( math.radians(180) ) * (panjang * 2/81)
  AB18y = math.sin( math.radians(180) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB1x + AB3x + AB8x + AB18x, Ay + AB1y + AB3y + AB8y + AB18y, text='AB18')

  ATx = math.cos( math.radians(-120) ) * panjang/81
  ATy = math.sin( math.radians(-120) ) * panjang/81

  AUx = math.cos( math.radians(-60) ) * panjang/81
  AUy = math.sin( math.radians(-60) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (2)(1)------------------------------------------------
  AB19x = math.cos( math.radians(0) ) * (panjang /81)
  AB19y = math.sin( math.radians(0) ) * (panjang /81)
  # cnv.create_text(Ax + AB1x + AB4x + AB10x + AB19x, Ay + AB1y + AB4y + AB10y + AB19y, text='AB19')

  AB20x = math.cos( math.radians(0) ) * (panjang * 2/81)
  AB20y = math.sin( math.radians(0) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB1x + AB4x + AB10x + AB20x, Ay + AB1y + AB4y + AB10y + AB20y, text='AB20')

  AVx = math.cos( math.radians(-60) ) * panjang/81
  AVy = math.sin( math.radians(-60) ) * panjang/81

  AWx = math.cos( math.radians(-120) ) * panjang/81
  AWy = math.sin( math.radians(-120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (2)(2)------------------------------------------------
  AB21x = math.cos( math.radians(-60) ) * (panjang /81)
  AB21y = math.sin( math.radians(-60) ) * (panjang /81)
  # cnv.create_text(Ax + AB1x + AB4x + AB9x + AB21x, Ay + AB1y + AB4y + AB9y + AB21y, text='AB21')

  AB22x = math.cos( math.radians(-60) ) * (panjang * 2/81)
  AB22y = math.sin( math.radians(-60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB1x + AB4x + AB9x + AB22x, Ay + AB1y + AB4y + AB9y + AB22y, text='AB22')

  AXx = math.cos( math.radians(0) ) * panjang/81
  AXy = math.sin( math.radians(0) ) * panjang/81

  AYx = math.cos( math.radians(60) ) * panjang/81
  AYy = math.sin( math.radians(60) ) * panjang/81

  # ----------------------------------------- PADA SEGI3 LVL 4 (3)(1)------------------------------------------------
  AB23x = math.cos( math.radians(0) ) * (panjang /81)
  AB23y = math.sin( math.radians(0) ) * (panjang /81)
  # cnv.create_text(Ax + AB2x + AB6x + AB13x + AB23x, Ay + AB2y + AB6y + AB13y + AB23y, text='AB23')

  AB24x = math.cos( math.radians(0) ) * (panjang * 2/81)
  AB24y = math.sin( math.radians(0) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB2x + AB6x + AB13x + AB24x, Ay + AB2y + AB6y + AB13y + AB24y, text='AB24')

  AZx = math.cos( math.radians(-60) ) * panjang/81
  AZy = math.sin( math.radians(-60) ) * panjang/81

  BAx = math.cos( math.radians(-120) ) * panjang/81
  BAy = math.sin( math.radians(-120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (3)(2)------------------------------------------------
  AB25x = math.cos( math.radians(-60) ) * (panjang /81)
  AB25y = math.sin( math.radians(-60) ) * (panjang /81)
  # cnv.create_text(Ax + AB2x + AB6x + AB14x + AB25x, Ay + AB2y + AB6y + AB14y + AB25y, text='AB25')

  AB26x = math.cos( math.radians(-60) ) * (panjang * 2/81)
  AB26y = math.sin( math.radians(-60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB2x + AB6x + AB14x + AB26x, Ay + AB2y + AB6y + AB14y + AB26y, text='AB26')

  BBx = math.cos( math.radians(0) ) * panjang/81
  BBy = math.sin( math.radians(0) ) * panjang/81

  BCx = math.cos( math.radians(60) ) * panjang/81
  BCy = math.sin( math.radians(60) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (4)(1)------------------------------------------------
  AB27x = math.cos( math.radians(120) ) * (panjang /81)
  AB27y = math.sin( math.radians(120) ) * (panjang /81)
  # cnv.create_text(Ax + AB2x + AB5x + AB12x + AB27x, Ay + AB2y + AB5y + AB12y + AB27y, text='AB27')

  AB28x = math.cos( math.radians(120) ) * (panjang * 2/81)
  AB28y = math.sin( math.radians(120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB2x + AB5x + AB12x + AB28x, Ay + AB2y + AB5y + AB12y + AB28y, text='AB28')

  BDx = math.cos( math.radians(60) ) * panjang/81
  BDy = math.sin( math.radians(60) ) * panjang/81

  BEx = math.cos( math.radians(0) ) * panjang/81
  BEy = math.sin( math.radians(0) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (4)(2)------------------------------------------------
  AB29x = math.cos( math.radians(60) ) * (panjang /81)
  AB29y = math.sin( math.radians(60) ) * (panjang /81)
  # cnv.create_text(Ax + AB2x + AB5x + AB11x + AB29x, Ay + AB2y + AB5y + AB11y + AB29y, text='AB29')

  AB30x = math.cos( math.radians(60) ) * (panjang * 2/81)
  AB30y = math.sin( math.radians(60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + AB2x + AB5x + AB11x + AB30x, Ay + AB2y + AB5y + AB11y + AB30y, text='AB30')

  BFx = math.cos( math.radians(120) ) * panjang/81
  BFy = math.sin( math.radians(120) ) * panjang/81

  BGx = math.cos( math.radians(180) ) * panjang/81
  BGy = math.sin( math.radians(180) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (5)(1)------------------------------------------------
  BC15x = math.cos( math.radians(0) ) * (panjang /81)
  BC15y = math.sin( math.radians(0) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC2x + BC5x + BC11x + BC15x, Ay + Cy + BC2y + BC5y + BC11y + BC15y, text='BC15')

  BC16x = math.cos( math.radians(0) ) * (panjang * 2/81)
  BC16y = math.sin( math.radians(0) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC2x + BC5x + BC11x + BC16x, Ay + Cy + BC2y + BC5y + BC11y + BC16y, text='BC16')

  BHx = math.cos( math.radians(-60) ) * panjang/81
  BHy = math.sin( math.radians(-60) ) * panjang/81

  BIx = math.cos( math.radians(-120) ) * panjang/81
  BIy = math.sin( math.radians(-120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (5)(2)------------------------------------------------
  BC17x = math.cos( math.radians(-60) ) * (panjang /81)
  BC17y = math.sin( math.radians(-60) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC2x + BC5x + BC12x + BC17x, Ay + Cy + BC2y + BC5y + BC12y + BC17y, text='BC17')

  BC18x = math.cos( math.radians(-60) ) * (panjang * 2/81)
  BC18y = math.sin( math.radians(-60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC2x + BC5x + BC12x + BC18x, Ay + Cy + BC2y + BC5y + BC12y + BC18y, text='BC18')

  BJx = math.cos( math.radians(0) ) * panjang/81
  BJy = math.sin( math.radians(0) ) * panjang/81

  BKx = math.cos( math.radians(60) ) * panjang/81
  BKy = math.sin( math.radians(60) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (6)(1)------------------------------------------------
  BC19x = math.cos( math.radians(120) ) * (panjang /81)
  BC19y = math.sin( math.radians(120) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC2x + BC6x + BC14x + BC19x, Ay + Cy + BC2y + BC6y + BC14y + BC19y, text='BC19')

  BC20x = math.cos( math.radians(120) ) * (panjang * 2/81)
  BC20y = math.sin( math.radians(120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC2x + BC6x + BC14x + BC20x, Ay + Cy + BC2y + BC6y + BC14y + BC20y, text='BC20')

  BLx = math.cos( math.radians(60) ) * panjang/81
  BLy = math.sin( math.radians(60) ) * panjang/81

  BMx = math.cos( math.radians(0) ) * panjang/81
  BMy = math.sin( math.radians(0) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (6)(2)------------------------------------------------
  BC21x = math.cos( math.radians(60) ) * (panjang /81)
  BC21y = math.sin( math.radians(60) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC2x + BC6x + BC13x + BC21x, Ay + Cy + BC2y + BC6y + BC13y + BC21y, text='BC21')

  BC22x = math.cos( math.radians(60) ) * (panjang * 2/81)
  BC22y = math.sin( math.radians(60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC2x + BC6x + BC13x + BC22x, Ay + Cy + BC2y + BC6y + BC13y + BC22y, text='BC22')

  BNx = math.cos( math.radians(120) ) * panjang/81
  BNy = math.sin( math.radians(120) ) * panjang/81

  BOx = math.cos( math.radians(180) ) * panjang/81
  BOy = math.sin( math.radians(180) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (7)(1)------------------------------------------------
  BC23x = math.cos( math.radians(120) ) * (panjang /81)
  BC23y = math.sin( math.radians(120) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC1x + BC4x + BC9x + BC23x, Ay + Cy + BC1y + BC4y + BC9y + BC23y, text='BC23')

  BC24x = math.cos( math.radians(120) ) * (panjang * 2/81)
  BC24y = math.sin( math.radians(120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC1x + BC4x + BC9x + BC24x, Ay + Cy + BC1y + BC4y + BC9y + BC24y, text='BC24')

  BPx = math.cos( math.radians(60) ) * panjang/81
  BPy = math.sin( math.radians(60) ) * panjang/81

  BQx = math.cos( math.radians(0) ) * panjang/81
  BQy = math.sin( math.radians(0) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (7)(2)------------------------------------------------
  BC25x = math.cos( math.radians(60) ) * (panjang /81)
  BC25y = math.sin( math.radians(60) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC1x + BC4x + BC10x + BC25x, Ay + Cy + BC1y + BC4y + BC10y + BC25y, text='BC25')

  BC26x = math.cos( math.radians(60) ) * (panjang * 2/81)
  BC26y = math.sin( math.radians(60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC1x + BC4x + BC10x + BC26x, Ay + Cy + BC1y + BC4y + BC10y + BC26y, text='BC26')

  BRx = math.cos( math.radians(120) ) * panjang/81
  BRy = math.sin( math.radians(120) ) * panjang/81

  BSx = math.cos( math.radians(180) ) * panjang/81
  BSy = math.sin( math.radians(180) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (8)(1)------------------------------------------------
  BC27x = math.cos( math.radians(180) ) * (panjang /81)
  BC27y = math.sin( math.radians(180) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC1x + BC3x + BC7x + BC27x, Ay + Cy + BC1y + BC3y + BC7y + BC27y, text='BC27')

  BC28x = math.cos( math.radians(180) ) * (panjang * 2/81)
  BC28y = math.sin( math.radians(180) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC1x + BC3x + BC7x + BC28x, Ay + Cy + BC1y + BC3y + BC7y + BC28y, text='BC28')

  BTx = math.cos( math.radians(-120) ) * panjang/81
  BTy = math.sin( math.radians(-120) ) * panjang/81

  BUx = math.cos( math.radians(-60) ) * panjang/81
  BUy = math.sin( math.radians(-60) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (8)(2)------------------------------------------------
  BC29x = math.cos( math.radians(-120) ) * (panjang /81)
  BC29y = math.sin( math.radians(-120) ) * (panjang /81)
  # cnv.create_text(Ax + Cx + BC1x + BC3x + BC8x + BC29x, Ay + Cy + BC1y + BC3y + BC8y + BC29y, text='BC29')

  BC30x = math.cos( math.radians(-120) ) * (panjang * 2/81)
  BC30y = math.sin( math.radians(-120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + Cx + BC1x + BC3x + BC8x + BC30x, Ay + Cy + BC1y + BC3y + BC8y + BC30y, text='BC30')

  BVx = math.cos( math.radians(180) ) * panjang/81
  BVy = math.sin( math.radians(180) ) * panjang/81

  BWx = math.cos( math.radians(120) ) * panjang/81
  BWy = math.sin( math.radians(120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (9)(1)------------------------------------------------
  CA15x = math.cos( math.radians(120) ) * (panjang /81)
  CA15y = math.sin( math.radians(120) ) * (panjang /81)
  # cnv.create_text(Ax + CA2x + CA5x + CA11x + CA15x, Ay + CA2y + CA5y + CA11y + CA15y, text='CA15')

  CA16x = math.cos( math.radians(120) ) * (panjang * 2/81)
  CA16y = math.sin( math.radians(120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA2x + CA5x + CA11x + CA16x, Ay + CA2y + CA5y + CA11y + CA16y, text='CA16')

  BXx = math.cos( math.radians(60) ) * panjang/81
  BXy = math.sin( math.radians(60) ) * panjang/81

  BYx = math.cos( math.radians(0) ) * panjang/81
  BYy = math.sin( math.radians(0) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (9)(2)------------------------------------------------
  CA17x = math.cos( math.radians(60) ) * (panjang /81)
  CA17y = math.sin( math.radians(60) ) * (panjang /81)
  # cnv.create_text(Ax + CA2x + CA5x + CA12x + CA17x, Ay + CA2y + CA5y + CA12y + CA17y, text='CA17')

  CA18x = math.cos( math.radians(60) ) * (panjang * 2/81)
  CA18y = math.sin( math.radians(60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA2x + CA5x + CA12x + CA18x, Ay + CA2y + CA5y + CA12y + CA18y, text='CA18')

  BZx = math.cos( math.radians(120) ) * panjang/81
  BZy = math.sin( math.radians(120) ) * panjang/81

  CAx = math.cos( math.radians(180) ) * panjang/81
  CAy = math.sin( math.radians(180) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (10)(1)------------------------------------------------
  CA19x = math.cos( math.radians(-120) ) * (panjang /81)
  CA19y = math.sin( math.radians(-120) ) * (panjang /81)
  # cnv.create_text(Ax + CA2x + CA6x + CA14x + CA19x, Ay + CA2y + CA6y + CA14y + CA19y, text='CA19')

  CA20x = math.cos( math.radians(-120) ) * (panjang * 2/81)
  CA20y = math.sin( math.radians(-120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA2x + CA6x + CA14x + CA20x, Ay + CA2y + CA6y + CA14y + CA20y, text='CA20')

  CBx = math.cos( math.radians(180) ) * panjang/81
  CBy = math.sin( math.radians(180) ) * panjang/81

  CCx = math.cos( math.radians(120) ) * panjang/81
  CCy = math.sin( math.radians(120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (10)(2)------------------------------------------------
  CA21x = math.cos( math.radians(180) ) * (panjang /81)
  CA21y = math.sin( math.radians(180) ) * (panjang /81)
  # cnv.create_text(Ax + CA2x + CA6x + CA13x + CA21x, Ay + CA2y + CA6y + CA13y + CA21y, text='CA21')

  CA22x = math.cos( math.radians(180) ) * (panjang * 2/81)
  CA22y = math.sin( math.radians(180) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA2x + CA6x + CA13x + CA22x, Ay + CA2y + CA6y + CA13y + CA22y, text='CA22')

  CDx = math.cos( math.radians(-120) ) * panjang/81
  CDy = math.sin( math.radians(-120) ) * panjang/81

  CEx = math.cos( math.radians(-60) ) * panjang/81
  CEy = math.sin( math.radians(-60) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (11)(1)------------------------------------------------
  CA23x = math.cos( math.radians(-120) ) * (panjang /81)
  CA23y = math.sin( math.radians(-120) ) * (panjang /81)
  # cnv.create_text(Ax + CA1x + CA4x + CA9x + CA23x, Ay + CA1y + CA4y + CA9y + CA23y, text='CA21')

  CA24x = math.cos( math.radians(-120) ) * (panjang * 2/81)
  CA24y = math.sin( math.radians(-120) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA1x + CA4x + CA9x + CA24x, Ay + CA1y + CA4y + CA9y + CA24y, text='CA24')

  CFx = math.cos( math.radians(180) ) * panjang/81
  CFy = math.sin( math.radians(180) ) * panjang/81

  CGx = math.cos( math.radians(120) ) * panjang/81
  CGy = math.sin( math.radians(120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (11)(2)------------------------------------------------
  CA25x = math.cos( math.radians(180) ) * (panjang /81)
  CA25y = math.sin( math.radians(180) ) * (panjang /81)
  # cnv.create_text(Ax + CA1x + CA4x + CA10x + CA25x, Ay + CA1y + CA4y + CA10y + CA25y, text='CA21')

  CA26x = math.cos( math.radians(180) ) * (panjang * 2/81)
  CA26y = math.sin( math.radians(180) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA1x + CA4x + CA10x + CA26x, Ay + CA1y + CA4y + CA10y + CA26y, text='CA26')

  CHx = math.cos( math.radians(-120) ) * panjang/81
  CHy = math.sin( math.radians(-120) ) * panjang/81

  CIx = math.cos( math.radians(-60) ) * panjang/81
  CIy = math.sin( math.radians(-60) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (12)(1)------------------------------------------------
  CA27x = math.cos( math.radians(0) ) * (panjang /81)
  CA27y = math.sin( math.radians(0) ) * (panjang /81)
  # cnv.create_text(Ax + CA1x + CA3x + CA8x + CA27x, Ay + CA1y + CA3y + CA8y + CA27y, text='CA21')

  CA28x = math.cos( math.radians(0) ) * (panjang * 2/81)
  CA28y = math.sin( math.radians(0) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA1x + CA3x + CA8x + CA28x, Ay + CA1y + CA3y + CA8y + CA28y, text='CA28')

  CJx = math.cos( math.radians(-60) ) * panjang/81
  CJy = math.sin( math.radians(-60) ) * panjang/81

  CKx = math.cos( math.radians(-120) ) * panjang/81
  CKy = math.sin( math.radians(-120) ) * panjang/81
  # ----------------------------------------- PADA SEGI3 LVL 4 (12)(1)------------------------------------------------
  CA29x = math.cos( math.radians(-60) ) * (panjang /81)
  CA29y = math.sin( math.radians(-60) ) * (panjang /81)
  # cnv.create_text(Ax + CA1x + CA3x + CA7x + CA29x, Ay + CA1y + CA3y + CA7y + CA29y, text='CA21')

  CA30x = math.cos( math.radians(-60) ) * (panjang * 2/81)
  CA30y = math.sin( math.radians(-60) ) * (panjang * 2/81)
  # cnv.create_text(Ax + CA1x + CA3x + CA7x + CA30x, Ay + CA1y + CA3y + CA7y + CA30y, text='CA30')

  CLx = math.cos( math.radians(0) ) * panjang/81
  CLy = math.sin( math.radians(0) ) * panjang/81

  CMx = math.cos( math.radians(60) ) * panjang/81
  CMy = math.sin( math.radians(60) ) * panjang/81
  if curlvl -1 == lvl:
    pass
  else :
    if curlvl == 1:
      cnv.create_line(Ax, Ay, Ax+Bx, Ay+By)
      cnv.create_line(Ax, Ay, Ax+Cx, Ay+Cy)
      cnv.create_line(Ax+Bx, Ay+By, Ax+Cx, Ay+Cy)

      segitiga(cnv, lvl, curlvl + 1, panjang, titikA)
    elif curlvl == 2:
      cnv.create_line(Ax + AB1x, Ay + AB1y, Ax + AB1x + Dx, Ay + AB1y + Dy )
      cnv.create_line(Ax + AB2x, Ay + AB2y, Ax + AB2x + Ex, Ay + AB2y + Ey )
      cnv.create_line(Ax + CA1x, Ay + CA1y, Ax + CA1x + Fx, Ay + CA1y + Fy )
      cnv.create_line(Ax + CA2x, Ay + CA2y, Ax + CA2x + Gx, Ay + CA2y + Gy)
      cnv.create_line(Ax + Cx + BC1x, Ay + Cy + BC1y, Ax + Cx + BC1x + Hx, Ay + Cy + BC1y + Hy)
      cnv.create_line(Ax + Cx + BC2x, Ay + Cy + BC2y, Ax + Cx + BC2x + Ix, Ay + Cy + BC2y + Iy)
      segitiga(cnv, lvl, curlvl + 1, panjang, titikA)

      
    elif curlvl == 3:
      #----------------------------------------------------AB------------------------------------------------------------
      cnv.create_line(Ax + AB1x + AB3x,  Ay + AB1y + AB3y, Ax + AB1x + AB3x + Jx,  Ay + AB1y + AB3y + Jy)
      cnv.create_line(Ax + AB1x + AB4x,  Ay + AB1y + AB4y, Ax + AB1x + AB4x + Kx,  Ay + AB1y + AB4y + Ky)
      cnv.create_line(Ax + AB2x + AB5x,  Ay + AB2y + AB5y, Ax + AB2x + AB5x + Lx,  Ay + AB2y + AB5y + Ly)
      cnv.create_line(Ax + AB2x + AB6x,  Ay + AB2y + AB6y, Ax + AB2x + AB6x + Mx,  Ay + AB2y + AB6y + My)

      # --------------------------------------------BC----------------------------------------------------
      cnv.create_line(Ax + Cx + BC1x + BC3x, Ay + Cy + BC1y + BC3y, Ax + Cx + BC1x + BC3x + Nx, Ay + Cy + BC1y + BC3y + Ny)
      cnv.create_line(Ax + Cx + BC1x + BC4x, Ay + Cy + BC1y + BC4y, Ax + Cx + BC1x + BC4x + Ox, Ay + Cy + BC1y + BC4y + Oy)
      cnv.create_line(Ax + Cx + BC2x + BC5x, Ay + Cy + BC2y + BC5y, Ax + Cx + BC2x + BC5x + Px, Ay + Cy + BC2y + BC5y + Py)
      cnv.create_line(Ax + Cx + BC2x + BC6x, Ay + Cy + BC2y + BC6y, Ax + Cx + BC2x + BC6x + Qx, Ay + Cy + BC2y + BC6y + Qy)

      # -----------------------------------------------AC-------------------------------------------------
      cnv.create_line(Ax + CA1x + CA3x,  Ay + CA1y + CA3y, Ax + CA1x + CA3x + Rx,  Ay + CA1y + CA3y + Ry)
      cnv.create_line(Ax + CA1x + CA4x,  Ay + CA1y + CA4y, Ax + CA1x + CA4x + Sx,  Ay + CA1y + CA4y + Sy)
      cnv.create_line(Ax + CA2x + CA5x,  Ay + CA2y + CA5y, Ax + CA2x + CA5x + Tx,  Ay + CA2y + CA5y + Ty)
      cnv.create_line(Ax + CA2x + CA6x,  Ay + CA2y + CA6y, Ax + CA2x + CA6x + Ux,  Ay + CA2y + CA6y + Uy)
      segitiga(cnv, lvl, curlvl + 1, panjang, titikA)

    elif curlvl == 4 :
      # ----------------------------------------------------2 SEGI3 Kanan Atas------------------------------------------
      cnv.create_line(Ax + AB1x + AB3x + AB7x, Ay + AB1y + AB3y + AB7y,Ax + AB1x + AB3x + AB7x + Vx, Ay + AB1y + AB3y + AB7y + Vy)
      cnv.create_line(Ax + AB1x + AB3x + AB8x, Ay + AB1y + AB3y + AB8y,Ax + AB1x + AB3x + AB8x + Wx, Ay + AB1y + AB3y + AB8y + Wy)
      cnv.create_line(Ax + AB1x + AB4x + AB9x, Ay + AB1y + AB4y + AB9y,Ax + AB1x + AB4x + AB9x + Xx, Ay + AB1y + AB4y + AB9y + Xy)
      cnv.create_line(Ax + AB1x + AB4x + AB10x, Ay + AB1y + AB4y + AB10y,Ax + AB1x + AB4x + AB10x + Yx, Ay + AB1y + AB4y + AB10y + Yy)

      # ----------------------------------------------------2 SEGI3 Kanan Bawah------------------------------------------
      cnv.create_line(Ax + AB2x + AB5x + AB11x, Ay + AB2y + AB5y + AB11y,Ax + AB2x + AB5x + AB11x + Vvx, Ay + AB2y + AB5y + AB11y + Vvy)
      cnv.create_line(Ax + AB2x + AB5x + AB12x, Ay + AB2y + AB5y + AB12y,Ax + AB2x + AB5x + AB12x + Wwx, Ay + AB2y + AB5y + AB12y + Wwy)
      cnv.create_line(Ax + AB2x + AB6x + AB13x, Ay + AB2y + AB6y + AB13y,Ax + AB2x + AB6x + AB13x + Zx, Ay + AB2y + AB6y + AB13y + Zy)
      cnv.create_line(Ax + AB2x + AB6x + AB14x, Ay + AB2y + AB6y + AB14y, Ax + AB2x + AB6x + AB14x + AAx, Ay + AB2y + AB6y + AB14y + AAy)
      
      # ------------------------------------ 2 SEGI3 Bawah Kiri---------------------------------------
      cnv.create_line(Ax + Cx + BC1x + BC3x + BC7x, Ay + Cy + BC1y + BC3y + BC7y,Ax + Cx + BC1x + BC3x + BC7x + ABx, Ay + Cy + BC1y + BC3y + BC7y + ABy)
      cnv.create_line(Ax + Cx + BC1x + BC3x + BC8x, Ay + Cy + BC1y + BC3y + BC8y,Ax + Cx + BC1x + BC3x + BC8x + ACx, Ay + Cy + BC1y + BC3y + BC8y + ACy)
      cnv.create_line(Ax + Cx + BC1x + BC4x + BC9x, Ay + Cy + BC1y + BC4y + BC9y,Ax + Cx + BC1x + BC4x + BC9x + ADx, Ay + Cy + BC1y + BC4y + BC9y + ADy)
      cnv.create_line(Ax + Cx + BC1x + BC4x + BC10x, Ay + Cy + BC1y + BC4y + BC10y,Ax + Cx + BC1x + BC4x + BC10x + AEx, Ay + Cy + BC1y + BC4y + BC10y + AEy)

      # ------------------------------------ 2 SEGI3 Bawah Kanan---------------------------------------
      cnv.create_line(Ax + Cx + BC2x + BC5x + BC11x, Ay + Cy + BC2y + BC5y + BC11y,Ax + Cx + BC2x + BC5x + BC11x + AFx, Ay + Cy + BC2y + BC5y + BC11y + AFy)
      cnv.create_line(Ax + Cx + BC2x + BC5x + BC12x, Ay + Cy + BC2y + BC5y + BC12y,Ax + Cx + BC2x + BC5x + BC12x + AGx, Ay + Cy + BC2y + BC5y + BC12y + AGy)
      cnv.create_line(Ax + Cx + BC2x + BC6x + BC13x, Ay + Cy + BC2y + BC6y + BC13y,Ax + Cx + BC2x + BC6x + BC13x + AHx, Ay + Cy + BC2y + BC6y + BC13y + AHy)
      cnv.create_line(Ax + Cx + BC2x + BC6x + BC14x, Ay + Cy + BC2y + BC6y + BC14y,Ax + Cx + BC2x + BC6x + BC14x + AIx, Ay + Cy + BC2y + BC6y + BC14y + AIy)

      # ---------------------------------------------2 SEGI3 Kiri Atas----------------------------------------
      cnv.create_line(Ax + CA1x + CA3x + CA7x, Ay + CA1y + CA3y + CA7y,Ax + CA1x + CA3x + CA7x + AJx, Ay + CA1y + CA3y + CA7y + AJy)
      cnv.create_line(Ax + CA1x + CA3x + CA8x, Ay + CA1y + CA3y + CA8y,Ax + CA1x + CA3x + CA8x + AKx, Ay + CA1y + CA3y + CA8y + AKy)
      cnv.create_line(Ax + CA1x + CA4x + CA9x, Ay + CA1y + CA4y + CA9y,Ax + CA1x + CA4x + CA9x + ALx, Ay + CA1y + CA4y + CA9y + ALy)
      cnv.create_line(Ax + CA1x + CA4x + CA10x, Ay + CA1y + CA4y + CA10y,Ax + CA1x + CA4x + CA10x + AMx, Ay + CA1y + CA4y + CA10y + AMy)

      # ------------------------------------------2 SEGI3 Kiri Bawah------------------------------------------------
      cnv.create_line(Ax + CA2x + CA5x + CA11x, Ay + CA2y + CA5y + CA11y,Ax + CA2x + CA5x + CA11x + ANx, Ay + CA2y + CA5y + CA11y + ANy)
      cnv.create_line(Ax + CA2x + CA5x + CA12x, Ay + CA2y + CA5y + CA12y,Ax + CA2x + CA5x + CA12x + AOx, Ay + CA2y + CA5y + CA12y + AOy)
      cnv.create_line(Ax + CA2x + CA6x + CA13x, Ay + CA2y + CA6y + CA13y,Ax + CA2x + CA6x + CA13x + APx, Ay + CA2y + CA6y + CA13y + APy)
      cnv.create_line(Ax + CA2x + CA6x + CA14x, Ay + CA2y + CA6y + CA14y,Ax + CA2x + CA6x + CA14x + AQx, Ay + CA2y + CA6y + CA14y + AQy)
      segitiga(cnv, lvl, curlvl + 1, panjang, titikA)

    elif curlvl == 5 :
      # ============================================5555555555555=====================================================
      # ----------------------------------------- PADA SEGI3 LVL 4 (1)(1)------------------------------------------------
      cnv.create_line(Ax + AB1x + AB3x + AB7x + AB15x, Ay + AB1y + AB3y + AB7y + AB15y,Ax + AB1x + AB3x + AB7x + AB15x + ARx, Ay + AB1y + AB3y + AB7y + AB15y + ARy)
      cnv.create_line(Ax + AB1x + AB3x + AB7x + AB16x, Ay + AB1y + AB3y + AB7y + AB16y,Ax + AB1x + AB3x + AB7x + AB16x + ASx, Ay + AB1y + AB3y + AB7y + AB16y + ASy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (1)(2)------------------------------------------------
      cnv.create_line(Ax + AB1x + AB3x + AB8x + AB17x, Ay + AB1y + AB3y + AB8y + AB17y,Ax + AB1x + AB3x + AB8x + AB17x + ATx, Ay + AB1y + AB3y + AB8y + AB17y + ATy)
      cnv.create_line(Ax + AB1x + AB3x + AB8x + AB18x, Ay + AB1y + AB3y + AB8y + AB18y,Ax + AB1x + AB3x + AB8x + AB18x + AUx, Ay + AB1y + AB3y + AB8y + AB18y + AUy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (2)(1)------------------------------------------------
      cnv.create_line(Ax + AB1x + AB4x + AB10x + AB19x, Ay + AB1y + AB4y + AB10y + AB19y,Ax + AB1x + AB4x + AB10x + AB19x + AVx, Ay + AB1y + AB4y + AB10y + AB19y + AVy)
      cnv.create_line(Ax + AB1x + AB4x + AB10x + AB20x, Ay + AB1y + AB4y + AB10y + AB20y,Ax + AB1x + AB4x + AB10x + AB20x + AWx, Ay + AB1y + AB4y + AB10y + AB20y + AWy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (2)(2)------------------------------------------------
      cnv.create_line(Ax + AB1x + AB4x + AB9x + AB21x, Ay + AB1y + AB4y + AB9y + AB21y,Ax + AB1x + AB4x + AB9x + AB21x + AXx, Ay + AB1y + AB4y + AB9y + AB21y + AXy)
      cnv.create_line(Ax + AB1x + AB4x + AB9x + AB22x, Ay + AB1y + AB4y + AB9y + AB22y,Ax + AB1x + AB4x + AB9x + AB22x + AYx, Ay + AB1y + AB4y + AB9y + AB22y + AYy)
      
      # ----------------------------------------- PADA SEGI3 LVL 4 (3)(1)------------------------------------------------
      cnv.create_line(Ax + AB2x + AB6x + AB13x + AB23x, Ay + AB2y + AB6y + AB13y + AB23y,Ax + AB2x + AB6x + AB13x + AB23x + AZx, Ay + AB2y + AB6y + AB13y + AB23y + AZy)
      cnv.create_line(Ax + AB2x + AB6x + AB13x + AB24x, Ay + AB2y + AB6y + AB13y + AB24y,Ax + AB2x + AB6x + AB13x + AB24x + BAx, Ay + AB2y + AB6y + AB13y + AB24y + BAy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (3)(2)------------------------------------------------
      cnv.create_line(Ax + AB2x + AB6x + AB14x + AB25x, Ay + AB2y + AB6y + AB14y + AB25y,Ax + AB2x + AB6x + AB14x + AB25x + BBx, Ay + AB2y + AB6y + AB14y + AB25y + BBy)
      cnv.create_line(Ax + AB2x + AB6x + AB14x + AB26x, Ay + AB2y + AB6y + AB14y + AB26y,Ax + AB2x + AB6x + AB14x + AB26x + BCx, Ay + AB2y + AB6y + AB14y + AB26y + BCy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (4)(1)------------------------------------------------
      cnv.create_line(Ax + AB2x + AB5x + AB12x + AB27x, Ay + AB2y + AB5y + AB12y + AB27y,Ax + AB2x + AB5x + AB12x + AB27x + BDx, Ay + AB2y + AB5y + AB12y + AB27y + BDy)
      cnv.create_line(Ax + AB2x + AB5x + AB12x + AB28x, Ay + AB2y + AB5y + AB12y + AB28y,Ax + AB2x + AB5x + AB12x + AB28x + BEx, Ay + AB2y + AB5y + AB12y + AB28y + BEy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (4)(2)------------------------------------------------
      cnv.create_line(Ax + AB2x + AB5x + AB11x + AB29x, Ay + AB2y + AB5y + AB11y + AB29y,Ax + AB2x + AB5x + AB11x + AB29x + BFx, Ay + AB2y + AB5y + AB11y + AB29y + BFy)
      cnv.create_line(Ax + AB2x + AB5x + AB11x + AB30x, Ay + AB2y + AB5y + AB11y + AB30y,Ax + AB2x + AB5x + AB11x + AB30x + BGx, Ay + AB2y + AB5y + AB11y + AB30y + BGy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (5)(1)------------------------------------------------
      cnv.create_line(Ax + Cx + BC2x + BC5x + BC11x + BC15x, Ay + Cy + BC2y + BC5y + BC11y + BC15y,Ax + Cx + BC2x + BC5x + BC11x + BC15x + BHx, Ay + Cy + BC2y + BC5y + BC11y + BC15y + BHy)
      cnv.create_line(Ax + Cx + BC2x + BC5x + BC11x + BC16x, Ay + Cy + BC2y + BC5y + BC11y + BC16y,Ax + Cx + BC2x + BC5x + BC11x + BC16x + BIx, Ay + Cy + BC2y + BC5y + BC11y + BC16y + BIy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (5)(2)------------------------------------------------
      cnv.create_line(Ax + Cx + BC2x + BC5x + BC12x + BC17x, Ay + Cy + BC2y + BC5y + BC12y + BC17y,Ax + Cx + BC2x + BC5x + BC12x + BC17x + BJx, Ay + Cy + BC2y + BC5y + BC12y + BC17y + BJy)
      cnv.create_line(Ax + Cx + BC2x + BC5x + BC12x + BC18x, Ay + Cy + BC2y + BC5y + BC12y + BC18y,Ax + Cx + BC2x + BC5x + BC12x + BC18x + BKx, Ay + Cy + BC2y + BC5y + BC12y + BC18y + BKy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (6)(1)------------------------------------------------
      cnv.create_line(Ax + Cx + BC2x + BC6x + BC14x + BC19x, Ay + Cy + BC2y + BC6y + BC14y + BC19y,Ax + Cx + BC2x + BC6x + BC14x + BC19x + BLx, Ay + Cy + BC2y + BC6y + BC14y + BC19y + BLy)
      cnv.create_line(Ax + Cx + BC2x + BC6x + BC14x + BC20x, Ay + Cy + BC2y + BC6y + BC14y + BC20y,Ax + Cx + BC2x + BC6x + BC14x + BC20x + BMx, Ay + Cy + BC2y + BC6y + BC14y + BC20y + BMy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (6)(2)------------------------------------------------
      cnv.create_line(Ax + Cx + BC2x + BC6x + BC13x + BC21x, Ay + Cy + BC2y + BC6y + BC13y + BC21y,Ax + Cx + BC2x + BC6x + BC13x + BC21x + BNx, Ay + Cy + BC2y + BC6y + BC13y + BC21y + BNy)
      cnv.create_line(Ax + Cx + BC2x + BC6x + BC13x + BC22x, Ay + Cy + BC2y + BC6y + BC13y + BC22y,Ax + Cx + BC2x + BC6x + BC13x + BC22x + BOx, Ay + Cy + BC2y + BC6y + BC13y + BC22y + BOy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (7)(1)------------------------------------------------
      cnv.create_line(Ax + Cx + BC1x + BC4x + BC9x + BC23x, Ay + Cy + BC1y + BC4y + BC9y + BC23y,Ax + Cx + BC1x + BC4x + BC9x + BC23x + BPx, Ay + Cy + BC1y + BC4y + BC9y + BC23y + BPy)
      cnv.create_line(Ax + Cx + BC1x + BC4x + BC9x + BC24x, Ay + Cy + BC1y + BC4y + BC9y + BC24y,Ax + Cx + BC1x + BC4x + BC9x + BC24x + BQx, Ay + Cy + BC1y + BC4y + BC9y + BC24y + BQy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (7)(2)------------------------------------------------
      cnv.create_line(Ax + Cx + BC1x + BC4x + BC10x + BC25x, Ay + Cy + BC1y + BC4y + BC10y + BC25y,Ax + Cx + BC1x + BC4x + BC10x + BC25x + BRx, Ay + Cy + BC1y + BC4y + BC10y + BC25y + BRy)
      cnv.create_line(Ax + Cx + BC1x + BC4x + BC10x + BC26x, Ay + Cy + BC1y + BC4y + BC10y + BC26y,Ax + Cx + BC1x + BC4x + BC10x + BC26x + BSx, Ay + Cy + BC1y + BC4y + BC10y + BC26y + BSy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (8)(1)------------------------------------------------
      cnv.create_line(Ax + Cx + BC1x + BC3x + BC7x + BC27x, Ay + Cy + BC1y + BC3y + BC7y + BC27y,Ax + Cx + BC1x + BC3x + BC7x + BC27x + BTx, Ay + Cy + BC1y + BC3y + BC7y + BC27y + BTy)
      cnv.create_line(Ax + Cx + BC1x + BC3x + BC7x + BC28x, Ay + Cy + BC1y + BC3y + BC7y + BC28y,Ax + Cx + BC1x + BC3x + BC7x + BC28x + BUx, Ay + Cy + BC1y + BC3y + BC7y + BC28y + BUy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (8)(2)------------------------------------------------
      cnv.create_line(Ax + Cx + BC1x + BC3x + BC8x + BC29x, Ay + Cy + BC1y + BC3y + BC8y + BC29y,Ax + Cx + BC1x + BC3x + BC8x + BC29x + BVx, Ay + Cy + BC1y + BC3y + BC8y + BC29y + BVy)
      cnv.create_line(Ax + Cx + BC1x + BC3x + BC8x + BC30x, Ay + Cy + BC1y + BC3y + BC8y + BC30y,Ax + Cx + BC1x + BC3x + BC8x + BC30x + BWx, Ay + Cy + BC1y + BC3y + BC8y + BC30y + BWy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (9)(1)------------------------------------------------
      cnv.create_line(Ax + CA2x + CA5x + CA11x + CA15x, Ay + CA2y + CA5y + CA11y + CA15y,Ax + CA2x + CA5x + CA11x + CA15x + BXx, Ay + CA2y + CA5y + CA11y + CA15y + BXy)
      cnv.create_line(Ax + CA2x + CA5x + CA11x + CA16x, Ay + CA2y + CA5y + CA11y + CA16y,Ax + CA2x + CA5x + CA11x + CA16x + BYx, Ay + CA2y + CA5y + CA11y + CA16y + BYy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (9)(2)------------------------------------------------
      cnv.create_line(Ax + CA2x + CA5x + CA12x + CA17x, Ay + CA2y + CA5y + CA12y + CA17y,Ax + CA2x + CA5x + CA12x + CA17x + BZx, Ay + CA2y + CA5y + CA12y + CA17y + BZy)
      cnv.create_line(Ax + CA2x + CA5x + CA12x + CA18x, Ay + CA2y + CA5y + CA12y + CA18y,Ax + CA2x + CA5x + CA12x + CA18x + CAx, Ay + CA2y + CA5y + CA12y + CA18y + CAy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (10)(1)------------------------------------------------
      cnv.create_line(Ax + CA2x + CA6x + CA14x + CA19x, Ay + CA2y + CA6y + CA14y + CA19y,Ax + CA2x + CA6x + CA14x + CA19x + CBx, Ay + CA2y + CA6y + CA14y + CA19y + CBy)
      cnv.create_line(Ax + CA2x + CA6x + CA14x + CA20x, Ay + CA2y + CA6y + CA14y + CA20y,Ax + CA2x + CA6x + CA14x + CA20x + CCx, Ay + CA2y + CA6y + CA14y + CA20y + CCy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (10)(2)------------------------------------------------
      cnv.create_line(Ax + CA2x + CA6x + CA13x + CA21x, Ay + CA2y + CA6y + CA13y + CA21y,Ax + CA2x + CA6x + CA13x + CA21x + CDx, Ay + CA2y + CA6y + CA13y + CA21y + CDy)
      cnv.create_line(Ax + CA2x + CA6x + CA13x + CA22x, Ay + CA2y + CA6y + CA13y + CA22y,Ax + CA2x + CA6x + CA13x + CA22x + CEx, Ay + CA2y + CA6y + CA13y + CA22y + CEy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (11)(1)------------------------------------------------
      cnv.create_line(Ax + CA1x + CA4x + CA9x + CA23x, Ay + CA1y + CA4y + CA9y + CA23y,Ax + CA1x + CA4x + CA9x + CA23x + CFx, Ay + CA1y + CA4y + CA9y + CA23y + CFy)
      cnv.create_line(Ax + CA1x + CA4x + CA9x + CA24x, Ay + CA1y + CA4y + CA9y + CA24y, Ax + CA1x + CA4x + CA9x + CA24x + CGx, Ay + CA1y + CA4y + CA9y + CA24y + CGy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (11)(2)------------------------------------------------
      cnv.create_line(Ax + CA1x + CA4x + CA10x + CA25x, Ay + CA1y + CA4y + CA10y + CA25y,Ax + CA1x + CA4x + CA10x + CA25x + CHx, Ay + CA1y + CA4y + CA10y + CA25y + CHy)
      cnv.create_line(Ax + CA1x + CA4x + CA10x + CA26x, Ay + CA1y + CA4y + CA10y + CA26y,Ax + CA1x + CA4x + CA10x + CA26x + CIx, Ay + CA1y + CA4y + CA10y + CA26y + CIy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (12)(1)------------------------------------------------
      cnv.create_line(Ax + CA1x + CA3x + CA8x + CA27x, Ay + CA1y + CA3y + CA8y + CA27y,Ax + CA1x + CA3x + CA8x + CA27x + CJx, Ay + CA1y + CA3y + CA8y + CA27y + CJy)
      cnv.create_line(Ax + CA1x + CA3x + CA8x + CA28x, Ay + CA1y + CA3y + CA8y + CA28y,Ax + CA1x + CA3x + CA8x + CA28x + CKx, Ay + CA1y + CA3y + CA8y + CA28y + CKy)

      # ----------------------------------------- PADA SEGI3 LVL 4 (12)(1)------------------------------------------------
      cnv.create_line(Ax + CA1x + CA3x + CA7x + CA29x, Ay + CA1y + CA3y + CA7y + CA29y,Ax + CA1x + CA3x + CA7x + CA29x + CLx, Ay + CA1y + CA3y + CA7y + CA29y + CLy)
      cnv.create_line(Ax + CA1x + CA3x + CA7x + CA30x, Ay + CA1y + CA3y + CA7y + CA30y,Ax + CA1x + CA3x + CA7x + CA30x  + CMx, Ay + CA1y + CA3y + CA7y + CA30y + CMy)
      segitiga(cnv, lvl, curlvl + 1, panjang, titikA)


lvl = int(input("Masukkan Level Segitiga (1-5) : "))

window = tk.Tk()

cnv = tk.Canvas(window, width=1000, height=700)
cnv.pack()

panjang = 500
xcenter = 500
ycenter = 350

Ax=500
Ay=50

segitiga(cnv, lvl, 1, panjang, (Ax, Ay) )

window.mainloop()
