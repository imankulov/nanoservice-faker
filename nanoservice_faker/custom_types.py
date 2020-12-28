#!/usr/bin/env python
import enum

from faker import Faker, config


def all_locales():
    return config.AVAILABLE_LOCALES


def all_methods():
    return [method for method in dir(Faker()) if is_valid_method(method)]


def is_valid_method(method: str) -> bool:
    own_methods = {
        "add_provider",
        "unique",
        "seed",
        "format",
        "seed_instance",
        "seed_locale",
        "random",
        "locales",
        "weights",
        "factories",
        "items",
        "cache_pattern",
        "del_arguments",
        "generator_attrs",
        "get_arguments",
        "get_formatter",
        "get_providers",
        "parse",
        "provider",
        "providers",
        "set_arguments",
        "set_formatter",
    }
    non_serializable_methods = {"binary", "pytimezone", "tar", "zip"}
    forbidden_methods = own_methods | non_serializable_methods
    return method not in forbidden_methods and not method.startswith("_")


Locale = enum.Enum(  # type: ignore
    "Locale", {locale: locale for locale in all_locales()}, type=str
)
Method = enum.Enum(  # type: ignore
    "Method", {method: method for method in all_methods()}, type=str
)
