from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "question" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "result" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "answer" TEXT NOT NULL,
    "score" DOUBLE PRECISION NOT NULL,
    "question_id" INT NOT NULL REFERENCES "question" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmG1v2jAQgP8K4tMmdVPL2rXat0Dpxspgo3SqVFWRSUyw6jipbUZRxX+f7STY5G2gwk"
    "RUPgH3Yt898vnOvNT9wIWYffw1hYyjgNS/1F7qBPhQfMnojmp1EIZaIwUcjLAyfjKtRoxT"
    "4HAhHwPMoBC5kDkUhfEeZIqxFAaOMETE06IpQWIlmwce5BNIheL+QYgRceEzZMnP8NEeI4"
    "jdlXCRK/dWcpvPQyXrEH6lDOVuI9sJ8NQn2jic80lAltaIcCn1IIEUcCiX53Qqw5fRxZkm"
    "GUWRapMoRMPHhWMwxdxId00GTkAkPxENUwl6cpcPjZPT89OLT59PL4SJimQpOV9E6encI0"
    "dFoDesL5QecBBZKIyaG0dcLJdB15oAms9u6ZDCJ4JO40tglfFLBBqgPjRbIuiDZxtD4vGJ"
    "xHZ2VsLrtzVofbMG74TVe5lNIA5ydMJ7saoR6SRUDdGMLINyCJ8LjmHKrSpAS/gN23dDGb"
    "TP2BM2sb37Yd0pov481nT7va+JuYG51e03U3SnDFJ7o/o2PP5d5PsBdRt1Li/H8WNumUsi"
    "WYBXAYXII9dwrjh2RESAOHnVHXeD23iZ/eO3SM5AItVXMQWzZcMwj4ZITyQFeXThWTct67"
    "JdVxBHwHmcAeraBTQpZCJmlgXajB2vrgcQg4LCjlkO1CLVoqnoBI3AoLLCK6vyG35aAgjw"
    "VNRyb7nTKpCcIUSjKh5BqLY5DCB7djGVDSCAsFne3VTcNrXHoWPmd0zmiIs957rHAShguv"
    "RIIR1Ll8pBvezfNrvt2s9Bu9W56fR7KxgjpRQJAYpu/0Hb6qYYJk+azSaPlNdh+sg8D185"
    "gZjv0f3juO4Ukjomm04iu+zCasTL6cHJ6FfcgZMZ89B/9600y/qv+syQK37/J/ZV6b3/4f"
    "kPfYDwJgyXDtuBuPMjuHuEIWBsFtCcGi6maPq88dOY6b3rvGKTJvTKd2w1O/JOX7IWpMiZ"
    "5HXRWFPaR4G2OXTSCnXSP5Cy3CG3+AozXN74DWY2A1kaG0CMzasJ8OT4eA2AwqoQoNKtAh"
    "Q7chjV4CrE7zf9Xj5EwyUF8paIBO9d5PCjGkaMP+wn1hKKMuvy/1jSf6dICgHjHlWrqAWa"
    "m7XZ7beXxV+cEYgW"
)
