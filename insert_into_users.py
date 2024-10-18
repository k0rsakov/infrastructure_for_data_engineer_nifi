import datetime
from uuid import uuid4

import pandas as pd
from connectors_to_databases import PostgreSQL
from faker import Faker

fake = Faker(locale="ru_RU")
dict_ = {
    "id": [uuid4()],
    "created_at": [fake.date_time_ad(tzinfo=datetime.UTC)],
    "first_name": [fake.first_name()],
    "last_name": [fake.last_name()],
    "middle_name": [fake.middle_name()],
    "birthday": [fake.date_time_ad()],
    "email": [fake.email()],
}

df = pd.DataFrame.from_dict(data=dict_)

pg = PostgreSQL(
    database="nifi",
    login="nifi",
    password="nifi",  # noqa: S106
)

pg.insert_df(
    df=df,
    table_name="users",
)
