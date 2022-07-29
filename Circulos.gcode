; Inicializacion
G28
G0 F5000 Z10
M106 S255   ; Enciende Succion
G4 S5
M107        ; Apaga Succion

G0 X0 Y0
G0 F5000 Z0
G4 P1500
G0 F5000 Z10

G0 X0 Y200
G0 F5000 Z0
G4 P1500
G0 F5000 Z10

G0 X200 Y200
G0 F5000 Z0
G4 P1500
G0 F5000 Z10

G0 X200 Y0
G0 F5000 Z0
G4 P1500
G0 F5000 Z10

G0 X0 Y0
; fin inicializacion
; ----------------------------------------------------------------- 
; inicia toma de pieza
G0 F500 Z10
G0 F500 X200 Y200
M106 S255
G0 F500 Z0
G4 P1500
G0 F500 Z0
;finaliza toma de pieza

G0 F1000 X101.5 Y101.5

;inicia aplicacion de pieza
G0 F500 Z0
M106 S0
G4 P1500
G0 F500 Z10
;finaliza aplicacion de pieza

; ----------------------------------------------------------------- 
; inicia toma de pieza
G0 F500 Z10
G0 F500 X200 Y200
M106 S255
G0 F500 Z0
G4 P1500
G0 F500 Z0
;finaliza toma de pieza

G0 F1000 X151.5 Y101.5

;inicia aplicacion de pieza
G0 F500 Z0
M106 S0
G4 P1500
G0 F500 Z10
;finaliza aplicacion de pieza

; ----------------------------------------------------------------- 
; inicia toma de pieza
G0 F500 Z10
G0 F500 X200 Y200
M106 S255
G0 F500 Z0
G4 P1500
G0 F500 Z0
;finaliza toma de pieza

G0 F1000 X101.5 Y151.5

;inicia aplicacion de pieza
G0 F500 Z0
M106 S0
G4 P1500
G0 F500 Z10
;finaliza aplicacion de pieza

; ----------------------------------------------------------------- 
; inicia toma de pieza
G0 F500 Z10
G0 F500 X200 Y200
M106 S255
G0 F500 Z0
G4 P1500
G0 F500 Z0
;finaliza toma de pieza

G0 F1000 X51.5 Y101.5

;inicia aplicacion de pieza
G0 F500 Z0
M106 S0
G4 P1500
G0 F500 Z10
;finaliza aplicacion de pieza

; ----------------------------------------------------------------- 
; inicia toma de pieza
G0 F500 Z10
G0 F500 X200 Y200
M106 S255
G0 F500 Z0
G4 P1500
G0 F500 Z0
;finaliza toma de pieza

G0 F1000 X101.5 Y51.5

;inicia aplicacion de pieza
G0 F500 Z0
M106 S0
G4 P1500
G0 F500 Z10
;finaliza aplicacion de pieza

; ----------------------------------------------------------------- 
; inicia toma de pieza
G0 F500 Z10
G0 F500 X200 Y200
M106 S255
G0 F500 Z0
G4 P1500
G0 F500 Z0
;finaliza toma de pieza

G0 F1000 X105.00001 Y210

;inicia aplicacion de pieza
G0 F500 Z0
M106 S0
G4 P1500
G0 F500 Z10
;finaliza aplicacion de pieza

;Finalizacion
G0 F5000 Z10
G0 X0 Y0
M104 S0
