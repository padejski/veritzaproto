from django.core.files.storage import Storage
from django.core.files import File


class DummyStorage(Storage):
    def _open(self, name, mode='rb'):
        return File(open(name), mode)

    def _save(self, name, content):
        return name

    def save(self, name, content):
        return name

    def exists(self, name):
        return False
