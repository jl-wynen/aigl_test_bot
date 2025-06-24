class Bot:
    def __init__(self) -> None:
        try:
            import rich  # noqa: F401
        except ImportError as err:
            raise RuntimeError(f"rich is not available in the bot env: {err}") from None

        try:
            import pydantic  # noqa: F401
        except ImportError as err:
            raise RuntimeError(
                f"pydantic is not available in the bot env: {err}"
            ) from None

    def update(self, state: object) -> str:
        return str(state)
