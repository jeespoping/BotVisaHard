from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from time import sleep
from datetime import datetime
import tkinter as tk
from tkinter import *

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.ventana()
        self.numvariables = None
        self.numvarestricciones = None
        self.tiempoResponse = None
        self.fecha1 = None
        self.fecha2 = None

    def userText(self,even):
        self.numvariables.delete(0, tk.END)
        self.numvariables.config(fg="#ecf0f1")
    def userText2(self,even):
        self.tiempoResponse.delete(0, tk.END)
        self.tiempoResponse.config(fg="#ecf0f1")
    def userText1(self, even):
        self.numvarestricciones.delete(0, tk.END)
        self.numvarestricciones.config(fg="#ecf0f1")
    def userText3(self, even):
        self.fecha1.delete(0, tk.END)
        self.fecha1.config(fg="#ecf0f1")
    def userText4(self, even):
        self.fecha2.delete(0, tk.END)
        self.fecha2.config(fg="#ecf0f1")

    def seleniumV(self):
        # Inicializa el navegador Firefox controlado por SeleniumWire
        driver = webdriver.Chrome()

        # Carga una página web
        driver.get("https://ais.usvisa-info.com/es-co/niv/users/sign_in")

        username_field = driver.find_element(by=By.ID, value='user_email')
        username_field.send_keys("claudiabecerra829@gmail.com")

        password_field = driver.find_element(by=By.ID, value='user_password')
        password_field.send_keys("colombia2024")

        checkbox = driver.find_element(by=By.CSS_SELECTOR, value=".icheckbox.icheck-item")

        checkbox.click()

        password_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-info-footer")))

        button = driver.find_element(by=By.CSS_SELECTOR, value=".button.primary.small")
        button.click()

        item1 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".accordion-item"))
        )

        # Hacer clic en el enlace
        item1.click()

        enlace = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.small.primary.small-only-expanded"))
        )

        enlace.click()

        driver.implicitly_wait(10)
        refresh = True
        fecha_hoy = datetime.now().date()
        fecha2 = datetime.strptime('2024-04-23', '%Y-%m-%d').date()
        fecha = datetime.strptime('2024-12-31', '%Y-%m-%d').date()

        while refresh:
            try:
                input_element = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.ID, "appointments_consulate_appointment_date_input")))
                input_element.click()
                body = driver.find_element(by=By.TAG_NAME, value="body")
                actions = ActionChains(driver)
                actions.move_to_element(body).click().perform()
                refresh = False
                break
            except:
                driver.refresh()
        noDate = True
        sleep(2)
        while noDate:
            for request in driver.requests:
                if "/appointment/days/25.json?appointments[expedite]=false" in request.url and request.response and request.response.status_code == 200:
                    print("URL:", request.response)
                    print("Fecha:", request.response.date)
                    print(request.response.body)
                    bytes_representation = request.response.body
                    lista_diccionarios = json.loads(bytes_representation.decode('utf-8'))
                    fechas = [elemento["date"] for elemento in lista_diccionarios]
                    print("Fechas encontradas:", fechas)
                    fecha_encontrada = datetime.strptime(fechas[0], '%Y-%m-%d').date()
                    if fecha_encontrada <= fecha and fecha_encontrada >= fecha2:
                        input_element.click()
                        diferencia_meses = (
                                                   fecha_encontrada.year - fecha_hoy.year) * 12 + fecha_encontrada.month - fecha_hoy.month
                        for i in range(diferencia_meses):
                            next = driver.find_element(by=By.CSS_SELECTOR, value=".ui-icon.ui-icon-circle-triangle-e")
                            next.click()
                        driver.find_element(by=By.CSS_SELECTOR, value="[data-handler='selectDay']").click()
                        refresh2 = True
                        while refresh2:
                            try:
                                selectHour = driver.find_element(by=By.ID,
                                                                 value='appointments_consulate_appointment_time')
                                selectHour.click()
                                Hour = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                                       "/html/body/div[4]/main/div[4]/div/div/form/fieldset[1]/ol/fieldset/div/div[1]/div[3]/li[2]/select/option[2]")))
                                Hour.click()
                                refresh2 = False
                            except:
                                input_element.click()
                                driver.find_element(by=By.CSS_SELECTOR, value="[data-handler='selectDay']").click()
                        refresh1 = True
                        while refresh1:
                            try:
                                input_element = WebDriverWait(driver, 30).until(
                                    EC.presence_of_element_located((By.ID, "appointments_asc_appointment_date")))
                                input_element.click()
                                for i in range(diferencia_meses):
                                    next = driver.find_element(by=By.CSS_SELECTOR,
                                                               value=".ui-icon.ui-icon-circle-triangle-e")
                                    next.click()
                                driver.find_element(by=By.CSS_SELECTOR, value="[data-handler='selectDay']").click()

                                refresh3 = True
                                while refresh3:
                                    try:
                                        selectHour = driver.find_element(by=By.ID,
                                                                         value='appointments_asc_appointment_time')
                                        selectHour.click()
                                        Hour = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                                               "/html/body/div[4]/main/div[4]/div/div/form/fieldset[2]/ol/fieldset/div/div/div[1]/div/div[3]/li/select/option[2]")))
                                        Hour.click()
                                        refresh1 = False
                                        refresh3 = False
                                    except:
                                        input_element.click()
                                        driver.find_element(by=By.CSS_SELECTOR,
                                                            value="[data-handler='selectDay']").click()
                                break
                            except:
                                driver.find_element(by=By.ID, value='appointments_asc_appointment_facility_id').click()
                                driver.find_element(by=By.XPATH,
                                                    value='//*[@id="appointments_asc_appointment_facility_id"]/option[1]').click()
                                driver.find_element(by=By.ID, value='appointments_asc_appointment_facility_id').click()
                                driver.find_element(by=By.XPATH,
                                                    value='//*[@id="appointments_asc_appointment_facility_id"]/option[2]').click()
                        noDate = False
                        sleep(20)
                    else:
                        del driver.requests
                        refresh = True
                        while refresh:
                            try:
                                ocultar = driver.find_element(by=By.ID, value="consulate_date_time")
                                driver.execute_script("arguments[0].style.display = 'none';", ocultar)
                                print("ocultando")
                                sleep(10)
                                driver.find_element(by=By.ID,
                                                    value="appointments_consulate_appointment_facility_id").click()
                                driver.find_element(by=By.XPATH,
                                                    value="/html/body/div[4]/main/div[4]/div/div/form/fieldset[1]/ol/fieldset/div/div[1]/div[1]/div/li/select/option[1]").click()
                                driver.find_element(by=By.ID,
                                                    value="appointments_consulate_appointment_facility_id").click()
                                driver.find_element(by=By.XPATH,
                                                    value="/html/body/div[4]/main/div[4]/div/div/form/fieldset[1]/ol/fieldset/div/div[1]/div[1]/div/li/select/option[2]").click()
                                input_element = WebDriverWait(driver, 50).until(
                                    EC.presence_of_element_located(
                                        (By.ID, "appointments_consulate_appointment_date_input")))
                                input_element.click()
                                body = driver.find_element(by=By.TAG_NAME, value="body")
                                actions = ActionChains(driver)
                                actions.move_to_element(body).click().perform()
                                refresh = False
                                sleep(10)
                                print("Fin")
                            except:
                                driver.refresh()
                    break

        # Cierra el navegador
        driver.quit()

    def ventana(self):
        self.window.title("Buscador de citas")
        self.window.resizable(0, 0)
        self.window.iconbitmap("logo.ico")
        inicio = tk.Frame()  # el frame
        inicio.pack(fill="both", expand="true")  # adaptarse
        inicio.config(bg="#34495e", width="1000", height="768")

        tk.Label(inicio, text="Ingrese el correo: ", fg="#ecf0f1", bg="#34495e", font=("Comic Sans MS", 18)).place( x=10, y=10)
        self.numvariables = tk.Entry(inicio, bg="#34495e", font=("Comic Sans MS", 18), fg="#bdc3c7", justify=tk.CENTER,width=30, borderwidth=5)
        self.numvariables.place(x=270, y=10)
        self.numvariables.insert(0, "Digite")
        self.numvariables.bind("<Button>", self.userText)

        tk.Label(inicio, text="Ingrese la clave:", fg="#ecf0f1", bg="#34495e",
                 font=("Comic Sans MS", 18)).place(x=10, y=80)
        self.numvarestricciones = tk.Entry(inicio, bg="#34495e", font=("Comic Sans MS", 18), fg="#bdc3c7",
                                           justify=tk.CENTER, width=30, borderwidth=5)
        self.numvarestricciones.place(x=320, y=80)
        self.numvarestricciones.insert(0, "Digite")
        self.numvarestricciones.bind("<Button>", self.userText1)

        tk.Label(inicio, text="Ingrese Tiempo response", fg="#ecf0f1", bg="#34495e",
                 font=("Comic Sans MS", 18)).place(x=10, y=160)
        self.tiempoResponse = tk.Entry(inicio, bg="#34495e", font=("Comic Sans MS", 18), fg="#bdc3c7",
                                           justify=tk.CENTER, width=30, borderwidth=5)
        self.tiempoResponse.place(x=320, y=160)
        self.tiempoResponse.insert(0, "Digite")
        self.tiempoResponse.bind("<Button>", self.userText2)

        tk.Label(inicio, text="Ingrese la fecha incial", fg="#ecf0f1", bg="#34495e",
                 font=("Comic Sans MS", 18)).place(x=10, y=320)
        self.fecha1 = tk.Entry(inicio, bg="#34495e", font=("Comic Sans MS", 18), fg="#bdc3c7",
                                       justify=tk.CENTER, width=30, borderwidth=5)
        self.fecha1.place(x=320, y=240)
        self.fecha1.insert(0, "YYYY-MM-DD")
        self.fecha1.bind("<Button>", self.userText3)

        tk.Label(inicio, text="Ingrese la fecha incial", fg="#ecf0f1", bg="#34495e",
                 font=("Comic Sans MS", 18)).place(x=10, y=240)
        self.fecha2 = tk.Entry(inicio, bg="#34495e", font=("Comic Sans MS", 18), fg="#bdc3c7",
                               justify=tk.CENTER, width=30, borderwidth=5)
        self.fecha2.place(x=320, y=320)
        self.fecha2.insert(0, "YYYY-MM-DD")
        self.fecha2.bind("<Button>", self.userText4)

        tk.Button(inicio, text="Continuar", fg="#34495e", bg="#95a5a6", font=("Comic Sans MS", 19), cursor="hand2",
                  command=self.validar).place(x=350, y=450)

        self.window.mainloop()

    def validar(self):
        correo = self.numvariables.get()
        password = self.numvarestricciones.get()
        respons = self.tiempoResponse.get()
        fecha1 = self.fecha1.get()
        fecha2 = self.fecha2.get()
        print(correo, password, respons, fecha1, fecha2)
        self.window.destroy()
        Ejecutable(correo, password, respons, fecha1, fecha2)

class Ejecutable:
    def __init__(self,correo,password, respons, fecha1, fecha2):
        self.correo = correo
        self.password = password
        self.respons = respons
        self.fecha1 = fecha1
        self.fecha2 = fecha2
        self.window = Tk()
        self.ventana()
        self.inicio = None

    def ventana(self):

        self.seleniumV()


    def seleniumV(self):
        # Inicializa el navegador Firefox controlado por SeleniumWire
        driver = webdriver.Chrome()

        # Carga una página web
        driver.get("https://ais.usvisa-info.com/es-co/niv/users/sign_in")

        username_field = driver.find_element(by=By.ID, value='user_email')
        username_field.send_keys(self.correo)

        password_field = driver.find_element(by=By.ID, value='user_password')
        password_field.send_keys(self.password)

        checkbox = driver.find_element(by=By.CSS_SELECTOR, value=".icheckbox.icheck-item")

        checkbox.click()

        password_field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-info-footer")))

        button = driver.find_element(by=By.CSS_SELECTOR, value=".button.primary.small")
        button.click()

        item1 = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".accordion-item"))
        )

        # Hacer clic en el enlace
        item1.click()

        enlace = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.small.primary.small-only-expanded"))
        )

        enlace.click()

        driver.implicitly_wait(10)
        refresh = True
        fecha_hoy = datetime.now().date()
        fecha2 = datetime.strptime(self.fecha1, '%Y-%m-%d').date()
        fecha = datetime.strptime(self.fecha2, '%Y-%m-%d').date()

        while refresh:
            try:
                input_element = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.ID, "appointments_consulate_appointment_date_input")))
                input_element.click()
                body = driver.find_element(by=By.TAG_NAME, value="body")
                actions = ActionChains(driver)
                actions.move_to_element(body).click().perform()
                refresh = False
                break
            except:
                driver.refresh()
        noDate = True
        sleep(2)
        while noDate:
            for request in driver.requests:
                if "/appointment/days/25.json?appointments[expedite]=false" in request.url and request.response and request.response.status_code == 200:
                    print("URL:", request.response)
                    print("Fecha:", request.response.date)
                    print(request.response.body)
                    bytes_representation = request.response.body
                    lista_diccionarios = json.loads(bytes_representation.decode('utf-8'))
                    fechas = [elemento["date"] for elemento in lista_diccionarios]
                    print("Fechas encontradas:", fechas)
                    fecha_encontrada = datetime.strptime(fechas[0], '%Y-%m-%d').date()
                    if fecha_encontrada <= fecha and fecha_encontrada >= fecha2:
                        input_element.click()
                        diferencia_meses = (
                                                   fecha_encontrada.year - fecha_hoy.year) * 12 + fecha_encontrada.month - fecha_hoy.month
                        for i in range(diferencia_meses):
                            next = driver.find_element(by=By.CSS_SELECTOR, value=".ui-icon.ui-icon-circle-triangle-e")
                            next.click()
                        driver.find_element(by=By.CSS_SELECTOR, value="[data-handler='selectDay']").click()
                        refresh2 = True
                        while refresh2:
                            try:
                                selectHour = driver.find_element(by=By.ID,
                                                                 value='appointments_consulate_appointment_time')
                                selectHour.click()
                                Hour = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                                       "/html/body/div[4]/main/div[4]/div/div/form/fieldset[1]/ol/fieldset/div/div[1]/div[3]/li[2]/select/option[2]")))
                                Hour.click()
                                refresh2 = False
                            except:
                                input_element.click()
                                driver.find_element(by=By.CSS_SELECTOR, value="[data-handler='selectDay']").click()
                        refresh1 = True
                        while refresh1:
                            try:
                                input_element = WebDriverWait(driver, 30).until(
                                    EC.presence_of_element_located((By.ID, "appointments_asc_appointment_date")))
                                input_element.click()
                                for i in range(diferencia_meses):
                                    next = driver.find_element(by=By.CSS_SELECTOR,
                                                               value=".ui-icon.ui-icon-circle-triangle-e")
                                    next.click()
                                driver.find_element(by=By.CSS_SELECTOR, value="[data-handler='selectDay']").click()

                                refresh3 = True
                                while refresh3:
                                    try:
                                        selectHour = driver.find_element(by=By.ID,
                                                                         value='appointments_asc_appointment_time')
                                        selectHour.click()
                                        Hour = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                                                               "/html/body/div[4]/main/div[4]/div/div/form/fieldset[2]/ol/fieldset/div/div/div[1]/div/div[3]/li/select/option[2]")))
                                        Hour.click()
                                        refresh1 = False
                                        refresh3 = False
                                    except:
                                        input_element.click()
                                        driver.find_element(by=By.CSS_SELECTOR,
                                                            value="[data-handler='selectDay']").click()
                                break
                            except:
                                driver.find_element(by=By.ID, value='appointments_asc_appointment_facility_id').click()
                                driver.find_element(by=By.XPATH,
                                                    value='//*[@id="appointments_asc_appointment_facility_id"]/option[1]').click()
                                driver.find_element(by=By.ID, value='appointments_asc_appointment_facility_id').click()
                                driver.find_element(by=By.XPATH,
                                                    value='//*[@id="appointments_asc_appointment_facility_id"]/option[2]').click()
                        noDate = False
                        sleep(20)
                    else:
                        del driver.requests
                        refresh = True
                        while refresh:
                            try:
                                ocultar = driver.find_element(by=By.ID, value="consulate_date_time")
                                driver.execute_script("arguments[0].style.display = 'none';", ocultar)
                                print("ocultando")
                                sleep(int(self.respons) / 2)
                                driver.find_element(by=By.ID,
                                                    value="appointments_consulate_appointment_facility_id").click()
                                driver.find_element(by=By.XPATH,
                                                    value="/html/body/div[4]/main/div[4]/div/div/form/fieldset[1]/ol/fieldset/div/div[1]/div[1]/div/li/select/option[1]").click()
                                driver.find_element(by=By.ID,
                                                    value="appointments_consulate_appointment_facility_id").click()
                                driver.find_element(by=By.XPATH,
                                                    value="/html/body/div[4]/main/div[4]/div/div/form/fieldset[1]/ol/fieldset/div/div[1]/div[1]/div/li/select/option[2]").click()
                                sleep(int(self.respons) / 2)
                                input_element = WebDriverWait(driver, 50).until(
                                    EC.presence_of_element_located(
                                        (By.ID, "appointments_consulate_appointment_date_input")))
                                input_element.click()
                                body = driver.find_element(by=By.TAG_NAME, value="body")
                                actions = ActionChains(driver)
                                actions.move_to_element(body).click().perform()
                                refresh = False
                                sleep(int(self.respons))
                                print("Fin")
                            except:
                                driver.refresh()
                    break

        # Cierra el navegador
        driver.quit()

if __name__ == '__main__':
    aplicacion = Main()