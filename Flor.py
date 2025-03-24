import turtle
import colorsys as cs
from typing import Tuple

class DibujantePatron:
    def __init__(self):
        self.setup_pantalla()
        self.tortuga = turtle.Turtle()
        self.configurar_tortuga()
    
    def setup_pantalla(self) -> None:
        """Configura la pantalla de dibujo."""
        pantalla = turtle.Screen()
        pantalla.setup(width=800, height=800)
        pantalla.bgcolor("BLACK")
        pantalla.title("Patrón Espiral de Colores")
    
    def configurar_tortuga(self) -> None:
        """Configura la tortuga para dibujar."""
        self.tortuga.speed(0)                  # Velocidad máxima
        self.tortuga.width(2)                  # Grosor de línea
        self.tortuga.hideturtle()             # Ocultar la tortuga
    
    def obtener_color(self, i: int, j: int) -> Tuple[float, float, float]:
        """Genera un color basado en HSV."""
        return cs.hsv_to_rgb(i/15, j/25, 1)
    
    def dibujar_segmento(self, radio: float, angulo: float) -> None:
        """Dibuja un segmento del patrón."""
        self.tortuga.circle(radio, angulo)
    
    def dibujar_patron(self) -> None:
        """Dibuja el patrón completo."""
        radio_inicial = 200
        
        for j in range(25):  # Número de filas
            color_actual = self.obtener_color(j, j)
            self.tortuga.pencolor(color_actual)
            
            for i in range(15):  # Número de columnas
                self.tortuga.right(90)
                
                # Dibujar primer cuarto círculo
                self.dibujar_segmento(radio_inicial - j*4, 90)
                
                # Dibujar segundo cuarto círculo
                self.tortuga.left(90)
                self.dibujar_segmento(radio_inicial - j*4, 90)
                
                # Dibujar arco interior
                self.tortuga.right(180)
                self.dibujar_segmento(50, 25)
        
        turtle.done()

# Crear y ejecutar el programa
if __name__ == "__main__":
    dibujante = DibujantePatron()
    dibujante.dibujar_patron()
