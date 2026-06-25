# TicketFast — Sistema de Reserva de Boletos

**Maria Luisa Londoño Moncada**  
Pruebas de Software — Semestre V  
Corporación Universitaria Empresarial Alexander von Humboldt

---

## ¿Qué es este proyecto?

TicketFast es una plataforma de reserva de boletos para eventos masivos.
Este repositorio contiene las pruebas automatizadas del sistema, organizadas
en tres niveles: integración, sistema y E2E de frontend.

---

## Estructura del proyecto
---

## ¿Cómo correr las pruebas?

### 1. Levantar el entorno
```bash
docker compose -f docker-compose.test.yml up -d db-test
docker compose -f docker-compose.test.yml up -d api-test
```

### 2. Pruebas de integración
```bash
docker run --rm --network parcial3_red-test \
  -e DATABASE_URL="postgresql://test_user:test_pass@db-test:5432/test_db" \
  -e PYTHONPATH="/app" \
  parcial3-api-test python -m pytest tests/integration/ -v
```

### 3. Pruebas de sistema
```bash
docker run --rm --network parcial3_red-test \
  -e DATABASE_URL="postgresql://test_user:test_pass@db-test:5432/test_db" \
  -e API_BASE_URL="http://ticketfast-api-test:8001" \
  -e PYTHONPATH="/app" \
  parcial3-api-test python -m pytest tests/system/ -v
```

---

## Reglas de negocio

| Zona    | Precio por asiento |
|---------|--------------------|
| VIP     | $150.000 COP       |
| General | $50.000 COP        |

- Toda reserva debe tener mínimo 1 asiento.
- Solo se aceptan las zonas VIP y General.
- El total recaudado se calcula sumando todas las reservas activas del evento.