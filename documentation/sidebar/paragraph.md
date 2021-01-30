```python
def read_paragraph(filename):
    """
    ENGLISH:
        Returns each paragraph in the file as a sequence.
    TÜRKÇE:
        Dosyadaki her bir paragrafı bir dizi olarak geri döndürür.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns each line in the given file as a string.
        TÜRKÇE:
            Verilen dosyadaki her bir satırı dizi şeklinde geri döndürür.
    """
    doc = _readFile.Document(filename)
    return [p.text for p in doc.paragraphs]
```





```jinja2
{% include 'includes/table_freeze_header.html' %}

<table class="table">
    <thead class="thead-color">
        <tr>
        <th scope="col"><i class="fas fa-paragraph"></i></th>
        <th scope="col">Paragraf etiketine sahip olan satırlar</th>
        </tr>
    </thead>
    <tbody>
        {% for p in content_list %}
            {% if p != "" %}
                <tr>
                <th scope="row">
                    {{loop.index}}
                </th>
                <td>{{p}}</td>
                </tr>
            {% endif %}
        {% endfor %}
    </tbody>
</table>
```

