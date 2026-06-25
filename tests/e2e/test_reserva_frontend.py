from playwright.sync_api import Page, expect

FRONTEND_URL = "http://localhost:4200"


def test_reserva_vip_muestra_total_correcto(page: Page):
    # PASO 1: navegar a la página de reservas
    page.goto(f"{FRONTEND_URL}/reservas")
    page.wait_for_load_state("networkidle")

    # PASO 2: llenar el formulario
    page.get_by_test_id("input-email-cliente").fill("cliente@correo.com")
    page.get_by_test_id("select-zona-evento").fill("VIP")
    page.get_by_test_id("input-cantidad-asientos").fill("1")

    # PASO 3: hacer clic en confirmar
    page.get_by_test_id("btn-confirmar-reserva").click()

    # PASO 4: verificar que el total muestra 150.000
    # expect() espera dinámicamente sin usar sleep
    expect(page.get_by_test_id("seccion-resumen-total")).to_contain_text("150.000")