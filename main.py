import sqlite3


conn = sqlite3.connect("app.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS pupil(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        address VARCHAR(255) NOT NULL
)
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS school(
        id INTEGER PRIMARY KEY,
        address VARCHAR(255) NOT NULL
);
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS class(
        id INTEGER PRIMARY KEY,
        school_id INTEGER FOREIGN_KEY REFERENCES school(id),
        room_address INTEGER NOT NULL
);
""")

#
cursor.execute("""
    ALTER TABLE pupil
    ADD class_id FOREIGN_KEY REFERENCES class(id)
""")


cursor.execute("""
    ALTER TABLE pupil
    ADD school_id FOREIGN_KEY REFERENCES school(id)
""")


cursor.execute("""
    INSERT INTO school (address) VALUES
    ('Києвська область, Фастівський район'),
    ('Києвська область, Вишгородський район'),
    ('Києвська область, Бориспільський район');
""")


cursor.execute("""
    INSERT INTO class (school_id, room_address) VALUES
    (1, 245),
    (1, 123),
    (2, 145),
    (3, 145);
""")


cursor.execute("""
    INSERT INTO pupil (first_name, last_name, address, class_id, school_id) VALUES
        ('Максим', 'Максимвоич', 'Києвська область, Бориспільський район', 1, 3),
        ('Олег', 'Олегович', 'Києвська область, Вишгородський район', 2, 2),
        ('Наталія', 'Наталіївна', 'Києвська область, Фастівський район', 3, 1);
""")

conn.commit()
