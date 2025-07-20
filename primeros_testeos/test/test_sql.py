class TestSQLPytest:
    def test_crear_persona(self, fxt_db, fxt_cursor, fake_persona):
        fxt_cursor.execute(
            "INSERT INTO personas (nombre, apellido, dni) VALUES (?, ?, ?)",
            fake_persona
        )
        fxt_db.commit()

        persona = fxt_cursor.execute(
            "SELECT * FROM personas WHERE personas.dni = 1234"
        ).fetchone()
        assert  persona == fake_persona

        fxt_cursor.execute(
            "DELETE FROM personas WHERE personas.dni = 1234"
        )

        fxt_db.commit()
        persona = fxt_cursor.execute(
            "SELECT * FROM personas WHERE personas.dni = 1234"
        ).fetchone()
        assert persona is None


