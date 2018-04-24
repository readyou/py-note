# -*- coding: utf-8 -*-

from py_note import create_app

app = create_app()
app.run(debug=True, port=5555)
