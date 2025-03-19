from django.forms import ModelForm 

from .models import Property

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = (
            'title',             # No 'Titulo'
            'description',       # No 'Descripcion'
            'price_per_night',   # No 'Precio'
            'bedrooms',          # No 'Habitaciones'
            'bathrooms',         # No 'Baños'
            'guests',            # No 'Invitados'
            'country',           # No 'Pais'
            'country_code',      # No 'Pais_CODIGO'
            'category',          # No 'Categoria'
            'image'              # No 'Imagen'
        )