from src.database.models import ReservaDB


def test_crear_reserva_retorna_201_y_persiste_en_bd(client_con_bd, db_session):
    # ACT: petición POST al endpoint
    response = client_con_bd.post(
        "/reservas/concierto-2026",
        json={
            "cliente_email": "test@correo.com",
            "zona": "VIP",
            "cantidad": 2,
        },
    )

    # ASSERT 1: código de estado HTTP 201
    assert response.status_code == 201

    # ASSERT 2: el registro existe en la BD con el email correcto
    reserva = db_session.query(ReservaDB).filter(
        ReservaDB.evento_id == "concierto-2026"
    ).first()

    assert reserva is not None
    assert reserva.cliente_email == "test@correo.com"