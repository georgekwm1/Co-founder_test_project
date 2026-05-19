from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "reset_token" VARCHAR(255);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "reset_token";"""


MODELS_STATE = (
    "eJztmG1v2jAQgP8K4lMndVPL2rXat0Dpxspgo3SqVFWRSUywSJzUNgNU8d9nOwk2eRusMB"
    "Epn0rvxb57dPad81r3fBu69MPPGaQM+bj+ufZax8CD/EdKd1qrgyBQGiFgYORK4xfdakQZ"
    "ARbj8jFwKeQiG1KLoCDaA89cVwh9ixsi7CjRDCO+ksl8B7IJJFzx9MzFCNtwAWn8bzA1xw"
    "i69ka4yBZ7S7nJloGUdTC7lYZit5Fp+e7Mw8o4WLKJj9fWCDMhdSCGBDAolmdkJsIX0UWZ"
    "xhmFkSqTMETNx4ZjMHOZlu6WDCwfC348GioTdMQu7xvnF1cX1x8/XVxzExnJWnK1CtNTuY"
    "eOkkBvWF9JPWAgtJAYFTeGGF8uha41ASSb3dohgY8HncQXwyriFwsUQFU0eyLogYXpQuyw"
    "icB2eVnA65cxaH01Bifc6p3IxueFHFZ4L1I1Qp2AqiDqkaVQDuEipwwTbmUBWsBv2H4ciq"
    "A9Sl9cHdvJd+NREvWWkabb732JzTXMrW6/maA7o5CYO51vzePvh/w4oO7jnIvLcTzNPOaC"
    "SBrgrU8gcvAdXEqOHR4RwFbW6Y66wUO0zPHxW8U1EEvVVUzAfN0w9NLg6fGkIAsvPOO+Zd"
    "y06xLiCFjTOSC2mUOTQMpjpmmgzcjx9m4AXZBzsCOWA7lIuWhKOn7D16hs8EqrvIaXlAAM"
    "HBm12FvstAkkYwhRqPJHEKJsqgHkyC6mogEEYDrPupvy26byqDpmdsekFr/YM6571wc5TN"
    "ceCaRj4VI6qDf9h2a3XfsxaLc6951+bwNjqBQiLkDh7T9oG90Ew/hJs9vkkfCqpo/U8/CN"
    "E4j+Hj0+jttOIYky2XUSOWQXliNeRg+OR7/8DhzPmFX/PbajWdR/5d8Uufz3f2xflt77H5"
    "7/0API3YXh2mE/EA9egodHGABK5z7JOMP5FHWfqhr1xylk/Aqdwox+m08z4fZPQKO6Kz/P"
    "1CyzzVeBuKm/8btAOSecg34ZMCBB1iRrKok0hXMJUDbVZFKiyeQ3JDTz0ZB/iWkuVUdQn1"
    "j40dgBYmReToDnZ2dbAORWuQClbhMg35HB8AxuQvx23+9lQ9RcEiAfME/wyUYWO625iLLn"
    "48RaQFFkXfzNKvl5SlDwKXOIXEUu0Nytze6/vaz+AB1r888="
)
