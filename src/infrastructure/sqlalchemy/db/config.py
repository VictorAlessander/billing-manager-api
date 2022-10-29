def configure():
    return dict(
        conn=dict(database_uri="sqlite:///billing.db"),
        configs=dict(
            track_modifications=False,
            secret_key="ef5bcb77da527eb6901dcaf2ad046e3cab938983b71d6d1c",
        ),
    )
