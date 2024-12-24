import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BarberiaAluraTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Edge()
    cls.driver.maximize_window()
    cls.base_url = "http://192.168.5.91:5500/index.html"
    if not os.path.exists("capturas"):
      os.makedirs("capturas")
  
  def setUp(self):
    self.driver.get(self.base_url)

  def take_screenshot(self, test_name):
    screenshot_path = f"capturas/{test_name}.png"
    self.driver.save_screenshot(screenshot_path)
    print(f"Captura guardada: {screenshot_path}")

  def test_01_navegacion_paginas(self): 
    """Navegar por los enlaces en la página"""
    ruta_archivo = os.path.abspath("C:\\Users\\francisco javier\\OneDrive\\Escritorio\\barberia_Alura\\index.html")
    url = f"file://{ruta_archivo}"
    self.driver.get(url)

    WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )
    enlaces = self.driver.find_elements(By.TAG_NAME, "a")

    for i, enlace in enumerate(enlaces):
        enlace_actualizado = enlaces[i]  
        self.driver.execute_script("arguments[0].click();", enlace_actualizado)
        self.take_screenshot(f"pagina_{i}")
        self.driver.back()  
        enlaces = self.driver.find_elements(By.TAG_NAME, "a")  

  
  def test_02_mapa_interactivo(self):
    """Verificar el mapa interactivo"""
    mapa = self.driver.find_element(By.XPATH, "//iframe[contains(@src, 'google.com/maps')]")
    self.assertTrue(mapa.is_displayed())
    self.take_screenshot("mapa_interactivo")
    
  def test_03_video_youtube(self):
    """El video de YouTube es ve en la pagina"""
    self.driver.get("C:\\Users\\francisco javier\\OneDrive\\Escritorio\\barberia_Alura\\index.html")

    video = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'youtube.com')]"))
    )
    assert video.is_displayed(), "El video no está visible"
  
  def test_04_servicios(self):
    """Verificar que los servicios estén presentes en la página"""
    ruta_archivo = os.path.abspath("C:\\Users\\francisco javier\\OneDrive\\Escritorio\\barberia_Alura\\servicio.html")
    url = f"file://{ruta_archivo}"
    self.driver.get(url)

    try:
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "producto-descripcion"))
        )
        servicios = self.driver.find_elements(By.CLASS_NAME, "producto-descripcion")
        precios = self.driver.find_elements(By.CLASS_NAME, "producto-precio")
        imagenes = self.driver.find_elements(By.CLASS_NAME, "img")

        self.assertGreater(len(servicios), 0, "No se encontraron descripciones de servicio.")
        self.assertGreater(len(precios), 0, "No se encontraron precios de servicio.")
        self.assertGreater(len(imagenes), 0, "No se encontraron imágenes de servicio.")

    except Exception as e:
        self.take_screenshot('error_servicios')
        self.fail(f"Error al verificar los servicios: {str(e)}")

  def test_05_formulario(self):
    """Validar el formulario de contacto"""
    ruta_archivo = os.path.abspath("C:\\Users\\francisco javier\\OneDrive\\Escritorio\\barberia_Alura\\contacto.html")
    url = f"file://{ruta_archivo}"
    self.driver.get(url)
    
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "nombreapellido"))
    ).send_keys("Prueba Nombre")
    self.driver.find_element(By.NAME, "correo").send_keys("prueba@correo.com")
    self.driver.find_element(By.NAME, "telefono").send_keys("123456789")
    self.driver.find_element(By.NAME, "mensaje").send_keys("Mensaje de prueba")  
    self.driver.find_element(By.ID, "submit").click()
    self.take_screenshot("formulario_completado")

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

if __name__ == "__main__":
    unittest.main()