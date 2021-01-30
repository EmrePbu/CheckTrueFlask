```python
def read_alignment_and_indent(filename):
    """
    ENGLISH:
        It is used to find the indent values of each paragraph in the file.
    TÜRKÇE:
        Dosyadaki her bir paragrafın girinti değerlerini bulmaya yarar.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns the indent values as a dictionary data structure.
        TÜRKÇE:
            Girinti değerlerini sözlük veri yapısı şeklinde geri döndürür.
        `read_alignment_and_indent['left']`
        `read_alignment_and_indent['right']`
    """
    mainIndentArray = {}
    leftIndent = []
    rightIndent = []
    doc = _readFile.Document(filename)
    indent = doc.paragraphs
    for i in indent:
        leftIndent.append(round(Metric.emuToCm(
            i.paragraph_format.left_indent), 2))
        rightIndent.append(round(Metric.emuToCm(
            i.paragraph_format.right_indent), 2))
    mainIndentArray['left'] = leftIndent
    mainIndentArray['right'] = rightIndent
    return mainIndentArray
```



```jinja2
{% include 'includes/table_freeze_header.html' %}
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      {% for i in file_indent %}
        <th scope="col">
          
          {% if i == 'left' %}
          Sol Kenar Boşluğu(0 cm)
          {% elif i == 'right' %}
          Sağ Kenar Boşluğu(0 cm)
          {% endif %}
            
        </th>
      {% endfor %}
      {% for i in file_alignment %}
        <th scope="col">
          {% if i == 'alignment' %}
            Hizalama
          {% elif i == 'text' %}
            Yazı
          {% endif %}
          
        </th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for i in file_alignment['text']  %}
      {% set _alignment = file_alignment['alignment'][loop.index-1] %}
      {% set _text = file_alignment['text'][loop.index-1] %}
      {% set _left = file_indent['left'][loop.index-1]%}
      {% set _right = file_indent['right'][loop.index-1]%}
      {% if (_text != '' and _text != '\t') and (_text != '\t\t') %}
        <tr>
          <th scope="row">{{loop.index}}</th>
            <td>
              {% if _left == 0 %}
              <i class="fas fa-check"></i> {{_left}} cm
              {% else %}
              <i class="fas fa-times-circle"></i> {{_left}} cm
              {% endif %}
            </td>
            <td>
              {% if _right == 0 %}
              <i class="fas fa-check"></i> {{_right}} cm
              {% else %}
              <i class="fas fa-times-circle"></i> {{_right}} cm
              {% endif %}
            </td>
            <td>
              {% if _alignment == 1 %}
                ORTALI
              {% elif _alignment == 2 %}
                SAĞA YASLI
              {% elif _alignment == 3 %}
                İKİ YANA YASLI
              {% else %}
                SOLA YASLI
              {% endif %}
            </td>
          <td>{{_text}}</td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>
```

