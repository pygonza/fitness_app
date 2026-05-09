import copy


def pytest_configure(config):
    try:
        from django.template.context import BaseContext

        def base_context_copy(self):
            duplicate = object.__new__(type(self))
            duplicate.__dict__.update(getattr(self, '__dict__', {}))
            duplicate.dicts = self.dicts[:]
            return duplicate

        BaseContext.__copy__ = base_context_copy
    except Exception:
        pass
