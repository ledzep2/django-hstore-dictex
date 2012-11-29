from django_hstore.hstore import DictionaryField
from django_jsonformfieldex.field import JSONFormFieldEx

class DictionaryFieldEx(DictionaryField):
    def __init__(self, *args, **kwargs):
        self.fields = kwargs.pop('fields', {})
        self.allow_json_input = kwargs.pop('allow_json_input', False)

        super(DictionaryFieldEx, self).__init__(self, *args, **kwargs)

    def formfield(self, **kwargs):
        if "form_class" not in kwargs:
            kwargs["form_class"] = JSONFormFieldEx

        kwargs['fields'] = self.fields
        kwargs['allow_json_input'] = self.allow_json_input

        return super(DictionaryField, self).formfield(**kwargs)
