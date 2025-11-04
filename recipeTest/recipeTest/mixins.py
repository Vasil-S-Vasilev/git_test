class PlaceholderMixin:
    def add_placeholders(self):
        custom_placeholders = getattr(self, 'custom_placeholders', {})
        
        for field_name, field in self.fields.items():
            placeholder = custom_placeholders.get(
                field_name,
                field.label or field_name.replace('_', ' ').capitalize()
            )
            field.widget.attrs['placeholder'] = placeholder
            

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()

    