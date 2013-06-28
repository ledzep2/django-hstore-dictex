Django HStore Dictionary Field Ex
=================================

This is a subclass of hstore.DictionaryField which uses JSONFormFieldEx to render full featured forms.


How it works?
-------------

    class MyCustomer(Model):
        slug = SlugField()
        store = DictionaryFieldEx({
            "profile": {
                "name": forms.CharField(max_length=10),
    			"email": forms.EmailField,
            },
            "account1": {
    			"number": forms.IntegerField,
    			"balance": forms.DecimalField(max_digits=10, decimal_places=2),
            },
    		"date_joined": forms.DateTimeField,
        })

    class MyCustomerForm(forms.ModelForm):
    	model = MyCustomer

And `MyCustomerForm` renders like this:

![screenshot1](http://ledzep2.github.com/django-jsonformfieldex/screenshot1.jpg)

Usage
------

Patched version of `DictionaryField` constructor takes three arguments itself. The original DictionaryField arguments still work.

* `fields`: a dict of fields  
You can provide either field type or field instance for each field. `Fields` also supports SortedDict or [(k,v)...] to preserve ordering of fields.

* `allow_json_input`: True|False  
If True, it will render an additional textarea allowing user to enter arbitary json string (just like jsonfield). The value in this field will be loaded to python dict and merged RECURSIVELY into the fielded values with priority.

Note: when `fields` is empty, `allow_json_input` will be automatically set to True

* `allow_empty`: True|False  
If False, cleaned value dict will be filtered to keep only keys that have values.
