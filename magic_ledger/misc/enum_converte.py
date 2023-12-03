from enum import Enum


def enum_converter(enum_class):
    def decorator(cls):
        class Wrapped(cls):
            def __setattr__(self, name, value):
                if name in enum_class.__members__ and isinstance(value, str):
                    value = enum_class(value)
                super().__setattr__(name, value)

            def as_dict(self):
                result = (
                    super().as_dict()
                    if hasattr(super(), "as_dict")
                    else self.__dict__.copy()
                )
                for key, value in result.items():
                    if isinstance(value, Enum):
                        result[key] = value.value
                return result

        return Wrapped

    return decorator
