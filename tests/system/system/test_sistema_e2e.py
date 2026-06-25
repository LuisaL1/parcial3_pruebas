import httpx
import os

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8001")


def test_flujo_reserva_y_total_recaudado():
    with httpx.Client(base_url=API_BASE_URL, timeout=30.0) as client:

        # PASO 1: crear reserva zona General, cantidad 3
        # Regla de negocio: General = 50.000 × 3 = 150.000
        response_post = client.post(
            "/reservas/sistema-evento-xyz",
            json={
                "cliente_email": "sistema@correo.com",
                "zona": "General",
                "cantidad": 3,
            },
        )
        assert response_post.status_code == 201

        # PASO 2: consultar resumen del evento
        response_get = client.get("/reservas/sistema-evento-xyz/resumen")
        assert response_get.status_code == 200

        # PASO 3: validar total recaudado según regla de negocio
        # General: 50.000 × 3 = 150.000
        data = response_get.json()
        assert data["total_recaudado"] == 150_000