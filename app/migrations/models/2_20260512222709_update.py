from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "question" ADD "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "result" ADD "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "result" DROP COLUMN "score";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "result" ADD "score" DOUBLE PRECISION NOT NULL;
        ALTER TABLE "result" DROP COLUMN "created_at";
        ALTER TABLE "question" DROP COLUMN "created_at";"""


MODELS_STATE = (
    "eJztmG1v2jAQx78KyqtO6qqW9Ul7l1K6sraw0XSrWlWRSUyImtg0dkZRxXef7cQ4z4MVJt"
    "DyCjjf2Xe/GPufe9N8bEOP7H0PIaEuRtrnxpuGgA/Zl9zYbkMD47Ea4QYKBp5wfkl6DQgN"
    "gEWZfQg8ApnJhsQK3HG8Bgo9jxuxxRxd5ChTiFw2k0mxA+kIBmzg8YmZXWTDV0jkz/GzOX"
    "ShZ6fSdW2+trCbdDoWtg6iF8KRrzYwLeyFPlLO4ykdYTT3dhHlVgciGAAK+fQ0CHn6PLu4"
    "UllRlKlyiVJMxNhwCEKPJspdkIGFEefHsiGiQIev8rF5cHhyePrp+PCUuYhM5paTWVSeqj"
    "0KFAS6hjYT44CCyENgVNyoS9l0OXStEQiK2c0DMvhY0ll8ElYVP2lQANWmWRFBH7yaHkQO"
    "HXFsR0cVvH7o/dal3t9hXh94NZht5GiHd+OhZjTGoSqIycxyKA34WrINM2HbArSCn9G+N3"
    "jSPiEvXhLbzo1+L4j603jkutf9It0TmFvXvbMMXSuAvH4T0DzcczZCXR8WA05HZvjaceie"
    "/LKZtDVWg91D3jQ+W6rod27at4Z+8y31CM51o81Hmin80rpznNno80kaPzvGZYP/bDz0um"
    "1BEBPqBGJF5Wc8aDwnEFJsIjwxgZ04BqVVgkk92JDAwFzq4E5E/Pn03pDnt4IDnN96w+fC"
    "85sTyQO8wAF0HXQFp4Jjh2UEkFV0bMfX/F08zebxm8k9IK1qcwVgMlcCya3BymNFQRrdZP"
    "ptSz9vawLiAFjPExDYZglNtrdZziQP9CwOvLjqQw+UnNgxy76YZLtoCjq4iRNUUrzyQ37T"
    "z1oAAo7Imq/NV0oDKVCXClW5tgyUT60sN+xgqlKWAJFJ0dlUrodURC2Fain0X0kh+QK9nB"
    "zKRNWSKNeMeKcsSnY/No/jotIos02WlUfrlAZCdxYIA6lHy2WBFL61KNi0v2aVKBCfOXLl"
    "3Sbpvy2C4B80m6APXG8ZhvOA1UBc+xZcP8IxIGSCg4L/cDnFZEy9G5NvzJCyI/QZFty35T"
    "QzYX8FNN53288zp2UWaVXIS/2dzYrtVDhrbVfoMHCtUZEqiUcqdQlQPrUy2SJl8gsGpPCl"
    "ofwQS4TUN4Lq+7C/xhIQY/ftBHiwv78AQOZVClCMZZo8GFGICjo8X2973ZLujgrJgLxDrM"
    "BH27XobsNzCX3aTKwVFHnV1Y20bM9sN92e4ROcLXfNrv56mf0G6Za7OA=="
)
