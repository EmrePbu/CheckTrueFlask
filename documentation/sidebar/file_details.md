```python
def file_properties(filename):
    """
    ENGLISH:
        It is a method that provides access to file properties.
    TÜRKÇE:
        Dosya özelliklerine ulaşmayı sağlayan metoddur.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns a dictionary data structure containing file properties.
        TÜRKÇE:
            Dosya özelliklerini içeren bir sözlük veri yapısı döndürür.
    """
    doc = docx2python(filename)
    return doc.properties
```

```jinja2
{% include 'includes/table_freeze_header.html' %}
<table class="table">
  <thead class="thead-color">
    <tr>
      <th scope="col"><i class="fas fa-user-tag"></i></th>
      {% for key,value in file_details.items() %}
      <th scope="col">
        {% if key =='creator' %}Dosya Sahibi
        {% elif key =='lastModifiedBy'%}Son Düzenleyen
        {% elif key=='revision'%}Gözden Geçirme
        {% elif key=='created'%}Oluşturulma Tarihi
        {% elif key =='modified'%}Düzenlenme Tarihi
        {% elif key=='title' %}Başlık
        {% elif key =='subject'%}Konu 
        {% elif key =='keywords'%}Anahtar Kelimeler
        {% elif key =='description'%}Açıklama
        {% elif key =='category'%}Kategori
        {% elif key=='contentStatus'%}İçerik Durumu
        {% endif %}
      </th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row"><i class="fas fa-info-circle"></i></th>
      {% for key,value in file_details.items() %}
      <td>
        {% if value!=None %}{{value}}
        {% else %} -- 
        {% endif %}</td>
      {% endfor %}
    </tr>
  </tbody>
</table>
```

