# tests/test_lavadero_unittest.py

import unittest
# Importamos la clase Lavadero desde el módulo padre
from lavadero import Lavadero

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    def test_reseteo_estado_con_terminar(self):
        """Test 4: Verifica que terminar() resetea todas las flags y el estado."""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero._cobrar()
        self.lavadero.terminar()
        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
        
    # ----------------------------------------------------------------------
    # TESTS  
    # ----------------------------------------------------------------------
        
    def test1_estado_inicial_correcto(self):
        """Test 1: Verifica que el estado inicial es Inactivo y con 0 ingresos."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)

   
    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Comprueba que encerar sin secado a mano lanza ValueError."""
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)

    # ----------------------------------------------------------------------
    # Test 3:Cuando se intenta hacer un lavado mientras que otro ya está en marcha, se produce una ValueError.
    def test3_excepcion_lavado_mientras_ocupado(self):
        # Inicia el primer lavado
        self.lavadero.hacerLavado(True, False, False)
        # Comprueba si lanza el error mientras el lavado está en curso  
        with self.assertRaises(ValueError):
             # Intenta iniciar otro lavado mientras el primero está en curso
            self.lavadero.hacerLavado(False, True, False) 

    # ----------------------------------------------------------------------
    # Test 4: Si seleccionamos un lavado con prelavado a mano, los ingresos de lavadero son 6,50€.
    def test4_ingresos_con_prelavado_mano(self):
        self.lavadero.hacerLavado(True, False, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.50)
    
    # ----------------------------------------------------------------------
    # Test 5: Si seleccionamos un lavado con secado a mano, los ingresos son 6,00€.
    def test5_ingresos_con_secado_mano(self):
        self.lavadero.hacerLavado(False, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 6.00)
    
    # ----------------------------------------------------------------------
    # Test 6: Si seleccionamos un lavado con secado a mano y encerado, los ingresos son 7,20€.
    def test6_ingresos_con_secado_mano_y_encerado(self):
        self.lavadero.hacerLavado(False, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.20)
    
    # ----------------------------------------------------------------------
    # Test 7: Si seleccionamos un lavado con prelavado a mano y secado a mano, los ingresos son 7,50€.
    def test7_ingresos_con_prelavado_mano_y_secado_mano(self):
        self.lavadero.hacerLavado(True, True, False)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 7.50)
    
    # ----------------------------------------------------------------------
    # Test 8: Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado, los ingresos son 8,70€.
    def test8_ingresos_con_prelavado_mano_secado_mano_y_encerado(self):
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero._cobrar()
        self.assertEqual(self.lavadero.ingresos, 8.70)

    # ----------------------------------------------------------------------
    # Tests de flujo de fases
    # Utilizamos la función def ejecutar_y_obtener_fases(self, prelavado, secado, encerado)
    # Estos tests dan errores ya que en el código original hay errores en las las fases esperados, en los saltos.
    # ----------------------------------------------------------------------
    def test9_flujo_rapido_sin_extras(self):
        """Test 9: Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas, 
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
        
    # ----------------------------------------------------------------------
    # Test 10: Si seleccionamos un lavado con prelavado a mano y vamos avanzando fases, 
    # el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 6, 0.
    def test10_flujo_con_prelavado_mano(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=False, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas, 
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
      
    # ----------------------------------------------------------------------
    # Test 11: Si seleccionamos un lavado con secado a mano y vamos avanzando fases, 
    # el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 0.
    def test11_flujo_con_secado_mano(self):
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas, 
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
    
    # ----------------------------------------------------------------------
    # Test 12: Si seleccionamos un lavado con secado a mano y encerado y vamos avanzando fases, 
    # el lavadero pasa por las fases 0, 1, 3, 4, 5, 7, 8, 0.
    def test12_flujo_con_secado_mano_y_encerado(self):
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=True)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas, 
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
    
    # ----------------------------------------------------------------------
    # Test 13: Si seleccionamos un lavado con prelavado a mano y secado a mano y vamos avanzando fases, 
    # el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 0.
    def test13_flujo_con_prelavado_mano_y_secado_mano(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=False)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas, 
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
 
   # ----------------------------------------------------------------------
   # Test 14: Si seleccionamos un lavado con prelavado a mano, secado a mano y encerado y vamos avanzando fases, 
   # el lavadero pasa por las fases 0, 1, 2, 3, 4, 5, 7, 8, 0.
    def test14_flujo_con_prelavado_mano_secado_mano_y_encerado(self):
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        # Ejecutar el ciclo completo y obtener las fases
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=True)
        
        # Verificar que las fases obtenidas coinciden con las esperadas
        self.assertEqual(fases_obtenidas, fases_esperadas, 
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
 
# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()