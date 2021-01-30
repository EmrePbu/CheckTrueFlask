## Üst Başlık

```python
def file_header(filename):
    """
    ENGLISH:
        It is the method that provides access to the header of the file.
    TÜRKÇE:
        Dosyanın üst başlığını ulaşmayı sağlayan metoddur.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns a TablesList containing file properties.
        TÜRKÇE:
            Dosya özelliklerini içeren bir TablesList döndürür.
    """
    doc = docx2python(filename)
    return doc.header
```

```jinja2
{% include 'includes/table_freeze_header.html' %}
<table class="table">
    <thead class="thead-color">
        <tr>
            <th scope="col"><i class="fas fa-heading"></i></th>
            <th scope="col">Üst Başlık</th>
        </tr>
    </thead>
    <tbody>
        {% if file_header %}
            {% for i in file_header[0][0][0] %}
                {% if i == null or i == '' %}
                    <tr>
                        <th scope="row"><i class="fas fa-times"></i></th>
                        <td>Üst başlıkta boşluk yada alt satır var</td>
                    </tr>
                {% elif i!= null or i != '' or i != ' ' %}
                    <tr>
                        <th scope="row"><i class="fas fa-check"></i></th>
                        <td>{{i}}</td>
                    </tr>
                {% endif %}
            {% endfor %}
        {% else %}
            <tr>
                <th scope="row"><i class="fas fa-minus"></i></th>
                <td>Üst başlık bulunamaktadır.</td>
            </tr>
        {% endif %}
    </tbody>
</table>
```

## Alt Başlık

```python
def file_footer(filename):
    """
    ENGLISH:
        It is the method that provides access to the footer of the file.
    TÜRKÇE:
        Dosyanın alt başlığını ulaşmayı sağlayan metoddur.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns a TablesList containing file properties.
        TÜRKÇE:
            Dosya özelliklerini içeren bir TablesList döndürür.
    """
    doc = docx2python(filename)
    return doc.footer

```



```jinja2
{% include 'includes/table_freeze_header.html' %}
<table class="table">
    <thead class="thead-color">
        <tr>
            <th scope="col"><i class="fas fa-heading"></i></th>
            <th scope="col">Alt Başlık</th>
        </tr>
    </thead>
    <tbody>
        {% if file_footer %}
            {% for i in file_footer[0][0][0] %}
                {% if i == null or i == '' %}
                    <tr>
                        <th scope="row"><i class="fas fa-times"></i></th>
                        <td>Alt başlıkta boşluk yada alt satır var</td>
                    </tr>
                {% elif i!= null or i != '' or i != ' ' %}
                    <tr>
                        <th scope="row"><i class="fas fa-check"></i></th>
                        <td>{{i}}</td>
                    </tr>
                {% endif %}
            {% endfor %}
        {% else %}
            <tr>
                <th scope="row"><i class="fas fa-minus"></i></th>
                <td>Alt başlık bulunamaktadır.</td>
            </tr>
        {% endif %}
    </tbody>
</table>
```

