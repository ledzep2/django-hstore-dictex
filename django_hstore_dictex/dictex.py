from django_hstore.hstore import DictionaryField
from jsonformfieldex.field import JSONFormFieldEx

class DictionaryFieldEx(DictionaryField):
    def __init__(self, *args, **kwargs):
        self._fields = kwargs.pop('fields', {})
        self.allow_empty = kwargs.pop('allow_empty', True)
        self.allow_json_input = kwargs.pop('allow_json_input', False)

        super(DictionaryFieldEx, self).__init__(self, *args, **kwargs)

    def formfield(self, **kwargs):
        #if "form_class" not in kwargs:
        #    kwargs["form_class"] = JSONFormFieldEx

        kwargs['allow_empty'] = self.allow_empty
        kwargs['fields'] = self._fields
        kwargs['allow_json_input'] = self.allow_json_input

        #return super(DictionaryFieldEx, self).formfield(**kwargs)
        return JSONFormFieldEx(**kwargs)
