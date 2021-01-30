```python
def read_page_structure(filename):
    """
    ENGLISH:
        It is used to find the margin values of each paragraph in the file.
    TÜRKÇE:
        Dosyadaki her bir paragrafın kenar boşluk değerlerini bulmaya yarar.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns the margin values as a dictionary data structure.
        TÜRKÇE:
            Kenar boşluk değerlerini sözlük veri yapısı şeklinde geri döndürür.
        `mainMarginArray['top']`
        `mainMarginArray['right']`
        `mainMarginArray['bottom']`
        `mainMarginArray['left']`
        `mainMarginArray['portrait']`
    """
    mainMarginArray = {}
    topMarginArray = []
    rightMarginArray = []
    bottomMarginArray = []
    leftMarginArray = []
    portraitMarginArray = []
    doc = _readFile.Document(filename)
    sections = doc.sections
    for i in sections:
        if(str(i.start_type) == 'NEW_PAGE (2)'):
            if(str(i.orientation) == 'PORTRAIT (0)'):
                portraitMarginArray.append('Dikey')
            if(str(i.orientation) == 'LANDSCAPE (1)'):
                portraitMarginArray.append('Yatay')
            topMarginArray.append(round(Metric.emuToCm(i.top_margin), 2))
            rightMarginArray.append(round(Metric.emuToCm(i.right_margin), 2))
            bottomMarginArray.append(round(Metric.emuToCm(i.bottom_margin), 2))
            leftMarginArray.append(round(Metric.emuToCm(i.left_margin), 2))
    mainMarginArray['top'] = topMarginArray
    mainMarginArray['right'] = rightMarginArray
    mainMarginArray['bottom'] = bottomMarginArray
    mainMarginArray['left'] = leftMarginArray
    mainMarginArray['portrait'] = portraitMarginArray
    return mainMarginArray
```



```jinja2
{% include 'includes/table_freeze_header.html' %}
<table class="table">
  <thead>
    <tr>
      <th scope="col"><i class="fas fa-sliders-h"></i></th>
      {% for i in file_margin  %}
        <th scope="col">
          
          {% if i =='top' %}
          Üst Kenar Boşluğu(3 cm)
          {% elif i == 'right' %}
          Sağ Kenar Boşluğu(2.5 cm)
          {% elif i == 'bottom' %}
          Alt Kenar Boşluğu(2.5 cm)
          {% elif i == 'left' %}
          Sol Kenar Boşluğu(3.25 cm)
          {% elif i == 'portrait' %}
          Yönlendirme
          {% endif %}
            
        </th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for i in file_margin['top'] %}
      <tr>
      <th scope="row">{{loop.index}}</th>
      {% set _top = file_margin['top'][loop.index-1] %}
      {% set _right = file_margin['right'][loop.index-1] %}
      {% set _bottom = file_margin['bottom'][loop.index-1] %}
      {% set _left = file_margin['left'][loop.index-1] %}
      {% set _portrait = file_margin['portrait'][loop.index-1] %}
      <td>
        {% if _checkMargin(3.00, _top) %}
        <i class="fas fa-check"></i> {{_top}} cm
        {% else %}
        <i class="fas fa-times-circle"></i> {{_top}} cm
        {% endif %}
      </td>
      <td>
        {% if _checkMargin(2.50, _right) %}
        <i class="fas fa-check"></i> {{_right}} cm
        {% else %}
        <i class="fas fa-times-circle"></i> {{_right}} cm
        {% endif %}
      </td>
      <td>
        {% if _checkMargin(2.50, _bottom) %}
        <i class="fas fa-check"></i> {{_bottom}} cm
        {% else %}
        <i class="fas fa-times-circle"></i> {{_bottom}} cm
        {% endif %}
      </td>
      <td>
        {% if _checkMargin(3.25, _left) %}
        <i class="fas fa-check"></i> {{_left}} cm
        {% else %}
        <i class="fas fa-times-circle"></i> {{_left}} cm
        {% endif %}
      </td>
      <td>
        
        {% if _portrait == 'Dikey' %}
        <i class="fas fa-arrows-alt-v"></i> {{_portrait}}
        {% elif _portrait == 'Yatay' %}
        <i class="fas fa-arrows-alt-h"></i> {{_portrait}}
        {% endif %}
          
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
```

